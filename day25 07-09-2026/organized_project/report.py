from .inventory import get_inventory
from .utils import total_cost


def create_report():
    products = get_inventory()
    item_names = [product["name"] for product in products]
    total = total_cost([product["price"] for product in products])

    return {
        "items": item_names,
        "total_price": total,
    }
