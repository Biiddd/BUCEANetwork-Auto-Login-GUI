# build.py
import PyInstaller.__main__

PyInstaller.__main__.run([
    'main.py',  # 你的主Python脚本
    '--onefile',  # 打包成单个可执行文件
    '--noconsole'  # 隐藏命令行窗口（仅对GUI应用程序有效）
])
