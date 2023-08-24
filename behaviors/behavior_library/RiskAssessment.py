class RiskAssessmentBot:
    def __init__(self):
        pass

    def assess_risk(self, situation):
        # Basic scenarios with associated risk levels
        risks = {
            "crossing a busy street": (0.7, "high"),
            "walking in a park during the day": (0.1, "low"),
            "investing in a new untested venture": (0.6, "medium"),
            "putting money in a savings account": (0.01, "very low")
        }

        risk_chance, risk_level = risks.get(situation, (0, "unknown"))

        if risk_chance > 0.6:
            action = "Avoiding the situation."
        elif risk_chance > 0.3:
            action = "Proceeding with caution."
        else:
            action = "Proceeding confidently."

        return f"Assessed Risk for {situation}: {risk_level}. Suggested Action: {action}"

# Usage:
situations = ["crossing a busy street", "walking in a park during the day", "investing in a new untested venture"]
bot = RiskAssessmentBot()
for situation in situations:
    print(bot.assess_risk(situation))