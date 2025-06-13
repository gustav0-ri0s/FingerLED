import cv2
import mediapipe as mp
import serial
import time

# Inicializar comunicación serial con Arduino (ajusta el puerto COM)
arduino = serial.Serial('COM6', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands()
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

# Índices de las puntas de los dedos
tip_ids = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    finger_count = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            # Verifica dedos arriba (excepto pulgar con comparación especial)
            if lm_list:
                # Pulgar
                if lm_list[tip_ids[0]][0] > lm_list[tip_ids[0] - 1][0]:
                    finger_count += 1
                # Otros dedos
                for i in range(1, 5):
                    if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
                        finger_count += 1

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # Mostrar imagen y dedos detectados
    cv2.putText(img, f'Dedos: {finger_count}', (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 3)
    cv2.imshow("Image", img)

    # Enviar al Arduino
    arduino.write(f"{finger_count}\n".encode())

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

arduino.close()
cap.release()
cv2.destroyAllWindows()

