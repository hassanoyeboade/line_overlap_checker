from program import line_overlap_checker

import unittest


class LineOverlapCheckerTest(unittest.TestCase):

    def test_when_lines_overlap(self):
        line_1 = (1, 5)
        line_2 = (2, 6)

        self.assertEqual(line_overlap_checker(line_1, line_2), True)

    def test_when_lines_with_unordered_points_overlap(self):
        line_1 = (5, 6)
        line_2 = (8, 5)

        self.assertEqual(line_overlap_checker(line_1, line_2), True)

    def test_when_lines_with_negative_points_overlap(self):
        line_1 = (1, -5)
        line_2 = (-4, 6)

        self.assertEqual(line_overlap_checker(line_1, line_2), True)

    def test_when_lines_do_not_overlap(self):
        line_1 = (1, 5)
        line_2 = (6, 8)

        self.assertEqual(line_overlap_checker(line_1, line_2), False)

    def test_when_lines_do_not_overlap_but_intersect(self):
        line_1 = (1, 5)
        line_2 = (5, 8)

        self.assertEqual(line_overlap_checker(line_1, line_2), False)

    def test_when_line_tuples_contain_less_than_required_number_of_elements(self):
        line_1 = (5, )
        line_2 = (4, 6)

        with self.assertRaises(ValueError):
            self.assertRaises(line_overlap_checker(line_1, line_2))

    def test_when_line_tuples_contain_more_than_required_number_of_elements(self):
        line_1 = (5, 5)
        line_2 = (4, 6, 9)

        with self.assertRaises(ValueError):
            self.assertRaises(line_overlap_checker(line_1, line_2))


if __name__ == '__main__':
    unittest.main()
