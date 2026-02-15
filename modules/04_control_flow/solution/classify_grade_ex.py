def classify_grade(score: int) -> str:
    grades_score = {"A": range(90, 101), "B": range(80, 90), "C": range(70, 80), "D": range(60, 70), "F": range(0, 60)}
    for grade, score_range in grades_score.items():
        if score in score_range:
            return grade
    raise ValueError("Score must be between 0 and 100")


if __name__ == "__main__":
    print(classify_grade(95))
    print(classify_grade(85))
    print(classify_grade(55))
