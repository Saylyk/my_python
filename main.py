class Trafficlight:
    _color = ["Красный", "Желтый", "Зеленый"]
def running(self):
    i = 0
   while i != 3:
      print(Trafficlight._color[i])
   if i == 0
      sleep(7)
   elif i == 1:
      sleep(2)
   elif i == 2:
      sleep(5)
   i += 1

t = Trafficlight()
t.running()
##


class Road:

    def __init__(self, length.width):
        self.length = length
        self._width = width
        self.weigth = 25
        self.heigt = 5
    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weigth * self.heidth / 1000
        print(f"Для покрытия всего дорожного полотна необходимо {round(asphalt_mass)}массы асфальта}
r = Road(5000, 20)
r.asphalt_mass()

#
class Worker:
    def_init_(self, name, surname, position, wage, bonus):
       self.name = name
       self.surname = surname
       self.position = position
       self._income = {"wage":int(wage), "bonus": int(bonus)}
class Position(Worker):
    def_init_(self, name, surname, position, wage, bonus):
       super()._init_(name, surname, position, wage, bonus)