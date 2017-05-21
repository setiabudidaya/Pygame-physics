import unittest
from Pendulum import Pendulum, dist


class MyTest(unittest.TestCase):

	def setUp(self):
		pass


	def test_dist(self):
		"""
		Check dist function greturns correct distance 
		Between two points
		"""
		point_A = (0, 0)
		point_B = (3, 4)
		self.assertEqual(dist(point_A[0], point_A[1], point_B[0], point_B[1]), 5)


if __name__ == '__main__':
    unittest.main()