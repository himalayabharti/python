
str1=input("Enter the 1st string: ")
str2=input("Enetr the 2nd string: ")
n=int(input("Enter the no.of swap characters: "))
swped_1=""
swped_2=""
remain_1=""
remain_2=""

swped_1=str2[:n:1]+str1[n::1]
swped_2=str1[:n:1]+str2[n::1]



print(f"Updated string 1st ={swped_1}")
print(f"Updated string 2nd ={swped_2}")

