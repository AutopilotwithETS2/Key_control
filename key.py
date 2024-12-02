import keyboard
import time

sit = 0 #오른쪽으로 이동해야 하는 경우
sit2 = 0 #왼쪽으로 이동해야 하는 경우

def change_sit():
    global sit
    sit = 1

def change_sit2():
    global sit2
    sit2 = 1


def control_direction():
    global sit  #지역변수 전역변수r
    global sit2
    if sit == 1:
        print(sit)
        # 오른쪽 방향키를 0.2초 동안 누르기
        keyboard.press('right') #누르기
        time.sleep(0.2)
        keyboard.release('right') #떼기
        sit = 0
    elif sit2 == 1:
        print(sit2)
        # 왼쪽 방향키를 0.2초 동안 누르기
        keyboard.press('left')
        time.sleep(0.2)
        keyboard.release('left')
        sit2 = 0

keyboard.add_hotkey('r', change_sit)
keyboard.add_hotkey('l', change_sit2)



# 프로그램의 실행 흐름
while True:
    print("sit =", sit)
    print("sit2 =", sit2)
    control_direction()
    time.sleep(0.01) 
    
keyboard.wait('esc')