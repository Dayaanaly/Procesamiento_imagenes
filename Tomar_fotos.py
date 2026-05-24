import cv2 as cv
import os

# Carpeta donde se guardarán las imágenes
output_dir = "capturas_calibracion_2"
os.makedirs(output_dir, exist_ok=True)

# Abrir webcam
# # 0 = cámara integrada
# 1 = normalmente webcam USB
# #cap = cv.VideoCapture(0)
cap = cv.VideoCapture(0, cv.CAP_DSHOW)


if not cap.isOpened():
    print("No se pudo abrir la webcam.")
    exit()

contador = 0

print("Presiona 'c' para capturar una imagen.")
print("Presiona 'q' para salir.")

while True:
    ret, frame = cap.read()

    if not ret:
        print("No se pudo leer la imagen de la webcam.")
        break

    # Mostrar contador sobre la imagen
    texto = f"Capturas: {contador} | c = capturar | q = salir"
    cv.putText(frame, texto, (20, 40), cv.FONT_HERSHEY_SIMPLEX,
               0.8, (0, 255, 0), 2)

    cv.imshow("Webcam - Calibracion", frame)

    key = cv.waitKey(1) & 0xFF

    # Presionar 'c' para capturar
    if key == ord('c'):
        nombre = os.path.join(output_dir, f"calib_{contador:02d}.jpg")
        cv.imwrite(nombre, frame)
        print(f"Imagen guardada: {nombre}")
        contador += 1

    # Presionar 'q' para salir
    elif key == ord('q'):
        break

cap.release()
cv.destroyAllWindows()

print(f"Total de imágenes guardadas: {contador}")