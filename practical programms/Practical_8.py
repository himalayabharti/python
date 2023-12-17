#a<-for loop

def even_int(n):
    print(f"Cube of only even numbers:")
    for i in range(1,n+1):
        if i%2==0:
            cube=i**3
            print(f"cube of {i}={cube}")
n=int(input("Enter the maximum no. to find the cube: "))
even_int(n)

#b<- list comprehension
#def even_com(num):
   # num_range=[i for i in range(1,num+1) if i%2==0]
   # cube=str(num_range)
   # cube_1=int(cube)
   # cube_2=cube_1**3

   # print(f"cube of {str(num_range)}={str(cube_2)}")

#num=int(input("Enter the max no. of cube: "))
#even_com(num)
