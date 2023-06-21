# https://github.com/dask/dask/blob/main/dask/datasets.py#L139-L158
from typing import Dict, List

def _suitable_agent(a:Dict) -> str:
    """
    Decides which agent will conduct the current goal based on cost

    Parameters
    ----------
    a : Dict[str: int]
        Dictionary containing the cost values for each agent

    Returns
    -------
    name: str
        Name of the agent with the minimum cost.
    """
    min_cost = list(a.values())[0]
    name = list(a.keys())[0]
    for key, value in a.items():
        if value < min_cost:
            min_cost = value
            name = key
    return name



class GoalNode:

    """
    This class creates Multi Agent Goal Nodes

    Attributes
    ----------
    name : str
        Goal Name
    data : dict
        Dictonary containing key as agent and value as planning cost
    children: List
        List of children GoalNodes, initializing with an empty list
    agent: str
        Agent that costs the least
    cost: int
        Most optimized cost
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of the Child Goals

    level_order_tranversal(self)
        Tranverse through the tree in the level-by-level order
    """

    def __init__(self,
                 name: str, 
                 data: Dict) -> None:
        
        self.name = name 
        self.data = data
        self.children = []
        self.agent = None
        self.cost = None

    def set_agent(self, name, cost) -> None:
        self.agent = name
        self.cost = cost
        
    def add_child(self, a) -> None:
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
    
    def set_cost(self, cost):
        self.cost = cost

def level_order_transversal(root) -> None:
        
        """
        Transverses through the goal tree and prints out the goals (with the parent node in the front if the node has a parent)

        Parameters
        ----------
        root : GoalNode
            The root of the goal tree

        """
        if root is None:
            return

        q = []
        q.append((root, None)) # enqueue the root into the queue

        while len(q) != 0:
            level_size = len(q)

            while level_size > 0:
                node, parent = q.pop(0)
                if parent is not None:
                    print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
                print(node.name + " " + node.agent, end="\t")

                children = node.get_children()
                for child in children:
                    q.append((child, node))  # Add the children into the queue along with their parent

                level_size -= 1

            print("\n" * 2)

def print_goal_tree(node, indent=0):
    prefix = "  " * indent
    print(f"{prefix}- {node.name}: {node.cost}")
    for child in node.children:
        print_goal_tree(child, indent + 1)





def jonathan_allocation(node):
    if not node.children:
        return [node]
    
    selected_goals = []
    child_goals = []
    
    for child in node.children:
        child_goals.extend(jonathan_allocation(child))
    
    child_cost = sum(child.cost for child in child_goals)
    
    if child_cost < node.cost:
        selected_goals.extend(child_goals)
    else:
        selected_goals.append(node)
    
    return selected_goals

# Temporary Tests

# Test Case 1
def test1():
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

    # Print the goal tree
    print_goal_tree(root)

    # Perform DFS to determine the selected goals
    selected_goals = jonathan_allocation(root)

    # Print the selected goals
    print("Goals:")
    for goal in selected_goals:
        print(goal.name)

# Run the test case
print()
print("Test Case 1:")
test1()

# Test Case 2
def test2():
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

    # Print the goal tree
    print_goal_tree(root)

    # Perform DFS to determine the selected goals
    selected_goals = jonathan_allocation(root)

    # Print the selected goals
    print("Goals:")
    for goal in selected_goals:
        print(goal.name)

# Run the test case
print()
print("Test Case 2:")
test2()

# Test Case 3
def test3():
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

    # Print the goal tree
    print_goal_tree(root)

    # Perform DFS to determine the selected goals
    selected_goals = jonathan_allocation(root)

    # Print the selected goals
    print("Goals:")
    for goal in selected_goals:
        print(goal.name)

# Run the test case
print()
print("Test Case 3:")
test3()

# Test Case 4
def test4():
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

    # Print the goal tree
    print_goal_tree(root)

    # Perform DFS to determine the selected goals
    selected_goals = jonathan_allocation(root)

    # Print the selected goals
    print("Goals:")
    for goal in selected_goals:
        print(goal.name)

# Run the test case
print()
print("Test Case 4:")
test4()

# Test Case 5
def test5():
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

    # Print the goal tree
    print_goal_tree(root)

    # Perform DFS to determine the selected goals
    selected_goals = jonathan_allocation(root)

    # Print the selected goals
    print("Goals:")
    for goal in selected_goals:
        print(goal.name)

# Run the test case
print()
print("Test Case 5:")
test5()