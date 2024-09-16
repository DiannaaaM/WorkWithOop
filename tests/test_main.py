import pytest

from src.main import Category, Product


@pytest.fixture()
def product() -> Product:
    return Product("Лимон", 30, 40, "Цитрусовый фрукт")


@pytest.fixture()
def category() -> Category:
    return Category("Фрукты", "Свежие плоды и ягоды")


def test_Product(product: Product) -> None:
    assert product.description == "Цитрусовый фрукт"
    assert product.name == "Лимон"
    assert product.price == 30


def test_Category(category: Category) -> None:
    assert category.name == "Фрукты"
    assert category.description == "Свежие плоды и ягоды"


def test_add_prducts(product: Product, category: Category) -> None:
    category.add_product(product)
    category.add_product(Product("Апельсин", 45, 10, "Цитрусовый фрукт"))
    assert Category.category_count == 1
    assert Category.product_count == 2
