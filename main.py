import logging
import sys

from callable import Call_Sleep
from dispatcher import Dispatcher
from Task import Task

logging.basicConfig(level = logging.INFO, 
                    format = "%(asctime)s %(message)s",
                    stream = sys.stdout)

logger = logging.getLogger(__name__)

def func_1(i: int) -> None:
    logger.info(f'Func {i} started')
    yield Call_Sleep(5)
    logger.info(f'Func {i} ended')

if __name__ == '__main__':
    disp = Dispatcher()

    for i in range(5):
        task = Task(i, func_1, f"Task {i}")
        disp.add(task)
    disp.run()

    
