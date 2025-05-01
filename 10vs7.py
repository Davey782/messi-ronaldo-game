import random
import time


def choose_best_player(messi, ronaldo):
    if messi > ronaldo:
        return "Messi is better than Ronaldo!"
    if ronaldo > messi:
        return "Ronaldo is better than Messi!"
    return "Both players are equally great!"


print("Welcome to the Messi vs Ronaldo game!")
print("Let's see who wins today...\n")

# generate random scores for messi and cr7
print("Generating scores...")
time.sleep(1)  # delay 1 sec
messi = random.randint(1, 10)
ronaldo = random.randint(1, 10)

# show scores
print(f"Messi's score: {messi}")
print(f"Ronaldo's score: {ronaldo}\n")

# winner
time.sleep(1)  # delay 1 sec
result = choose_best_player(messi, ronaldo)
print(result)