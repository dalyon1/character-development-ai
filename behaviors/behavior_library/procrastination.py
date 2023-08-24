import time

class Procrastination:
    def __init__(self):
        pass

    def do_task(self, task_name):
        if random.random() < 0.5:  # 50% chance to procrastinate
            delay = random.randint(1, 5)  # delay for 1 to 5 seconds
            print(f"Procrastinating for {delay} seconds...")
            time.sleep(delay)
        print(f"Doing the task: {task_name}")

# Usage:
tasks = ["clean data", "train model", "evaluate results"]
bot = Procrastination()
for task in tasks:
    bot.do_task(task)
