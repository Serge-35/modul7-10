# Фабрика функций для умножения и деления:
def create_operation(operation):
    if operation == "multipl":
        def multipl(x, y):
            return x * y
        return multipl # возвращаем функцию как объект!! Тут скобки не нужны
    elif operation == "division":
        def division(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                print('Error: Division by zero')
        return division

my_func_mul = create_operation("multipl")
print(my_func_mul(2,3))
my_func_div = create_operation("division")
print(my_func_div(10,5))
print(my_func_div(10,0))


# Пример лямбда функции с аналогом через def
multiply = lambda x: x ** 2
print(multiply(4)) #Выводит 16

def multiply_def(x):
   return x ** 2
print(multiply_def(4)) # Выводит 16

# Пример создания вызываемого объекта
class Square:
   def __init__(self, a, b):
       self.a = a
       self.b = b

   def __str__(self):
       return (f'Стороны: {self.a}, {self.b}\nПлощадь: {self.a * self.b}')

area_of_the_rectangle = Square(2, 4)
print(area_of_the_rectangle)
