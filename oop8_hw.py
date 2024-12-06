#1
def additional_logic(func):
    def wrapper(*args, **kwargs):
        print("Додаткова логіка перед викликом функції")
        return func(*args, **kwargs)
    return wrapper

class MyClass:
    @additional_logic
    def foo(self):
        print("Виклик методу foo")

    @additional_logic
    def bar(self):
        print("Виклик методу bar")

obj = MyClass()
obj.foo()
obj.bar()


#2
def modify_class_name(cls):
    class ModifiedClass(cls):
        pass

    ModifiedClass.__name__ = "Modified_" + cls.__name__

    return ModifiedClass


@modify_class_name
class MyClass:
    pass


print(MyClass.__name__)

#3
def add_attributes(cls):
    setattr(cls, 'added_attribute', "This is an added attribute")
    return cls

@add_attributes
class MyClass:
    pass

print(hasattr(MyClass, 'added_attribute'))
print(MyClass.added_attribute)

#4
def process_init(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        print("Перевірка та обробка аргументів у __init__")

        original_init(self, *args, **kwargs)

    cls.__init__ = new_init

    return cls

@process_init
class MyClass:
    def __init__(self, arg1, arg2):
        self.arg1 = arg1
        self.arg2 = arg2

obj = MyClass(10, 20)
