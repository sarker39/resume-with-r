from pdf2docx import Converter

# Define the PDF path and the output DOCX path
pdf_path = './CV_DevPNS.pdf'
docx_path = './CV_DevPNS_converted.docx'

# Convert PDF to DOCX
converter = Converter(pdf_path)
converter.convert(docx_path, start=0, end=None)
converter.close()

# Return the path to the converted DOCX file
docx_path

