"""檢查課堂需要的Python版本與套件。"""

import platform
import sys


def print_result(name: str, value: str) -> None:
    print(f"{name:<18}: {value}")


print("===== YOLO課程環境檢查 =====")
print_result("Python", sys.version.split()[0])
print_result("作業系統", platform.platform())
print_result("CPU架構", platform.machine())

try:
    import cv2

    print_result("OpenCV", cv2.__version__)
except ImportError:
    print_result("OpenCV", "尚未安裝")

try:
    import ultralytics

    print_result("Ultralytics", ultralytics.__version__)
except ImportError:
    print_result("Ultralytics", "尚未安裝")

print("============================")

