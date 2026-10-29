import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
	"""
	reshaped_matrix = []
	arr = np.array(a)
	if arr.size != new_shape[0]*new_shape[1]:
		return reshaped_matrix
	arr = arr.reshape(new_shape)
	reshaped_matrix = arr.tolist()
	return reshaped_matrix
	"""

	#no numpy method (took time and alot of drawings)
	reshaped_matrix = []
	flat_list = []
	rows, cols = new_shape

	if (len(a)*len(a[0])) != rows*cols:
		return []

	for i in range(len(a)):
		for j in range(len(a[0])):
			flat_list.append(a[i][j])

	for i in range(rows):
		new_row = []
		for j in range(cols):
			value = i * cols + j
			new_row.append(flat_list[value])
		reshaped_matrix.append(new_row)

	return reshaped_matrix
	