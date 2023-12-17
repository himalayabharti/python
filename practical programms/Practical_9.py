
file = open("txtfile.txt", "w")
char ="Programs that we have developed so far take data from the user in an interactive manner. Such data remain memory only during the lifetime of the program. Oftenwe want to store data permanently, in the form of filesthat usually reside on disks, so that it is available as andwhen required."
input_string=char
file.write(char)

def counting(char):
    
    count=0
    file = open("textfile.txt")
    
    for i in char:
        count+=1
    print(f"Total no. of characters,numbers,words = {count}")
counting(char)

def count_frequency(input_string):
    frequency_count = {}
    for char in input_string:
        if char in frequency_count:
            frequency_count[char] += 1
        else:
            frequency_count[char] = 1
    output_string = ''
    for char, count in frequency_count.items():
        output_string += f'{char}:{count} '
    return output_string
output_string = count_frequency(input_string)
print(output_string) # Output: 'a:2 b:3 c:3 d:4'

count_frequency(char)

def inverse(char):
    print(char[::-1])

inverse(char)




   
    
    














