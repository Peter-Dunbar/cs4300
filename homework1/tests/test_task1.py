import pytest


def testSpeech(capsys):
    print("Hello World")
    captured = capsys.readouterr()
    assert captured.out == "Hello World\n"