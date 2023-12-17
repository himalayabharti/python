import math
#equation of root 
#x = -b +- root of b**2-4ac/2a
#quadratic equation = x**2*a+x*b+c=0
a=int(input("Enter the value of a or cofficient of x**2: "))
b=int(input("Enetr the vaue of b or cofficient of x: "))
c=int(input("Enter the value of c or constant term: "))

root_value=b**2-4*a*c #value under root 

if a!=0: #a<0
    if root_value!=0:
        value_1=(-b+math.sqrt(root_value)/(2*a))#consider  with + sign
        value_2=(-b-math.sqrt(root_value)/(2*a))# consoder with _ sign
        print(f" Root are \n Roots are : {value_1} ,{value_2}")

    else:
        value_1=-b/(2*a)
        print(f" Root are real and same {value_1}")

else: #a==0 
    print("No x**2 exist so their is no quadratic equation")
        


num=5
print(int(num**0.5))
#num is power 0.5 ko integer converter kia hai

