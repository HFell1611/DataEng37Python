class Dog:
    def __init__(self, dog_name, colour):  # initialise
        self.animal_type = "canine"
        self.legs = 4
        self.name = dog_name
        self.colour = colour

#    animal_type = "canine"  # class variable

    def bark(self):  # self means the current class
        return f"Woof! I am a {self.animal_type}"


# fido = Dog()  # instantiation = creating in INSTANCE of the class
# print(fido.animal_type)
# # print(fido.bark())
#
# lassie = Dog()
# print(lassie.animal_type)
# # print(lassie.bark())
#
# # print(fido)
# # print(type(fido))
#
# Dog.animal_type = "arachnid"
# Dog.legs = 8
#
# print(fido.legs)
# print(lassie.animal_type)
# print(fido.bark())
#
# fido.legs = 3
# print(fido.legs)

fido = Dog("Fido", "Black")
print(fido.animal_type)
print(fido.name)
print(fido.colour)
