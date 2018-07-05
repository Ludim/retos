from balanceo_operaciones import es_entrada_balanceada
import unittest

class BalanceoOperacionesTest(unittest.TestCase):
    def setUp(self):
        self.input_output = (("(){}[]", True),    ("{[()]}", True),
                        ("([)])", False),    ("{{[[(())]]}}", True),
                        ("{({))})]", False), ("[[()", False))

    def test_entrada_balanceada(self):
        print()
        for input_, output_ in self.input_output:
            res = es_entrada_balanceada(input_)
            print("Input={} | Expected_output={} | Function_output={}".format(input_,output_,res))
            self.assertEqual(output_, res)

if __name__ == '__main__':
    unittest.main()