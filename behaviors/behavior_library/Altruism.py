class Altruism:
    def __init__(self, resources):
        self.resources = resources

    def distribute_resources(self, needy):
        share = min(self.resources, needy)
        self.resources -= share
        return share

# Usage:
bot = Altruism(100)
print(f"Bot starts with {bot.resources} resources.")
needs = [20, 50, 40]
for need in needs:
    given = bot.distribute_resources(need)
    print(f"Bot gives away {given} resources. Remaining: {bot.resources}")
