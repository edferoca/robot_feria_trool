import pyautogui
import time

# Ruta de la imagen que quieres detectar
imagen = "img/capitan_miau_100interfas.png"

print("🔍 Buscando la imagen en pantalla... (Presiona Ctrl+C para salir)")

while True:
    try:
        # Intenta localizar la imagen en la pantalla con confianza del 70%
        encontrado = pyautogui.locateOnScreen(imagen, confidence=0.7)

        if encontrado:
            print(f"✅ Imagen encontrada en {encontrado}")
        else:
            print("❌ Imagen NO encontrada")
        
        time.sleep(1)  # Espera 1 segundo antes de volver a buscar
    except KeyboardInterrupt:
        print("\n⏹ Programa detenido por el usuario.")
        break
    except Exception as e:
        print(f"⚠ Error: {e}")
