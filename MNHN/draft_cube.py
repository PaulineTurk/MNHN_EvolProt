import numpy as np

vect = [np.array([5, 2, 3])] + [np.array([1, 2, 3])] + [np.array([1, 2, 3])]
print(vect)
final_vector = np.prod(np.vstack(vect), axis=0)
print(final_vector[0])
final_vector_normalized = final_vector/np.sum(final_vector)
print(final_vector_normalized)