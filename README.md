# Guess the number

## Guess the number game

This Python program is a simple guessing game. The user has to guess a predefined number, and the program will give hints if the guess is too high or too low. The game continues until the correct number is guessed.

## Code Explanation
```Python
guess = int(input("What is your guess?"))  # Prompts user for their initial guess
your_number = 6  # Set the target number to be guessed

while guess != your_number:  # Loop continues until the correct guess is made
    Guess_count = 2  # Initialize guess count
    if guess < your_number:
        guess = int(input("Wrong. You need to guess higher. What is your guess?"))
    else:
        guess = int(input("Wrong. You need to guess lower. What is your guess?"))

    print(f"Congrats! The right answer was {your_number}. It took you {Guess_count} guesses.")
```



## Code Update

I did run into issues with the code where it would not track the attempts correctly and the  print ststment woukd excute before user made the correct guess.
1. Guess_count was assded outsided the loop and within the loop
2. print statement taking out of loop statement.
3. 

   ```Python
   guess = int(input("What is your guess?"))
   your_number = 6
   guess_count = 1  # Start count at 1 to account for the initial guess

     while guess != your_number:
        guess_count += 1  # Increment guess count each time a new guess is made
         if guess < your_number:
            guess = int(input("Wrong. You need to guess higher. What is your guess?"))
        else:
            guess = int(input("Wrong. You need to guess lower. What is your guess?"))

   print(f"Congrats! The right answer was {your_number}. It took you {guess_count} guesses.")

   ```
   
   
