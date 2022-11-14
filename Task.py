import logging
from datetime import datetime, timedelta
from callable import Call_Sleep
from typing import Callable, Optional

logger = logging.getLogger(__name__)

class Task:
    def __init__(self, id: int, task: Callable, *args, **kwargs):
        self._id = id
        self._task = task
        self._args = args
        self._kwargs = kwargs
        self.core = self._task(*self._args)
        self.defferd = None

    @property
    def id(self) -> int:
        return self._id

    def run(self) -> Optional[Call_Sleep]:
        if self.defferd and self.defferd > datetime.now():
            logger.info(f"Task {self._id} is not ready. Skip")
            return 
        
        result = next(self.core)

        if isinstance(result, Call_Sleep):
            logger.info(f"Task {self._id} Inited.")
            self.defferd = timedelta(seconds = result.seconds) + datetime.now()
            return
        
        return result


