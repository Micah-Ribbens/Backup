from copy import deepcopy

from base.velocity_calculator import VelocityCalculator


class HistoryKeeper:
    last_objects = {}
    last_time = 0

    def add(self, name, history_keeper_object, needs_deepcopy):
        if needs_deepcopy:
            history_keeper_object = deepcopy(history_keeper_object)

        self.last_objects[f"{name}{VelocityCalculator.time}"] = history_keeper_object

    def get_last(self, name):
        return self.last_objects[f"{name}{self.last_time}"]








