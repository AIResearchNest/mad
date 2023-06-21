from mad.data_structures import GoalNode
from mad.data_structures import print_goal_tree

def test_children():
    # Create goal tree
    root_node = GoalNode("Root Goal", {"Agent1": 1, "Agent2": 2})
    child_node1 = GoalNode("Child Goal 1", {"Agent1": 4, "Agent2": 1})
    root_node.add_child(child_node1)

    assert child_node1 in root_node.children
    
def test_set_agent():
    # Create goal tree
    root_node = GoalNode("Goal 1", {"grace": 10})
    root_node.set_agent("grace")
    print(root_node.agent, root_node.cost)

    assert root_node.agent is "grace"
    assert root_node.cost is 10
