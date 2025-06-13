
# 🖐 Project FingerLED

**FingerLED** es un proyecto interactivo que combina visión por computadora y electrónica básica para encender LEDs según la cantidad de dedos levantados frente a la cámara. Utiliza **Python + OpenCV + Mediapipe** para detectar los dedos, y un **Arduino Uno** para encender los LEDs mediante comunicación serial.

---

## 🚀 Características

- Detección en tiempo real de 0 a 5 dedos.
- Control de 5 LEDs a través de Arduino.
- Compatible con mano izquierda y derecha.
- Finalización del programa con tecla `ESC`.

---

## 🧰 Requisitos

### Hardware

- Arduino Uno
- 5 LEDs
- 5 resistencias de 220Ω
- Protoboard
- Cables macho-macho
- Cable USB para conexión al PC

### Software

- Python 3.x
- Arduino IDE
- Librerías de Python:
  - `opencv-python`
  - `mediapipe`
  - `pyserial`

---

## ⚙️ Instalación

### 1. Instalar librerías de Python

```bash
pip install opencv-python mediapipe pyserial
```

---

## 🔌 Conexión de LEDs al Arduino

| LED | Pin Arduino |
|-----|-------------|
| 1   | D2          |
| 2   | D3          |
| 3   | D4          |
| 4   | D5          |
| 5   | D6          |

Cada LED debe conectarse en serie con una resistencia de 220Ω hacia GND.

---

## ▶️ Ejecución del proyecto

1. Conecta Arduino por USB y carga el código `.ino`.
2. Ejecuta el script de Python:
   ```bash
   python fingerled.py
   ```
3. Levanta de 0 a 5 dedos frente a la cámara.
4. Verifica cómo se encienden los LEDs.
5. Presiona `ESC` para cerrar.

---

## 📸 Demo

> Puedes insertar aquí una imagen o GIF del sistema funcionando, o un enlace a tu video de TikTok.

---

## 📚 Créditos

Desarrollado por Gustavo Rios Quevedo 
Inspirado en proyectos de robótica educativa, visión computacional y control físico con Python + Arduino.
