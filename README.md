# Raspberry Pi YOLO物件偵測課程

這份教材供Raspberry Pi 5課堂實作使用。學生會直接使用預訓練YOLO模型進行圖片推論，不在Raspberry Pi上訓練模型，也不使用攝影機。

## 課堂成果

完成後可以：

- 批次讀取`input_images/`中的圖片。
- 使用預訓練YOLO模型偵測物件。
- 儲存包含類別、信心值與Bounding Box的結果圖片。
- 在終端機統計各類物件的數量。
- 修改Confidence threshold並比較偵測差異。

## 1. 下載教材

```bash
cd ~
git clone https://github.com/warlock-hhh/raspberry-pi-yolo-course.git
cd raspberry-pi-yolo-course
```

## 2. 建立虛擬環境

```bash
python3 -m venv .venv
source .venv/bin/activate
```

終端機提示字元前方出現`(.venv)`代表環境已啟用。

## 3. 安裝套件

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

檢查環境：

```bash
python check_environment.py
```

## 4. 第一次物件偵測

```bash
python first_detection.py
```

第一次執行時會下載`yolo26n.pt`模型權重，因此需要網路。完成後到下列資料夾查看圖片：

```text
outputs/first_detection/
```

## 5. 物件數量統計

```bash
python object_counter.py
```

終端機會顯示每張圖片的偵測結果與全部圖片的物件總數，畫框圖片位於：

```text
outputs/object_counter/
```

## 6. 課堂修改

在`first_detection.py`或`object_counter.py`找到：

```python
CONFIDENCE = 0.25
```

依序測試`0.10`、`0.50`與`0.80`，比較：

- 保留的偵測框數量。
- 誤檢是否增加。
- 原本漏掉的物件是否出現。
- 高信心值是否一定代表正確。

也可以將自己的圖片複製到`input_images/`後重新執行。

## 常見問題

### `ModuleNotFoundError: No module named 'ultralytics'`

先確認終端機前方有`(.venv)`：

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

### `can't open file`

確認目前位於教材資料夾：

```bash
pwd
ls
```

畫面中應該能看到`first_detection.py`與`object_counter.py`。

### 沒有任何偵測框

- 確認`input_images/`中有JPG或PNG圖片。
- 將`CONFIDENCE`暫時降低至`0.10`。
- 確認圖片內容屬於COCO預訓練模型支援的常見類別。

### 重複執行是否會產生很多資料夾

程式使用`exist_ok=True`，會持續使用固定的輸出資料夾。

## 專案結構

```text
raspberry-pi-yolo-course/
├── README.md
├── requirements.txt
├── check_environment.py
├── first_detection.py
├── object_counter.py
├── input_images/
└── outputs/                 # 執行後產生，不會上傳GitHub
```

## 執行環境

本課程目前以以下環境為目標：

- Raspberry Pi 5
- 8 GB RAM
- Raspberry Pi OS／Debian GNU/Linux 13
- aarch64
- Python 3.13

正式上課前仍應在同型號Raspberry Pi重新執行完整流程，確認套件版本與模型下載正常。
