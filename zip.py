name = ["Rashid", "Saima", "Abdullah", "Abeeha"]
age = [40, 30, 20, 10]
gender = ["Male", "Female", "Male", "Female"]

family = list (zip(name, age, gender))
print (family)

for name, age, gender in family:
    print (f"{name} is {age} years old & is {gender}.")
