from behavior_library import CognitiveDecision, IntuitiveDecision, stubbornness, empathy, Fear, Reciprocity, Bias, Prejudice, MistakeLearner, Gratitude, Regret, Sympathy, RiskAssessment, wing_it, social_conformity, Adaptability, Altruism, Ambition, Generosity, Grit, curiosity, procrastination

class CharacterLearningSystem:
    def __init__(self):
        self.experiences = []  # Database to store past experiences and outcomes
        self.behaviors = {
            "cognitive": CognitiveDecision(),
            "intuitive": IntuitiveDecision(),
            "stubborn": stubbornness(),
            "empathy": empathy(),
            "fear": Fear(),
	    "Reciprocity": Reciprocity(),
            "Bias": Bias(),
	    "Prejudice": Prejudice(),
	    "MistakeLearner": MistakeLearner(),
	    "Gratitude": Gratitude(),
	    "Regret": Regret(),
	    "Sympathy": Sympathy(),
	    "RiskAssessment": RiskAssessment(),
	    "wing_it": wing_it(),
	    "social_conformity": social_conformity(),
	    "Adaptability": Adaptability(),
	    "Altruism": Altruism(),
	    "Ambition": Ambition(),
	    "Generosity": Generosity(),
	    "Grit": Grit(),
	    "curiosity": curiosity(),
	    "procrastination": procrastination(),
	    # ... add other behaviors
        }
        self.current_behavior_weights = {behavior: 1 for behavior in self.behaviors}  # Default weight is 1

    def decide(self, situation):
        # Get decision values from each behavior
        decisions = {name: behavior.decide(situation) for name, behavior in self.behaviors.items()}
        
        # Weighted decision making
        weighted_sum = sum(self.current_behavior_weights[name] * value for name, value in decisions.items())
        
        # Normalize the decision to get a final decision
        final_decision = weighted_sum / sum(self.current_behavior_weights.values())
        
        # Store the situation and decision for future reference
        self.experiences.append((situation, final_decision))
        
        return final_decision

    def feedback(self, outcome):
        # Here we adjust the behavior weights based on the outcome.
        # If a decision led to a positive outcome, increase the weight of that behavior.
        # If it led to a negative outcome, decrease its weight.
        last_situation, last_decision = self.experiences[-1]
        for name, behavior in self.behaviors.items():
            if behavior.recent_decision == last_decision:
                if outcome == "positive":
                    self.current_behavior_weights[name] *= 1.1  # Increase by 10%
                else:
                    self.current_behavior_weights[name] *= 0.9  # Decrease by 10%

    def interact(self, situation, user_feedback):
        decision = self.decide(situation)
        print(f"Decision based on {situation}: {decision}")
        self.feedback(user_feedback)

# Usage
character = CharacterLearningSystem()
character.interact("faced with a moral dilemma", "positive")
character.interact("encountered a risky situation", "negative")

 	def enter_heightened_state(self):
        # Save current weights
        self.normal_behavior_weights = self.current_behavior_weights.copy()

        # Adjust weights for heightened state
        self.current_behavior_weights["cognitive"] *= 0.5  # Decrease reliance on cognitive thought
        self.current_behavior_weights["intuitive"] *= 1.5  # Increase reliance on intuition
        self.current_behavior_weights["stubborn"] *= 1.5  # More stubbornness
        self.current_behavior_weights["fear_risk"] *= 0.5  # Decrease fear and risk aversion

  def exit_heightened_state(self):
        # Restore normal state
        self.current_behavior_weights = self.normal_behavior_weights

# Usage
character = CharacterLearningSystem()
character.interact("faced with a moral dilemma", "positive")  # Normal state
character.enter_heightened_state()
character.interact("encountered a risky situation", "positive")  # Heightened state
character.exit_heightened_state()
character.interact("faced with another moral dilemma", "negative")  # Back to normal state