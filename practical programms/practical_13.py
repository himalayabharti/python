name=input("Enter only alphabets: ")
num=name.isalpha()
digit=name.isdigit()

if num==True:
    print("It is not containing any digit or special character")
    
if digit==True:
    print("It contain digit/s")

if name.isalpha()==False and name.isdigit()==False:
    print("It contain special characters")

