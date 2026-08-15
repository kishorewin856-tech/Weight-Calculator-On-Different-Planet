planets = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.53,
    "Saturn": 1.07,
    "Uranus": 0.90,
    "Neptune": 1.14
}

weight = float(input("Enter your weight (kg): "))
print(" \n Weight on different planets: \n ")

for planet, g in planets.items():
    print(f"{planet}: {round(weight * g, 2)} kg")

    