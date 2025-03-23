import importlib
import module_b
import time
import sys
print(module_b.hello_from_b())

time.sleep(10)
# Вносим изменения в module_a.py

importlib.reload(module_b)  # Перезагружаем модуль A
importlib.reload(sys.modules['module_a'])  # Перезагружаем модуль B

print(module_b.hello_from_b())
