import random
import time

class CallBalancer:
    def __init__(self, balancing_objects: list):
        self.balancing_objects = []

        for balanc_ob in balancing_objects:
            self.balancing_objects.append({"balanc_ob": balanc_ob, "num_requests": self.get_number_requests()})

    def get_element(self, bal_obj):
        bal_obj['num_requests']  = bal_obj['num_requests'] - 1
        self.balancing_objects.insert(0, bal_obj)
        time.sleep(random.randrange(2, 6, 1))
        return bal_obj.get("balanc_ob")

    def call_next(self):
        bal_obj = self.balancing_objects.pop(0)
        if bal_obj.get('num_requests') == 0:
            bal_obj['num_requests'] = self.get_number_requests()
            self.balancing_objects.append(bal_obj)
            bal_obj = self.balancing_objects.pop(0)


        return self.get_element(bal_obj)



    @staticmethod
    def get_number_requests():
        return random.randrange(2, 5, 1)
