import random
from typing import Dict, List, Tuple
import heapq

# Start of class
class GoalNode:
    """
    This class creates Multi Agent Goal Nodes

    Attributes
    ----------
    name : str
        Goal Name
    cost : int
        Cost associated with the node
    agent: str
        Agent assigned to the node
    children: List
        List of child GoalNodes, initialized with an empty list
    
    Methods
    ----------
    add_child(self, GoalNode)
        Add Child Goal into the Children list

    get_children(self) -> List[GoalNode]
        Return the list of child Goals
    level_order_transversal(self)
        Traverse through the tree in the level-by-level order
    """

    def __init__(self, name: str, cost: int) -> None:
        self.name = name
        self.cost = cost
        self.agent = None
        self.children = []

    def add_child(self, a):
        self.children.append(a)

    def get_children(self) -> List:
        return self.children


def level_order_transversal(root) -> None:
    """
    Traverses through the goal tree and prints out the goals (with the parent node in the front if the node has a parent)
    along with the assigned agent for each node.

    Parameters
    ----------
    root : GoalNode
        The root of the goal tree
    """
    if root is None:
        return

    q = []
    q.append((root, None))  # enqueue the root into the queue

    while len(q) != 0:
        level_size = len(q)

        while level_size > 0:
            node, parent = q.pop(0)
            if parent is not None:
                print(parent.name + "|", end="")  # Print branch symbol if the node has a parent
            print(node.name + " Cost:", node.cost, " Assigned Agent:", node.agent, end="\t")

            children = node.get_children()
            for child in children:
                q.append((child, node))  # Add the children into the queue along with their parent

            level_size -= 1

        print()  # Print a new line after traversing each level


# Function that randomizes the cost of nodes
def random_cost(start_range: int, end_range: int) -> int:
    """
    This function generates a random cost for a node based on a specified cost range.

    Parameters
    ----------
    start_range: int
        The lower bound of the cost range.

    end_range: int
        The upper bound of the cost range.

    Returns
    -------
    int
        Randomized cost value for the node.
    """
    return random.randint(start_range, end_range)


def _agent_goal(a: Dict[str, int], resources: Dict[str, int]) -> str:
    """
    Decides which agent will conduct the current goal based on the agent's current available resources.

    Parameters
    ----------
    a : Dict[str, int]
        Dictionary containing the cost values for each agent.
    resources : Dict[str, int]
        Dictionary containing the available resources for each agent.

    Returns
    -------
    name: str
        Name of the agent assigned to each node.
    """
    agents = ["grace", "remus", "franklin"]

    # Assign the first three agents to the first three nodes
    if len(a) <= 3:
        agent_assigned = agents[len(a) - 1]
        resources[agent_assigned] -= a[agent_assigned]
        return agent_assigned

    # Calculate the cost difference for each agent
    cost_diff = {agent: resources[agent] - a[agent] for agent in agents}

    # Sort the agents based on the cost difference in ascending order
    sorted_agents = sorted(cost_diff, key=lambda agent: cost_diff[agent])

    # Find the first agent with a non-negative cost difference
    for agent in sorted_agents:
        if cost_diff[agent] >= 0:
            agent_assigned = agent
            resources[agent_assigned] -= a[agent_assigned]
            return agent_assigned

    # If no agent has a non-negative cost difference, choose the agent with the smallest negative cost difference
    agent_assigned = sorted_agents[0]
    resources[agent_assigned] -= a[agent_assigned]
    return agent_assigned




def perform_auction(node, agent_resources):
    """
    Performs the auction process for assigning an agent to a goal node based on available agent resources.

    Parameters
    ----------
    node : GoalNode
        The goal node to be assigned an agent.
    agent_resources : Dict[str, int]
        Dictionary containing the available resources for each agent.

    Returns
    -------
    None
    """
    bids = {}  # Dictionary to store the bids of each agent

    # Generate bids from each agent based on their available resources
    for agent in agent_resources:
        if agent_resources[agent] > 0:
            bids[agent] = agent_resources[agent]

    # Print agent resources before the auction
    print("Agent Resources:", agent_resources)

    # Determine the winning bidder based on the highest bid
    winning_bidder = max(bids, key=bids.get)
    winning_bid = bids[winning_bidder]

    # Check if the winning bidder can cover the cost of the goal node
    if winning_bid >= node.cost:
        node.agent = winning_bidder
        agent_resources[winning_bidder] -= node.cost
    else:
        # If the winning bidder cannot cover the cost, find the second highest bidder
        bids.pop(winning_bidder)
        if len(bids) > 0:
            second_bidder = max(bids, key=bids.get)
            second_bid = bids[second_bidder]
            if second_bid >= node.cost:
                node.agent = second_bidder
                agent_resources[second_bidder] -= node.cost

    # Print agent resources after the auction
    
def compare(shortest_cost: int, root_node_cost: int):
    print("\nRoot node cost", root_node_cost )
    print("\nShortest path cost", shortest_cost )
    
    if shortest_cost < root_node_cost:
        print("\nCost effective: Choose Shortest path" )
    else:
        print("\nCost effective: Choose root node")
        
    """
    Compare the shortest path cost with the cost of the root node's agent and print the result.

    Parameters
    ----------
    shortest_cost : int
        The shortest path cost.

    root_node_cost : int
        The cost of the root node's agent.
    """
#Diajkstraaas
def dijkstra_shortest_path(root_node: GoalNode) -> tuple[int, List[str], List[str]]:
    """
    Implements Dijkstra's algorithm to find the shortest path with the given conditions.

    Parameters
    ----------
    root_node : GoalNode
        The root node of the goal tree.

    Returns
    -------
    Tuple[int, List[str], List[str]]
        The shortest path cost, list of goals, and list of agents.
    """
    # Initialize a priority queue to store nodes based on their costs
    pq = [(0, root_node)]  # Cost of root_node is set to 0

    # Initialize dictionaries to store costs and paths
    costs = {root_node: 0}
    paths = {root_node: []}

    # Process nodes in the priority queue until it becomes empty
    while pq:
        current_cost, current_node = heapq.heappop(pq)

        # Check if the current node is the goal node
        if not current_node.children:
            # Return the shortest path cost, list of goals, and list of agents
            return current_cost, paths[current_node] + [current_node.name], [current_node.agent]

        # Explore child nodes
        for child_node in current_node.children:
            child_cost = current_cost + child_node.cost

            # Update the cost and path if a shorter path is found
            if child_node not in costs or child_cost < costs[child_node]:
                costs[child_node] = child_cost
                paths[child_node] = paths[current_node] + [current_node.name]

                # Add the child node to the priority queue
                heapq.heappush(pq, (child_cost, child_node))

    # If no goal node is found, return None
    return None


def main():
    #"\n\nNodes cost assignment:\n"
    G1 = GoalNode("G1", random_cost(1, 20))  # Assigning random cost values between 1-20 to nodes
    G2 = GoalNode("G2", random_cost(1, 20))
    G3 = GoalNode("G3", random_cost(1, 20))
    G4 = GoalNode("G4", random_cost(1, 20))
    G5 = GoalNode("G5", random_cost(1, 20))

    print("\nNodes assignment to Goals:\n")
    # Goal relationship
    G1.add_child(G2)
    G1.add_child(G3)
    G2.add_child(G4)
    G2.add_child(G5)

    # Define agent resources and initial balances
    agent_resources = {"grace": 40, "remus": 50, "franklin": 30}

    # Iterate through each goal node and perform the auction
    nodes = [G1, G2, G3, G4, G5]
    for node in nodes:
        perform_auction(node, agent_resources)

        # Print the updated node information after each assignment
        level_order_transversal(G1)
        print("Updated Agent Resources:", agent_resources)
        print("\n")
    #shortest_cost, shortest_goals, shortest_agents = _optimize_tree(G1)
    shortest_cost, shortest_goals, shortest_agents = dijkstra_shortest_path(G1)

    print("\nList of Goals for minimum cost:", shortest_goals[1:]) #remove G1 from representation 
    print("\nList of Agents:", shortest_agents)
    compare(shortest_cost, G1.cost)

if __name__ == "__main__":
    main()
