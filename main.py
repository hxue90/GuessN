import random

def compRand(guessRandom, trueRandom):
    if (trueRandom == guessRandom):
        print("Congrats!!")
        exit(0)
    elif (trueRandom-1 == guessRandom) or (trueRandom+1 == guessRandom):
        print("Hot!!")
    elif (trueRandom-2 == guessRandom) or (trueRandom+2 == guessRandom):
        print("Warm!!")
    else:
        print("Cold!!")

def genRand():
    return random.randint(0, 10)

def askRand():
    return int(input("Please enter a random number: "))

def main():
    trueRandom = genRand()

    for i in range(0, 3):
        guessRandom = askRand()
        compRand(guessRandom, trueRandom)


if __name__ == "__main__":
    main()