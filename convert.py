import PyPDF2
from PIL import Image
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfWriter
from tqdm import tqdm  

#
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\dreno\Desktop\UraitDownloader-main\tesseract.exe'  # Измените путь при необходимости

def ocr_pdf(input_pdf_path, output_pdf_path, poppler_path=None):
    
    images = convert_from_path(input_pdf_path, poppler_path=poppler_path)

    pdf_writer = PdfWriter()

    
    total_pages = len(images)
    progress_bar = tqdm(total=total_pages, desc="Обработка страниц", unit="page")

    for i, image in enumerate(images):
        
        text = pytesseract.image_to_pdf_or_hocr(image, lang='rus', extension='pdf')

        
        pdf_path = f"page_{i + 1}.pdf"
        with open(pdf_path, "w+b") as f:
            f.write(text)

       
        with open(pdf_path, "rb") as f:
            pdf_writer.add_page(PyPDF2.PdfReader(f).pages[0])

        
        progress_bar.update(1)

   
    progress_bar.close()

 
    with open(output_pdf_path, "wb") as f:
        pdf_writer.write(f)

    print(f"Текстовый PDF сохранен как {output_pdf_path}")

if __name__ == "__main__":
    input_pdf = "Основы финансовой грамотности.pdf"  
    output_pdf = "Выход.pdf"  
    poppler_path = r"C:\Users\dreno\Desktop\UraitDownloader-main\poppler-24.08.0\Library\bin"  # Путь к Poppler

    ocr_pdf(input_pdf, output_pdf, poppler_path)