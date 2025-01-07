import pikepdf
from reportlab.pdfgen import canvas
from .utils import generate_xml

def create_invoice(data, output_pdf_path):
    """
    Create a ZUGFeRD-compliant PDF invoice.

    Args:
        data (dict): Invoice data (buyer, seller, items, etc.).
        output_pdf_path (str): Path to save the generated PDF.
    """
    # Step 1: Generate the PDF
    temp_pdf = "temp_invoice.pdf"
    c = canvas.Canvas(temp_pdf)
    c.drawString(100, 750, f"Invoice for {data['buyer']['name']}")
    c.drawString(100, 730, f"Amount: {data['amount']}")
    c.save()

    # Step 2: Generate ZUGFeRD XML
    xml_data = generate_xml(data)

    # Step 3: Embed XML in PDF/A-3
    with pikepdf.Pdf.open(temp_pdf) as pdf:
        # Attach the XML file
        pdf.attachments['zugferd-invoice.xml'] = xml_data
        pdf.save(output_pdf_path)

    print(f"Invoice created at: {output_pdf_path}")
