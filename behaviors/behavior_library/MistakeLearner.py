class MistakeLearner:
    def __init__(self):
        self.previous_guesses = []
        self.learning_rate = 10  # Determines the magnitude of adjustment.

    def guess_number(self, true_value):
        guess = 50  # A middle-of-the-road initial guess.
        
        if self.previous_guesses:
            last_guess = self.previous_guesses[-1]
            if last_guess < true_value:
                guess = last_guess + self.learning_rate
            else:
                guess = last_guess - self.learning_rate

        self.previous_guesses.append(guess)
        
        if guess == true_value:
            return f"Guessed it right! The number is {guess}."
        else:
            direction = "lower" if guess > true_value else "higher"
            return f"Guessed {guess}. Need to guess {direction} next time."

# Usage:
bot = MistakeLearner()
true_values = [70, 60, 55, 45]
for value in true_values:
    print(bot.guess_number(value))