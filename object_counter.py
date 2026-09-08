"""批次偵測圖片，列出每張圖片與全部圖片的物件統計。"""

from collections import Counter
import os
from pathlib import Path


PROJECT_DIR = Path(__file__).resolve().parent
os.environ.setdefault("YOLO_CONFIG_DIR", str(PROJECT_DIR / "Ultralytics"))

from ultralytics import YOLO  # noqa: E402


INPUT_DIR = PROJECT_DIR / "input_images"
OUTPUT_DIR = PROJECT_DIR / "outputs"
MODEL_NAME = "yolo26n.pt"
CONFIDENCE = 0.25


def main() -> None:
    if not INPUT_DIR.exists():
        raise FileNotFoundError(f"找不到輸入資料夾：{INPUT_DIR}")

    model = YOLO(MODEL_NAME)
    results = model.predict(
        source=str(INPUT_DIR),
        conf=CONFIDENCE,
        save=True,
        project=str(OUTPUT_DIR),
        name="object_counter",
        exist_ok=True,
        verbose=False,
    )

    all_counts: Counter[str] = Counter()

    for result in results:
        image_name = Path(result.path).name
        image_counts: Counter[str] = Counter()

        for detected_box in result.boxes:
            class_id = int(detected_box.cls[0])
            class_name = model.names[class_id]
            confidence = float(detected_box.conf[0])
            image_counts[class_name] += 1
            print(f"{image_name}：{class_name}，信心值 {confidence:.2f}")

        all_counts.update(image_counts)
        print(f"本張統計：{dict(image_counts) if image_counts else '沒有偵測結果'}\n")

    print("===== 所有圖片加總 =====")
    if not all_counts:
        print("所有圖片都沒有偵測到物件")
    else:
        for class_name, count in sorted(all_counts.items()):
            print(f"{class_name}：{count} 個")
        print(f"物件總數：{sum(all_counts.values())} 個")

    print(f"結果位置：{OUTPUT_DIR / 'object_counter'}")


if __name__ == "__main__":
    main()
