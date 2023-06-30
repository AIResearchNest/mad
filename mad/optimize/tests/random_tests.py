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

def random_large_tree():
    
    x = 30
    y = 60
    root = GoalNode("Main Goal", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal8 = GoalNode("Sub Goal 8", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal9 = GoalNode("Sub Goal 9", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal10 = GoalNode("Sub Goal 10", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal11 = GoalNode("Sub Goal 11", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal12 = GoalNode("Sub Goal 12", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal13 = GoalNode("Sub Goal 13", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal14 = GoalNode("Sub Goal 14", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)}) 
    subgoal16 = GoalNode("Sub Goal 16", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal17 = GoalNode("Sub Goal 17", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal18 = GoalNode("Sub Goal 18", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal19 = GoalNode("Sub Goal 19", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal20 = GoalNode("Sub Goal 20", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal21 = GoalNode("Sub Goal 21", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal22 = GoalNode("Sub Goal 22", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal23 = GoalNode("Sub Goal 23", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal24 = GoalNode("Sub Goal 24", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal25 = GoalNode("Sub Goal 25", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal26 = GoalNode("Sub Goal 26", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal27 = GoalNode("Sub Goal 27", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal28 = GoalNode("Sub Goal 28", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal29 = GoalNode("Sub Goal 29", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    subgoal30 = GoalNode("Sub Goal 30", {"grace": r.randrange(x,y), "remus": r.randrange(x,y), "franklin": r.randrange(x,y)})
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)
    subgoal4.add_child(subgoal9)
    subgoal4.add_child(subgoal10)
    subgoal5.add_child(subgoal11)
    subgoal5.add_child(subgoal12)
    subgoal6.add_child(subgoal13)
    subgoal6.add_child(subgoal14)

    subgoal7.add_child(subgoal15)
    subgoal7.add_child(subgoal16)
    subgoal8.add_child(subgoal17)
    subgoal8.add_child(subgoal18)
    subgoal9.add_child(subgoal19)
    subgoal9.add_child(subgoal20)
    subgoal10.add_child(subgoal21)
    subgoal10.add_child(subgoal22)
    subgoal11.add_child(subgoal23)
    subgoal11.add_child(subgoal24)
    subgoal12.add_child(subgoal25)
    subgoal12.add_child(subgoal26)
    subgoal13.add_child(subgoal27)
    subgoal13.add_child(subgoal28)
    subgoal14.add_child(subgoal29)
    subgoal14.add_child(subgoal30)

    return root

def main():

    scores = []
    discrepancy = []

    for i in range(1):
        
        print("---------------------")
        print(f"Test {i}:")
        print("---------------------")

        root = random_large_tree()
        # root = random_binary_symetric()
        output = jonathan_algorithm(root, 30, 1)
        score = _score_allocation(output)

        scores.append(score[0])
        discrepancy.append(score[1])
        
        print()
        print(f"Score: {score[0]}")
        print(f"Discrepancy: {score[1]}")

if __name__ == '__main__':
    main()
