# Attribute errors


class MyClass:
    pass


x = MyClass()
print(x.myproperty)

# ImportError
import my_module

# RuntimeError
1 / 0

# KeyError
my_dict = {"x": 5, "y": 10}
print(my_dictp['z'])

# TypeError
int([])

# ValueError
int("a")

# IOError
open("my_file.txt", 'r')
