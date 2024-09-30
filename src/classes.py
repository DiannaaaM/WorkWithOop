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
        if type(other) == type(self):
            return self.__price * self.quantity + other.check_price * other.quantity
        return "Нельзя сложить это"


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
        if isinstance(product, (LawnGrass, Smartphone)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Этого у нас нет")

    @property
    def return_product_info(self) -> Any:
        product_info = []
        for product in self.__products:
            product_info.append(f"{product.name}, {product.check_price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_info)

    def __str__(self) -> str:
        return f"{self.name}, количество продуктов: {Category.product_count} шт."


class Smartphone(Product):
    efficiency: str
    model: str
    memory: str
    color: str

    def __init__(
        self,
        efficiency: Any,
        model: Any,
        memory: Any,
        color: Any,
        name: Any,
        price: Any,
        quantity: Any,
        description: Any,
    ) -> None:
        super().__init__(name, price, quantity, description)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country: str
    germination_period: int
    color: str

    def __init__(
        self, country: Any, germination_period: Any, color: Any, name: Any, price: Any, quantity: Any, description: Any
    ) -> None:
        super().__init__(name, price, quantity, description)
        self.country = country
        self.germination_period = germination_period
        self.color = color
