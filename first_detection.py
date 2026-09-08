"""使用預訓練YOLO模型，批次偵測input_images中的圖片。"""

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

    images = [
        path
        for path in INPUT_DIR.iterdir()
        if path.suffix.lower() in {".jpg", ".jpeg", ".png", ".webp"}
    ]
    if not images:
        raise FileNotFoundError(f"{INPUT_DIR} 中沒有可偵測的圖片")

    # 若本機沒有權重檔，Ultralytics會在第一次執行時下載。
    model = YOLO(MODEL_NAME)
    results = model.predict(
        source=str(INPUT_DIR),
        conf=CONFIDENCE,
        save=True,
        project=str(OUTPUT_DIR),
        name="first_detection",
        exist_ok=True,
        verbose=True,
    )

    print("\n===== 偵測完成 =====")
    print(f"共處理 {len(results)} 張圖片")
    print(f"信心門檻：{CONFIDENCE}")
    print(f"結果位置：{OUTPUT_DIR / 'first_detection'}")


if __name__ == "__main__":
    main()
