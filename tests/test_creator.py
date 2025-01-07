# tests/test_creator.py
from zugpy.creator import create_invoice

def test_create_invoice():
    data = {
        "buyer": {"name": "John Doe"},
        "amount": 100.0,
    }
    create_invoice(data, "test_invoice.pdf")
    assert True  # Add proper checks for output files
