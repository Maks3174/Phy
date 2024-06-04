#1
class AdditionalFunctionalityMeta(type):
    def __new__(cls, name, bases, dct):
        dct['additional_functionality'] = lambda self: print("Additional functionality added!")

        return super().__new__(cls, name, bases, dct)


class MyClass(metaclass=AdditionalFunctionalityMeta):
    def __init__(self, x):
        self.x = x


obj = MyClass(10)
obj.additional_functionality()


#2
class AttributeCheckMeta(type):
    required_attributes = ['attr1']

    def __init__(cls, name, bases, dct):
        for attr in cls.required_attributes:
            if attr not in dct:
                raise AttributeError(f"Class '{name}' must have attribute '{attr}'")
        super().__init__(name, bases, dct)


class MyClass1(metaclass=AttributeCheckMeta):
    attr1 = 'value1'
    attr2 = 'value2'


class MyClass2(metaclass=AttributeCheckMeta):
    attr1 = 'value1'


obj1 = MyClass1()
print("Attributes of MyClass1:", obj1.attr1, obj1.attr2)

obj2 = MyClass2()
print("Attributes of MyClass2:", obj2.attr1)

#3
class InheritanceControlMeta(type):
    def __new__(cls, name, bases, dct):
        for base in bases:
            if base.__name__ == 'ForbiddenBaseClass':
                raise TypeError(f"Class '{name}' cannot inherit from '{base.__name__}'")

        if 'AdditionalBaseClass' in [base.__name__ for base in bases]:
            bases = (AdditionalBaseClass,) + tuple(base for base in bases if base.__name__ != 'AdditionalBaseClass')

        return super().__new__(cls, name, bases, dct)


class ForbiddenBaseClass:
    pass

class AdditionalBaseClass:
    pass

class MyClass1(metaclass=InheritanceControlMeta):
    pass

class MyClass2(MyClass1):
    pass

class MyClass3(AdditionalBaseClass, MyClass1):
    pass

print("MyClass3 bases:", [base.__name__ for base in MyClass3.__bases__])

#4
class ClassRegistryMeta(type):
    registry = {}

    def __init_subclass__(cls, **kwargs):
        cls.registry[cls.__name__] = cls
        super().__init_subclass__(**kwargs)


class MyClass1(metaclass=ClassRegistryMeta):
    pass

class MyClass2(metaclass=ClassRegistryMeta):
    pass

class MyClass3(metaclass=ClassRegistryMeta):
    pass

print("Registered classes:", ClassRegistryMeta.registry.keys())
