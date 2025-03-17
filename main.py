from Graph import Graph
import graphviz
class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def __str__(self):
        return self.name + "-->" + self.email

people = Graph()
per01 = Person("George", 'george@email.com')
per02 = Person("Sue", 'Sue@email.com')
per03 = Person("John", 'john@email.com')
per04 = Person("Bob", 'Bob@email.com')
per05 = Person("Geo", 'geo@email.com')
per06 = Person("Avery", 'avery@email.com')
per07 = Person("Mike", 'mike@email.com')
per08 = Person("Dan", 'dan@email.com')

people.add_node(per01)
people.add_node(per02)
people.add_node(per03)
people.add_node(per04)
people.add_node(per05)
people.add_node(per06)
people.add_node(per07)
people.add_node(per08)



people.add_edge(per01, per02)
people.add_edge(per01, per03)
people.add_edge(per01, per04)
people.add_edge(per02, per05)
people.add_edge(per03, per07)
people.add_edge(per04, per08)
people.add_edge(per08, per04)
people.add_edge(per05, per06)

people.visualize("graph", arrow_style='both')
print('text')