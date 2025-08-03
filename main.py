import random

from MenuBuilder import MenuBuilder
from utils import CallbackOption


@CallbackOption
def option_1():
    print("Option 1")

@CallbackOption
def option_2():
    print("Option 2")

@CallbackOption
def option_3A():
    print("Option 3 A")

@CallbackOption
def option_3B():
    print("Option 3 B")

@CallbackOption
def option_4():
    print("Option 4")

def is_admin():
    return random.choice([True, False])



builder = MenuBuilder("Menu Principal")

(builder.add_option("Option 1", option_1, visible=False )
        .add_option("Option 2", option_2 )
        .add_submenu("SubMenu - Option3")
            .add_option("Option 3A", option_3A)
            .add_option("Option 3B", option_3B)
            .end_submenu()
        .add_option("Option 4", option_4 ))

menu = builder.build()

while True:
    menu.show()