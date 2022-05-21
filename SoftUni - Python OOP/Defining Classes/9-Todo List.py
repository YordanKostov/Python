class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.comments = []
        self.completed = False

    def change_name(self, new_name):
        if new_name != self.name:
            self.name = new_name
            return self.name
        else:
            return f"Name cannot be the same."

    def change_due_date(self, new_date):
        if new_date != self.due_date:
            self.due_date = new_date
            return self.due_date
        else:
            return f"Date cannot be the same."

    def add_comment(self, comment):
        self.comments.append(comment)

    def edit_comment(self, comment_number, new_comment):
        if comment_number in range(len(self.comments)):
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        else:
            return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"


class Section:
    def __init__(self, name):
        self.name = name
        self.tasks = []

    def add_task(self, new_task: Task):
        if new_task not in self.tasks:
            self.tasks.append(new_task)
            return f"Task {new_task.details()} is added to the section"
        else:
            return f"Task is already in the section {self.name}"

    def complete_task(self, task_name):
        filtered_task = [t for t in self.tasks if t.name == task_name]
        if filtered_task[0]:
            filtered_task[0].completed = True
            return f"Completed task {task_name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        count = 0
        for t in self.tasks:
            if t.completed is True:
                self.tasks.remove(t)
                count += 1
        return f"Cleared {count} tasks."

    def view_section(self):
        res = f"Section {self.name}:\n"
        for task in self.tasks:
            res += f"{task.details()}\n"
        return res


task = Task("Make bed", "27/05/2020")
print(task.change_name("Go to University"))
print(task.change_due_date("28.05.2020"))
task.add_comment("Don't forget laptop")
print(task.edit_comment(0, "Don't forget laptop and notebook"))
print(task.details())
section = Section("Daily tasks")
print(section.add_task(task))
second_task = Task("Make bed", "27/05/2020")
section.add_task(second_task)
section.complete_task("Make bed")
print(section.clean_section())
print(section.view_section())