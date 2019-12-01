obj = {
    "first_name" : "Jaffar",
    "last_name," : "Abbas",
    "age":"19",
    "city" : "Karachi"
}

for i in obj.values():
    print(i)

obj.update({"qualification":"Matric"})

print(obj["qualification"])

obj["qualification"] = "BSSE"
print("fter update Qualification ",obj["qualification"])

del obj["qualification"]

print(obj)