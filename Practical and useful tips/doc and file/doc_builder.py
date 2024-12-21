from docx import Document

# Create a new Document
doc = Document()

# Add content to the document
doc.add_paragraph("test paragraph builder ...")

# Save the document
doc_path = ".\doc_test.docx"
doc.save(doc_path)