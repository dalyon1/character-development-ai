import random

class Curiosity:
    def __init__(self, exploration_rate=0.8):
        self.memory = set()  # Remember states that have been explored
        self.exploration_rate = exploration_rate  # Probability of exploring a new state

    def explore(self, environment):
        current_state = environment.get_state()

        # If the state is novel or the agent decides to explore
        if current_state not in self.memory or random.random() < self.exploration_rate:
            action = self._choose_random_action(environment)
            reward = 1  # Intrinsic reward for novelty or exploration
        else:
            action = self._choose_known_action(environment)
            reward = 0  # No intrinsic reward for known states

        self.memory.add(current_state)
        return action, reward

    def _choose_random_action(self, environment):
        return environment.get_random_action()

    def _choose_known_action(self, environment):
        # This can be further refined to choose the best known action in the environment
        return environment.get_random_action()


class SimpleEnvironment:
    def get_state(self):
        return random.choice(['A', 'B', 'C', 'D', 'E'])

    def get_random_action(self):
        return random.choice(['left', 'right', 'up', 'down'])


# Usage:
environment = SimpleEnvironment()
agent = Curiosity()

for _ in range(10):
    action, reward = agent.explore(environment)
    print(f"Action taken: {action}. Reward received: {reward}.")
