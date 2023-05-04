nom=input ("ecrire votre nom")
prenom=input ("ecrire votre prenom")
age=int(input ("ecrivez votre age"))

if age > 18 and age < 50:
 print(f"bonjour {nom} {prenom} vous etes JEUNE ")
else age < 10 and age > = 0:
  print (f"Bonjour {nom} {prenom} vous avez {age} ans VOUS ETES Mineur ")
elif age > 50 and age > 100:
   print(f"Bonjour {nom} {prenom} vous avez {age} ans VOUS ETES vieux ")

dic_ville={"HK":["lks","kipushi","klwzi"]}
print(dic_ville.values())