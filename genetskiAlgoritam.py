import math
import random
import pylab

POP_SIZE = 100
ELIMINATION_PERCENT=10
ELIMINATION_NUMBER=int(ELIMINATION_PERCENT*POP_SIZE/100)
#SURVIVERS=POP_SIZE-ELIMINATION_NUMBER
DNA_SIZE = 32
MUTATIONS_PERCENT=10
MUTATIONS_NUMBER=int(MUTATIONS_PERCENT*POP_SIZE/100)
N=2**DNA_SIZE-1
GENERATIONS = 10
LEFT = 0.0
RIGHT = 10.0

fdna1 = 0.0
fdna2 = 0.0

najbolji = list()
najboljiF = list()

def f(x):
    return 3*math.sin(x/4)*math.cos(x)

def random_item():  #kreiranje jednog hromozoma
    dna = random.uniform(0,10.1)
    return dna

def random_population(): # kreiranje populacije hromozoma
    pop = []
    for i in range(POP_SIZE):
        pop.append(random_item())
    return pop

def fitness(pop): #definisanje dobrote  i kazne cele populacije
    quality=[]
    for word in pop:
        x=word
        quality.append(f(x))
    dmin=min(quality)
    for i in range(len(quality)):
        quality[i]-=dmin
    dmax=max(quality)
    penals=[]
    for i in range(len(quality)):
        penals.append(dmax-quality[i])
    return quality, penals

def cumulative_quality(pop):
    s = []
    for i in range(len(pop)):
        s.append(sum(item[0] for item in pop[:i]))
    return s

def elimination(pop):
    for j in range(ELIMINATION_NUMBER):
        s=cumulative_quality(pop)
        n = random.uniform(0, s[len(pop)-1])
        for i in range(len(pop)):
            if n<s[i] and pop[i][0]:
                del pop[i]
                break
    return pop

def crossover(dna1, dna2): # ukrstanje
    global fdna1
    global fdna2
    fdna1 = dna1
    fdna2 = dna2
    if(fdna1>fdna2):
        d = fdna2 + random.random() * (fdna1-fdna2)
        fdna1 -= d
        fdna2 += d
    else:
        d = fdna1 + random.random() * (fdna2 - fdna1)
        fdna1 += d
        fdna2 -= d

def mutation(pair):
    if pair[0]:
        sign = random.randrange(0,2,1)
        if(sign == 0):
            sign = -1
        else:
            sign = 1
        LEFT1 = LEFT + pair[1] * sign
        RIGHT1 = RIGHT + pair[1] * sign
        broj = LEFT1 + random.random() * (RIGHT1-LEFT1)
        if (sign == -1):
            potomak = pair[1]+broj
        else:
            potomak = pair[1] - broj
        return potomak
    else:
        return pair[1]

def evaluation_pairs(population):
    quality, penals = fitness(population)
    eval_population = []
    for i in range(POP_SIZE):
        pair=(penals[i], population[i] )
        eval_population.append(pair)
    return eval_population



def prikazi():
    global najbolji
    global najboljiF
    pylab.plot(najbolji, najboljiF, 'ro')
    pylab.show()

flask_poruka = list()


#POCETAK*******************************************************************************


def glavnaPetlja():
    population = random_population()
    global flask_poruka
    flask_poruka = list()

    for k in range(GENERATIONS):

        eval_population = evaluation_pairs(population)  # kreiranje parova kazna, hromozom
        for penal, hromosome in eval_population:  # trazenje najboljeg para-kazna=0
            if penal:
                continue
            else:
                best = hromosome
                break
        x = best

        if(k==9):
            for hromosome in population:
                global najbolji
                hr1 = hromosome
                najbolji.append(hr1)
                global najboljiF
                najboljiF.append(f(hr1))


        flask_poruka.append(str(k) + ' ' + str(x) + ' ' + str(f(x))) # stampanje najboljeg u svakoj iteraciji

        eval_population = elimination(eval_population)  # eliminacija losih

        # kreiranje nove populacije
        population = []
        for penal, dna in eval_population:  # oni koji nisu eliminisani, ulaze u novu generaciju
            population.append(dna)
        for i in range(ELIMINATION_NUMBER):  # oni koji su eliminisani nadomešćuju se ukrštanjem preostalih
            i1 = int(random.randrange(0, ELIMINATION_NUMBER, 1))
            i2 = int(random.randrange(0, ELIMINATION_NUMBER, 1))
            parent1 = eval_population[i1]
            parent2 = eval_population[i2]
            if parent1 != parent2:
                # child=crossover(parent1[1],parent2[1])
                crossover(parent1[1], parent2[1])
                # population.append(child)
                population.append(fdna1)
                population.append(fdna2)
            else:
                child = random_item()
                population.append(child)
                if parent2[0]:
                    mparent = mutation(parent2)
                    del population[i2]
                    del eval_population[i2]
                    population.append(mparent)
                    eval_population.append((0., mparent))

        eval_population = evaluation_pairs(population)

        for i in range(MUTATIONS_NUMBER):
            index = random.randrange(0, POP_SIZE, 1)
            population[index] = mutation(eval_population[index])

    print(flask_poruka)
    return flask_poruka