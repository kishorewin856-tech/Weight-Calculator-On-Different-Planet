import tkinter as tk

def calculate_weight():
    planets = {
    "Mercury": 0.38,
    "Venus": 0.91,
    "Mars": 0.38,
    "Jupiter": 2.53,
    "Saturn": 1.07,
    "Uranus": 0.90,
    "Neptune": 1.14
    }
    weight = float(entry.get())
    result.config(text=" \n Weight on different planets: \n ")
    for planet, g in planets.items():
        result.config(text=result.cget("text") + f"Weight on {planet}: {round(weight * g, 2)} kg\n")


#window
root = tk.Tk()
root.title("Your Weight on Different Planets")
root.geometry("400x400")

#lable
label = tk.Label(root, text="Enter your weight On Earth(kg):")
label.pack()

#Enter data
entry = tk.Entry(root)
entry.pack()

#Button_to_calculate
button = tk.Button(root, text="Calculate", command=calculate_weight)
button.pack()

#result
result = tk.Label(root, text="")
result.pack()

root.mainloop()