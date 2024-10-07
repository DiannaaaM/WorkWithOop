import pytest

from src.classes import BaseProduct, Category, LawnGrass, Product, Smartphone


@pytest.fixture()
def product() -> Product:
    return Product("Лимон", 30, 40, "Цитрусовый фрукт")


@pytest.fixture()
def category() -> Category:
    return Category("Фрукты", "Свежие плоды и ягоды")


@pytest.fixture()
def smatphone() -> Category:
    return Category("Смартфоны", "Техника")


@pytest.fixture()
def lawnGrass() -> Category:
    return Category("Растения", "Семена")


@pytest.fixture()
def smartphone_iphone() -> Smartphone:
    return Smartphone(
        "High",
        "iPhone 13 Pro",
        "256GB",
        "Silver",
        "iPhone 13 Pro",
        1299.99,
        10,
        "The latest iPhone with advanced features and high performance.",
    )


@pytest.fixture()
def smartphone_xiaomi() -> Smartphone:
    return Smartphone(
        "High",
        "Xiaomi Mi 11 Ultra",
        "512GB",
        "Ceramic Black",
        "Xiaomi Mi 11 Ultra",
        1199.99,
        6,
        "A premium smartphone with top-tier specifications and innovative design.",
    )


@pytest.fixture()
def lawnGrass_tomato() -> LawnGrass:
    return LawnGrass("USA", 7, "Red", "Tomato Seeds", 2.99, 100, "High-quality tomato seeds for home gardening.")


@pytest.fixture()
def lawnGrass_sunflower() -> LawnGrass:
    return LawnGrass(
        "Russia", 10, "Yellow", "Sunflower Seeds", 1.99, 200, "Easy-to-grow sunflower seeds for a vibrant garden."
    )


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
    assert Category.product_count == 0


def test_add_products() -> None:
    pr1 = Product("Лимон", 30, 40, "Цитрусовый фрукт")
    pr2 = Product("Апельсин", 45, 10, "Цитрусовый фрукт")
    assert pr1 + pr2 == 1650


def test_return_Product_info(product: Product) -> None:
    assert str(product) == "Лимон, 30 руб. Остаток: 40 шт."


def test_return_Category_info(category: Category) -> None:
    assert str(category) == "Фрукты, количество продуктов: 0 шт."


def test_Smartphone(smartphone_iphone: Smartphone) -> None:
    assert smartphone_iphone.description == "The latest iPhone with advanced features and high performance."
    assert smartphone_iphone.name == "iPhone 13 Pro"
    assert smartphone_iphone.check_price == 1299.99


def test_LawnGrass(lawnGrass_sunflower: LawnGrass) -> None:
    assert lawnGrass_sunflower.quantity == 200
    assert lawnGrass_sunflower.check_price == 1.99
    assert lawnGrass_sunflower.color == "Yellow"
    assert lawnGrass_sunflower.germination_period == 10


def test_add_products2(
    smartphone_iphone: Smartphone,
    smartphone_xiaomi: Smartphone,
    lawnGrass_sunflower: LawnGrass,
    lawnGrass_tomato: LawnGrass,
) -> None:
    assert smartphone_xiaomi + smartphone_iphone == 20199.84
    assert lawnGrass_tomato + lawnGrass_sunflower == 697.0


def test_count_categories(
    smatphone: Category, lawnGrass: Category, smartphone_iphone: Smartphone, lawnGrass_sunflower: LawnGrass
) -> None:
    smatphone.add_product(lawnGrass_sunflower)
    smatphone.add_product(smartphone_iphone)
    assert Category.product_count == 2


def test_Product_class() -> None:
    assert BaseProduct == BaseProduct
    assert issubclass(Product, BaseProduct)


def test_middle_price(smatphone):
    assert smatphone.middle_price() == 0
