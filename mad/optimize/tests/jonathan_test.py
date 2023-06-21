from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

from mad.optimize import jonathan_average_cost
from mad.optimize import jonathan_optimal_path
from mad.optimize import _get_goals


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

print_goal_tree(root)

# Assign goals average costs
goal_assignments = jonathan_average_cost(root)

goals = _get_goals(root)

for goal in goals:
    print(goal.name, goal.cost)

print()

# Create a path off of the average goals
selected_goals = jonathan_optimal_path(root)

for goal in selected_goals:
    print(goal.name, goal.cost)

# Distribute the goals evenly with (max_resources)