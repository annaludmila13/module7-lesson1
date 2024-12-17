class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"


class Shop:
    def __init__(self):
        self.__file_name = 'products.txt'

    def get_products(self):
        with open(self.__file_name, 'r') as file:
            content = file.read().strip()
        return content if content else ''

    def add(self, *products):
        existing_names = set()
        new_content = []

        try:
            with open(self.__file_name, 'r') as file:
                for line in file:
                    product_data = line.strip().split(', ')
                    existing_names.add(product_data[0])
        except FileNotFoundError:
            pass

        for product in products:
            if product.name not in existing_names:
                new_content.append(str(product))
                print(f"Добавлен новый продукт: {product}")
            else:
                print(f"Продукт {product.name} уже есть в магазине")

        with open(self.__file_name, 'a+') as file:
            for item in new_content:
                file.write(item + '\n')
# Создаем объекты класса Product
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

# Выводим результат метода __str__
print(p2)  # Spaghetti, 3.4, Groceries

# Создаем магазин
s1 = Shop()

# Добавляем продукты в магазин
s1.add(p1, p2, p3)

# Получаем список всех продуктов из файла
print(s1.get_products())

