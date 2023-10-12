#!/usr/bin/python3.8

"""command interpreter"""

import cmd
import shlex

from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """quit the command interpreter"""
        return True

    def do_EOF(self, line):
        """quit the program on end-of-file."""
        print()
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it
           (to the JSON file) and prints the id. Ex: $ create BaseModel
        """
        args = shlex.split(line)

        if len(args) > 0:
            if args[0] == "BaseModel":
                base_model = BaseModel()
                base_model.save()
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()