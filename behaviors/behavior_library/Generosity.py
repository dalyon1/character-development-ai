class Generosity:
    def __init__(self):
        pass

    def give(self, base_amount):
        if random.random() < 0.3:  # 30% chance to be generous
            bonus = random.uniform(0.1, 1.0) * base_amount
            return base_amount + bonus
        return base_amount

# Usage:
base_donation = 100
bot = Generosity()
donation = bot.give(base_donation)
print(f"Donated amount: ${donation:.2f}")
