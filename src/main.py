from src.classes import Category, Product

category = Category("Фрукты", "Свежие плоды и ягоды")
category.add_product(Product("Лимон", 30, 40, "Цитрусовый фрукт"))
category.add_product(Product("Апельсин", 45, 10, "Цитрусовый фрукт"))
print(category.return_product_info)
