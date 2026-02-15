from class_exercises.example import calculate_test_statistics


def test_calculate_test_statistics():
    scores = [85, 92, 78, 45, 88, 67, 95, 54, 73, 81]
    assert calculate_test_statistics(scores) == {
        "average": 75.8,
        "highest": 95,
        "lowest": 45,
        "passed": 8,
        "failed": 2,
        "pass_rate": 80.0,
    }


def test_calculate_test_statistics_second():
    scores = [85, 92, 78, 45, 70, 25, 99, 50, 73, 81]
    assert calculate_test_statistics(scores) == {
        "average": 69.8,
        "highest": 99,
        "lowest": 25,
        "passed": 7,
        "failed": 3,
        "pass_rate": 70.0,
    }
