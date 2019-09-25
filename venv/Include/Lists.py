
ninjas = ["Sasuke", "Madara", "Naruto", "Obito", "Minato"]
jutsus = ["Kirin", "Susanoo", "Rasen-shuriken", "Kamui", "Flying-raijin"]

print(ninjas)
print(jutsus)

ninjas.extend(jutsus)

print(ninjas)

ninjas.append("Shippuden Characters")
print(ninjas)

ninjas.insert(2, "Shikamaru")

print(ninjas[1:4])

ninjas.remove("Shippuden Characters")
print(ninjas)

print(jutsus.index("Susanoo"))

#count is used to determine how many times a value occurs in the list
print(ninjas.count("Madara"))

print(jutsus.sort())

print(jutsus.reverse())


