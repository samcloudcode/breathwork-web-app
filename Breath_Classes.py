import math
from functools import reduce


class Action:
    def __init__(self):
        self.name = ""
        self.time = 1
        self.scale = True
        self.description = ""

class BreathCycle:
    def __init__(self):
        self.actions = []

    def add_action(self, action):
        self.actions.append(action)

    def add_actions(self, actions):
        for action in actions:
            self.actions.append(action)

    def total_time(self):
        total_time = 0
        for action in self.actions:
            total_time = total_time + action.time

        return total_time

    def gcd(self):
        times = []
        for action in self.actions:
            times.append(int(action.time))
        gcd = reduce(math.gcd, times)

        return gcd

    def scale(self, factor):
        gcd = self.gcd()
        for action in self.actions:
            if action.scale:
                action.time = int((factor + action.time/gcd) * gcd)
        return self.total_time()




class BreathSequence:
    def __init__(self):
        self.breath_cycles = []

    def add_breath_cycle(self, breath_cycle_object, scale_factor=0, repeat=1):
        breath_cycle_object.scale(scale_factor)
        for i in range(repeat):
            self.breath_cycles.append(breath_cycle_object)

    def total_time(self):
        total_time = 0
        for breath_cycle in self.breath_cycles:
            total_time = total_time + breath_cycle.total_time()

        return total_time

    def load_sequence(self, sequence_name):
        pass

if __name__ == '__main__':
    action1 = Action(name='Breath In', time=4, scale=True)
    action2 = Action(name='Hold In', time=8, scale=True)
    action3 = Action(name='Breath Out', time=12, scale=True)
    action4 = Action(name='Hold Out', time=4, scale=True)

    sq_breath_cycle = BreathCycle('Square Breathing')
    sq_breath_cycle.add_actions([action1, action2, action3, action4])

    breath_sequence = BreathSequence("square breathing")
    breath_sequence.add_breath_cycle(sq_breath_cycle, repeat=3)

    for action in sq_breath_cycle.actions:
        print(action.name, action.time)

    print(sq_breath_cycle.total_time())
    print(sq_breath_cycle.scale(2))
    print(breath_sequence.total_time())







