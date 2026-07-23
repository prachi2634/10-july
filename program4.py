

s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
s4 = float(input("Enter marks of subject 4: "))
s5 = float(input("Enter marks of subject 5: "))

total = s1 + s2 + s3 + s4 + s5
average = total / 5
percentage = (total / 500) * 100

print(f"Total Marks = {total}")
print(f"Average = {average:.2f}")
print(f"Percentage = {percentage:.2f}%")
