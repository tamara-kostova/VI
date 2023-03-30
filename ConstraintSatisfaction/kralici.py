from constraint import *

def not_attacking (k1, k2):
    if k1[0]!=k2[0] and k1[1]!=k2[1] and k1[0]-k1[1]!=k2[0]-k2[1] and k1[0]+k1[1]!=k2[0]+k2[1]:
        return True
    return False

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    """variables = ["A", "B", "C", "D", "E", "F"]
    for variable in variables:
        problem.addVariable(variable, Domain(set(range(100))))"""
    n = int(input())
    kralici = range(1,n+1)
    domain = [(i,j) for i in range (0,n) for j in range (0,n)]
    problem.addVariables(kralici,domain)
    # ---Tuka dodadete gi ogranichuvanjata----------------
    for k1 in kralici:
        for k2 in kralici:
            if k1 < k2:
                problem.addConstraint(not_attacking, (k1,k2))
    # ----------------------------------------------------
    if (n<=6):
        print(len(problem.getSolutions()))
    else:
        print(problem.getSolution())