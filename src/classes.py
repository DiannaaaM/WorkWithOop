from abc import ABC, abstractmethod
from typing import Any, List


class BaseProduct(ABC):
    @abstractmethod
    def __init__(self) -> None:
        pass

    @abstractmethod
    def __add__(self, other: Any) -> Any:
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass


class MixinLog:
    def __init__(self, name: Any, description: Any, price: Any, quantity: Any, *args: Any,  **kwargs: Any) -> None:
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        print(repr(self))

    def __repr__(self) -> str:
        return f"{self.name}, {self.description}, {self.__price}, {self.quantity}"


class Product(MixinLog, BaseProduct):
    name: str
    price: int
    quantity: int
    description: str

    def __init__(self, name: Any, price: Any, quantity: Any, description: Any) -> None:
        super().__init__(name, description, price, quantity)
        self.name = name
        self.__price = price
        self.quantity = quantity
        self.description = description

    @classmethod
    def new_product(cls, new_ret: dict) -> "Product":
        return cls(new_ret["name"], new_ret["price"], new_ret["quantity"], new_ret["description"])

    @property
    def check_price(self) -> int:
        return self._MixinLog__price

    @check_price.setter
    def check_price(self, new_price: int) -> None:
        try:
            if isinstance(new_price, int) and new_price <= 0:
                raise ValueError("Цена не должна быть нулевая или отрицательная")
        finally:
            self.__price = new_price

    def __str__(self) -> str:
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: Any) -> int:
        if isinstance(other, Product):
            return self.__price * self.quantity + other.check_price * other.quantity
        raise TypeError("Нельзя сложить это")

    def __repr__(self) -> str:
        return f"{self.name}, {self.description}, {self.check_price}, {self.quantity}"


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
        self.__products: List[Product] = []
        self.product_count = len(self.__products)

        Category.category_count += 1

    def add_product(self, product: Product) -> None:
        if isinstance(product, (LawnGrass, Smartphone)):
            self.__products.append(product)
            Category.product_count += 1
        else:
            print("Он недоступен")

    @property
    def return_product_info(self) -> str:
        product_info = []
        for product in self.__products:
            product_info.append(f"{product.name}, {product.check_price} rub. Quantity: {product.quantity} pcs.")
        return "\n".join(product_info)

    def middle_price(self) -> float:
        try:
            if not self.__products:
                return 0
            total_price = sum(product.check_price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0

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
