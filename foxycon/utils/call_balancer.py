import random
import time


class CallBalancer:
    def __init__(self, balancing_objects: list):
        self.balancing_objects = balancing_objects

    def call_next(self):
        bal_obj = self.balancing_objects.pop(0)
        self.balancing_objects.append(bal_obj)
        sec = random.randrange(2, 8, 1)
        time.sleep(sec)
        return bal_obj
