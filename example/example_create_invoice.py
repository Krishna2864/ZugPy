# Save this in the root directory as example_create_invoice.py
from zugpy.creator import create_invoice

# Sample data
invoice_data = {
    "buyer": {"name": "John Doe"},
    "amount": 150.0,
}

# Create invoice
create_invoice(invoice_data, "output_invoice.pdf")
print("Invoice created!")
