import random as r
from typing import Dict
from mad.data_structures import GoalNode
from mad.optimize import jonathan_algorithm

def _random_cost(m: int, n: int) -> Dict[str, int]:
    
    """
    This function randomizes the cost of an agent when it conducts a goal based on an assigned range

    Parameters
    ----------
    m: int
        The starting point of the range
    n: int
        The ending point of the range
    
    Returns
    -------
    
    Dict[str,int]
        A dictionary with the agents as keys and corresponding costs as values
    
    """
    
    d = {}
    d["grace"] = r.randint(m,n)
    d["remus"] = r.randint(m,n)
    d["franklin"] = r.randint(m,n)
    #print(d)
    return d

def random_binary_symetric():

    root = GoalNode("Main Goal", _random_cost(25, 35))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 15))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 15))

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    return root

def random_binary_left():

    root = GoalNode("Main Goal", _random_cost(25, 35))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(10, 20))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(10, 20))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(5, 15))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 15))
    
    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)

    return root

def random_root():

    root = root = GoalNode("Main Goal", _random_cost(25, 35))

    return root

def random_tree_symetric():

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(5, 10))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(5, 10))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(5, 10))

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

    root = GoalNode("Main Goal", _random_cost(30, 45))
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(15, 25))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(15, 25))
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(15, 25))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(5, 10))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(5, 10))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(5, 10))
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(5, 10))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(5, 10))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(5, 10))

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
    root = GoalNode("Main Goal", _random_cost(x, y))
    
    x = 23
    y = 30
    subgoal1 = GoalNode("Sub Goal 1", _random_cost(x, y))
    subgoal2 = GoalNode("Sub Goal 2", _random_cost(x, y))
    
    x = 10
    y = 20
    subgoal3 = GoalNode("Sub Goal 3", _random_cost(x, y))
    subgoal4 = GoalNode("Sub Goal 4", _random_cost(x, y))
    subgoal5 = GoalNode("Sub Goal 5", _random_cost(x, y))
    subgoal6 = GoalNode("Sub Goal 6", _random_cost(x, y))
    
    x = 5
    y = 10
    subgoal7 = GoalNode("Sub Goal 7", _random_cost(x, y))
    subgoal8 = GoalNode("Sub Goal 8", _random_cost(x, y))
    subgoal9 = GoalNode("Sub Goal 9", _random_cost(x, y))
    subgoal10 = GoalNode("Sub Goal 10", _random_cost(x, y))
    subgoal11 = GoalNode("Sub Goal 11", _random_cost(x, y))
    subgoal12 = GoalNode("Sub Goal 12", _random_cost(x, y))
    subgoal13 = GoalNode("Sub Goal 13", _random_cost(x, y))
    subgoal14 = GoalNode("Sub Goal 14", _random_cost(x, y))

    x = 3
    y = 6
    subgoal15 = GoalNode("Sub Goal 15", _random_cost(x, y)) 
    subgoal16 = GoalNode("Sub Goal 16", _random_cost(x, y))
    subgoal17 = GoalNode("Sub Goal 17", _random_cost(x, y))
    subgoal18 = GoalNode("Sub Goal 18", _random_cost(x, y))
    subgoal19 = GoalNode("Sub Goal 19", _random_cost(x, y))
    subgoal20 = GoalNode("Sub Goal 20", _random_cost(x, y))
    subgoal21 = GoalNode("Sub Goal 21", _random_cost(x, y))
    subgoal22 = GoalNode("Sub Goal 22", _random_cost(x, y))
    subgoal23 = GoalNode("Sub Goal 23", _random_cost(x, y))
    subgoal24 = GoalNode("Sub Goal 24", _random_cost(x, y))
    subgoal25 = GoalNode("Sub Goal 25", _random_cost(x, y))
    subgoal26 = GoalNode("Sub Goal 26", _random_cost(x, y))
    subgoal27 = GoalNode("Sub Goal 27", _random_cost(x, y))
    subgoal28 = GoalNode("Sub Goal 28", _random_cost(x, y))
    subgoal29 = GoalNode("Sub Goal 29", _random_cost(x, y))
    subgoal30 = GoalNode("Sub Goal 30", _random_cost(x, y))
    
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

    for i in range(1):
        
        print("---------------------")
        print(f"Test {i}:")
        print("---------------------")
        
        # root = random_binary_symetric()
        # root = random_binary_left()
        # root = random_root()
        # root = random_tree_symetric()
        # root = random_tree_left_right()
        root = random_large_tree()

        output = jonathan_algorithm(root, 30, 1)

if __name__ == '__main__':
    main()
