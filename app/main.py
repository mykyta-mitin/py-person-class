class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    persons = [Person(p["name"], p["age"]) for p in people]

    for p in people:
        if "wife" in p and p["wife"] is not None:
            Person.people[p["name"]].wife = Person.people[p["wife"]]

        if "husband" in p and p["husband"] is not None:
            Person.people[p["name"]].husband = Person.people[p["husband"]]

    return persons
