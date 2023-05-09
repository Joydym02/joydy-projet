list_name = [ 
  "Franck", "Bea","Tegra"  ,
  "Joydy", "Moise","Germain"  
]

list_note = [34, 46, 20,30,40,25]


list_etudiant = [list_name,list_note]

# Structure itarative 

for index in list_etudiant:
    for nomnote in index: 
        print(f"Nom {nomnote}")


password = "1234"
# password_enter = input("Entre le mot de pass")

while password != True :
    password_enter = input("Entre le mot de pass")

    if password == password_enter:
        print("Bienvenu")
        break

    
 