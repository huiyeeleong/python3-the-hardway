name = 'Hui'
age = 35
height = 74
weight = 180
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

centimeters_in_height = round(height  * 2.54)
kilograms_in_weight = round(weight / 2.2)

print(f"Let's talk about {name}.")
print(f"He's {centimeters_in_height} centimeters tall.")
print(f"He's {kilograms_in_weight} kilograms heavy.")
print("Actually that's not too heavy")
print(f"His teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If i add {age}, {height}, and {weight} I get {total}.")