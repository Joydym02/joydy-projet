def passwor_fuction():
    password = "1234"
    # password_enter = input("Entre le mot de pass")

    while password != True :
        password_enter = input("Entre le mot de pass")

        if password == password_enter:
            print("Bienvenu")
        break

# passwor_fuction()

def somme_nmbr():
    return 5+5

# a = somme_nmbr()
# print(a)


def calcul_nbr(nbr1, nbr2):
    return nbr1*nbr2

produit = calcul_nbr(4,5)
print(produit)



