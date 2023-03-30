from constraint import *

def f(s,e,n, d, m, o, r, y):
    return 1000*(s+m) + 100*(e+o) +10*(n+r) +d+e == 10000*m+1000*o+100*n+10*e+y

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    variables = ["S", "E", "N", "D", "M", "O", "R", "Y"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(10))))

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(f,variables)
    problem.addConstraint(AllDifferentConstraint(),variables)
    # ----------------------------------------------------
    print(problem.getSolution())