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
    descrepancy: int
        Finds cost difference between best fit agent and worst fit agent
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of the Child Goals

    find_descrepancy(self)
        Finds the descrepancy between best fit agent and worst fit agent and assigns it to self.descrepancy
    """

    def __init__(self,
                 name: str, 
                 data: Dict) -> None:
        
        self.name = name 
        self.data = data
        self.children = []
        self.agent = None 
        self.cost = None
        self.descrepancy = None
        self.d = self.data.copy()

    def set_agent(self, name) -> None:
        if name in self.data.keys():
            self.agent = name
            self.cost = self.data[name]
        else:
            raise ValueError("Not a viable agent name")        

    def initial_agent_assign(self) -> None:
        self.agent = _suitable_agent(self.data)
        self.cost = self.data[self.agent]

    def switch_agent(self) -> bool:
        if len(self.d) == 1:
            #print("No agent is capable to complete " + self.name)
            self.agent = None
            self.cost = None
            return False
        self.d.pop(self.agent)
        #print(self.d)
        self.agent = _suitable_agent(self.d)
        self.cost = self.d[self.agent]
        return True

    def add_child(self, a) -> None:
        self.children.append(a)

    def get_children(self) -> List:
        return self.children
    
    def find_descrepancy(self):
        high = max([x for x in self.data.values()])
        low = min([x for x in self.data.values()])

        self.descrepancy = abs(high - low)

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

        # enqueue the root into the queue
        q.append((root, None)) 

        while len(q) != 0:
            level_size = len(q)

            while level_size > 0:
                node, parent = q.pop(0)

                if parent:
                    # Print branch symbol if the node has a parent
                    print(parent.name + "|", end="")  

                if node.agent:
                    print(node.name + " " + node.agent + " " + str(node.cost), end="\t")
                else:
                       print(node.name, end="\t")

                children = node.get_children()
                
                for child in children:
                    # Add the children into the queue along with their parent
                    q.append((child, node))  

                level_size -= 1

            print("\n" * 2)

def print_goal_tree(node, indent=0):
    prefix = "  " * indent
    print(f"{prefix}- {node.name}: {min(node.data.values())}")
    for child in node.children:
        print_goal_tree(child, indent + 1)

def print_tree_and_agents(node):
    goals = []
    q = []
    q.append(node)

    while q:
        current = q[0]
        q.pop(0)
        print(f"- {current.name}: {min(current.data.values())}")

        for agent in current.data.keys():
            print(f"   - {agent}: {current.data[agent]}")

        for child in current.get_children():
            q.append(child)
