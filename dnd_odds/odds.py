"""dnd_odds.py"""
import argparse
from itertools import combinations_with_replacement
from typing import List, Generator, Tuple, Optional


def valid_combinations(target: int,
                       max_num: int,
                       forbidden_numbers: Optional[List[int]] = None
                       ) -> Generator[Tuple[int], None, None]:
    """
    Generate valid combinations that sum up to the target, avoiding forbidden numbers.

    Args:
        target (int): The desired target sum.
        max_num (int): Maximum number on the die.
        forbidden_numbers (List[int], optional): Numbers that are to be avoided during the rolls. Defaults to None.

    Returns:
        Generator[Tuple[int], None, None]: Valid combinations that sum up to the target.
    """
    if forbidden_numbers is None:
        forbidden_numbers = []

    allowed_numbers = [
        num for num in range(1, max_num + 1) if num not in forbidden_numbers
    ]

    for rng in range(1, target // min(allowed_numbers) + 1):
        for combo in combinations_with_replacement(allowed_numbers, rng):
            if sum(combo) == target:
                yield combo


def probability_of_combo(combo: Tuple[int], max_num: int) -> float:
    """
    Calculate the probability of a given combination for a die with max_num faces.

    Args:
        combo (Tuple[int]): A combination of numbers.
        max_num (int): Maximum number on the die.

    Returns:
        float: Probability of the combination.
    """
    return (1 / max_num)**len(combo)


def expected_rolls(target: int,
                   max_num: int,
                   forbidden_numbers: Optional[List[int]] = None) -> float:
    """
    Calculate the expected number of rolls to reach the target sum, avoiding forbidden numbers.

    Args:
        target (int): The desired target sum.
        max_num (int): Maximum number on the die.
        forbidden_numbers (List[int], optional): Numbers that are to be avoided during the rolls. Defaults to None.

    Returns:
        float: Expected number of rolls to achieve the target.
    """
    total_probability = 0
    total_rolls = 0

    for combo in valid_combinations(target, max_num, forbidden_numbers):
        prob = probability_of_combo(combo, max_num)
        total_probability += prob
        total_rolls += len(combo) * prob

    return total_rolls / total_probability if total_probability else float('inf')


def probability_of_one_in_expected_rolls(
        target: int,
        max_num: int,
        forbidden_numbers: Optional[List[int]] = None) -> float:
    """
    Calculate the probability of having rolled a forbidden number in the expected rolls.

    Args:
        target (int): The desired target sum.
        max_num (int): Maximum number on the die.
        forbidden_numbers (List[int], optional): Numbers that are to be avoided during the rolls. Defaults to None.

    Returns:
        float: Probability of having rolled a forbidden number.
    """
    expected = expected_rolls(target, max_num, forbidden_numbers)
    return 1 - ((max_num - len(forbidden_numbers)) / max_num)**expected


def main():
    """argparse main entry"""
    parser = argparse.ArgumentParser(description="Compute odds related to dice rolls.")
    parser.add_argument("--target",
                        type=int,
                        help="Target sum to be achieved",
                        required=True)
    parser.add_argument("--max_num",
                        type=int,
                        help="Maximum number on the die",
                        required=True)
    parser.add_argument("--forbidden_numbers",
                        nargs="*",
                        type=int,
                        default=[],
                        help="Numbers that are to be avoided during the rolls")

    args = parser.parse_args()

    expected = expected_rolls(args.target, args.max_num, args.forbidden_numbers)
    probability_one = probability_of_one_in_expected_rolls(args.target, args.max_num,
                                                           args.forbidden_numbers)

    print(
        f"Expected rolls to get a total of {args.target} (avoiding {args.forbidden_numbers}): {expected:.3f}"
    )
    print(
        f"Probability of rolling a '1' in the expected number of rolls: {probability_one:.3f}"
    )


if __name__ == "__main__":
    main()
