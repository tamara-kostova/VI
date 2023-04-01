from constraint import *

def check_other(simona, marija, petar):
    if simona == 1 and (marija==1 or petar==1):
        return True
    return False


def check_all(simonat, marijat, petart, time):
    if marijat == 1 and time != 14 and time != 15 and time != 18:
        return False
    if petart == 1 and time != 12 and time != 13 and time != 16 and time != 17 and time != 18 and time != 19:
        return False
    if simonat == 1 and time != 13 and time != 14 and time != 16 and time != 19:
        return False
    return True

def simona(s):
    return s == 1

if __name__ == '__main__':
    problem = Problem(BacktrackingSolver())

    # ---Dadeni se promenlivite, dodadete gi domenite-----
    problem.addVariable("Marija_prisustvo", [0, 1])
    problem.addVariable("Simona_prisustvo", [0, 1])
    problem.addVariable("Petar_prisustvo", [0, 1])
    problem.addVariable("vreme_sostanok", range(12, 21))
    # ----------------------------------------------------

    # ---Tuka dodadete gi ogranichuvanjata----------------
    problem.addConstraint(simona, ['Simona_prisustvo'])
    problem.addConstraint(check_all, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo", "vreme_sostanok"])
    problem.addConstraint(check_other, ["Simona_prisustvo", "Marija_prisustvo", "Petar_prisustvo"])
    # ----------------------------------------------------

    [print(solution) for solution in problem.getSolutions()]