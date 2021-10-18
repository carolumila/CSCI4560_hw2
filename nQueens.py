from pyevolve import G1DList
from pyevolve import GSimpleGA
from pyevolve import Crossovers
from pyevolve import Consts
from pyevolve import GAllele
import pyevolve
import random

# This function is the evaluation function, we want
# to give high score to chromosomes that have higher collisions
# want to minimize
def eval_func(chromosome):
    score = 0.0

    # check diagonals
    for value, i in enumerate(chromosome):
        for value2, j in enumerate(chromosome):
            #print(i, j, value, value2, score)
            if value != value2:
                if abs(value - value2) == abs(i-j):
                    score += 1

    #print("check row----------------")

    # check row
    for value, i in enumerate(chromosome):
        for value2, j in enumerate(chromosome):
            #print(i, j, value, value2, score)
            if value != value2:
                if i == j:
                    score += 1
                
    return score

def G1DListTSPInitializator(genome, **args):
    n = 100

    genome.clearList()
    lst = [i+1 for i in xrange(n)]

    for i in xrange(n):
        choice = random.choice(lst)
        lst.remove(choice)
        genome.append(choice)

def run_main():
    # number of queens
    n = 100

    setOfAlleles = GAllele.GAlleles(homogeneous=True)
    lst = [ i+1 for i in xrange(n) ]
    a = GAllele.GAlleleList(lst)
    setOfAlleles.add(a)

    # Genome instance
    genome = G1DList.G1DList(n)
    genome.setParams(rangemin=1, rangemax=n, bestRawScore=0.00, roundDecimal=2)
    genome.crossover.set(Crossovers.G1DListCrossoverCutCrossfill)
    genome.setParams(allele=setOfAlleles)
    genome.initializator.set(G1DListTSPInitializator)

    # the evaluator function 
    genome.evaluator.set(eval_func)

    # genetic algorithm instance
    ga = GSimpleGA.GSimpleGA(genome)
    ga.setPopulationSize(100)
    ga.setGenerations(10000)
    ga.terminationCriteria.set(GSimpleGA.ConvergenceCriteria)
    ga.setMinimax(Consts.minimaxType["minimize"])
    ga.setMutationRate(0.03)

    # run the evolution
    ga.evolve(freq_stats=100)

    # print best individual
    print(ga.bestIndividual())
    
if __name__ == "__main__":
    run_main()