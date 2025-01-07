#pip install PyPDF2
from PyPDF2 import PdfMerger

def merge_pdfs(pdf_files, output_filename):
    """
        this function will merges the given PDF files into a single PDF and saves it.
        args ->
            pdf_files: an array of files urls in string format
            output_filename -> the specific output root which we wanna save the merged file
    """
    merger = PdfMerger()
    for pdf in pdf_files:
        merger.append(pdf)
    merger.write(output_filename)
    merger.close()
    print(f"given files {pdf} are merged as a new PDF which is saved as\n{output_filename}")

try:
    pdf1 = ".....url1.pdf" 
    pdf2 = ".....url2.pdf" 
    merged_filename = ".....url3.pdf"
    merge_pdfs([pdf1, pdf2], merged_filename)

except Exception as error:
    print(f"An error occurred: {error}")