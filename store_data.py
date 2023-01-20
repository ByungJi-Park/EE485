
import os
import pickle
path = os.path.abspath(__file__)
print(os.path.join('dd', 'aa', 'hh'))

n = 1    
data = {'c':1, 'b':2}
with open(f"data/data.pickle {n}", "wb") as f:
    pickle.dump(data, f)
    
with open(f"data/data.pickle {n}", "rb") as f:
    data = pickle.load(f)
    print(len(data))
    print(data)
'''    
class Person:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self._age = age

    @property
    def agee(self):
        return self._age

    @agee.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Invalid age")
        self._age = age
person = Person('a','b',3)
print(person.age)

from collections import namedtuple
Action1 = namedtuple('Action', ['type', 'target', 'pos', 'orn'])
s = Action1('a', 'b', 'c', 'd')
print(s)
print(type(s))
print(s.type)

def haha(x=9):
    return 1,2,3,4
y, *rest = haha(7)
print(y)
print(rest)

# Store data
import numpy as np
from collections import namedtuple
def change_dict(x):
    for uid in list(x.keys()):
        obj = agent.env.uid_to_target[uid]
        x[obj] = x.pop(uid)
Action = namedtuple('Action', ['type', 'target', 'pos', 'orn'])
Observation = namedtuple('Observation', ['img', 'mask'])
data_action = []
data_observation = []
data_reward = []
for a, o, r in agent.history:
    traj = np.asarray(a.traj)
    data_action.append(Action(a.type, a.target, a.pos, a.orn))
    data_observation.append(Observation(o.observation.tolist(), change_dict(o.seg_mask)))
    data_reward.append(r)
data = {"action": data_action, "observation": data_observation, "reward": data_reward}
'''
