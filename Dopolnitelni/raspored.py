from constraint import *

def twohours(x,y):
    if x[0:4] == y[0:4]:
        if abs(int(x[4:6])-int(y[4:6]))<=1:
            return False
    return True

def ml_hours(x, y):
    return x[4:6] != y[4:6]

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())
    casovi_AI = int(input())
    casovi_ML = int(input())
    casovi_R = int(input())
    casovi_BI = int(input())

    AI_predavanja_domain = ["Mon_11", "Mon_12", "Wed_11", "Wed_12", "Fri_11", "Fri_12"]
    ML_predavanja_domain = ["Mon_12", "Mon_13", "Mon_15", "Wed_12", "Wed_13", "Wed_15", "Fri_11", "Fri_12", "Fri_15"]
    R_predavanja_domain = ["Mon_10", "Mon_11", "Mon_12", "Mon_13", "Mon_14", "Mon_15", "Wed_10", "Wed_11", "Wed_12",
                           "Wed_13", "Wed_14", "Wed_15", "Fri_10", "Fri_11", "Fri_12", "Fri_13", "Fri_14", "Fri_15"]
    BI_predavanja_domain = ["Mon_10", "Mon_11", "Wed_10", "Wed_11", "Fri_10", "Fri_11"]

    AI_vezbi_domain = ["Tue_10", "Tue_11", "Tue_12", "Tue_13", "Thu_10", "Thu_11", "Thu_12", "Thu_13"]
    ML_vezbi_domain = ["Tue_11", "Tue_13", "Tue_14", "Thu_11", "Thu_13", "Thu_14"]
    BI_vezbi_domain = ["Tue_10", "Tue_11", "Thu_10", "Thu_11"]

    # ---Tuka dodadete gi promenlivite--------------------
    casovi_ai=list()
    casovi_bi=list()
    casovi_r=list()
    casovi_ml=list()
    variables = ["AI_vezbi", "BI_vezbi", "ML_vezbi"]
    for i in range(casovi_AI):
        casovi_ai.append(f'AI_cas_{i+1}')
        variables.append(f'AI_cas_{i+1}')
    for i in range(casovi_BI):
        casovi_bi.append(f'BI_cas_{i+1}')
        variables.append(f'BI_cas_{i+1}')
    for i in range(casovi_R):
        casovi_r.append(f'R_cas_{i+1}')
        variables.append(f'R_cas_{i+1}')
    for i in range(casovi_ML):
        casovi_ml.append(f'ML_cas_{i+1}')
        variables.append(f'ML_cas_{i+1}')
    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addVariables(casovi_ai,AI_predavanja_domain)
    problem.addVariables(casovi_bi, BI_predavanja_domain)
    problem.addVariables(casovi_r, R_predavanja_domain)
    problem.addVariables(casovi_ml, ML_predavanja_domain)
    problem.addVariable("AI_vezbi", AI_vezbi_domain)
    problem.addVariable("BI_vezbi", BI_vezbi_domain)
    problem.addVariable("ML_vezbi", ML_vezbi_domain)
    problem.addConstraint(AllDifferentConstraint())
    for x in variables:
        for y in variables:
            if x!=y:
                problem.addConstraint(twohours,[x,y])
    casovi_ml.append("ML_vezbi")
    for x in casovi_ml:
        for y in casovi_ml:
            if x != y:
                problem.addConstraint(ml_hours, [x, y])
    # ----------------------------------------------------
    solution = problem.getSolution()

    print(solution)