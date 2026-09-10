# 測試圖片：共 10 張

本資料夾包含 10 張課程用 AI 生成圖片，供 YOLO 推論、物件計數與信心門檻比較練習。01 為原有圖片，02–10 為新增的合成情境，並非真實拍攝的評測資料。

| 圖片 | 情境 | 可觀察的常見類別 |
| --- | --- | --- |
| 01_park_scene.png | 公園 | person、dog、bicycle、car、bench、backpack |
| 02_street.jpg | 街道與車輛 | person、bus、car |
| 03_cats.jpg | 沙發上的貓 | cat、couch |
| 04_dogs.jpg | 草地上的狗 | dog |
| 05_dining.jpg | 餐桌用品 | cup、bowl、bottle、fork、spoon |
| 06_fruit.jpg | 水果與碗 | banana、apple、orange、bowl |
| 07_bicycles.jpg | 腳踏車停放區 | bicycle |
| 08_workspace.jpg | 書桌 | laptop、keyboard、mouse、cell phone、book、chair |
| 09_crosswalk.jpg | 行人穿越街道 | person、car、traffic light |
| 10_living_room.jpg | 客廳與遮擋 | couch、potted plant、tv、chair、cat |

表中類別是觀察方向，不是模型必定輸出的結果，也不是人工標註的標準答案。請看原圖，逐一核對預測框；合成圖的物件形狀、遮擋與光線也可能影響辨識。

## 使用方式

沿用主 README 與課程 PPT 的安裝、執行流程，不需新增套件。兩支程式會讀取 input_images 中的圖片，現在預設會處理 10 張，因此執行時間及全部圖片加總會與原先單張公園圖不同。

先確認公園圖的操作流程，再從其餘圖片挑選三張進行觀察。比較 0.25 與 0.80 時，使用相同圖片與模型，先保存第一次結果再重跑。若所有圖片都保留在資料夾，總計仍包含全部圖片，三張比較表則只記錄選定的圖片。

學生也可以加入自己的 JPG、JPEG、PNG 或 WebP 圖片。請放原始圖，勿放已畫框的輸出圖。

## 來源

- 01：原有課程生成素材，保留原檔。
- 02–10：2026-09-10 以 OpenAI 內建圖片生成工具為本課程產生，轉成 JPG 並縮小尺寸以減少下載量。
- 這些素材用於學習操作與討論錯誤，不能取代真實資料集的準確率評估。
