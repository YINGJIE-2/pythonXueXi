
class Clock:
    id = None  #编号
    price = None  #价格

    def ring(self):
        import winsound
        winsound.Beep(2000,3000)

clock1=Clock()
clock1.id=220312
clock1.price=19.98
print(clock1.id)
print(clock1.price)

clock1.ring()