"""test_dnd_odds.py"""
import pytest
from dnd_odds.odds import valid_combinations, probability_of_combo, expected_rolls, probability_of_one_in_expected_rolls


def test_valid_combinations():
    """
    Test the valid_combinations function to ensure that it produces valid combinations
    that sum up to the target without including forbidden numbers.
    """
    result = list(valid_combinations(5, 6, [1]))
    expected = [
        (5, ),
        (2, 3),
    ]
    assert set(result) == set(expected)  # Using set to compare ignoring order


def test_probability_of_combo():
    """
    Test the probability_of_combo function to check if it returns the correct probability
    of a given combination.
    """
    assert abs(probability_of_combo((2, 3), 6) - (1 / 6 * 1 / 6)) < 0.01


def test_expected_rolls():
    """
    Test the expected_rolls function to determine if it provides the correct expected
    number of rolls needed to hit the target without forbidden numbers.
    """
    rolls = expected_rolls(5, 6, [1])
    expected_value = 1.142857142857143  # Corrected expected value
    assert abs(rolls - expected_value) < 0.01


def test_probability_of_one_in_expected_rolls():
    """
    Test the probability_of_one_in_expected_rolls function to check if it returns
    the correct probability of rolling a forbidden number within the expected number of rolls.
    """
    probability = probability_of_one_in_expected_rolls(5, 6, [1])
    e_rolls = expected_rolls(5, 6, [1])
    expected_probability = 1 - (5 / 6)**e_rolls
    assert abs(probability - expected_probability) < 0.01
