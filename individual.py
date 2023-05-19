from dataclasses import dataclass, field
from random import random

@dataclass
class Individual():
    space: list = field(default_factory=list)
    prices: list = field(default_factory=list)
    space_limit: float = 0.0
    score_eval: int =0
    used_space: float = 0.0
    generation: int = 0
    chromosome: list = field(default_factory=list)
    

    def set_chromosome(cls):
        """Decides randomly which product we'll load
            0- We dont select, 1- We select."""
        for i in range(len(cls.space)):
            if random() < 0.5:
                cls.chromosome.append('0')
            else:
                cls.chromosome.append('1')
    
    def fitness(cls):
        score = 0
        total_space = 0
        for i in range(len(cls.chromosome)):
            if cls.chromosome[i] == '1':
                score += float(cls.prices[i])
                total_space+=float(cls.space[i])
        
        if total_space>cls.space_limit:
            cls.score=1
        cls.score_eval=score
        cls.used_space=total_space
        
    def crossover(cls, parent):
        cutoff = round(random()*len(cls.chromosome))
        chromosome_a = parent.chromosome[0:cutoff] + cls.chromosome[cutoff::]
        chromosome_b = cls.chromosome[0:cutoff] + parent.chromosome[cutoff::]