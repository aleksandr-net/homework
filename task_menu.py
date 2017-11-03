from abc import ABCMeta, abstractmethod
from collections import OrderedDict


class CommandException(Exception):
    pass


class MenuException(Exception):
    pass


class Command(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class Menu(object):
    def __init__(self):
        self.__commands = OrderedDict()
        self.__index = len(self.__commands)


    def __iter__(self):
        return self


    def __next__(self):
        if self.__index == 0:
            self.__index = len(self.__commands)
            raise StopIteration
        num = len(self.__commands) - self.__index
        key = list(self.__commands.keys())[num]
        self.__index -= 1
        return (key, self.__commands[key])


    def add_command(self, name, klass):
        if not name:
            raise CommandException('Command must have a name!')

        if not issubclass(klass, Command):
            raise CommandException('Class "{}" is not Command!'.format(klass))

        self.__commands[name] = klass
        self.__index += 1


    def execute(self, name, *args, **kwargs):
        command = self.__commands.get(name)
        if not command:
            raise CommandException(
                'Command with name "{}" not found'.format(name))
        return command(*args, **kwargs).execute()


class ShowCommand(Command):
    def __init__(self, task_id):
        self.task_id = task_id

    def execute(self):
        print('execute show task {}'.format(self.task_id))


class ListCommand(Command):
    def __init__(self, menu):
        self.menu = None
        self.set_menu(menu)


    def set_menu(self, menu):
        if not isinstance(menu, Menu):
            raise MenuException

        self.menu = menu


    def execute(self):
        for name, command in self.menu:
            print(name)


if __name__ == '__main__':
    menu = Menu()
    menu.add_command('show', ShowCommand)
    menu.add_command('list', ListCommand)
    menu.execute('show', 1)
    menu.execute('list', menu)

    for item in menu:
        print(item)

    for name, command in menu:
        print(name, command)
