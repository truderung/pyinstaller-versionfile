# -*- mode: python ; coding: utf-8 -*-

block_cipher = None


a = Analysis(['--version-file C:\\Users\\Andi\\AppData\\Local\\Temp\\tmpeabwevlq\\version_file.txt', 'D:\\Programming\\Referenzarchitektur\\pyinstaller-versionfile\\test\\resources\\testapp.py'],
             pathex=['D:\\Programming\\Referenzarchitektur\\pyinstaller-versionfile\\test'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          [],
          name='version_file',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=True )