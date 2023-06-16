from mad.data_structures import GoalNode
from typing import Dict
from queue import Queue

# private function should be as follows
def level_search(self):
    output = []
    Q = Queue()
    Q.put(self.root)
    while (not Q.empty()):
        node = Q.get()
        if node == None:
            continue
        output.append(node)
        for child in node.get_children():
            Q.put(child)
    return output

def initial_goal_allocation(goal_tree: GoalNode,
                            max_resources: int) -> Dict:
    
    """
    Optimizes allocation of goals to multiple agents

    Parameters
    ----------
    goal_tree : mad.data_structures.GoalNode
        Heirarichal Multi Agent Goal Tree 
    max_resources : int
        Maximum resources available for each agent

    Returns
    -------
    goal_allocation: Dict
        Allocates list of goals (value) to each agent (key)
    """

    # write your code here


    # Raise an error if goal_tree is empty