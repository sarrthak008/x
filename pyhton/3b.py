from pulp import *
# Create a minimization problem
prob = LpProblem("Minimization Problem", LpMinimize)
# Define the decision variables
x = LpVariable('x', lowBound=0, cat='Continuous')
y = LpVariable('y', lowBound=0, cat='Continuous')
z = LpVariable('z', lowBound=0, cat='Continuous')
# Define the objective function
prob += 3*x + 2*y + 5*z, "Z"
# Define the constraints
prob += x + 2*y + z <= 430
prob += 3*x + 4*z <= 460
prob += x + 4*y <= 120
# Solve the problem
prob.solve()
# Print the status of the solution
print("Status: ", LpStatus[prob.status])
# If the problem is solved successfully, print the optimal solution
if prob.status == LpStatusOptimal:
    print("Optimal Solution:")
    print("x = ", value(x))
    print("y = ", value(y))
    print("z = ", value(z))
    print("Z = ", value(prob.objective))