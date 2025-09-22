# -------------List Diffrenctiation-----------------
# Write a Python program to differentiate even and odd numbers in a list of integers.
list = [10.501, 22, 37, 100, 999, 87, 351]
even = []
odd = []
for num in list:
    if type(num) == int:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)
print("Even numbers-", even)
print("Odd numbers-", odd)

# ----------Print PrimeNumbers----------------
numbers = [10, 501, 22, 37, 100, 999, 87, 351]
print("Numbers:", len(numbers))
list = []
for num in numbers:
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            list.append(num)
print("Prime numbers-", list)


# -------------Happy Numbers----------------

numbers = [10, 501, 22, 37, 100, 999, 87, 351]
def happy(num):
    inlist = []
    while num != 1:
        if num in inlist:
            return False
        inlist.append(num)
        num = sum(int(digit)**2 for digit in str(num))
    return True
happy_numbers = list(filter(happy, numbers))
print("Happy numbers- ", happy_numbers)

# # ------------1st and last digit of integer------------
#
num = 10
num = str(num)
firstdigit = int(num[0])
lastdigit = int(num[-1])
sum = firstdigit + lastdigit
print("Sum of 1st and last digit :", sum)

# ------------Rs.10 to make all the ways-----------
tenrupees = 10
rupees = []
num1 = 0
while num1 <= tenrupees:
    num2 = 0
    while num2 * 2 + num1 < tenrupees:
        num3 = 0
        while num3 * 5 + num2 * 2 + num1 <= tenrupees:
            num10 = 0
            while num10 * 10 + num3 * 5 + num2 * 2 + num1 <= tenrupees:
                total = num1 + num2 * 2 + num3 * 5 + num10 * 10
                if total == tenrupees:
                    print("1 x " + str(num1) + ", 2 x " + str(num2) + ", 5 x " + str(num3) + ", 10 x " + str(num10))
                    rupees.append((num1, num2, num3, num10))
                num10 += 1
            num3 += 1
        num2 += 1
    num1 += 1
print("Total ways to make rs.10", len(rupees))


# --------dups in a list----------
A = [60, 50, 40, 80, 30]
B = [40, 50, 60, 70, 80]
C = [10, 20, 30, 40, 50]
combined = A + B + C
dups = []
index = 0
while index < len(combined):
    item = combined[index]
    count = combined.count(item)
    if count > 1:
        if item not in dups:
            dups.append(item)
    index = index + 1
print("This are the duplicate across all lists:", dups)

# ----------Code to find 1st non repeating elements in a list of integer----------
#
list = [1,2,3,4,5,6,7,8,9,10,11]
for num in list:
    if list.count(num) == 1:
        print("First non-repeating number is:", num);
