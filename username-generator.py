import random

adjectives = ["cool", "fast", "smart", "crazy", "happy", "sleepy"]
nouns = ["tiger", "lion", "ninja", "coder", "wizard", "robot"]

name = input("enter the name :").lower()

adj = random.choice(adjectives)
noun = random.choice(nouns)
numbers = random.randint(10,99)

username = f"{name}{adj}{noun}_{numbers}"
print(username)