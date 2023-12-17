def upper_lower(char):
    if char.isupper():#check char is capital only
        print(f"{char} is uppercase")
    if char.islower():# check char is small only
        print(f"{char} is lowecase")


def number_print(char):
    number=["ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"]
    I=char
    print(number[int(I)])
    
def check(char):
    num="0123456789"
    letters="abcdefghijklmnopqrstuvwxyz"
    for i in char:
        if i in num: #check char is number
            print(f"{i} is number")
            number_print(char)
    
        elif i.lower() in letters:#check char is letter 
            print(f"{i} is letter")
            upper_lower(char)
        else: #print char is specail symbol if both are incorrt or false
            print(f"{i} is special symbol")


char=input("Enter the character: ")
check(char)


