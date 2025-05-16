Summary: Takes text from video and stores it "extracted_text.txt" along with frames captured in the video to "frames" directory.


1. Prepare the Environment

a. Install Python (if not already installed)
Download from: https://www.python.org/downloads/windows

During installation, make sure to check ✅ "Add Python to PATH"

b. Install Required Libraries
Open Command Prompt and run:

pip install opencv-python pytesseract pillow

2. Install Tesseract OCR

Follow these steps:

Go to Tesseract GitHub Releases https://github.com/tesseract-ocr/tesseract/releases

Download and install the .exe file (tesseract-ocr-w64-setup-*.exe)

During install:

✅ Select “Add to PATH”

✅ Choose language packs if needed

Note the install location (usually: C:\Program Files\Tesseract-OCR\tesseract.exe)

3. Save and Run the Python Script
a. Create a Python file:
Open Notepad or VS Code

Paste the script below and save it as video_text_extractor.py

b. Replace video_path in the script:
Change this line to match your video file: 
video_path = "product.wmv"

Note: Make sure the video file is in the same folder as the script (or use the full path).

c. (Optional) Set Tesseract Path in Script:
If needed, uncomment and update this line:

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


4. Run the Script

Open Command Prompt, navigate to the script's folder:
cd path\to\your\script

Then run:
python video_text_extractor.py
