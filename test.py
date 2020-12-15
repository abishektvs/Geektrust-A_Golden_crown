import unittest
from kingdom import King, emblem_of



class SupportAnalyzeTest(unittest.TestCase):
    test_kingdom = "SPACE"
    test_secret_message = ['LAND FDIXXSOKKOFBBMU',
                            'ICE MOMAMVTMTMHTM',
                            'WATER SUMMER IS COMING',
                            'AIR OWLAOWLBOWLC', 
                            'FIRE AJXGAMUTA']
    test_king = King(test_kingdom, test_secret_message)

    def test_support_analyze(self):
        self.expected_support = "SPACE LAND ICE FIRE"
        self.support = self.test_king.analyze_support()
        self.assertEqual(self.support, self.expected_support)

if __name__ == "__main__":
    unittest.main()