import unittest
from StringCalculator import formatted_name

class StringCalculator(unittest.TestCase):

   def add(self):


    
        result = formatted_name("122,10")
        self.assertEqual(result, 132)


        number="122\n10"
        result = formatted_name(number)
        self.assertEqual(result, 132)
        
        
        number="a,10"
        result = formatted_name(number)
        self.assertEqual(result, 11)
        
        
        number="122"
        result = formatted_name(number)
        self.assertEqual(result, 122)
        
        
        number="1222,10"
        result = formatted_name(number)
        self.assertEqual(result, 10)
        



obj = StringCalculator()
print(obj.add())