"""离线公开版回归；隔离目录和生成夹具保留供审查，不调用发布网络。"""
import importlib.util
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


class PublicPackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        parent = os.environ.get('BG_TEST_ARTIFACTS')
        cls.work = Path(tempfile.mkdtemp(prefix='bg-wechat-isolated-', dir=parent))
        cls.package = cls.work / 'install' / 'bg-wechat'
        cls.manifest = (ROOT / 'release-files.txt').read_text(encoding='utf-8').splitlines()
        for rel in cls.manifest:
            path = Path(rel)
            if not rel or path.is_absolute() or '..' in path.parts:
                raise ValueError('发布白名单包含无效路径')
            destination = cls.package / path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, destination)
        cls.cwd = cls.work / 'work'
        cls.cwd.mkdir()
        cls.fixtures = cls.package / 'tests/fixtures'
        cls.env = {k: v for k, v in os.environ.items() if not k.startswith('WECHAT_OA_') and k != 'PYTHONPATH'}
        cls.env['PYTHONUTF8'] = '1'
        cls.env['PYTHONDONTWRITEBYTECODE'] = '1'
        print(f'保留隔离验证目录：{cls.work}')

    def run_script(self, rel, *args, input=None):
        return subprocess.run([sys.executable, str(self.package / rel), *map(str, args)], cwd=self.cwd,
                              env=self.env, input=input, text=True, encoding='utf-8', capture_output=True)

    def test_standalone_paths_and_source_lint(self):
        self.assertFalse((self.package.parent / 'gzh-design').exists())
        for base in ('',):
            result = self.run_script(base + 'scripts/component_lint.py', self.package / base)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn('ERROR×0', result.stdout)

    def test_real_html_paths_and_counterexamples(self):
        for base in ('',):
            for name, code, marker in [('valid.html', 0, '未发现'), ('invalid.html', 1, 'ERROR'), ('gradient.html', 0, 'darkmode-no-gradient')]:
                with self.subTest(base=base, name=name):
                    result = self.run_script(base + 'scripts/validate_gzh_html.py', self.fixtures / name)
                    self.assertEqual(result.returncode, code, result.stdout + result.stderr)
                    self.assertIn(marker, result.stdout)

    def test_preview_preserves_body_and_escapes_title(self):
        source = self.cwd / '标题&样例.html'
        body = (self.fixtures / 'valid.html').read_text(encoding='utf-8')
        source.write_text(body, encoding='utf-8')
        for number, base in enumerate(('',)):
            output = self.cwd / f'preview-{number}.html'
            result = self.run_script(base + 'scripts/wrap_preview.py', source, output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            preview = output.read_text(encoding='utf-8')
            self.assertIn(body.strip(), preview)
            self.assertIn('<title>标题&amp;样例', preview)
            self.assertIn('gzhCopy', preview)
            rejected = self.run_script(base + 'scripts/wrap_preview.py', self.fixtures / 'invalid.html', self.cwd / f'rejected-{number}.html')
            self.assertEqual(rejected.returncode, 1)
            self.assertFalse((self.cwd / f'rejected-{number}.html').exists())

    def test_native_class_does_not_hide_invalid_content(self):
        native = '<mp-common-profile class="js_uneditable"></mp-common-profile><span leaf="">正文</span>'
        ok = self.run_script('scripts/validate_gzh_html.py', '--stdin', input=native)
        self.assertEqual(ok.returncode, 0, ok.stdout + ok.stderr)
        for content in ('<script>void 0;</script>', '<div>内容</div>', '<p class="bad">内容</p>'):
            source = '<mp-common-profile class="js_uneditable">' + content + '</mp-common-profile><span leaf="">正文</span>'
            result = self.run_script('scripts/validate_gzh_html.py', '--stdin', input=source)
            self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_executable_attributes_rejected(self):
        samples = ['<img src="x" onerror="void 0">', '<a href="java&#x73;cript:void(0)">链接</a>', '<iframe srcdoc="x"></iframe>']
        for base in ('',):
            for sample in samples:
                result = self.run_script(base + 'scripts/validate_gzh_html.py', '--stdin', input=sample + '<span leaf="">正文</span>')
                self.assertEqual(result.returncode, 1, result.stdout + result.stderr)

    def test_prose_preserves_technical_literals(self):
        result = self.run_script('scripts/check_prose.py', self.fixtures / 'prose.txt')
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        text = '保留实际代码。\n```python\nprint("中文:原样")\n```\n链接 https://example.com/a:b\n'
        result = self.run_script('scripts/check_prose.py', '-', input=text)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        result = self.run_script('scripts/check_prose.py', '-', input='这不是简单变化，而是彻底改变。')
        self.assertEqual(result.returncode, 1)

    def test_release_allowlist_excludes_local_material(self):
        actual = {p.relative_to(self.package).as_posix() for p in self.package.rglob('*') if p.is_file()}
        self.assertEqual(actual, set(self.manifest))
        self.assertEqual(len(self.manifest), len(set(self.manifest)))
        self.assertFalse((self.package / 'vendor').exists())
        self.assertEqual(list(self.package.parent.iterdir()), [self.package])
        for rel in self.manifest:
            self.assertNotRegex(rel, r'(?i)(vendor/|license\.original|third|\.local\.|content-system|_skillhub_meta|_knot_meta|\.env)')
        template = (self.package / 'references/author-memory.md').read_text(encoding='utf-8')
        self.assertIn('待填写', template)

    def test_basic_theme_and_core_reference_paths(self):
        skill = (self.package / 'SKILL.md').read_text(encoding='utf-8')
        for rel in re.findall(r'`(references/[a-z-]+\.md)`', skill):
            self.assertTrue((self.package / rel).is_file(), rel)
        for branch in ('`write`', '`layout`', '`theme`'):
            self.assertIn(branch, skill)
        text = (self.package / 'references/themes-and-components.md').read_text(encoding='utf-8')
        blocks = re.findall(r'```html\s*\n(.*?)```', text, re.S)
        self.assertTrue(blocks)
        for i, body in enumerate(blocks):
            source = self.cwd / f'basic-{i}.html'
            source.write_text(body, encoding='utf-8')
            result = self.run_script('scripts/validate_gzh_html.py', source)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            output = self.cwd / f'basic-{i}-preview.html'
            result = self.run_script('scripts/wrap_preview.py', source, output)
            self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
            self.assertIn(body.strip(), output.read_text(encoding='utf-8'))

    def test_publish_missing_config_stops_before_network(self):
        scripts = str(self.package / 'scripts')
        sys.path.insert(0, scripts)
        try:
            spec = importlib.util.spec_from_file_location('offline_publish_test', self.package / 'scripts/publish.py')
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            with patch.dict(os.environ, {}, clear=True), patch.object(module.urllib.request, 'urlopen') as network:
                with self.assertRaisesRegex(ValueError, 'WECHAT_OA_APPID'):
                    module.publish_to_wechat(self.fixtures / 'valid.html')
                with self.assertRaisesRegex(ValueError, 'cover'):
                    module.publish_to_wechat(self.fixtures / 'valid.html', appid='test-app', secret='test-only')
                network.assert_not_called()
            with patch.object(module, 'upload_image_to_cdn', return_value='https://example.com/image.png') as upload:
                image = self.cwd / 'image.png'
                image.write_bytes(b'test-fixture')
                result = module.replace_local_images('<img src="image.png"><img src="image.png">', 'test-only', str(self.cwd))
                self.assertEqual(upload.call_count, 1)
                self.assertEqual(result.count('https://example.com/image.png'), 2)
        finally:
            sys.path.remove(scripts)


if __name__ == '__main__':
    unittest.main()
