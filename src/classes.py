from typing import Any


class Product:
    name: str
    price: int
    quantity: int
    description: int

    def __init__(self, name: Any, price: Any, quantity: Any, description: Any) -> None:
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.description = description

    @classmethod
    def new_product(cls, new_ret: Any) -> Any:
        return Product(new_ret["name"], new_ret["price"], new_ret["quantity"], new_ret["description"])

    @property
    def check_price(self) -> Any:
        return self.__price

    @check_price.setter
    def check_price(self, chek_price: Any) -> Any:
        if isinstance(chek_price, int) and chek_price <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        return chek_price

    def __str__(
        self,
    ) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> Any:
        return self.__price * self.quantity + other.check_price * other.quantity


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
        self.__products: list = []
        self.product_count = len(self.__products)

        Category.category_count = 1

    def add_product(self, product: Any) -> None:
        self.__products.append(product)
        Category.product_count += 1

    @property
    def return_product_info(self) -> Any:
        product_info = []
        for product in self.__products:
            product_info.append(f"{product.name}, {product.check_price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_info)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."
