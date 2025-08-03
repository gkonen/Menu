from collections.abc import Callable
from utils import Return, CallbackOption, CallbackSubMenu


class MenuOption:

    def __init__(self, name, callback: Callable[ [], None] | Return, visible = True):
        self.name = name
        self.callback = callback
        self.visible = visible

    def execute(self):
        if isinstance(self.callback, Return):
            return self.callback
        return self.callback()

class OptionSubMenu(MenuOption):

    def __init__(self, name, sub_menu: 'Menu', visible = True):
        super().__init__(name, None, visible)
        self.sub_menu = sub_menu

    @CallbackSubMenu
    def execute(self):
        self.sub_menu.show()

class Menu:

    def __init__(self, title: str):
        self.title = title
        self.options = []
        self.menu_parent = None

    def add_option(self, option: MenuOption):
        self.options.append(option)

    def __get_options_visible(self):
        return [ option for option in self.options if option.visible ]

    def __show_options(self):
        print(self.title)
        visible_options = self.__get_options_visible()
        for i in range( len(visible_options) ):
            print(f"{i+1}. {visible_options[i].name}")


    def __ask_input(self):
        entry = ""
        visible_options = self.__get_options_visible()
        good_input = False
        while not good_input:
            try:
                entry = int(input("> ")) -1
                if 0 <= entry < len(visible_options):
                    return visible_options[entry].execute()
                else:
                    raise IndexError

            except ValueError:
                print("Please enter a number")
            except IndexError:
                print("Please enter a number between 1 and " + str(len(self.options)))
            else:
                good_input = True

    @CallbackOption("You will return to previous menu")
    def show(self):
        while True:
            self.__show_options()
            result = self.__ask_input()
            match result:
                case Return.BACK:
                    return None
                case Return.EXIT:
                    exit()

