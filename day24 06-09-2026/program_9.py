#design a employee hierarchy

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.subordinates = []

    def add_subordinate(self, subordinate):
        self.subordinates.append(subordinate)

    def display_hierarchy(self, level=0):
        print(" " * level * 4 + f"{self.position}: {self.name}")
        for subordinate in self.subordinates:
            subordinate.display_hierarchy(level + 1)

# Example usage
ceo = Employee("Alice", "CEO")
cto = Employee("Bob", "CTO")
dev1 = Employee("Charlie", "Developer")
dev2 = Employee("David", "Developer")

ceo.add_subordinate(cto)
cto.add_subordinate(dev1)
cto.add_subordinate(dev2)

ceo.display_hierarchy()