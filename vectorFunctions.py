from math import sqrt

class Vector(object):
	def __init__(self, coordinates):
		try:
			if not coordinates:
				raise ValueError
			self.coordinates = tuple(coordinates)
			self.dimension = len(coordinates)

		except ValueError:
			raise ValueError('Vetor está vazio')
		except TypeError:
			raise TypeError('O vetor só deve ser interável')

	def __str__(self):
		return('Vetor: {}'.format(self.coordinates))

	def __eq__(self, v):
		return(self.coordinates == v.coordinates)

	def plus(self, v):
		new_coordinates = [x+y for x, y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def minus(self, v):
		new_coordinates = [x-y for x, y in zip(self.coordinates, v.coordinates)]
		return Vector(new_coordinates)

	def scalar(self, c):
		new_coordinates = [c*x for x in self.coordinates]
		return Vector(new_coordinates)

	def __str__(self):
		return 'Vector: {}'.format(self.coordinates)

	def magnitude(self):
		coordinates_square = [x**2 for x in self.coordinates]
		return(sqrt(sum(coordinates_square)))

	def normalized(self):
		try:
			magnitude = self.magnitude()
			return(self.scalar(1/magnitude))
		except ZeroDivisionError:
			raise Exception('Não é possível normalizar um vetor de valor zero')



v1 = Vector([5.581, -2.136])
print(v1.normalized())
