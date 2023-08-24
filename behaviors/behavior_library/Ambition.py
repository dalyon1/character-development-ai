class Ambition:
    def __init__(self):
        self.achievement_level = 0

    def work_towards_goal(self):
        progress = random.uniform(0.1, 0.5)  # Random progress between 10% to 50%
        self.achievement_level += progress
        if self.achievement_level >= 1:
            return "Goal achieved!"
        else:
            return f"Working towards the goal. Current progress: {self.achievement_level * 100:.2f}%"

# Usage:
bot = Ambition()
for _ in range(5):
    print(bot.work_towards_goal())
