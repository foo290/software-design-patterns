class Observer:
    def update(self, obj, *args, **kwargs):
        raise NotImplemented


class Observable:
    def __init__(self):
        self._observers = []

    def add_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observer(self, *args, **kwargs):
        for observer in self._observers:
            observer.update(self, *args, **kwargs)


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


class TaskAdapter(Observable):
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
            self.notify_observer(key=key, value=value, msg="Attribute Change")  # notifying observer


class Developer(Observer):
    def update(self, obj, *args, **kwargs):
        print("\nUpdate Received...")
        print(f'You received an update from {obj} with info: {args}, {kwargs}')


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
            adapter.notify_observer(name=adapter.name, state=adapter.state, msg="Task complete")


    @classmethod
    def monitor_task(cls, observer):
        print('Adding observers...')
        for eachAdapter in cls.task_adapters:
            eachAdapter.add_observer(observer)


if __name__ == '__main__':
    dev = Developer()

    TaskFacade.create_tasks()
    TaskFacade.monitor_task(dev)

    TaskFacade.mark_all_complete()


