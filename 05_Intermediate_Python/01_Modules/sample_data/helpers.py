TAX_RATE = 0.15

def with_tax(amount):
    # Adds 15% VAT to a price.
    return amount * (1 + TAX_RATE)
