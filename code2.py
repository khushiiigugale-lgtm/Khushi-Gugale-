import random

adjectives = [
    "sleepy", "clumsy", "confused",
    "dramatic", "lazy", "silly"
]

nouns = [
    "potato", "penguin", "robot",
    "banana", "hamster", "noodle"
]

while True:
    insult = f"You {random.choice(adjectives)} {random.choice(nouns)}!"
    print("\n😂", insult)

    again = input("Generate another? (yes/no): ").lower()

    if again != "yes":
        print("Goodbye! 👋")
        break