#!/usr/bin/python3

"""command interpreter"""

import cmd
import json
import shlex
import re

from models.base_model import BaseModel
import models
from models.user import User
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.state import State

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State",
               "City", "Amenity", "Place"]

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
            if args[0] in self.classes:
                instance_ = globals()[args[0]]()
                instance_.save()
                print(instance_.id)
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an instance based on
            the class name and id. Ex: $ show BaseModel 1234-1234-1234
        """
        args = shlex.split(line)
        if len(args) > 0:
            if args[0] in self.classes and len(args) > 1:
                for key, obj in models.storage.all().items():
                    class_name, id = key.split(".")
                    if id == args[1]:
                        # new_object = globals()[class_name](**obj)
                        print(obj)
            elif args[0] in self.classes and len(args) < 2:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_destroy(self, line):
        """destroy: Deletes an instance based on the class name and id
        (save the change into the JSON file). Ex: $ destroy BaseModel 1234-1234-1234.
        """
        args = shlex.split(line)
        objects = models.storage.all()
        args_len = len(args)
        if args_len > 0:
            if args_len > 1 and args[0] in self.classes:
                deleted = False
                for key, value in objects.items():
                    class_name, id = key.split(".")
                    if id == args[1]:
                        del objects[key]
                        deleted = True
                        models.storage.save()
                        break
                if not deleted:
                    print("** no instance found **")
            elif args[0] in self.classes and len(args) < 2:
                print("** instance id missing **")
            else:
                print("** class doesn't exist **")
        else:
            print("** class name missing **")

    def do_all(self, line):
        """Prints all string representation of all instances based
            or not on the class name. Ex: $ all BaseModel or $ all
         """
        args = shlex.split(line)
        args_len = len(args)
        all_objects = models.storage.all()
        if args_len > 0:
            if args[0] in self.classes:
                str_ojb_list = []
                for key, obj in all_objects.items():
                    class_name, id = key.split(".")
                    if class_name == args[0]:
                        str_ojb_list.append(str(obj))
                print(str_ojb_list)
            else:
                print("** class doesn't exist **")
        else:
            str_ojb_list = [str(obj) for key, obj in all_objects.items()]
            # str_ojb_list = []
            # for key, obj in all_objects.items():
            #     str_ojb_list.append(str(obj))

            print(str_ojb_list)

    def do_update(self, line):
        """
        update: Updates an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
         Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com".

        :param line:
        :return:
        """
        args = shlex.split(line)
        args_len = len(args)
        all_objs = models.storage.all()

        if args_len > 0:
            if args[0] in self.classes and args_len >= 4:
                instance_id_found = False
                for key, obj in all_objs.items():
                    class_name, id = key.split(".")
                    if args[1] == id:
                        setattr(obj, args[2], args[3])
                        print(obj)
                        instance_id_found = True
                if not instance_id_found:
                    print("** no instance found **")

            elif args[0] in self.classes and args_len < 2:
                print("** instance id missing **")
            elif args[0] in self.classes and args_len < 3:
                print("** attribute name missing  **")
            elif args[0] in self.classes and args_len < 4:
                print("** value missing **")
            else:
                print("** class doesn't exist **")

        else:
            print("** class name missing **")

    def default(self, line):
        """This is a method that is called on unrecognised commands"""
        class_name, method = line.split(".")
        str_line = f"{class_name}"
        all_objs = models.storage.all()
        if class_name in self.classes:
            if method == "all()":
                all_instances = []
                for key, obj in all_objs.items():
                    instance, id = key.split(".")
                    if instance == class_name:
                        all_instances.append(obj)
                print(all_instances)
                # self.do_all(str_line)
            elif method == "count()":
                count = 0
                for key, value in all_objs.items():
                    instance, id = key.split(".")
                    if instance == class_name:
                        count += 1
                print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()