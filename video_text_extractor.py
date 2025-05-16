import cv2
import pytesseract
from pathlib import Path
from PIL import Image

# Optional: Set tesseract executable path if it's not in PATH
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

video_path = "product.wmv"  # Replace with your video file
output_dir = Path("frames")
output_dir.mkdir(exist_ok=True)

# Load video
cap = cv2.VideoCapture(video_path)
fps = int(cap.get(cv2.CAP_PROP_FPS))
interval = fps * 2  # Capture a frame every 2 seconds

frame_count = 0
saved_count = 0
extracted_text = ""

success, frame = cap.read()

while success:
    if frame_count % interval == 0:
        frame_file = output_dir / f"frame_{saved_count}.jpg"
        cv2.imwrite(str(frame_file), frame)
        print(f"Saved: {frame_file}")

        # OCR on frame
        img = Image.open(frame_file)
        text = pytesseract.image_to_string(img)
        extracted_text += f"\n--- Frame {saved_count} ---\n{text.strip()}\n"
        saved_count += 1

    success, frame = cap.read()
    frame_count += 1

cap.release()

# Save extracted text to a file
with open("extracted_text.txt", "w", encoding="utf-8") as f:
    f.write(extracted_text)

print("\n✅ OCR complete. Text saved to 'extracted_text.txt'")
