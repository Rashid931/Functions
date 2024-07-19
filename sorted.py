# help (sorted)
n = {1,-10,99,-77,3.3}
print (sorted(n))
print (sorted(n, reverse=True))
people = [
{"Name":"Saima", "Age":39}, {"Name":"Abdullah", "Age":16}, {"Name":"Rashid", "Age":47},
{"Name":"Abeeha", "Age":14}
]
print (sorted(people, key=lambda x: x["Age"], reverse=True))