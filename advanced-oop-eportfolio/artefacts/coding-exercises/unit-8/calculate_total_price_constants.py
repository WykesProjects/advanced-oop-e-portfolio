BOOK_DISCOUNT_FACTOR = 0.90
ELECTRONICS_DISCOUNT_FACTOR = 0.80

def calculate_total_price(items: list[dict]) -> float:
    total = 0.0

    for item in items:
        item_type = item.get("type")
        price = float(item.get("price", 0.0))

        if item_type == "book":
            total += price * BOOK_DISCOUNT_FACTOR
        elif item_type == "electronics":
            total += price * ELECTRONICS_DISCOUNT_FACTOR
        else:
            total += price

    return total
