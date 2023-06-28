import random as r
from mad.data_structures import GoalNode
from mad.optimize import jonathan_algorithm
from mad.optimize import _score_allocation

def random_binary_symetric():

    root = GoalNode("Main Goal", {"grace": r.randrange(25, 35), "remus": r.randrange(25, 35), "franklin": r.randrange(25, 35)})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def main():
    root = random_binary_symetric()
    results = jonathan_algorithm(root, 30, 1)
    score = _score_allocation(results)
    
    print(score)

    for agent, goals in results.items():
        print(agent)
        for goal in goals:
            print(goal.name, goal.agent, goal.cost)

if __name__ == '__main__':
    main()
