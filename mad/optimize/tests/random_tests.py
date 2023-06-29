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

def random_binary_left():

    root = GoalNode("Main Goal", {"grace": r.randrange(25, 35), "remus": r.randrange(25, 35), "franklin": r.randrange(25, 35)})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def random_root():

    root = root = GoalNode("Main Goal", {"grace": r.randrange(25, 35), "remus": r.randrange(25, 35), "franklin": r.randrange(25, 35)})

    return root

def random_tree_symetric():

    root = GoalNode("Main Goal", {"grace": r.randrange(25, 35), "remus": r.randrange(25, 35), "franklin": r.randrange(25, 35)})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal7 = GoalNode("Sub Goal 7", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal8 = GoalNode("Sub Goal 8", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal9 = GoalNode("Sub Goal 9", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal10 = GoalNode("Sub Goal 10", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal11 = GoalNode("Sub Goal 11", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal12 = GoalNode("Sub Goal 12", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal2.add_child(subgoal7)
    subgoal2.add_child(subgoal8)
    subgoal2.add_child(subgoal9)
    subgoal3.add_child(subgoal10)
    subgoal3.add_child(subgoal11)
    subgoal3.add_child(subgoal12)
    
    return root

def random_tree_left_right():

    root = GoalNode("Main Goal", {"grace": r.randrange(25, 35), "remus": r.randrange(25, 35), "franklin": r.randrange(25, 35)})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": r.randrange(15, 25), "remus": r.randrange(15, 25), "franklin": r.randrange(15, 25)})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal7 = GoalNode("Sub Goal 7", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal8 = GoalNode("Sub Goal 8", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})
    subgoal9 = GoalNode("Sub Goal 9", {"grace": r.randrange(5, 15), "remus": r.randrange(5, 15), "franklin": r.randrange(5, 15)})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    root.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal1.add_child(subgoal5)
    subgoal1.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal3.add_child(subgoal9)
    
    return root

def main():

    scores = []
    discrepancy = []

    for i in range(1, 16):
        
        print("---------------------")
        print(f"Test {i}:")
        root = random_binary_symetric()
        output = jonathan_algorithm(root, 30, 1)
        score = _score_allocation(output)

        scores.append(score[0])
        discrepancy.append(score[1])
        
        print()
        print(f"Score: {score[0]}")
        print(f"Discrepancy: {score[1]}")

if __name__ == '__main__':
    main()
