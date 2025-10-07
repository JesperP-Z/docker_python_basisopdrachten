# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

gasten = []

gasten.append("Jij")
gasten.append("Jesper")
gasten.append("Mark")
gasten.append("Zelensky")
gasten.append("Putin")
gasten.append("Rutte")



#Gasten die niet meegaan
gasten.remove("Rutte")



index_mark = gasten.index("Mark")
gasten.insert(index_mark + 1, "Obamnba")
print(gasten)   

exit()

