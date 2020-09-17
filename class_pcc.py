
class Dog:
    #name = "Kalu"
    def speak(self,name):
        print(f"Ghou!I'm {name} Ghou!")

fst_obj = Dog()
#fst_obj.name = "Lali"
fst_obj.speak('Lali')

class Cat:
    year = 0
    def sound(self):
        return self.year * 10

cat = Cat()
cat.year = 2
print(cat.sound())
