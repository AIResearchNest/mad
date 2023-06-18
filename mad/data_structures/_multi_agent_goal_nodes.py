from queue import Queue
import random

class GoalNode:
    def __init__(self, name, data, parents=None, children=None):
        self.name = name
        self.data = data or {}
        self.parents = parents or []
        self.children = children or []
        self.assigned_agent = None

    def add_parent(self, parent_node):
        self.parents.append(parent_node)

    def add_child(self, child_node):
        self.children.append(child_node)

    def print_tree(self, indent=0):
        prefix = "  " * indent
        print(f"{prefix}- {self.name}")
        for child in self.children:
            child.print_tree(indent + 1)

'''
optimization.py
------------------------------------------------
'''
# Makes a list of all goals
def all_goals(GoalNode):
    output = []
    Q = Queue()
    Q.put(GoalNode)
    while (not Q.empty()):
        node = Q.get()
        if node == None:
            continue
        output.append(node)
        for child in node.children:
            Q.put(child)
    return output

# Greedy algorithm
def assign_goals_greedy(all_goals):
    agent_and_goals = {}
    for goal in all_goals:
        # Find best agent to complete the goal
        best_agent = min(goal.data, key=lambda k: goal.data[k])

        # Updates GoalNode
        goal.assigned_agent = best_agent

        # Check if agent is already in
        if best_agent not in agent_and_goals.keys():
            agent_and_goals[best_agent] = [goal]
        else:
            # Add agent to dictionary and add goal to list
            agent_and_goals[best_agent].append(goal)
    return agent_and_goals

def assing_goals_random(all_goals):
    agent_and_goals = {}
    for goal in all_goals:
        # Find best agent to complete the goal
        random_agent = random.choice(list(goal.data.keys()))

        # Updates GoalNode
        goal.assigned_agent = random_agent

        # Check if agent is already in
        if random_agent not in agent_and_goals.keys():
            agent_and_goals[random_agent] = [goal]
        else:
            # Add agent to dictionary and add goal to list
            agent_and_goals[random_agent].append(goal)
    return agent_and_goals

# Prints a dictionary: agent: [goals]
def print_assigned_goals(agent_and_goals):
    for agent in agent_and_goals.keys():
        list_of_goals = []
        for goal in agent_and_goals[agent]:
            list_of_goals.append(goal.name)
        print(f"{agent}: {list_of_goals}")

def compute_score(all_goals):
    if all_goals == []:
        print("Goals not distributed!")
        return -1
    
    score = 0
    for goal in all_goals:
        goal_cost = goal.data[goal.assigned_agent]
        score += goal_cost
    return score


'''
------------------------------------------------
'''

# Tests.py
def main():
    # Create goal tree
    root_node = GoalNode("Root Goal", {"Agent1": -1, "Agent2": -2})

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

    # Print Tree
    root_node.print_tree()


# Optimization tests.py
    # Get a list of all GoalNodes
    goals = all_goals(root_node)

    # Assign agents goals they are best fitted for
    agent_greedy_assignments = assign_goals_greedy(goals)
    # Print agents and goals
    print_assigned_goals(agent_greedy_assignments)
    # Compute score for greedy
    print(compute_score(goals))

    # Assign agents goals they randomly chosen for
    agent_random_assignments = assing_goals_random(goals)
    # Print agents and goals
    print_assigned_goals(agent_random_assignments)
    # Compute score for random
    print(compute_score(goals))

if __name__ == '__main__':
    main()