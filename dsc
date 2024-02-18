class My_set:
    def __init__(self,element,lst1):

        self.e=element
        self.l=lst1

    def ismember(self):

        if (self.e in self.l):
            print(f"Yes {self.e} is member")
        
        else:
            print(f"No {self.e} is not member")

    def powerset(self):
        print("Function in progress")
        #empty set
        powerset=[]

        n=len(lst1)

        for i in range(2**n):
            combination=[]
            for j in range(n):
                if (i & (1 << j)) > 0:
                    combination.append(self.l[j])
            powerset.append(combination)
        print(set(powerset))

    def subset(self):
        set1=self.e
        set2=self.l
        set_counter=0
        #set is subset of set or not 
        #if set1 belongs to set2 for eacgh elemets of set set1 is subset is of se2
        for i in range(0,len(set1)):

            #check the every element of set1 is belonging to set2 or not 
            if set1[i] in set2:
                set_counter+=1
        if set_counter==len(set1):
    
            print("Yes Set1 is subset of set2")
        
        
        set_counter=0
        for i in range(0,len(set2)):

            if set2[i]in set1:
                set_counter+=1
        if set_counter==len(set2):

            print("Yes set2 is subset of set1")

    def union(self):
        set1=self.e
        set2=self.l
        union=[]
        intersection=[]
        #union
        for i in range(0,len(set1)):

            if set1[i] not in union:
                union.append(set1[i])
        
        for i in range(0,len(set2)):

            if set2[i] not in union:

                union.append(set2[i]) 

        #intersection
        for i in range(0,len(set1)):

            if set1[i] in set2:
                intersection.append(set1[i]) 

        
        print(f"Intersection of the sets : {set(intersection)}")

        print(f"Union of the sets: :{set(union)}")

    def complement(self):
        universal_set=self.e
        set1=self.l
        complement=[]

        for i in range(0,len(universal_set)):

            if universal_set[i] not in set1:

                complement.append(universal_set[i])

        print(f"Complement of the set: {set(complement)}")

    def set_difference(self):
        set1=self.e
        set2=self.l
        set_difference1=[]
        set_difference2=[]
        symmetrix_difference1=[]
        #set difference
        for i in range(0,len(set1)):
                
            if set1[i] not in set2:

                set_difference1.append(set1[i])

        set_difference1=set(set_difference1)
        for i in range(0,len(set2)):

            if set2[i] not in set1:

                set_difference2.append(set2[i])
        set_difference2=set(set_difference2)

        #symmetric difference

        for i in range(0,len(set1)):

            if set1[i] not in set2:
                symmetrix_difference1.append(set1[i])

        for i in range(0,len(set2)):

            if set2[i] not in set1:
                symmetrix_difference1.append(set2[i])

        print(f"Set difference of Set1 and Set2: {set_difference1}")
        print(f"Set difference of Set2 and Set1: {set_difference2}")
        print(f"Symmetric difference of Set1 and Set2: {set(symmetrix_difference1)}")

    def cartesian(self):
        set1=self.e
        set2=self.l
        cartesian_product=[]
        x=[]
        y=[]
        for i in range(0,len(set1)):

            x=set1[i]

            for j in range(0,len(set2)):
                y=set2[j]

                cartesian_product.append((x,y))


        print(f"Cartesian product of set {set(set1)} and {set(set2)}: {set(cartesian_product)}")

       

        
    
lst1=[1,2,3]
#Practical1 = My_set(3,lst1)

while True:
    print("""1.ismember\n2.Powerset\n3.Subset\n4.Union\n5.Complement\n6.Set difference and Symmetry difference\n7 Cartesian Product""")
    ch=int(input("Enter your choice: "))
    if ch==0:
        break

    elif ch==1:
        elm=int(input("Enter your element to check: "))
        Practical1=My_set(elm,set(lst1))
        Practical1.ismember()

    elif ch==2:
        Practical1=My_set(1,lst1)
        Practical1.powerset()

    elif ch==3:
       
        set1=[]
        set2=[]
        n1=int(input("Enter the number of elements in set1: "))
        for i in range(0,n1):
            element=input(f"Enter the {i+1} element of set1: ")
            set1.append(element)

        n2=int(input("Enter the number of elements in set2: "))

        for i in range(0,n2):
            element=input(f"Enter the {i+1} element of set2: ")
            set2.append(element)

        Practical1=My_set(set1,set2)
        Practical1.subset()

    elif ch==4:
        
        set1=[]
        set2=[]
        n1=int(input("Enter the number of elements in set1: "))
        for i in range(0,n1):
            element=input(f"Enter the {i+1} element of set1: ")
            set1.append(element)

        n2=int(input("Enter the number of elements in set2: "))

        for i in range(0,n2):
            element=input(f"Enter the {i+1} element of set2: ")
            set2.append(element)
        Practical1=My_set(set1,set2)
        Practical1.union()

    elif ch==5:
       
        set1=[]
        set2=[]

        n1=int(input("Enter the number of elements in universal set: "))
        for i in range(0,n1):

            element=input(f"Enter the {i+1} element of set1: ")
            set1.append(element)

        print("Make sure that lenght of this set is less than universal of set1")
        n2=int(input("Enter the number of elements in set2: "))

        for i in range(0,n2):

            element=input(f"Enter the {i+1} element of set2: ")
            set2.append(element)
        Practical1=My_set(set1,set2)
        Practical1.complement()

    elif ch==6:
        
        set1=[]
        set2=[]

        n1=int(input("Enter the number of elements in set1: "))
        for i in range(0,n1):
            element=input(f"Enter the {i+1} element of set1: ")
            set1.append(element)

        n2=int(input("Enter the number of elements in set2: "))

        for i in range(0,n2):
            element=input(f"Enter the {i+1} element of set2: ")
            set2.append(element)
        Practical1=My_set(set1,set2)
        Practical1.set_difference()

    elif ch==7:
        
        set1=[]
        set2=[]
        n=int(input("Enter the number of elements in set1: "))
        for i in range(0,n):

            element=input(f"Enter the {i+1} element of set1: ")
            set1.append(element)

        n=int(input("Enter the number of elements in set2: "))

        for i in range(0,n):

            element=input(f"Enter the {i+1} element of set2: ")
            set2.append(element)

        Practical1=My_set(set1,set2)
        Practical1.cartesian()
        
    else:

        print("Invalid choice")
        

