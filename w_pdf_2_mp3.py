# PDF to Audiobook
# pip install PyPDF4
# pip install gTTS
from PyPDF4 import PdfFileReader
from gtts import gTTS
def Pdf_to_Audio(file_name):
    pdf = PdfFileReader(file_name)
    for page in range(pdf.getNumPages()):
        text = pdf.getPage(page).extractText()
        tts = gTTS(text=text, lang='en')
        tts.save(f"{page}.mp3")
Pdf_to_Audio("book.pdf")