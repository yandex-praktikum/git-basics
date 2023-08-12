class FloatValue:
    def __set_name__(self, owner, name):
        set.name = "_"+name

    def __set__(self, instance, value):