import random

class SocialConformity:
    def __init__(self, group_data):
        self.group_data = group_data  # data about choices or behaviors of the group

    def decide_based_on_group(self):
        most_common_choice = max(set(self.group_data), key=self.group_data.count)
        # With a small probability, the bot might not conform
        if random.random() > 0.9:
            return random.choice(self.group_data)
        return most_common_choice

# Usage:
group_choices = ['A', 'A', 'B', 'B', 'B', 'C']
bot = SocialConformity(group_choices)
decision = bot.decide_based_on_group()
print(f"The bot decided to choose: {decision}")
