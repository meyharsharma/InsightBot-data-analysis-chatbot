WORKER_REGISTRY = {}

def register_worker(cls):
    WORKER_REGISTRY[cls.__name__] = cls
    return cls

class BaseWorker:
    def __init__(self):
        pass

    def run(self, task_input):
        raise NotImplementedError("Subclasses must implement the run method.")