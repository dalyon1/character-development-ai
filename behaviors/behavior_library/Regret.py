class Regret:
    def __init__(self):
        self.past_decisions = []
        self.possible_outcomes = {
            "buy_stock": {"good": 50, "bad": -40},
            "sell_stock": {"good": 30, "bad": -20},
        }

    def make_decision(self, decision):
        outcome = self.evaluate_outcome(decision)
        self.past_decisions.append((decision, outcome))
        return outcome

    def evaluate_outcome(self, decision):
        import random

        # Let's say there's a 50% chance for each outcome
        return random.choice(list(self.possible_outcomes[decision].values()))

    def express_regret(self):
        if not self.past_decisions:
            return "I haven't made a decision yet."
        
        last_decision, last_outcome = self.past_decisions[-1]
        
        for alt_decision in self.possible_outcomes:
            if alt_decision != last_decision:
                if max(self.possible_outcomes[alt_decision].values()) > last_outcome:
                    return f"I regret {last_decision}. I should've chosen to {alt_decision}."

        return "I stand by my last decision."

# Usage:
bot = Regret()
print(bot.make_decision("buy_stock"))
print(bot.express_regret())
