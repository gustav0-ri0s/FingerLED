import cv2
import mediapipe as mp
import serial
import time

# Inicializar comunicación serial con Arduino (ajusta el puerto COM)
arduino = serial.Serial('COM6', 9600)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

tip_ids = [4, 8, 12, 16, 20]

def contar_dedos(lm_list, label):
    count = 0
    # Pulgar
    if label == "Right":
        if lm_list[4][0] > lm_list[3][0]:
            count += 1
    else:  # Left
        if lm_list[4][0] < lm_list[3][0]:
            count += 1
    # Otros dedos
    for i in range(1, 5):
        if lm_list[tip_ids[i]][1] < lm_list[tip_ids[i] - 2][1]:
            count += 1
    return count

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(img_rgb)

    dedos_derecha = 0
    dedos_izquierda = 0

    if results.multi_hand_landmarks and results.multi_handedness:
        for idx, handLms in enumerate(results.multi_hand_landmarks):
            label = results.multi_handedness[idx].classification[0].label  # 'Right' o 'Left'
            lm_list = []
            for id, lm in enumerate(handLms.landmark):
                h, w, _ = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append((cx, cy))

            count = contar_dedos(lm_list, label)
            if label == "Right":
                dedos_derecha = count
            else:
                dedos_izquierda = count

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    # Resta dedos: derecha - izquierda
    resultado = max(0, dedos_derecha - dedos_izquierda)

    # Mostrar en pantalla
    cv2.putText(img, f'Derecha: {dedos_derecha}', (10, 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(img, f'Izquierda: {dedos_izquierda}', (200, 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 2)

    cv2.putText(img, f'Resultado: {resultado}', (400, 70), 
            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)  # Azul


    cv2.imshow("FingerLED - Resta", img)

    # Enviar resultado al Arduino
    arduino.write(f"{resultado}\n".encode())

    # Salir con ESC
    if cv2.waitKey(1) & 0xFF == 27:
        break

arduino.close()
cap.release()
cv2.destroyAllWindows()
