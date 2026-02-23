import random

words = [
    "river", "cloud", "forest", "mountain", "ocean",
    "sunlight", "shadow", "breeze", "island", "desert",
    "garden", "sunset", "rainbow", "valley", "waterfall"
]

random.shuffle(words)

mistakes = 0

for word in words:
    input("\nPress Enter to see the next word...")
    print("Word:", word)
    
    answer = input("Type it here: ")

    if answer.strip() == word:
        print("Correct!")
    else:
        print("Wrong!")
        mistakes += 1

total = len(words)
accuracy = round((total - mistakes) / total * 100, 1)

print("\nFinished!")
print("Mistakes:", mistakes)
print("Accuracy:", accuracy, "%")