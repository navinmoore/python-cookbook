# -*-coding:utf-8-*-

class Person1:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError('Excepted a string')
        self._first_name = value
            
    def del_first_name(self):
        raise AttributeError("Can't delete a attribute")
        
    name = property(get_first_name, set_first_name, del_first_name) 
