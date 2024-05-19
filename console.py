#!/usr/bin/python3
""" Defines the HBnB console """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter class """

    prompt = "(hbnb) "

    def emptyline(self):
        """Shouldn’t execute anything if no command is passed"""
        pass

    def do_EOF(self, arg):
        """EOF (end of file) signal to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
