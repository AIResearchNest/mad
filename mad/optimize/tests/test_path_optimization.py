from mad.data_structures import GoalNode
from mad.optimize import jonathan_optimal_path

def test_output1():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    root.set_cost(10)
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal1.set_cost(3)
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal2.set_cost(4)
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal3.set_cost(1)
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal4.set_cost(1)
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal5.set_cost(2)
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal6.set_cost(1)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    selected_goals = jonathan_optimal_path(root)

    assert subgoal3 in selected_goals
    assert subgoal4 in selected_goals
    assert subgoal5 in selected_goals
    assert subgoal6 in selected_goals

def test_output2():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    root.set_cost(10)
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal1.set_cost(3)
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal2.set_cost(4)
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal3.set_cost(2)
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal4.set_cost(2)
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal5.set_cost(3)
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal6.set_cost(3)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    selected_goals = jonathan_optimal_path(root)

    assert subgoal1 in selected_goals
    assert subgoal2 in selected_goals

def test_output3():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    root.set_cost(10)
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal1.set_cost(10)
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal2.set_cost(10)
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal3.set_cost(2)
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal4.set_cost(2)
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal5.set_cost(2)
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal6.set_cost(2)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    selected_goals = jonathan_optimal_path(root)

    assert subgoal3 in selected_goals
    assert subgoal4 in selected_goals
    assert subgoal5 in selected_goals
    assert subgoal6 in selected_goals

def test_output4():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    root.set_cost(10)
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal1.set_cost(10)
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal2.set_cost(10)
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal3.set_cost(5)
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal4.set_cost(6)
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal5.set_cost(5)
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal6.set_cost(6)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)

    selected_goals = jonathan_optimal_path(root)

    assert root in selected_goals

def test_output5():
    # Create the goal tree structure
    root = GoalNode("Main Goal", {})
    root.set_cost(20)
    subgoal1 = GoalNode("Sub Goal 1", {})
    subgoal1.set_cost(10)
    subgoal2 = GoalNode("Sub Goal 2", {})
    subgoal2.set_cost(10)
    subgoal3 = GoalNode("Sub Goal 3", {})
    subgoal3.set_cost(5)
    subgoal4 = GoalNode("Sub Goal 4", {})
    subgoal4.set_cost(6)
    subgoal5 = GoalNode("Sub Goal 5", {})
    subgoal5.set_cost(5)
    subgoal6 = GoalNode("Sub Goal 6", {})
    subgoal6.set_cost(6)
    subgoal7 = GoalNode("Sub Goal 7", 1)
    subgoal7.set_cost(1)
    subgoal8 = GoalNode("Sub Goal 8", 1)
    subgoal8.set_cost(1)

    root.add_child(subgoal1)
    root.add_child(subgoal2)
    subgoal1.add_child(subgoal3)
    subgoal1.add_child(subgoal4)
    subgoal2.add_child(subgoal5)
    subgoal2.add_child(subgoal6)
    subgoal3.add_child(subgoal7)
    subgoal3.add_child(subgoal8)

    selected_goals = jonathan_optimal_path(root)

    assert subgoal7 in selected_goals
    assert subgoal8 in selected_goals
    assert subgoal4 in selected_goals
    assert subgoal2 in selected_goals