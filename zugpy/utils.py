# zugpy/utils.py
import xml.etree.ElementTree as ET

def generate_xml(data):
    """
    Generate ZUGFeRD-compliant XML from invoice data.
    
    Args:
        data (dict): Invoice data.
    Returns:
        bytes: XML content as bytes.
    """
    root = ET.Element("Invoice")
    buyer = ET.SubElement(root, "Buyer")
    buyer_name = ET.SubElement(buyer, "Name")
    buyer_name.text = data['buyer']['name']
    amount = ET.SubElement(root, "Amount")
    amount.text = str(data['amount'])
    return ET.tostring(root, encoding="utf-8")
