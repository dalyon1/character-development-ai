import random

class Empathy:
    def __init__(self):
        self.emotion_keywords = {
            "happy": ["happy", "glad", "joyful", "elated"],
            "sad": ["sad", "unhappy", "sorrowful", "mournful"],
            "angry": ["angry", "furious", "irritated", "annoyed"],
            "neutral": []
        }
        self.responses = {
            "happy": ["That's great to hear!", "I'm glad you're feeling good.", "Happiness is contagious!"],
            "sad": ["I'm sorry to hear that.", "It's okay to feel sad sometimes.", "I'm here for you."],
            "angry": ["I apologize if I upset you.", "Please let me know how I can assist.", "I understand your frustration."],
            "neutral": ["Can you tell me more?", "How can I help?", "What would you like to talk about?"]
        }

    def detect_emotion(self, text):
        for emotion, keywords in self.emotion_keywords.items():
            for keyword in keywords:
                if keyword in text.lower():
                    return emotion
        return "neutral"

    def generate_response(self, emotion):
        return random.choice(self.responses[emotion])

    def respond(self, text):
        emotion = self.detect_emotion(text)
        return self.generate_response(emotion)

# Usage:
bot = Empathy()
text = "I am feeling really sad today."
response = bot.respond(text)
print(response)
