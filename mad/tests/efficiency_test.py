#Fay's efficiency test cases
#
#RESOURCE UTILIZATION
#
#The less resources all agents use, the more efficient the algorithm is
# Define the input data
goal_tree = ...  # Define the goal tree
max_resources = ...  # Define the maximum resources for each agent

# Execute Jonathan's Algorithm
result1 = initial_goal_allocation(goal_tree, max_resources)

# Calculate total resource utilization for Jonathan's Algorithm
total_utilization1 = sum(sum(goal.cost for goal in goals) for goals in result1.values())

# Execute Fay's Algorithm
result2 = optimized_goal_allocation(goal_tree, max_resources)

# Calculate total resource utilization for Fay's Algorithm
total_utilization2 = sum(sum(goal.cost for goal in goals) for goals in result2.values())

# Execute Maheen's Algorithm
result3 = perform_auction_m(goal_tree, max_resources)

# Calculate total resource utilization for Maheen's Algorithm
total_utilization3 = sum(goal.cost for goal in result3)

# Compare total resource utilization
print("Total resource utilization for J:", total_utilization1)
print("Total resource utilization for F:", total_utilization2)
print("Total resource utilization for M:", total_utilization3)
"""
Plot idea: 
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the algorithm names and total resource utilization values
algorithm_names = ['Algorithm 1', 'Algorithm 2', 'Algorithm 3']
total_utilization_values = [total_utilization1, total_utilization2, total_utilization3]

# Generate data for the agents
agents = ['Agent 1', 'Agent 2', 'Agent 3']
X, Y = np.meshgrid(np.arange(len(agents)), np.arange(len(algorithm_names)))
Z = np.zeros((len(algorithm_names), len(agents)))

# Fill the Z-axis values with the total resource utilization
for i in range(len(algorithm_names)):
    Z[i] = total_utilization_values[i]

# Create the 3D plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Plot the bars
dx = dy = 0.8
dz = Z.flatten()
ax.bar3d(X.flatten(), Y.flatten(), np.zeros_like(Z.flatten()), dx, dy, dz, color='skyblue')

# Set the labels and title
ax.set_xticks(np.arange(len(agents)))
ax.set_xticklabels(agents)
ax.set_yticks(np.arange(len(algorithm_names)))
ax.set_yticklabels(algorithm_names)
ax.set_xlabel('Agents')
ax.set_ylabel('Algorithms')
ax.set_zlabel('Total Resource Utilization')
ax.set_title('Resource Utilization Comparison')

# Rotate the plot for better visibility
ax.view_init(azim=-60, elev=30)

# Display the plot
plt.show()
"""