

p = float(input("Enter principal: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (years): "))

ci = p * (1 + r/100) ** t - p
print(f"Compound Interest = {ci:.2f}")
