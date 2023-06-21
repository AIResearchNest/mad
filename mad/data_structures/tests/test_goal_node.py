from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

def test_children():

    # Create goal tree
    root_node = GoalNode("Root Goal", {"Agent1": 1, "Agent2": 2})
    child_node1 = GoalNode("Child Goal 1", {"Agent1": 4, "Agent2": 1})
    root_node.add_child(child_node1)

    assert child_node1 in root_node.children
    

def test_parents():
    # Create goal tree
    root_node = GoalNode("Root Goal", {"Agent1": 1, "Agent2": 2})
    child_node1 = GoalNode("Child Goal 1", {"Agent1": 4, "Agent2": 1})
    root_node.add_child(child_node1)
    child_node1.add_parent(root_node)

    assert root_node in child_node1.parents

# Test Case 1
def test1():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal6 = GoalNode("Sub Goal 6", {})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    # Print the goal tree
    print_goal_tree(root)

# Test Case 2
def test2():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal6 = GoalNode("Sub Goal 6", {})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    # Print the goal tree
    print_goal_tree(root)

# Test Case 3
def test3():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal6 = GoalNode("Sub Goal 6", {})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    # Print the goal tree
    print_goal_tree(root)

# Test Case 4
def test4():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal6 = GoalNode("Sub Goal 6", {})

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    # Print the goal tree
    print_goal_tree(root)

# Test Case 5
def test5():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal7 = GoalNode("Sub Goal 7", 1)
    subgoal8 = GoalNode("Sub Goal 8", 1)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)

    # Print the goal tree
    print_goal_tree(root)

test1()
test2()
test3()
test4()
test5()