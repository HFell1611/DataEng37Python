class Spartan:
    def __init__(self, name, age, stream, course, client):
        self.role = "Spartan"
        self.name = name
        self.age = age
        self.stream = stream
        self.course = course
        self.client = client

    def info(self):
        return f"This is {self.name}, he is {self.age} and he is a {self.role}"


harry = Spartan(
    name="Harry",
    course="Data 37",
    age="25",
    stream="Data Engineering",
    client="Home Office"
)


class Car:
    def __init__(self, make, model, top_speed):
        self.make = make
        self.model = model
        self.top_speed = top_speed
        self.speed = 0

    def accelerate(self, speed_add):
        if self.speed + speed_add > self.top_speed:
            self.speed = self.top_speed
        else:
            self.speed += speed_add

    def brake(self, speed_sub):
        if self.speed - speed_sub == 0:
            self.speed = 0
        else:
            self.speed -= speed_sub


car = Car("Hyundai", "i20", 150)
car.accelerate(50)
car.brake(20)
car.accelerate(150)

print(car.speed)


class Bird:
    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = can_fly
        self._age = 0

    def reproduce(self):
        if self._age < 2:
            return "Too young"
        else:
            return "Laying eggs..."

    def age_up(self, years=1):
        self._age += years

    def get_age(self):
        return self._age


class Penguin(Bird):
    def __init__(self, subspecies, colour=("Black", "White")):
        super().__init__("Penguin", colour, False)
        self.subspecies = subspecies

    def hunt_for_fish(self):
        return "Splash"


class Emperor(Penguin):
    def __init__(self, name, gender):
        super().__init__("Emperor", ("Black", "White", "Orange"))
        self.name = name
        self.gender = gender

    def info(self):
        return f"Their name is {self.name} and they are {self.gender}"

# Instantiate an object


# bird = Bird("Sparrow", "Brown")
#
# # Calling methods
# bird.age_up()
# bird.age_up()
# bird.age_up()
# egg = bird.reproduce()
# print(egg)
# print(bird.get_age())

# penguin = Penguin("Rockhopper")
# print(penguin.get_age())
# print(penguin.can_fly)

emperor = Emperor("Jeff", "Male")

print(emperor.info())

