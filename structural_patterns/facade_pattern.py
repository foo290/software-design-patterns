class Task1:
    def __init__(self):
        self.name = self.__class__.__name__
        self.state = "Running"

    def mark_complete(self):
        print(f"Marking {self.name} complete.")
        self.state = "Complete"


class Task2:
    def __init__(self):
        self.name = self.__class__.__name__
        self.state = "Running"

    def mark_complete(self):
        print(f"Marking {self.name} complete.")
        self.state = "Complete"


class Task3:
    def __init__(self):
        self.name = self.__class__.__name__
        self.state = "Running"

    def mark_complete(self):
        print(f"Marking {self.name} complete.")
        self.state = "Complete"


class TaskAdapter:
    _initialized = False

    def __init__(self, task, **kwargs):
        super().__init__()
        self.task = task

        for key, val in kwargs.items():
            func = getattr(self.task, val)
            self.__setattr__(key, func)
        self._initialized = True

    def __getattr__(self, item):
        return getattr(self.task, item)

    def __setattr__(self, key, value):
        if not self._initialized:
            super().__setattr__(key, value)
        else:
            setattr(self.task, key, value)


class TaskFacade:
    task_adapters = None

    @classmethod
    def create_tasks(cls):
        print("Initializing tasks...")
        cls.task_adapters = [
            TaskAdapter(Task1(), complete='mark_complete'),
            TaskAdapter(Task2(), complete='mark_complete'),
            TaskAdapter(Task3(), complete='mark_complete')
        ]

    @classmethod
    def mark_all_complete(cls):
        print("Marking all tasks as complete.")
        for adapter in cls.task_adapters:
            adapter.mark_complete()


if __name__ == '__main__':
    TaskFacade.create_tasks()
    TaskFacade.mark_all_complete()
