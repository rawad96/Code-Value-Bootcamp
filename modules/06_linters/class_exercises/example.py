"""
Example module to demonstrate the power of linters and formatters.
This code intentionally violates many best practices!
"""


def calculate_test_statistics(scores: list[int]) -> dict[str, float | int]:
    """
    Calculate statistics for a list of test scores.

    This function takes a list of test scores and calculates various statistics
    including the average score, highest and lowest scores, and counts how many
    students passed or failed.

    Purpose:
        Help teachers quickly analyze test results to understand class
        performance.
        A passing score is 60 or above.

    Parameters:
        scores: A list of numbers representing test scores (0-100 scale)

    Returns:
        A dictionary with the following keys:
        - 'average': The average (mean) score
        - 'highest': The highest score
        - 'lowest': The lowest score
        - 'passed': Number of scores >= 60
        - 'failed': Number of scores < 60
        - 'pass_rate': Percentage of students who passed

    Example:
        >>> scores = [75, 82, 55, 90, 68]
        >>> result = calculate_test_statistics(scores)
        >>> print(result['average'])
        74.0
    """
    total_scores = 0
    student_count = 0
    passed = 0
    failed = 0
    highest = 0
    lowest = 100

    for score in scores:
        if score >= 0 and score <= 100:
            total_scores += score
            student_count = student_count + 1
            if score > highest:
                highest = score
            if score < lowest:
                lowest = score
            if score >= 60:
                passed = passed + 1
            else:
                failed = failed + 1

    return {
        "average": total_scores / student_count if student_count > 0 else 0,
        "highest": highest,
        "lowest": lowest,
        "passed": passed,
        "failed": failed,
        "pass_rate": (passed / student_count) * 100 if student_count > 0 else 0,
    }


# Example usage
if __name__ == "__main__":
    test_scores = [85, 92, 78, 45, 70, 25, 99, 50, 73, 81]

    result = calculate_test_statistics(test_scores)
    print("Test Statistics:")
    print(f"  Average Score: {result['average']:.1f}")
    print(f"  Highest Score: {result['highest']}")
    print(f"  Lowest Score: {result['lowest']}")
    print(f"  Students Passed: {result['passed']}")
    print(f"  Students Failed: {result['failed']}")
    print(f"  Pass Rate: {result['pass_rate']:.1f}%")
