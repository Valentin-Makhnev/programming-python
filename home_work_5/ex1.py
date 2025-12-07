class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if self.items:
            return self.items.pop()
        return None
    
    def __len__(self):
        return len(self.items)

class TaskManager:
    def __init__(self):
        self.stack = Stack()
        self.tasks_by_priority = {}
    
    def new_task(self, task, priority):
        self.stack.push((task, priority))
        
        if priority not in self.tasks_by_priority:
            self.tasks_by_priority[priority] = []
        
        if task not in self.tasks_by_priority[priority]:
            self.tasks_by_priority[priority].append(task)
    
    def remove_task(self, task_name):
        for priority, tasks in list(self.tasks_by_priority.items()):
            if task_name in tasks:
                tasks.remove(task_name)
                if not tasks:
                    del self.tasks_by_priority[priority]
        
        temp_items = []
        while len(self.stack) > 0:
            task, priority = self.stack.pop()
            if task != task_name:
                temp_items.append((task, priority))
        
        for item in reversed(temp_items):
            self.stack.push(item)
    
    def __str__(self):
        result = []
        for priority in sorted(self.tasks_by_priority.keys()):
            tasks = self.tasks_by_priority[priority]
            result.append(f"{priority} {'; '.join(tasks)}")
        
        return '\n'.join(result) if result else "Нет задач"

manager = TaskManager()
manager.new_task("сделать уборку", 4)
manager.new_task("помыть посуду", 4)
manager.new_task("отдохнуть", 1)
manager.new_task("поесть", 2)
manager.new_task("сдать дз", 2)
print(manager)
