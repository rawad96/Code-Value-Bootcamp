def filter_adults(people: list[dict]) -> list[dict]:
    return list(filter(lambda person: person['age'] >= 18, people))

def sort_by_age(people: list[dict]) -> list[dict]:
    return sorted(people, key=lambda person: person['age'])

def get_names(people: list[dict]) -> list[str]:
    return list(map(lambda person: person['name'], people))

if __name__ == "__main__":
    people = [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 17},
        {"name": "Charlie", "age": 30},
        {"name": "Diana", "age": 16}
    ]

    adults = filter_adults(people)
    print("Adults:", adults)

    sorted_people = sort_by_age(people)
    print("Sorted by age:", sorted_people)

    names = get_names(people)
    print("Names:", names)