import win32gui
import pygetwindow as gw
import pyautogui, time
"""
def find_window_by_title(title):
    hwnd = win32gui.FindWindow(None, title)
    return hwnd

def list_open_windows():
    def callback(hwnd, windows):
        if win32gui.IsWindowVisible(hwnd):
            windows.append((hwnd, win32gui.GetWindowText(hwnd)))
    windows = []
    win32gui.EnumWindows(callback, windows)
    return windows

# Listar todas las ventanas abiertas en el sistema
windows = list_open_windows()
for hwnd, title in windows:
    print(f"Window Handle: {hwnd}, Title: {title}")


def find_window_by_title(title):
    windows = gw.getWindowsWithTitle(title)
    if windows:
        return windows[0]
    return None

def move_mouse_to_center_of_window(window):
    x = window.left + (window.width / 2)
    y = window.top + (window.height / 2)
    print(f"centro de ventana: x= {x}, y= {y}")
    pyautogui.moveTo(x, y)

def print_window_coordinates(window):
    print(f"Window Coordinates (left, top, width, height): {window.left}, {window.top}, {window.width}, {window.height}")

# Título de la ventana que deseas encontrar
window_title = "WAKFU"

# Encuentra la ventana por su título
window = find_window_by_title(window_title)

if window:
    print(f"Ventana encontrada con título '{window_title}'")
    print_window_coordinates(window)

    # Mueve el cursor del ratón al centro de la ventana
    move_mouse_to_center_of_window(window)
else:
    print(f"No se pudo encontrar la ventana con título '{window_title}'")
"""
val2= -22
val1 = 42
x=400
y=307

for x1 in range(-9,10):
    for y1 in range(9,-11,-1):
        newx= x+(val1*x1)
        newy= y+(val2*y1)
        pyautogui.moveTo(newx, newy)
        print(f' pos: (x;y= {newx}; {newy})    movimiento ( x;y= {x1};{y1})')