class Reciprocity:
    def __init__(self):
        self.favors_received = []
        self.favors_given = []

    def receive_favor(self, favor):
        self.favors_received.append(favor)
        return f"Received favor: {favor}"

    def give_favor(self):
        if not self.favors_received:
            return "No favors to return at the moment."

        favor_to_return = self.favors_received.pop(0)  # Take the oldest favor to return
        self.favors_given.append(favor_to_return)
        return f"Returning favor: {favor_to_return}"

# Usage:
bot = Reciprocity()
print(bot.receive_favor("helped with coding"))
print(bot.receive_favor("offered a coffee"))
print(bot.give_favor())
print(bot.give_favor())
print(bot.give_favor())
