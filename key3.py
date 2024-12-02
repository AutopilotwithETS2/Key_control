import pyautogui
import cv2
import numpy as np
import time
from pynput.keyboard import Key, Controller
import keyboard as kb

# 키보드 컨트롤러 및 전역 변수 초기화
keyboard = Controller()
limit_60 = "C:\\Users\\girookim\\Desktop\\Autopiliot\\Key_control\\speed_limit\\60_limit.png"
max_60 = 0  # 최대속도가 60도일 때를 위한 변수

# 방향 이동 상태 변수
sit_right = 0  # 오른쪽으로 이동해야 하는 경우
sit_left = 0  # 왼쪽으로 이동해야 하는 경우

# 흑백처리된 템플릿 이미지 로드
template_limit_60 = cv2.imread(limit_60, cv2.IMREAD_GRAYSCALE)
threshold = 0.8  # 유사도 임계값 설정 (80% 이상일 때)

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
        time.sleep(0.2)
        keyboard.release(Key.right)
        sit_right = 0
    elif sit_left == 1:
        print("왼쪽으로 이동 중...")
        keyboard.press(Key.left)
        time.sleep(0.2)
        keyboard.release(Key.left)
        sit_left = 0

# 방향 조정 핫키 설정
kb.add_hotkey('t', change_sit_right)
kb.add_hotkey('a', change_sit_left)

# 화면에서 limit_60 이미지 탐지
while True:
    # 스크린샷을 캡처하고 그레이스케일로 변환
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_BGR2GRAY)

    # limit_60 이미지 템플릿 매칭
    result = cv2.matchTemplate(screen_gray, template_limit_60, cv2.TM_CCOEFF_NORMED)
    locations = np.where(result >= threshold)

    # 템플릿 매칭이 있는 경우 max_60을 1로 설정
    if locations[0].size > 0:
        max_60 = 1
        print("속도 제한 60 감지됨: max_60 =", max_60)
    else:
        max_60 = 0  # 매칭이 없을 때는 0으로 재설정
        print("속도 제한 없음: max_60 =", max_60)

    # 방향 조정
    control_direction()

    # 'q' 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("프로그램 종료")
        break

    # 1초마다 탐색
    time.sleep(1.0)
