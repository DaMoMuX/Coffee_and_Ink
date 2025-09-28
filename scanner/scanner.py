import cv2
from pyzbar import pyzbar
from pyzbar.pyzbar import ZBarSymbol

# 0 = default laptop/PC webcam
# 1 or 2 = external camera (e.g., phone via Iriun/DroidCam)
cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("No se pudo abrir la cámara. Revisa el índice o la app de tu móvil.")
    exit()

print("Escaneando... pulsa 'q' para salir.")

flag = True
while flag:
    ret, frame = cap.read()
    if not ret:
        print("No se pudo capturar imagen desde la cámara.")
        break

    # Decode only QR codes and EAN-13 barcodes
    barcodes = pyzbar.decode(frame, symbols=[ZBarSymbol.QRCODE, ZBarSymbol.EAN13])

    for barcode in barcodes:
        # Draw a rectangle around the detected code
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # Decode the barcode value into text
        barcode_value = barcode.data.decode("utf-8")

        # Display the decoded value above the rectangle
        cv2.putText(frame, barcode_value, (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        print("Código detectado:", barcode_value)
        flag = False  # Stop scanning after the first detection

    # Show the camera frame with overlays
    cv2.imshow("Barcode Scanner", frame)

    # Exit manually by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()