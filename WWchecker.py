lenght=0
num=0
number= "0123456789"



wachtwoord=input("Voer wachtwoord in")

leng=len(wachtwoord)
if leng>=6:
   lenght=lenght+3

if leng>=4 and leng<=5: 
   lenght=lenght+2

if leng<=3:
   lenght=lenght+1

else:
   lenght=lenght


for i in wachtwoord:
    for u in number:
        if i==u:
            num=num+1


else:
    num=num

if lenght<=1 and num>=1:
    print("Niet veilig")

if lenght==2 and num>=1:
   print("Redelijk veilig")

if lenght>=3 and num>=1:
   print("super veilig")
   
if num<=0:
   print("niet veilig")









