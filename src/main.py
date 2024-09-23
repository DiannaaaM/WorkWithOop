from src.classes import Category, Product

# Category
category = Category("Фрукты", "Свежие плоды и ягоды")
category.add_product(Product("Лимон", 30, 40, "Цитрусовый фрукт"))
category.add_product(Product("Апельсин", 45, 10, "Цитрусовый фрукт"))
print(category.return_product_info)
print(category)

# Product
pr1 = Product("Лимон", 30, 40, "Цитрусовый фрукт")
pr2 = Product("Апельсин", 45, 10, "Цитрусовый фрукт")
print(pr1)
