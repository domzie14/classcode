# inheritance

'''Define a class Human. Give it some attributes: name, age, gender, ability(class called Ability, with attributes: speed, height, strength as numbers)
   and that is an attribute of the class Human. 

   And define a class Student that inherits from Human and has methods: learn, sleep, eat that does whatever you want to put there.
'''

class Animal:
   number_of_animals_created = 0

   def __init__(self, eating_speed, sound="Shout"):
      self.sound = sound
      self.hunger = 100
      self.eating_speed = eating_speed
      Animal.number_of_animals_created += 1
    
   def make_a_sound(self):
      return f"Making the sound: {self.sound}"
   
   def feed(self, food_count):
      self.hunger -= food_count * self.eating_speed
      print(f"{type(self).__name__} has eaten {food_count}")
    
class Elephant(Animal):
   number_of_animals_created = 0
   def __init__(self):
      super().__init__(eating_speed=4)
      Elephant.number_of_animals_created += 10
   
   def make_a_sound(self):
      return super().make_a_sound()
   
   def feed(self,food_count=10):
      print("Here's a magnificent elephant feeding...")
      super().feed(food_count)

   def __str__(self):
      return "[[ Elephant ]]"
   


elephant = Elephant()
elephant.feed(40)
elephant2 = Elephant()

print(elephant.number_of_animals_created)
print(elephant2.number_of_animals_created)

print(elephant.hunger)
print(elephant2.hunger)

print(elephant)
