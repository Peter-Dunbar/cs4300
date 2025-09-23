import pytest

favBook = [
    ("Rhythm of War", "Brandon Sanderson"),
    ("The Great Gatsby", "F. Scott Fitzgerald"),
    ("Not a Real book1", "Auth1"),
    ("Not a Real book2", "Auth2")
]

studentID = {
    "Peter": 1234,
    "Soo": 4321,
    "Wade": 3214,
    "Crung": 2134
}

def firstThree(favBook, n=3):
    print(favBook[:n])

firstThree(favBook, n=3)

def firstThreeTest():
    wanted = [
        ("Rhythm of War", "Brandon Sanderson"),
        ("The Great Gatsby", "F. Scott Fitzgerald"),
        ("Not a Real book1", "Auth1")
    ]
    captured = capsys.readouterr()
    assert captured.out == "[('Rhythm of War', 'Brandon Sanderson'), ('The Great Gatsby', 'F. Scott Fitzgerald'), ('Not a Real book1', 'Auth1')]\n"

def defaultIDs():
    assert studentID["Peter"] == 1234
    assert studentID["Soo"] == 4321
    assert studentID["Wade"] == 3214
    assert studentID["Crung"] == 2134