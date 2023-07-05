import pytest
from mad.data_structures import GoalNode, level_order_transversal
from mad.optimize import optimized_goal_allocation

# Test case 1
def test_optimized_goal_allocation_case_one():
    # Create a test goal tree
    G1 = GoalNode("G1", {"grace": 13, "remus": 15, "franklin": 16})
    G1.initial_agent_assign()
    G2 = GoalNode("G2", {"grace": 5, "remus": 5, "franklin": 5})
    G2.initial_agent_assign()
    G3 = GoalNode("G3", {"grace": 3, "remus": 5, "franklin": 4})
    G3.initial_agent_assign()
    G4 = GoalNode("G4", {"grace": 2, "remus": 3, "franklin": 1})
    G4.initial_agent_assign()
    G5 = GoalNode("G5", {"grace": 2, "remus": 3, "franklin": 4})
    G5.initial_agent_assign()

    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)

    # Call the optimized_goal_allocation function
    goal_allocation, remaining_resources = optimized_goal_allocation(G1, [10, 10, 10])
    
    # Assert the expected goal allocation for each agent
    assert goal_allocation["grace"] == ["G3", "G5"]
    assert goal_allocation["remus"] == []
    assert goal_allocation["franklin"] == ["G4"]
    
    # Assert the remaining resources for each agent
    assert remaining_resources["grace"] == 5
    assert remaining_resources["remus"] == 10
    assert remaining_resources["franklin"] == 9

def test_optimized_goal_allocation_case_two():
    # Create a test goal tree
    G1 = GoalNode("G1", {"grace": 20, "remus": 17, "franklin": 19})
    G1.initial_agent_assign()
    G2 = GoalNode("G2", {"grace": 15, "remus": 16, "franklin": 14})
    G2.initial_agent_assign()
    G3 = GoalNode("G3", {"grace": 17, "remus": 14, "franklin": 16   })
    G3.initial_agent_assign()
    G4 = GoalNode("G4", {"grace": 6, "remus": 7, "franklin": 4})
    G4.initial_agent_assign()
    G5 = GoalNode("G5", {"grace": 5, "remus": 6, "franklin": 7})
    G5.initial_agent_assign()
    G6 = GoalNode("G6", {"grace": 7, "remus": 6, "franklin": 5})
    G6.initial_agent_assign()
    G7 = GoalNode("G7", {"grace": 8, "remus": 4, "franklin": 5})
    G7.initial_agent_assign()
    G8 = GoalNode("G8", {"grace": 2, "remus": 1, "franklin": 4})
    G8.initial_agent_assign()
    G9 = GoalNode("G9", {"grace": 1, "remus": 3, "franklin": 2})
    G9.initial_agent_assign()
    G10 = GoalNode("G10", {"grace": 4, "remus": 2, "franklin": 3})
    G10.initial_agent_assign()

    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)
    G3.add_child(G6)
    G3.add_child(G7)
    G4.add_child(G8)
    G4.add_child(G9)
    G4.add_child(G10)

    # Call the optimized_goal_allocation function
    goal_allocation, remaining_resources = optimized_goal_allocation(G1, [12, 15, 14])

    # Assert the expected goal allocation for each agent
    assert goal_allocation["grace"] == ["G5", "G9"]
    assert goal_allocation["remus"] == ["G7", "G8", "G10"]
    assert goal_allocation["franklin"] == ["G6"]

    # Assert the remaining resources for each agent
    assert remaining_resources["grace"] == 6
    assert remaining_resources["remus"] == 8
    assert remaining_resources["franklin"] == 9

def test_optimized_goal_allocation_empty_tree():
    # Create an empty goal tree
    G1 = GoalNode("G1", {})  # Empty resource allocation for G1

    # Call the optimized_goal_allocation function and expect an exception
    with pytest.raises(Exception):
        goal_allocation, remaining_resources = optimized_goal_allocation(G1, [10, 10, 10])