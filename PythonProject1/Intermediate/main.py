from turtle import Turtle,Screen

robin=Turtle()
print(robin)
robin.shape("turtle")
robin.color("coral")
robin.forward(100)
robin.left(120)
robin.forward(100)
robin.left(120)
robin.forward(100)

my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
# Pokemon=[["Pikachu","Electric"],["Squirtle","Water"],["Charmander","Fire"]]
table.field_names = ["Pokemon","Type"]
print(table)
table.add_row(["Pikachu","Electric"])
table.add_row(["Squirtle","Water"])
table.add_row(["Charmander","Fire"])
print(table)
