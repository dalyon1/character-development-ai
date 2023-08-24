class CognitiveDecision:
    def __init__(self):
        self.memory = {}  # Storing past experiences and their outcomes

    def store_experience(self, experience, outcome):
        self.memory[experience] = outcome

    def make_decision(self, situation):
        # Check memory for past experiences
        past_outcome = self.memory.get(str(situation), None)
        if past_outcome:
            return past_outcome
        # If no past knowledge, fall back to a default behavior
        return "undecided"

class CognitiveCharacter:
    def __init__(self):
        self.decision_maker = CognitiveDecision()

    def decide(self, situation):
        return self.decision_maker.make_decision(situation)

    def learn_from_experience(self, situation, outcome):
        self.decision_maker.store_experience(str(situation), outcome)
