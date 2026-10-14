TAX_RATE = 0.08  # 8% tax rate for e-commerce calculations

def calculate_order_total(items, discount_percent=0.0):
    """
    Calculates subtotal, applies optional discount, adds tax, and returns rounded total.
    items format: [{'name': 'Backpack', 'price': 29.99, 'quantity': 2}]
    """
    if not items:
        return 0.0

    # List iteration and math using generator expression
    subtotal = sum(item["price"] * item["quantity"] for item in items)
    
    if discount_percent > 0:
        subtotal -= subtotal * (discount_percent / 100)

    total = subtotal + (subtotal * TAX_RATE)
    return round(total, 2)


def validate_order(order):
    """
    Validates order dictionary keys, data types, and status fields.
    """
    required_keys = ["order_id", "customer_email", "status"]
    
    # Check for missing or empty required string fields
    for key in required_keys:
        if key not in order or not order[key]:
            return "INVALID_MISSING_FIELDS"

    # Validate items structure specifically so empty lists return the correct error
    if "items" not in order or not isinstance(order["items"], list) or len(order["items"]) == 0:
        return "INVALID_EMPTY_ITEMS"

    # Validate status values
    valid_statuses = ["PENDING", "PROCESSING", "COMPLETED", "CANCELLED"]
    if order["status"] not in valid_statuses:
        return "INVALID_STATUS"

    return "VALID"


def update_order_status(order, new_status):
    """
    Updates order status based on allowed business rule transitions.
    """
    valid_transitions = {
        "PENDING": ["PROCESSING", "CANCELLED"],
        "PROCESSING": ["COMPLETED", "CANCELLED"],
        "COMPLETED": [],
        "CANCELLED": []
    }

    current_status = order.get("status")
    
    if new_status in valid_transitions.get(current_status, []):
        order["status"] = new_status
        return True
    return False
