import unittest, math
from Pendulum import Pendulum, dist, onPath, collide


class MyTest(unittest.TestCase):

	def setUp(self):
		pass


	def test_dist(self):
		"""
		Check dist function returns correct distance 
		Between two points
		"""
		point_A = (0, 0)
		point_B = (3, 4)
		self.assertEqual(dist(point_A[0], point_A[1], point_B[0], point_B[1]), 5)


	def test_onPath(self):
		"""
		onPath takes a point on the screen (a, b) and returns the closest
		point that lies on the path of the pendulum.
		"""
		point_A = (40, 30)
		pendulum_length = 20
		# pivot_y is the y component of the point at which the pendulum
		# swings from
		pivot_y = 0

		point_on_path = onPath(point_A[0], point_A[1], pendulum_length, pivot_y)
		self.assertEqual(point_on_path, (16, 12))

	def test_collision(self):
		"""
		Collision() determines whether 2 pendulums have collided and if so 
		adjusts the x component of their velocity accordingly
		"""
		# Define 2 pendulums and set their angles such that they should collide
		# and with arbitrary velocities
		angle1 = 0
		pivot1 = [0, 0]
		p1 = Pendulum(angle1, pivot1[0], pivot1[1])
		p1.v_x = 4

		angle2 = -0.02 * math.pi
		pivot2 = [50, 0]
		p2 = Pendulum(angle2, pivot2[0], pivot2[1])
		p2.v_x = -2

		collide(p1, p2)

		# Check their velicties have been swapped
		self.assertEqual(p1.v_x, -2)
		self.assertEqual(p2.v_x, 4)


	   	# Define a third pendulum angle shuch that it should not collide with p1
		angle3 = 0.4 * math.pi
		p3 = Pendulum(angle3, pivot2[0], pivot2[1])
		p3.v_x = 8

		collide(p1, p3)

		# Check their velocties have not been swapped
		self.assertEqual(p1.v_x, -2)
		self.assertEqual(p3.v_x, 8)


if __name__ == '__main__':
    unittest.main()