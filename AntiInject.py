import os
import time
import sys
import shutil
import ctypes

if sys.platform == 'win32':
    import win32gui, win32console, win32con
    hwnd = win32console.GetConsoleWindow()
    win32gui.ShowWindow(hwnd, win32con.SW_HIDE)

current = os.path.abspath(__file__)
startup = os.path.join(os.getenv('APPDATA'), r'Microsoft\Windows\Start Menu\Programs\Startup')
shutil.copy2(current, startup)
while True:
    discpathuwu = os.path.join(os.getenv('LOCALAPPDATA'), 'Discord')
    for folder in os.listdir(discpathuwu):
        if folder.startswith("app-"):
            pathuwu = os.path.join(discpathuwu, folder, 'modules', 'discord_desktop_core-1', 'discord_desktop_core', 'index.js')
            with open(pathuwu, 'r', encoding='utf-8') as f:
                code = f.read()
            if code != "module.exports = require('./core.asar');":
                with open(pathuwu, 'w', encoding='utf-8') as f:
                    f.write("module.exports = require('./core.asar');")
                    ctypes.windll.user32.MessageBoxW(0, "Your discord Index.js file was found to be injected with malware. (CLEANED)", "Error", 0x10)
    time.sleep(5)
