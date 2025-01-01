import random
import time


# class CallBalancer:
#     def __init__(self, balancing_objects: list):
#         self.balancing_objects = balancing_objects
#
#     def call_next(self):
#         bal_obj = self.balancing_objects.pop(0)
#         self.balancing_objects.append(bal_obj)
#         sec = random.randrange(2, 8, 1)
#         time.sleep(sec)
#         return bal_obj


class CallBalancer:
    def __init__(self, balancing_objects: list):
        self.balancing_objects = []

        for balanc_ob in balancing_objects:
            self.balancing_objects.append({"balanc_ob": balanc_ob, "num_requests": self.get_number_requests()})
            print(self.balancing_objects)

    def get_element(self, bal_obj):
        bal_obj['num_requests']  = bal_obj['num_requests'] - 1
        self.balancing_objects.insert(0, bal_obj)
        print(self.balancing_objects)
        return bal_obj.get("balanc_ob")

    def call_next(self):
        bal_obj = self.balancing_objects.pop(0)
        if bal_obj.get('num_requests') != 0:
            print(self.get_element(bal_obj))
            return self.get_element(bal_obj)
        else:
            bal_obj['num_requests'] = self.get_number_requests()
            self.balancing_objects.append(bal_obj)
            print(self.get_element(bal_obj))
            return self.get_element(bal_obj)

        # self.balancing_objects.append(bal_obj)
        # sec = random.randrange(2, 8, 1)
        # time.sleep(sec)

    @staticmethod
    def get_number_requests():
        return random.randrange(2, 5, 1)
