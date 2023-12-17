def frequency(char):
    string = ""
    count=0
    for i in char:
        count=char.count(i)
        string+=i
        print(f"Frequency of {i}={count}")

def replace(char):

    by_replace_char=input(" Which character you want to replace the character : ")#replace character

    which_replace_char=input("Enter the new character in the place of replacing character: ")#new char character

    newchar=char.replace(by_replace_char,which_replace_char)#it replace the charcters from  str

    #synatx <<string_variable.replace(replacing_char,new_char)>>

    print(newchar)
                
def remove_fisrt_occurance(char):
    lst=list(char)
    for i in lst:
        if lst.count(i)>=2:
            lst.remove(i)#it removes 1st occurence from string
    
    print(str(lst))

def all_accurance(char):
    lst=list(char)

    for i in lst:
        if lst.count(i)>=2:
            while lst.count(i)>=1:
                lst.remove(i)
    print(type(str(lst)))
    print(str(char))
                    
char=input("Enter the words/setences: ")
#frequency(char)
replace(char)
remove_fisrt_occurance(char)
all_accurance(char)

