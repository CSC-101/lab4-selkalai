import data
import lab4
import unittest
from data import Point


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_first_element_1(self):
        input = [[1,2], [3,4]]
        result = lab4.first_element(input)
        expected = [1, 3]
        self.assertEqual(expected, result)

    def test_first_element_2(self):
        input = [[4,5,7], [8,0], [], [-5,7]]
        result = lab4.first_element(input)
        expected = [4, 8, -5]
        self.assertEqual(expected, result)

    # Part 2
    def test_x_coordinates_1(self):
        point_one = Point(2,3)
        point_two = Point(0,9)
        point_three = Point(98, 4)
        list_of_points = [point_one, point_two, point_three]
        result = lab4.x_coordinates(list_of_points)
        expected = [2, 0, 98]
        self.assertEqual(expected, result)

    def test_x_coordinates_2(self):
        point_one = Point(0,19)
        point_two = Point(0,0)
        point_three = Point(28, 4)
        list_of_points = [point_one, point_two, point_three]
        result = lab4.x_coordinates(list_of_points)
        expected = [0, 0, 28]
        self.assertEqual(expected, result)

    def test_x_coordinates_3(self):
        list_of_points = []
        result = lab4.x_coordinates(list_of_points)
        expected = []
        self.assertEqual(expected, result)

    # Part 3
    def test_are_in_positive_quadrant_1(self):
        point_one = Point(1, 19)
        point_two = Point(0, 0)
        point_three = Point(28, 4)
        list_of_points = [point_one, point_two, point_three]
        result = lab4.are_in_positive_quadrant(list_of_points)
        expected = [Point(1, 19), Point(28, 4)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_2(self):
        point_one = Point(-2, -80)
        point_two = Point(-7, 0)
        point_three = Point(28, -4)
        point_four = Point(2, 7)
        list_of_points = [point_one, point_two, point_three, point_four]
        result = lab4.are_in_positive_quadrant(list_of_points)
        expected = [Point(2, 7)]
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_3(self):
        list_of_points = []
        result = lab4.are_in_positive_quadrant(list_of_points)
        expected = []
        self.assertEqual(expected, result)

    def test_are_in_positive_quadrant_4(self):
        point_one = Point(-2, -80)
        point_two = Point(-7, -6)
        point_three = Point(-28, -4)
        list_of_points = [point_one, point_two, point_three]
        result = lab4.are_in_positive_quadrant(list_of_points)
        expected = []
        self.assertEqual(expected, result)

    # Part 4
    def test_distance_1(self):
        point_one = Point(2,6)
        point_two = Point(6, 9)
        result = lab4.distance(point_one, point_two)
        expected = 5
        self.assertAlmostEqual(expected, result, 2)

    def test_distance_2(self):
        point_one = Point(4,5)
        point_two = Point(16, 10)
        result = lab4.distance(point_one, point_two)
        expected = 13
        self.assertAlmostEqual(expected, result, 2)

    # Part 5
    def test_manhattan_distance_1(self):
        point_one = Point(2, 6)
        point_two = Point(6, 9)
        result = lab4.manhattan_distance(point_one, point_two)
        expected = 7
        self.assertAlmostEqual(expected, result, 2)

    def test_manhattan_distance_2(self):
        point_one = Point(4,5)
        point_two = Point(16, 10)
        result = lab4.manhattan_distance(point_one, point_two)
        expected = 17
        self.assertAlmostEqual(expected, result, 2)

    # Part 6
    def test_distance_all_1(self):
        point_one = Point(0, 8)
        point_two = Point(6, 9)
        point_three = Point(16, 10)
        list_of_points = [point_one, point_two, point_three]
        result = lab4.distance_all(list_of_points)
        expected = [8, 11, 19]
        self.assertEqual(expected, result)

    def test_distance_all_2(self):
        point_one = Point(0, 4)
        point_two = Point(-3, 8)
        point_three = Point(0, 0)
        point_four = Point(-9,-7)
        list_of_points = [point_one, point_two, point_three, point_four]
        result = lab4.distance_all(list_of_points)
        expected = [4, 9, 0, 11]
        self.assertEqual(expected, result)



if __name__ == '__main__':
    unittest.main()
