#### [Dependencies] ###########
#   pip install PyPDF2        #
#   pip install pycryptodome  #
####[Dependencies] ############

from PyPDF2 import PdfReader, PdfWriter

reader = PdfReader("yourfile.pdf")
writer = PdfWriter()

if reader.is_encrypted:
    reader.decrypt("Your password")

# Add all pages to the writer
for page in reader.pages:
    writer.add_page(page)

# Save the new PDF to a file
with open("decrypted-pdf.pdf", "wb") as f:
    writer.write(f)
