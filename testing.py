import caesar
import pytest


text = "test should be fine"
key = 7

def start():
	caesar.encode(text,key)


def end():
	caesar.decode(text,key)



