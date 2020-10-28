import caesar
import unittest


class Test(unittest.TestCase):



	def test_encode(self):

		self.assertEqual(caesar.encode("abcd", -1), "zabc")
		self.assertEqual(caesar.encode("abcd", 1), "bcde")
		self.assertEqual(caesar.encode("nothing", -999), "cdiwxcv")	
		self.assertEqual(caesar.encode("nothing", 999), "yzestyr")
		self.assertEqual(caesar.encode("anything", 26), "anything")
		self.assertEqual(caesar.encode("anything", -26), "anything")



	def test_decode(self):

		self.assertEqual(caesar.decode("zabc", -1), "abcd")
		self.assertEqual(caesar.decode("bcde", 1), "abcd")
		self.assertEqual(caesar.decode("cdiwxcv", -999), "nothing")	
		self.assertEqual(caesar.decode("yzestyr", 999), "nothing")
		self.assertEqual(caesar.decode("anything", 26), "anything")
		self.assertEqual(caesar.decode("anything", -26), "anything")



if __name__ == "__main__":
	unittest.main()





