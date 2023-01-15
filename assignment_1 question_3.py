number = int(input("Enter The Number : "))
even_count = 0
odd_count = 0
for i in range(0,number):
    if i % 2==0:
        even_count += 1
    else:
        i % 2 != 0
        odd_count += 1

print("Number of even numbers: ", even_count)
print("Number of odd numbers: ", odd_count)
