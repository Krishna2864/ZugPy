# zugpy/validator.py
import pikepdf
from xmlschema import XMLSchema
from .constants import ZUGFERD_SCHEMA_PATH

def validate_invoice(pdf_path):
    """
    Validate the ZUGFeRD invoice.
    
    Args:
        pdf_path (str): Path to the PDF invoice.
    Returns:
        dict: Validation results.
    """
    with pikepdf.Pdf.open(pdf_path) as pdf:
        for name, attachment in pdf.attachments.items():
            if name.endswith(".xml"):
                xml_data = attachment.read_bytes()
                schema = XMLSchema(ZUGFERD_SCHEMA_PATH)
                is_valid = schema.is_valid(xml_data)
                return {"is_valid": is_valid, "errors": schema.validate(xml_data)}
    return {"is_valid": False, "errors": "No ZUGFeRD XML found in the PDF."}
