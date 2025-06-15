## CODING CHALLENGE
# 25 MARKS
"""
A] Design a parent class called Planet

It must have:
- General attributes: name, distance_from_sun, planet_type
- A get_distance_to_earth() method that gives you the absolute distance from the Earth.

!!! You can take the distance from the Sun to the Earth as 147 million kilometres !!!

For example, if the planet’s distance_from_sun was 148 million kilometres when you call the get_distance_from_earth()
method, it should give us the distance like this: {'distance to earth’': 1000000} where the implied unit is kilometres.
This means that the planet is 1 million kilometres away from Earth.

   > This question uses an oversimplification of the solar system model, not taking into account orbit position or the
    eccentricity of the orbit, so in reality the result will be an approximate value with a reasonable margin of error.
"""

class Planet:
    def __init__(self, name, distance_from_sun, planet_type):
        self.name = name
        self.distance_from_sun = distance_from_sun
        self.planet_type = planet_type

    def get_distance_to_earth(self):
        distance = abs(147000000 - self.distance_from_sun)
        calc_distance = {'distance to earth': distance}
        return calc_distance


#TEST CASES
test_planet = Planet("Mars",148000000 , "terrestrial")
test_distance = test_planet.get_distance_to_earth()

print(vars(test_planet))
print(test_distance)


"""
B] Design a child class called Mercury, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class,
Your child class should also have a static method called happy_new_year(), which
would give us the information on how long a year lasts on the planet (in whatever way you wish!). 
You can take Earth Days as the implied unit.

After, create a Mercury object and print out the value of all its attributes and methods.

!!! HELPFUL INFO ABOUT MERCURY !!!
Distance from Sun: 58 million
Planet Type: Terrestrial
Time taken for the planet to orbit the sun: 88 Earth days
!!!!!!!!!!!!!!!!!!!!

"""
class Mercury(Planet):

    @staticmethod
    def happy_new_year():
        print("A year on Mercury is 88 Earth days long!")
## TEST CASE
test_mercury = Planet("Mercury",58000000, "rocky planet")
print(vars(test_mercury))
print(f"Planet is {test_mercury.name}")
print(f"Distance from sun is {test_mercury.distance_from_sun} km")
print(f"Planet type is {test_mercury.planet_type}")

from_earth = test_mercury.get_distance_to_earth()
print(from_earth)

Mercury.happy_new_year()

"""
C] Design a child class called Jupiter, which inherits from the Planet class.
This class should have exactly the same attributes as its parent class, as well as the additional attribute 
number_of_moons.
Your child class should also have a static method called happy_new_year(), which would give us the information on how 
long a year lasts on the planet (in whatever way you wish!). You can take Earth Days as the implied unit.

After, create a Jupiter object and print out the value of all its attributes and methods.


!!! HELPFUL INFO ABOUT JUPITER !!!
Distance from Sun: 779 million
Planet Type: Gas Giant
Time taken for the planet to orbit the sun: 4383 Earth days
Number of Moons: 80
!!!!!!!!!!!!!!!!!!!!

"""
class Jupiter(Planet):
    def __init__(self, number_of_moons, **kwargs):
        super().__init__(**kwargs)
        self.number_of_moons = number_of_moons

    @staticmethod
    def happy_new_year():
        print("One year on Jupiter lasts 4383 Earth days!")

## TEST CASE
jupiter_test = Jupiter(name = "Jupiter", distance_from_sun = 779000000, planet_type="Gas Giant", number_of_moons=80)
print(vars(jupiter_test))
print(f"Planet is {jupiter_test.name}")
print(f"Distance from sun is {jupiter_test.distance_from_sun} km")
print(f"Planet type is {jupiter_test.planet_type}")
print(f"Number of moons orbiting Jupiter is {jupiter_test.number_of_moons}!")

from_earth = jupiter_test.get_distance_to_earth()
print(from_earth)

Jupiter.happy_new_year()