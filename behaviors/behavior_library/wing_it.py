mport random

class WingingItAlgorithm:
    def __init__(self, disposition="neutral"):
        self.memory = {}  # Very basic memory
        self.disposition = disposition  # Could be 'optimistic', 'pessimistic', or 'neutral'

    def store_experience(self, experience, outcome):
        if len(self.memory) > 10:  # Only remembers the last 10 experiences
            self.memory.pop(next(iter(self.memory)))
        self.memory[experience] = outcome

    def recall_experience(self, experience):
        return self.memory.get(experience, None)

    def decide_based_on_disposition(self):
        if self.disposition == "optimistic":
            return "do"
        elif self.disposition == "pessimistic":
            return "don't"
        else:
            return random.choice(["do", "don't"])

    def make_decision(self, situation):
        # Check immediate context
        if situation.get("immediate_reward", False):
            return "do"
        if situation.get("immediate_danger", False):
            return "don't"

        # Check basic memory
        past_outcome = self.recall_experience(situation)
        if past_outcome:
            return past_outcome

        # Use general disposition or randomness
        return self.decide_based_on_disposition()

class Character:
    def __init__(self, decision_making_style="winging_it"):
        self.style = decision_making_style
        self.decision_maker = WingingItAlgorithm()

    def decide(self, situation=None):
        if self.style == "winging_it":
            return self.decision_maker.make_decision(situation)
        else:
            raise ValueError(f"Unknown decision-making style: {self.style}")

    def learn_from_experience(self, situation, outcome):
        self.decision_maker.store_experience(situation, outcome)

# Test
character = Character()
print(character.decide({"immediate_reward": True}))  # Likely outputs "do"