from flask import Flask, render_template, request, flash
from PIL import Image, UnidentifiedImageError
import pytesseract
import io
from pdf2image import convert_from_bytes
import tempfile


app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Replace with a strong secret key

pytesseract.pytesseract.tesseract_cmd = r'C:\path\to\tesseract' #add direct path if not installed in default location

    # Perform OCR on each image
def ocr_pdf(pdf_bytes):
    # Convert PDF to a list of images
    popplerpath = r'C:\path\to\bin'  #add direct path if not installed in default location
    images = convert_from_bytes(pdf_bytes, poppler_path=popplerpath)

    # Perform OCR on each image
    text = ""
    for image in images:
        text += pytesseract.image_to_string(image)
    return text

def ocr_image(image):
    text = pytesseract.image_to_string(image)
    return text

@app.route('/', methods=['GET', 'POST'])
def index():
    text = None
    if request.method == 'POST':
        file = request.files['file']
        if file:
            # Check file extension
            if not file.filename.endswith(('.png', '.jpg', '.jpeg','.pdf')):
                flash('Invalid file type. Please upload an image or pdf file.', 'error')
                return render_template('index.html', text=text)

            # Check file size (e.g., 5 MB limit)
            file.seek(0, 2)  # Seek to the end of the file
            file_size = file.tell()
            if file_size > 5 * 1024 * 1024:  # 5 MB
                flash('File size exceeds the limit. Please upload a smaller image.', 'error')
                return render_template('index.html', text=text)
            file.seek(0)  # Reset file pointer to the beginning
            
            # Check if the file is a PDF
            if file.filename.endswith('.pdf'):
                pdf_bytes = file.read()  # Read the bytes of the uploaded PDF file
                text = ocr_pdf(pdf_bytes)  # Pass the bytes to the ocr_pdf function
 
            else:
             # Check MIME type
                mime_type = file.content_type
                if mime_type not in ['image/png', 'image/jpeg']:
                    flash('Invalid file format. Please upload a PNG or JPEG image.', 'error')
                    return render_template('index.html', text=text)
                
           # Process the image
                try:
                    image = Image.open(io.BytesIO(file.read()))
                    text = ocr_image(image)
                except UnidentifiedImageError:
                    flash('Invalid image file. Please upload a valid PNG or JPEG image.', 'error')
                    return render_template('index.html', text=text)

    return render_template('index.html', text=text)

if __name__ == '__main__':
    app.run(debug=True)