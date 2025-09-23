userIn = int(input("Enter a #: \n"))

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if userIn > 0:
    print("positive")
elif userIn < 0:
    print("negative")
else:
    print("Zero")

count = 0
number = 2
while count < 10:
    if prime(number):
        print(number)
        count += 1
    number +=1

total = 0
sumCount = 1
while sumCount <= 100:
    total += sumCount
    sumCount += 1
print(total)