# Monkey Patching
import my_module

def new_greet():
    return "Hello, from patched function!"

my_module.greet = new_greet  # Заменяем функцию

print(my_module.greet())  # Вывод: "Hello, from patched function!"
