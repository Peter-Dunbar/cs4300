import pytest

userIn = int(10) #change at will

def prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if userIn > 0:
    result = "positive"
elif userIn < 0:
    result = "negative"
else:
    result = "0"

count = 0
number = 2
primeList = []
while count < 10:
    if prime(number):
        primeList.append(number)
        count += 1
    number +=1

total = 0
sumCount = 1
while sumCount <= 100:
    total += sumCount
    sumCount += 1

def testEvenOdd():
    assert result == "positive"

def testPrime():
    assert primeList == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

def testSum():
    assert total == 5050