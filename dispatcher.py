import logging
from time import sleep
from Task import Task
from typing import Optional

logger = logging.getLogger(__name__)

class Dispatcher:
    def __init__(self):
        self._queue: list[Task] = []

    def add(self, task : Task) -> None:
        self._queue.append(task)
    
    def pop(self) -> Optional[Task]:
        return self._queue.pop(0)
    
    def process(self, task: Optional[Task]) -> None:
        if task is None:
            return
        try:
            result = task.run()
        except StopIteration:
            logger.info(f"Task {task.id} finished")
            return
        self.add(task)
        return result
    
    def run(self) -> None:
        try:
            while True:
                task = self.pop()
                self.process(task)
                sleep(0.2)
        except IndexError:
            logger.info("ALL TASKS FINISHED")




    