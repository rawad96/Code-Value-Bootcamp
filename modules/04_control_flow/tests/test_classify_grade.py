from solution.classify_grade_ex import classify_grade
import pytest 

def test_classify_grade():
    assert classify_grade(95) == "A"
    assert classify_grade(85) == "B"
    assert classify_grade(55) == "F"

def test_classify_grade_invalid_score():
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        classify_grade(101)
    with pytest.raises(ValueError, match="Score must be between 0 and 100"):
        classify_grade(-1)