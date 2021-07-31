"""
In Python, Interfaces are simply callable which is a in built interface.
Use "I" in front of the class name to identify the interface class in python.
we use classes as interface in python because classes are first class objects in python.

So simply all the child classes has a common method which might have different implementation based on the type of class.
This common method is then called in factory method to create objects at runtime.

"""

from abc import abstractmethod, ABCMeta


class IHuman(metaclass=ABCMeta):
    """
    Interface class
    """

    @abstractmethod
    def build_object(self):
        """ Interface Method """


class Student(IHuman):
    def __init__(self):
        self.name = self.__class__.__name__
        pass

    @classmethod
    def build_object(cls):
        print("Building student object...")
        return cls()


class Developer(IHuman):
    def __init__(self):
        self.name = self.__class__.__name__
        pass

    @classmethod
    def build_object(cls):
        print("Building Developer object...")
        return cls()


class Youtuber(IHuman):
    def __init__(self):
        self.name = self.__class__.__name__
        pass

    @classmethod
    def build_object(cls):
        print("Building Youtuber object...")
        return cls()


class HumanFactory:
    available_object = [Developer, Youtuber, Student]

    @classmethod
    def get_objects(cls, _type):
        if _type not in cls.available_object:
            print("Unknown type! can not generate object")
        else:
            print(f'Initializing build process...')
            obj = _type.build_object()
            print(f'Object built for {obj.name}.')


if __name__ == '__main__':
    for obj_ in HumanFactory.available_object:
        HumanFactory.get_objects(obj_)
        print()


