#Ths is the 12th pactical of python
t1=(1,2,5,7,9,2,4,6,8,10)

def fst_other_halfs(tuple):
    
    string=str(tuple)#connvert tuple into string
    
    half=int(len(string)/2)#it remove the decimal and return as a integer
    
    print(f"1st halt values = {string[1:half:1]}")#1st hald values = 1,2,5,7,9
    print(f"Other half = {string[half+1::1]}")#Other half values = 2,4,6,8,10


fst_other_halfs(tuple)
#function to add only evenelements of tuple t1
def even(tuple):
    lst=[]
    for i in t1:
        if i%2==0:
                lst.append(i)#add even element 
    
    t2=tuple(lst)#convert list into tuple 
    print(f"Even tuple = {t2}")#Even tupe = 2,2,4,6,8,10


even(tuple)


def add(t1):
    new_elements=(11,13,15)
    t2=t1+new_elements
    print(t2)
    return  t1,t2




def max_min(t1):
    a1,a2=add(t1)#a1=t1,a2=t2
    
    print(f"Maximum value = {max(a2)}")
    print(f"Minimun value = {min(a2)}")
    
max_min(t1)






