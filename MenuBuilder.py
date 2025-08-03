from Menu import Menu, MenuOption, OptionSubMenu
from utils import Return


class MenuBuilder:

    def __init__(self, title):
        self.main_menu = Menu(title)
        self.current_menu = self.main_menu

    def add_option(self, name, callback, visible = True):
        self.current_menu.add_option(MenuOption(name, callback, visible))
        return self

    def add_submenu(self, name, visible = True):
        sub_menu = Menu(name)
        sub_menu.menu_parent = self.current_menu
        self.current_menu.add_option( OptionSubMenu(name, sub_menu, visible) )
        self.current_menu = sub_menu
        return self

    def end_submenu(self):
        if self.current_menu.menu_parent is None:
            raise Exception("try to close main menu as sub menu")
        else:
            self.current_menu.add_option(MenuOption("Return", Return.BACK))
            self.current_menu = self.current_menu.menu_parent
            return self

    def build(self):
        self.current_menu.add_option(MenuOption("Exit", Return.EXIT))
        return self.main_menu