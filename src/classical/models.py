from abc import ABC


class Worker(ABC):
    def __init__(self, **args):
        self.args = args

    def __getattribute__(self, name):
        return super().__getattribute__(name)
    
    def __getstate__(self):
        return super().__getstate__()
    

class ProductionWorker(Worker):
    def __init__(self, production, items, **args):
        self.production = production
        self.items = items
        super().__init__(**args)

    def info(self):
        n = len(self.production)

        print("Worker produce:")
        for i in range(n):
            print(f"- {self.items[i]}: {self.production[i]}")