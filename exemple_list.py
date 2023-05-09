list_name = [ 
  "Franck", "Bea","Tegra"  ,
  "Joydy", "Moise","Germain"  
]

list_note = [34, 46, 20]
list_note.insert(0,30)
# list_note.clear()
# list_note.count(20)
list_note.reverse()
# list_note.remove(20)
print(list_note.sort(reverse=True))

list_etudiant = [list_name,list_note]
list_note.append(20)

# Slicing
name = list_name[:]
name = list_name[:-1]
name = list_name[1:]

print(name)
print(list_etudiant)

print(f"Nom et Note {list_etudiant[0][0]} {list_etudiant[1][2]} ")
print(f"Nom et Note {list_etudiant[0][1::2]} {list_etudiant[1][1:]} ")