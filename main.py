guess =int(input("what is your guess?"))
your_number = 6


while guess != your_number:
    Guess_count = 2
    if guess < your_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess?"))
    else:
        guess =int(input("Wrong. You need to guess lower. Whats is your guess?."))

    print(f"congrats! The right answer was {your_number}. it took you {Guess_count} guesses.")


