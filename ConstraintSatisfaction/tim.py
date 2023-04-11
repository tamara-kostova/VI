from constraint import *

if __name__ == '__main__':
    brclenovi = int(input())
    clenovi = dict()
    clenovitezina = list()
    for i in range(brclenovi):
        clen = input()
        clenovi[float(clen[0:4])]=clen[-1]
        clenovitezina.append(float(clen[0:4]))
    brlideri = int(input())
    lideri = dict()
    lideritezina = list()
    for i in range(brlideri):
        lider = input()
        lideri[float(lider[0:4])]=lider[-1]
        lideritezina.append(float(lider[0:4]))
    problem = Problem(BacktrackingSolver());
    variables = ["Team leader"]
    for i in range(1,6):
        problem.addVariable(f"Participant {i}",tuple(clenovitezina))
        variables.append(f"Participant {i}")
    problem.addVariable("Team leader",tuple(lideritezina))
    problem.addConstraint(MaxSumConstraint(100),variables)
    problem.addConstraint(AllDifferentConstraint(), variables)
    #solutions = problem.getSolutions()


    res=problem.getSolutions()
    res.sort(key=lambda e: sum(e.values()), reverse=True)
    sol = res[0]
    total = 0
    for i in range(5):
        total+=float(sol[f"Participant {i+1}"])
    total += float(sol[f"Team leader"])
    print(f"Total score: {round(total,2)}")
    print("Team leader: "+lideri[sol["Team leader"]])
    for i in range(5):
        print(f"Participant {i+1}: "+clenovi[sol[f"Participant {i+1}"]])


