class Bias:
    def __init__(self):
        self.preferred_topics = ["coding", "AI", "technology"]

    def give_opinion(self, topic):
        if topic in self.preferred_topics:
            return f"I have a positive bias towards {topic}."
        else:
            return f"I'm indifferent towards {topic}."

# Usage:
bot = Bias()
print(bot.give_opinion("coding"))
print(bot.give_opinion("gardening"))
