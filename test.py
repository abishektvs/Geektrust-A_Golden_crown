import unittest
from kingdom import King, emblem_of

# integration test
class SupportAnalyzeTest(unittest.TestCase):

    def test_support_analyze_with_three_or_more_allysupport(self):
        test_kingdom = "SPACE"
        test_secret_message = ['LAND FDIXXSOKKOFBBMU',
                                'ICE MOMAMVTMTMHTM',
                                'WATER SUMMER IS COMING',
                                'AIR OWLAOWLBOWLC', 
                                'FIRE AJXGAMUTA'
                            ]
        test_king = King(test_kingdom, test_secret_message)
        self.expected_support = "SPACE LAND ICE FIRE"
        self.support = test_king.analyze_support()
        self.assertEqual(self.support, self.expected_support)

    def test_support_analyze_with_lessthan_three_allysupport(self):
        test_kingdom = "SPACE"
        test_secret_message = ['AIR OWLAOWLBOWLC',
                                'LAND OFBBMUFDICCSO',
                                'ICE VTBTBHTBBBOBAB',
                                'WATER SUMMER IS COMING'
                            ]
        test_king = King(test_kingdom, test_secret_message)
        self.expected_support = "NONE"
        self.support = test_king.analyze_support()
        self.assertEqual(self.support, self.expected_support)
    
    def test_support_analyze_results_startswith_testkingdom_or_NONE(self):
        test_kingdom = "SPACE"
        test_secret_message = ['AIR ROZO',
                                'LAND FAIJWJSOOFAMAU',
                                'ICE STHSTSTVSASOS'
                            ]
        test_king = King(test_kingdom, test_secret_message)
        # regex to check whether solution startswith
        # testkingdom is a kingdom which seeks support
        self.expected_support = f"^{test_kingdom}"
        self.support = test_king.analyze_support()
        self.assertRegex(self.support, self.expected_support)



if __name__ == "__main__":
    unittest.main()