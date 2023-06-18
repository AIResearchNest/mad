from mad.data_structures import GoalNode
from mad.optimize import initial_goal_allocation
from mad.optimize import print_assigned_goals
from mad.optimize import random_goal_allocation

# data_structures tests
root_node = GoalNode("Root Goal", {"Agent1": 1, "Agent2": 2})

child_node1 = GoalNode("Child Goal 1", {"Agent1": 4, "Agent2": 1})
child_node2 = GoalNode("Child Goal 2", {"Agent1": 2, "Agent2": 3})
root_node.add_child(child_node1)
root_node.add_child(child_node2)
child_node1.add_parent(root_node)
child_node2.add_parent(root_node)

child_node11 = GoalNode("Child Goal 1.1", {"Agent1": 1, "Agent2": 2})
child_node12 = GoalNode("Child Goal 1.2", {"Agent1": 3, "Agent2": 1})
child_node1.add_child(child_node11)
child_node1.add_child(child_node12)
child_node11.add_parent(child_node1)
child_node12.add_parent(child_node1)

child_node21 = GoalNode("Child Goal 2.1", {"Agent1": 2, "Agent2": 1})
child_node2.add_child(child_node21)
child_node21.add_parent(child_node2)

child_node211 = GoalNode("Child Goal 2.1.1", {"Agent1": 1, "Agent2": 3})
child_node21.add_child(child_node211)
child_node211.add_parent(child_node21)

# root_node.print_tree()

# _goal_allocation tests
agent_and_goals = initial_goal_allocation(root_node, 10)
print_assigned_goals(agent_and_goals)

agent_and_goals_rand = random_goal_allocation(root_node, 10)
print_assigned_goals(agent_and_goals_rand)