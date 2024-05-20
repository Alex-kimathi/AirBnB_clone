#!/usr/bin/python3
""" Defines the HBnB console """
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review
from datetime import datetime
from shlex import shlex


class HBNBCommand(cmd.Cmd):
    """ Defines the command interpreter class """

    prompt = "(hbnb) "
    cls_dct = {'BaseModel': BaseModel}

    def emptyline(self):
        """Shouldn’t execute anything if no command is passed"""
        pass

    def do_create(self, cname=None):
        """Creates a new instance of BaseModel, saves & prints the id"""
        if not cname:
            print("** class name missing **")
        elif not self.cls_dct.get(cname):
            print("** class doesn't exist **")
        else:
            obj = self.cname[clsname]()
            models.storage.save()
            print(obj.id)

    def do_show(self, arg):
        """Display the string representation of a class instance based on id"""
        cname = None
        objid = None
        line = arg.split()

        if len(line) > 0:
            cname = line[0]
        if len(line) > 1:
            objid = line[1]
        if not cname:
            print("** class name missing **")
        elif not objid:
            print("** instance id missing **")
        elif not self.cls_dct.get(cname):
            print("** class doesn't exist **")
        else:
            key = cname + "." + objid
            obj = models.storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                print(obj)

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id0"""
        cname = None
        objid = None
        line = arg.split()

        if len(line) > 0:
            cname = line[0]
        if len(line) > 1:
            objid = line[1]
        if not cname:
            print("** class name missing **")
        elif not objid:
            print("** instance id missing **")
        elif not self.cls_dct.get(cname):
            print("** class doesn't exist **")
        else:
            key = cname + "." + objid
            obj = models.storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                del models.storage.all()[key]
                models.storage.save()

    def do_all(self, arg):
        """
        Prints __str__ of all instances based or not on the class name
        """
        if not arg:
            print([str(v) for k, v in models.storage.all().items()])
        else:
            if not self.cls_dct.get(arg):
                print("** class doesn't exist **")
            else:
                print([str(v) for k, v in models.storage.all().items()
                       if type(v) is self.cls_dct.get(arg)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute
        """
        cname, objid, attr_name, attr_val = None, None, None, None
        line = arg.split(' ', 3)

        if len(line) > 0:
            cname = line[0]
        if len(line) > 1:
            objid = line[1]
        if len(line) > 2:
            attr_name = line[2]
        if len(line) > 3:
            attr_val = list(shlex(line[3]))[0].strip('"')
        if not cname:
            print("** class name missing **")
        elif not objid:
            print("** instance id missing **")
        elif not attr_name:
            print("** attribute name missing **")
        elif not attr_val:
            print("** value missing **")
        elif not self.cls_dct.get(cname):
            print("** class doesn't exist **")
        else:
            key = cname + "." + objid
            obj = models.storage.all().get(key)
            if not obj:
                print("** no instance found **")
            else:
                if hasattr(obj, attr_name):
                    attr_val = type(getattr(obj, attr_name))(attr_val)
                else:
                    attr_val = self.valType(atrr_val)(attr_val)
                setattr(obj, attr_name, atrr_val)
                models.storage.save()

    def do_EOF(self, arg):
        """EOF (end of file) signal to exit the program"""
        print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the interpreter"""
        return True

    @staticmethod
    def valType(attr_val):
        """Checks data type of argument"""
        try:
            int(attr_val)
            return (int)
        except ValueError:
            pass
        try:
            float(attr_val)
            return (float)
        except ValueError:
            return (str)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
