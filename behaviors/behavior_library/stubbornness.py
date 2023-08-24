import random

class BaseStubbornness:
    def __init__(self):
        self.determination = 0.9

    def decide(self, situation, external_pressure=0):
        raise NotImplementedError("Subclasses should implement this method.")


class StubbornAgainstOppression(BaseStubbornness):
    def __init__(self, values=[]):
        super().__init__()
        self.values = values

    def is_oppressive_situation(self, situation):
        for value in self.values:
            if value in situation:
                return True
        return False

    def decide(self, situation, external_pressure=0):
        if self.is_oppressive_situation(situation) and random.random() < self.determination:
            return "resist"
        if external_pressure > self.determination:
            return "compromise"
        return "neutral_decision"


class StubbornAgainstChange(BaseStubbornness):
    def decide(self, situation, external_pressure=0):
        if 'change' in situation and random.random() < self.determination:
            return "resist_change"
        if external_pressure > self.determination:
            return "accept_change"
        return "neutral_decision"
class TunnelVision(BaseStubbornness):
    def __init__(self, focus):
        super().__init__()
        self.focus = focus  # What the entity is locked onto

    def decide(self, situation, external_pressure=0):
        if self.focus in situation and random.random() < self.determination:
            return "maintain_focus"
        if external_pressure > self.determination:
            return "distractiied"
        return "neutral_decision"
    