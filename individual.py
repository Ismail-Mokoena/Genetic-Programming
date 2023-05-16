from dataclasses import dataclass, field
from random import random

@dataclass
class Individual():
    space: list = field(default_factory=list)
    prices: list = field(default_factory=list)
    space_limit: int = 0
    generation: int = 0
    chromosome: list = field(default_factory=list)
    

    def set_chromosome(cls):
        for i in range(len(cls.space)):
            if random() < 0.5:
                cls.chromosome.append('0')
            else:
                cls.chromosome.append('1')