class Adaptability:
    def __init__(self):
        self.strategy = "default"

    def adapt(self, feedback):
        if feedback == "too slow":
            self.strategy = "fast"
        elif feedback == "too aggressive":
            self.strategy = "gentle"
        else:
            self.strategy = "default"

    def act(self):
        return f"Acting in {self.strategy} mode."

# Usage:
feedbacks = ["too slow", "too aggressive", "normal"]
bot = Adaptability()
for feedback in feedbacks:
    bot.adapt(feedback)
    print(bot.act())
