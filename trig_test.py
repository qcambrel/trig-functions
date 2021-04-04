# Unit tests for trig.py

import unittest
import math
import trig

class TrigTest(unittest.TestCase):
	def test_sin(self):
		self.assertEqual(trig.sin(trig.radians(45)), 1/math.sqrt(2))

	def test_cos(self):
		self.assertEqual(trig.cos(trig.radians(45)), 1/math.sqrt(2))

	def test_tan(self):
		theta = trig.radians(60)
		mytans = trig.tan(theta), trig.precise_tan(theta)
		pytan = math.tan(theta)
		self.assertTrue(True in [pytan == mytan for mytan in mytans])

	def test_sec(self):
		theta = trig.radians(60)
		mysecs = trig.precise_sec(theta), trig.precise_sec(theta)
		pysec = 1/math.cos(theta)
		self.assertTrue(True in [pysec == mysec for mysec in mysecs])

	def test_arcsin(self):
		pass

	def test_arccos(self):
		pass

	def test_arctan(self):
		pass

	def test_sinh(self):
		pass

	def test_cosh(self):
		pass

	def test_tanh(self):
		pass

	def test_arsinh(self):
		pass

	def test_artanh(self):
		pass

if __name__ == '__main__':
	unittest.main()