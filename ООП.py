class Circle:
    attrs = {"x": (int, float), "y": (int, float), "radius": (int, float)}

    def __init__(self, x, y, radius):
        self.__x = self.__y = self.__radius = None
        self.x = x
        self.y = y
        self.radius = radius

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, value):
        self.__radius = value

    def __setattr__(self, key, value):
        if key in self.attrs and type(value) not in self.attrs[key]:
            raise TypeError('Неверный тип присваиваемых данных.')
        if key == "radius" and value <= 0:
            return
        super().__setattr__(key, value)

    def __getattr__(self, item):
        return False
