import pytest

from src.classes import Category, Product


@pytest.fixture()
def product() -> Product:
    return Product("Лимон", 30, 40, "Цитрусовый фрукт")


@pytest.fixture()
def category() -> Category:
    return Category("Фрукты", "Свежие плоды и ягоды")


def test_Product(product: Product) -> None:
    assert product.description == "Цитрусовый фрукт"
    assert product.name == "Лимон"
    assert product.check_price == 30


def test_check_price() -> None:
    product = Product("Помело", -30, 50, "Цитрусовый фрукт")
    assert product.description == "Цитрусовый фрукт"
    assert product.name == "Помело"
    try:
        _ = product.check_price
    except ValueError as e:
        assert str(e) == "Цена не должна быть нулевая или отрицательная"


def test_Category(category: Category) -> None:
    assert category.name == "Фрукты"
    assert category.description == "Свежие плоды и ягоды"


def test_add_prducts(product: Product, category: Category) -> None:
    category.add_product(product)
    category.add_product(Product("Апельсин", 45, 10, "Цитрусовый фрукт"))
    assert Category.category_count == 1
    assert Category.product_count == 2


def test_add_products() -> None:
    pr1 = Product("Лимон", 30, 40, "Цитрусовый фрукт")
    pr2 = Product("Апельсин", 45, 10, "Цитрусовый фрукт")
    assert pr1 + pr2 == 1650


def test_return_Product_info(product: Product) -> None:
    assert str(product) == "Лимон, 30 руб. Остаток: 40 шт."


def test_return_Category_info(category: Category) -> None:
    assert str(category) == "Фрукты, количество продуктов: 2 шт."
