from pulp import *
# Create a maximization problem
prob = LpProblem("Maximization Problem", LpMaximize)
# Define the decision variables
x = LpVariable('x', lowBound=0, cat='Continuous')
y = LpVariable('y', lowBound=0, cat='Continuous')
# Define the objective function
prob += x + y, "Z"
# Define the constraints
prob += x - y >= 1
prob += x + y >= 2
# Solve the problem
prob.solve()
# Print the status of the solution
print("Status: ", LpStatus[prob.status])

# If the problem is solved successfully, print the optimal solution
if prob.status == LpStatusOptimal:
    print("Optimal Solution:")
    print("x = ", value(x))
    print("y = ", value(y))
    print("Z = ", value(prob.objective))