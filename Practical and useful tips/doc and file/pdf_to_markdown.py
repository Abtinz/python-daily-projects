'''
MarkItDown is a lightweight Python utility for converting various files to Markdown for use with LLMs and related text analysis pipelines.
To this end, it is most comparable to textract, but with a focus on preserving important document structure and content as Markdown
(including: headings, lists, tables, links, etc.) While the output is often reasonably presentable and human-friendly, it is meant to be consumed by text analysis tools 
-- and may not be the best option for high-fidelity document conversions for human consumption.

git clone git@github.com:microsoft/markitdown.git
cd markitdown
pip install -e 'packages/markitdown[all]'
'''

import os
from markitdown import MarkItDown

def convert_pdfs_to_markdown(directory):
    """
        this function will convert every .pdf file inside the given directory to a .md file using markitdown.
        the generated markdown file is saved next to the original pdf with the same name.
        args ->
            directory: the directory path (string) which contains the .pdf files we wanna convert
    """
    markitdown = MarkItDown()
    for filename in os.listdir(directory):
        if filename.lower().endswith(".pdf"):
            pdf_path = os.path.join(directory, filename)
            md_path = os.path.splitext(pdf_path)[0] + ".md"
            result = markitdown.convert(pdf_path)
            with open(md_path, "w", encoding="utf-8") as md_file:
                md_file.write(result.text_content)
            print(f"{pdf_path} is converted to markdown and saved as\n{md_path}")

try:
    pdf_directory = "/Users/abtinzandi/Documents/Documents - Abtin’s MacBook Air/IDINEXT/"
    convert_pdfs_to_markdown(pdf_directory)

except Exception as error:
    print(f"An error occurred: {error}")
