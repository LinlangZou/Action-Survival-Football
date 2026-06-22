import cv2
import mediapipe as mp
from pythonosc import udp_client
import time

# 设置发送到 UE5 的地址和端口 (必须与蓝图里一致)
IP = "127.0.0.1"
PORT = 8000
client = udp_client.SimpleUDPClient(IP, PORT)

# 初始化 MediaPipe AI 模块
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.7, min_tracking_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# 打开默认摄像头 (0代表第一个摄像头)
cap = cv2.VideoCapture(0)
last_send_time = 0

print("摄像头已启动，请对着镜头做出击掌（五指张开）手势...")

while True:
    success, img = cap.read()
    if not success:
        break

    # MediaPipe 需要 RGB 格式的图像
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(img, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # 判断手指是否竖起
            tips = [8, 12, 16, 20]
            joints = [6, 10, 14, 18]
            fingers_up = 0

            for i in range(4): 
                if hand_landmarks.landmark[tips[i]].y < hand_landmarks.landmark[joints[i]].y:
                    fingers_up += 1

            # 4根手指竖起即判定为击掌
            if fingers_up == 4:
                current_time = time.time()
                if current_time - last_send_time > 2.0: 
                    print("检测到击掌！正在向 UE5 发送信号...")
                    client.send_message("/gesture/highfive", 1) 
                    last_send_time = current_time

    # 显示画面
    cv2.imshow("High Five Detector", img)
    
    # 选中画面窗口按 Q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()