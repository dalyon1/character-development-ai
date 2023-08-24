class Fear:
    def __init__(self):
        self.threat_level = 0

    def perceive_threat(self, stimulus):
        if stimulus in ["predator", "high temperature", "dangerous terrain"]:
            self.threat_level += 1
        else:
            self.threat_level = max(0, self.threat_level - 0.5)

        if self.threat_level > 1:
            return "In panic mode! Searching for safety!"
        elif self.threat_level == 1:
            return "On alert. Preparing defensive measures."
        else:
            return "Calm and relaxed."

# Usage:
stimuli = ["high temperature", "normal temperature", "predator", "friendly entity"]
bot = Fear()
for stimulus in stimuli:
    print(f"Stimulus: {stimulus} - Bot Response: {bot.perceive_threat(stimulus)}")
