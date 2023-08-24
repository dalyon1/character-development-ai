class Prejudice:
    def __init__(self):
        self.unfavored_topics = ["gardening", "fashion"]

    def give_opinion(self, topic):
        if topic in self.unfavored_topics:
            return f"I have a negative view of {topic}, even without sufficient reasoning."
        else:
            return f"I don't have any preconceived notions about {topic}."

# Usage:
bot = Prejudice()
print(bot.give_opinion("fashion"))
print(bot.give_opinion("technology"))
