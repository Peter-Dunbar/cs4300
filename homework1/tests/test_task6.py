import pytest

filename = r"/home/student/cs4300/homework1/src/task6_read_me.txt"

def countAllWords(filename):
    with open(filename, "r") as file:
        fullText = file.read()
        totalWord = fullText.split()
        return len(totalWord)

print(countAllWords(filename))

def testWordCount():
    expected = 127
    assert countAllWords(filename) == 127
