#!/usr/bin/python3.8

"""command interpreter"""

import cmd
import json
import shlex

from models.base_model import BaseModel
import models


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel"]

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
                print(base_model.id)
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




if __name__ == '__main__':
    HBNBCommand().cmdloop()