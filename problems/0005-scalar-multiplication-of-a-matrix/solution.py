def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:
	result = []
	for row in matrix:
		tmp_row = []
		for element in row:
			element = element * scalar
			tmp_row.append(element)
		result.append(tmp_row)
	return result 
	pass