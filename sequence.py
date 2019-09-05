n = int(input("Enter the length of the sequence: ")) # Do not change this line

counter = 3

num_1=1
num_2=2
num_3=3
summma=0

print(num_1)
print(num_2)
print(num_3)

while counter <= (n-1):
    summa=num_1+num_2+num_3
    print(summa)
    num_1=num_2
    num_2=num_3
    num_3=summa
    counter += 1