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
	for_list = []
	if (len(a)*len(a[0])) != new_shape[0]*new_shape[1]:
		return []
	for i in range(len(a)):
		for j in range(len(a[0])):
			flat_list.append(a[i][j])
	j = 1
	i = 0
	for _ in range(len(flat_list)):
		if j == (len(flat_list) + 1):
			break
		else:
			new_list = []
			new_list.append(flat_list[i])
			new_list.append(flat_list[j])
			for_list.append(new_list)
			new_list = []
			i = i + 2
			j = j + 2
		
	return for_list
	return reshape_matrix
	