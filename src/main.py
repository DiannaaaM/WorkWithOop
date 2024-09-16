from typing import Any


class Product:
    name: str
    price: int
    quantity: int
    description: int

    def __init__(self, name: Any, price: Any, quantity: Any, description: Any) -> None:
        self.name = name
        self.price = price
        self.quantity = 0
        self.description = description


class Category:
    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    category_count = 0
    product_count = 0

    def __init__(self, name: Any, description: Any) -> None:
        self.name = name
        self.description = description
        self.products = []
        self.product_count = len(self.products)

        Category.category_count = 1

    def add_product(self, product: Any) -> None:
        self.products.append(product)
        Category.product_count += 1
