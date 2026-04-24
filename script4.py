class Task:
    def __init__(self, name: str, description: str, deadline: str):
        self.name = name
        self.description = description
        self.deadline = datetime.strptime(deadline, "%Y-%m-%d")
        self.completed = False

    def mark_completed(self):
        self.completed = True

    def __str__(self):
        self.tasks
def add tasks(tasks.name:)
self.tasks.append(task)
def delete tasks(tasks.name:)
self.tasks = [t for t in self.tasks if t.name != name]


