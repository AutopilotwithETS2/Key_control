from pynput.keyboard import Key, Controller
import time
import keyboard as kb


keyboard = Controller()

sit_right = 0  # 오른쪽으로 이동해야 하는 경우
sit_left = 0  # 왼쪽으로 이동해야 하는 경우
max_60 = 0 #최대속도가 60도일 때를 위한 변수

def change_sit_right():
    global sit_right
    sit_right = 1

def change_sit_left():
    global sit_left
    sit_left = 1

def control_direction():
    global sit_right, sit_left
    if sit_right == 1:
        print("오른쪽으로 이동 중...")
        keyboard.press(Key.right)
        time.sleep(0.1)
        keyboard.release(Key.right)
        sit_right = 0
    elif sit_left == 1:
        print("왼쪽으로 이동 중...")
        keyboard.press(Key.left)
        time.sleep(0.1)
        keyboard.release(Key.left)
        sit_left = 0
        
        
kb.add_hotkey('t', change_sit_right)
kb.add_hotkey('a', change_sit_left)


# 키 입력을 기다리며 sit_right 상태를 변경
while True:
    print("sit_right =", sit_right)
    print("sit_left =", sit_left)
    control_direction()
    time.sleep(0.01)  # 0.01초 간격으로 반복
