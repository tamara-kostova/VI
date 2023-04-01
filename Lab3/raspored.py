from constraint import *

def max4 (*args):
    t1=0
    t2=0
    t3=0
    t4=0
    for termin in args:
        if termin == 'T4':
            t4+=1
        if termin == 'T3':
            t3+=1
        elif termin == 'T2':
            t2+=1
        elif termin == 'T1':
            t1+=1
    if t1 >4 or t2 >4 or t3>4 or t4>4:
        return False
    return True

if __name__ == '__main__':
    num = int(input())

    papers = dict()

    ai_papers = []
    ml_papers = []
    nlp_papers = []

    paper_info = input()
    while paper_info != 'end':
        title, topic = paper_info.split(' ')
        papers[title] = topic
        paper_info = input()
        if topic == 'AI':
            ai_papers.append(title)
        elif topic == 'NLP':
            nlp_papers.append(title)
        else:
            ml_papers.append(title)

    # Tuka definirajte gi promenlivite

    variables = papers.keys()

    domain = [f'T{i + 1}' for i in range(num)]

    problem = Problem(BacktrackingSolver())

    # Dokolku vi e potrebno moze da go promenite delot za dodavanje na promenlivite
    problem.addVariables(variables, domain)

    # Tuka dodadete gi ogranichuvanjata
    problem.addConstraint(max4)
    for topic_papers in [ai_papers, ml_papers, nlp_papers]:
        if 0 < len(topic_papers) <= 4:
            problem.addConstraint(AllEqualConstraint(), topic_papers)

    result = problem.getSolution()
    for i in range(1,11):
        paper = "Paper"+str(i)
        print(f"{paper} ({papers[paper]}): {result[paper]}")

