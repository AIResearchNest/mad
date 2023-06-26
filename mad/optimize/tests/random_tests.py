import random as r
from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree
from mad.optimize import jonathan_algorithm
from mad.optimize import _get_goals
from mad.optimize import _score_allocation
from mad.optimize import jonathan_average_cost

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

root = random_binary_symetric()

print("Goal Tree:")
print_goal_tree(root)

jonathan_average_cost(root)

print()
print("Agent Costs:")
goals = _get_goals(root)
for goal in goals:
    print(f"{goal.name}: {goal.cost}")
    for agent, cost in goal.data.items():
        print(f"    -{agent}: {cost}")

print()
results = jonathan_algorithm(root, ["grace", "remus", "franklin"], 15)
print()
print("Goal Allocation:")
for key, value in results.items():
    for goal in value:
        print(f"{key}: {goal.name}, {goal.cost}")

print()
print("Score:")
print(_score_allocation(results))