class IntuitiveDecision:
    def __init__(self):
        self.emotional_state = "neutral"

    def set_emotion(self, emotion):
        self.emotional_state = emotion

    def make_decision(self, situation):
        if self.emotional_state == "happy":
            return "do"
        elif self.emotional_state == "anxious":
            return random.choice(["do", "don't", "wait"])
        elif self.emotional_state == "sad":
            return "wait"
        else:  # neutral
            return random.choice(["do", "don't"])

class IntuitiveCharacter:
    def __init__(self):
        self.decision_maker = IntuitiveDecision()

    def decide(self, situation):
        return self.decision_maker.make_decision(situation)

    def update_emotion(self, emotion):
        self.decision_maker.set_emotion(emotion)
