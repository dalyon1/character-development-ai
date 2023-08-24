class Sympathy:
    def __init__(self):
        self.sympathetic_keywords = ["sad", "hurt", "loss", "pain", "suffer", "mourn", "grieve"]
        self.sympathetic_responses = [
            "I'm truly sorry to hear that.",
            "That must be really tough for you.",
            "I can't imagine how you must feel.",
            "You have my deepest sympathies.",
            "It's okay to feel the way you do.",
            "Please know you're not alone."
        ]
    
    def respond(self, user_input):
        # Checking if any keyword in user's statement matches our predefined keywords
        for word in user_input.split():
            if word in self.sympathetic_keywords:
                import random
                return random.choice(self.sympathetic_responses)
        return "I'm here to help and listen."

# Usage:
bot = Sympathy()
print(bot.respond("I'm feeling very sad today."))
print(bot.respond("I recently suffered a loss in my family."))
