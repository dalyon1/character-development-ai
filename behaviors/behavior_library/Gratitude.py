class Gratitude:
    def __init__(self):
        self.positive_experiences = []

    def experience(self, interaction):
        if interaction in ["help", "gift", "support", "kindness"]:
            self.positive_experiences.append(interaction)
            return f"Thank you for the {interaction}. I appreciate it!"
        return f"Received {interaction}."

# Usage:
interactions = ["help", "question", "kindness", "feedback"]
bot = Gratitude()
for interaction in interactions:
    print(bot.experience(interaction))
