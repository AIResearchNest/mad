import pytest
from mad.data_structures import GoalNode, level_order_transversal

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

    assert root_node.agent == "grace"
    assert root_node.cost == 10

    

def test_initial_agent_assign():
    G1 = GoalNode("G1", {"grace": 20, "remus": 17, "franklin": 19})
    G1.initial_agent_assign()
    assert G1.agent in G1.data
    assert G1.cost == G1.data[G1.agent]

def test_switch_agent():
    G1 = GoalNode("G1", {"grace": 20, "remus": 17, "franklin": 19})
    G1.initial_agent_assign()
    original_agent = G1.agent
    G1.switch_agent()
    assert G1.agent != original_agent
    assert G1.agent in G1.d
    assert G1.cost == G1.d[G1.agent]

def test_add_child():
    G2 = GoalNode("G2", {"grace": 15, "remus": 16, "franklin": 14})
    new_goal = GoalNode("G11", {"grace": 10, "remus": 8, "franklin": 12})
    G2.add_child(new_goal)
    assert new_goal in G2.get_children()

def test_get_children():
    G1 = GoalNode("G1", {"grace": 20, "remus": 17, "franklin": 19})
    G2 = GoalNode("G2", {"grace": 15, "remus": 16, "franklin": 14})
    G3 = GoalNode("G3", {"grace": 17, "remus": 14, "franklin": 16})
    G4 = GoalNode("G4", {"grace": 6, "remus": 7, "franklin": 4})
    G5 = GoalNode("G5", {"grace": 5, "remus": 6, "franklin": 7})
    G6 = GoalNode("G6", {"grace": 7, "remus": 6, "franklin": 5})
    G7 = GoalNode("G7", {"grace": 8, "remus": 4, "franklin": 5})
    G8 = GoalNode("G8", {"grace": 2, "remus": 1, "franklin": 4})
    G9 = GoalNode("G9", {"grace": 1, "remus": 3, "franklin": 2})
    G10 = GoalNode("G10", {"grace": 4, "remus": 2, "franklin": 3})

    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G3.add_child(G6)
    G3.add_child(G7)
    G4.add_child(G8)
    G4.add_child(G9)
    G4.add_child(G10)

    assert G1.get_children() == G1.children