
import numpy as np
# Define the original points
A = np.array([1, 1])
B = np.array([2, -2])
C = np.array([1, 2])
# Define the rotation matrix for rotation by 90 degrees counterclockwise
angle = np.radians(90)
rotation_matrix = np.array([[np.cos(angle), -np.sin(angle)],
[np.sin(angle), np.cos(angle)]])
# Apply the rotation to the points
A_rotated = np.dot(rotation_matrix, A)
B_rotated = np.dot(rotation_matrix, B)
C_rotated = np.dot(rotation_matrix, C)
# Print the rotated points
print("Rotated Point A: ", A_rotated)
print("Rotated Point B: ", B_rotated)
print("Rotated Point C: ", C_rotated)