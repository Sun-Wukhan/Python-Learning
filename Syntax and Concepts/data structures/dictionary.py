person = {"name" : "Navid", "age": 30, "city": "Toronto"}
 
person["email"] = "navid_khan@icloud.com"
person["github"] =  "Sun_Wukhan"
person["level"] =  30

print(person)

del person["city"]
print(person)

print(f"this guy is {person['age']} years old")