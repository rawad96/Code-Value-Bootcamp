from solution.list_operations_with_lambda import (filter_adults, get_names, sort_by_age)

def test_filter_adults():
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 30},
        {"name": "Diana", "age": 16}
    ]
    filter_adults_expected = [{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]
    assert filter_adults(people) == filter_adults_expected

    get_names_expected = ["Alice", "Bob", "Charlie", "Diana"]
    assert get_names(people) == get_names_expected

    sort_by_age_expected = [{"name": "Diana", "age": 16}, {"name": "Bob", "age": 17},{"name": "Alice", "age": 25}, {"name": "Charlie", "age": 30}]
    assert sort_by_age(people) == sort_by_age_expected

