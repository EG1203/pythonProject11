class MyObject:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Объект MyObject с x = {self.x} и y = {self.y}"

    def process_fields(self):
        try:
            result = self.x // self.y
            print(f"Результат деления x на y: {result}")
            return result
        except ZeroDivisionError:
            print("Ошибка: Деление на ноль.")
            return None

obj = MyObject(10, 3)
print(obj)
obj.process_fields()
