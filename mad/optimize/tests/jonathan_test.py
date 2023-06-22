from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

from mad.optimize import jonathan_average_cost
from mad.optimize import jonathan_optimal_path
from mad.optimize import _get_goals
from mad.optimize import jonathan_distribute_goals

def test1():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {"grace": 30, "remus":32, "franklin": 35})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": 16, "remus":14, "franklin": 18})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": 16, "remus":12, "franklin": 19})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": 8, "remus":7, "franklin": 3})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": 7, "remus":3, "franklin": 5})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": 7, "remus":5, "franklin": 11})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": 9, "remus":5, "franklin": 2})
    subgoal7 = GoalNode("Sub Goal 7", {"grace": 9, "remus":7, "franklin": 6})
    subgoal8 = GoalNode("Sub Goal 8", {"grace": 4, "remus":7, "franklin": 8})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)

    print("Tree:")
    print_goal_tree(root)

    print()
    # Assign goals average costs
    jonathan_average_cost(root)
    goals = _get_goals(root)
    print("Goals:")
    for goal in goals:
        print(goal.name, goal.cost)

    print()

    # Choose a path
    selected_goals = jonathan_optimal_path(root)
    print("Best path:")
    for goal in selected_goals:
        print(goal.name, goal.cost)

    print()
    # Distribute the goals evenly with (max_resources)
    distributed_goals = jonathan_distribute_goals(selected_goals, ["grace", "remus", "franklin"], 20)
    print("Goal Allocation:")
    for key, value in distributed_goals.items():
        for goal in value:
            print(key, goal.name)

def test2():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {"grace": 10, "remus":10, "franklin": 10})
    subgoal1 = GoalNode("Sub Goal 1", {"grace": 3, "remus":3, "franklin": 3})
    subgoal2 = GoalNode("Sub Goal 2", {"grace": 4, "remus":4, "franklin": 4})
    subgoal3 = GoalNode("Sub Goal 3", {"grace": 1, "remus":1, "franklin": 1})
    subgoal4 = GoalNode("Sub Goal 4", {"grace": 1, "remus":1, "franklin": 1})
    subgoal5 = GoalNode("Sub Goal 5", {"grace": 2, "remus":2, "franklin": 2})
    subgoal6 = GoalNode("Sub Goal 6", {"grace": 1, "remus":1, "franklin": 1})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
    
    print("Tree:")
    print_goal_tree(root)

    print()
    # Assign goals average costs
    jonathan_average_cost(root)
    goals = _get_goals(root)
    print("Goals:")
    for goal in goals:
        print(goal.name, goal.cost)

    print()

    # Choose a path
    selected_goals = jonathan_optimal_path(root)
    print("Best path:")
    for goal in selected_goals:
        print(goal.name, goal.cost)

    print()
    # Distribute the goals evenly with (max_resources)
    distributed_goals = jonathan_distribute_goals(selected_goals, ["grace", "remus", "franklin"], 20)
    print("Goal Allocation:")
    for key, value in distributed_goals.items():
        for goal in value:
            print(key, goal.name)

test1()
print()
test2()