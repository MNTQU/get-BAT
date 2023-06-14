import subprocess
import datetime
import time
import pyautogui

dt_now = datetime.datetime.now()
output = dt_now.strftime('%H:%M:%S')
cmd = "osascript -e 'display notification \"GET-BAT will start!\n{0}\" with title\"GET-BAT\"'".format(output)
#通知で起動時間お知らせ
subprocess.run(cmd, shell=True)

time.sleep(3)

#Braveブラウザを新しいウインドウで開く
subprocess.run('open -na "Brave Browser" --args', shell=True)

T = 0.25

#リロード
pyautogui.hotkey("command", "r")
time.sleep(T)

#ShiftItで左上にウインドウ移動させる
pyautogui.hotkey("command","ctrlleft","optionleft", "1")
time.sleep(T)

pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)
pyautogui.hotkey("command", "r")
time.sleep(T)

#ウインドウ閉じる
pyautogui.hotkey("command", "W")

