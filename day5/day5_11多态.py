class Animal:  # 空实现的方法，抽象类！！
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("汪汪汪")


class Cat(Animal):
    def speak(self):
        print("喵喵喵")


def make_noise(animal: Animal):
    animal.speak()


# 两个对象演示多态
dog = Dog()
cat = Cat()

make_noise(dog)
make_noise(cat)


# 演示抽象类

class AC:

    def cool_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_l_r(self):
        """左右摆风"""
        pass


class Midea_AC(AC):
    def cool_wind(self):
        print("美的空调制冷")

    def hot_wind(self):
        print("美的空调制热")
    
    def swing_l_r(self):
        print("美的空调左右摆风")


class Geli_AC(AC):
    def cool_wind(self):
        print("格力空调制冷")

    def hot_wind(self):
        print("格力空调制热")

    def swing_l_r(self):
        print("格力空调左右摆风")


def cool_wind(ac: AC):
    ac.cool_wind()


midea_ac = Midea_AC()
geli_ac = Geli_AC()

cool_wind(midea_ac)
cool_wind(geli_ac)
