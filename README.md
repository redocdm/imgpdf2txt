# imgpdf2txt
flask python app convert image-pdf to text

# Image and PDF to Text Converter

This web application allows users to upload image files (PNG, JPEG) or PDF files and converts the text content within those files to plain text using OCR (Optical Character Recognition).

## Prerequisites

- Python 3.x
- Tesseract OCR
- Poppler (for PDF conversion)

## Installation

### 1. Clone the Repository:

`git clone https://github.com/redocdm/imgpdf2txt.git`

`cd repo`

2. Create a Virtual Environment (optional but recommended):
`python -m venv venv`

`source venv/bin/activate`
# On Windows, use `venv\Scripts\activate`

4. Install the Required Libraries:

`pip install -r requirements.txt`

4. Configure Tesseract Path:
Update the tesseract_cmd path in app.py to point to your Tesseract executable if not installed in default location

5. Configure Poppler Path:
Add the Poppler bin directory to your system's PATH, or update the poppler_path in app.py to point to your Poppler bin directory.

Running the Application
1. Start the Flask Application:

`python app.py`

2. Access the Web Interface:
Open your web browser and navigate to http://127.0.0.1:5000/.

Usage
-------------------------------------------
Upload an image (PNG, JPEG, JPG) or PDF file.
Click the "Upload" button.
View the recognized text on the web page.

Contributing
Feel free to fork the repository and submit pull requests for any enhancements, bug fixes, or other contributions.
