#!/usr/bin/python3
"""
This module provides a command-line interface for interacting with
models and objects in a hypothetical database management system.

Auth: codenvibes & amoskarugo
"""
import cmd
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import re
from shlex import split
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    This class provides a command-line interface for interacting
    with models and objects in a hypothetical database management system.

    Supported commands include creating, showing, updating,
    destroying, and listing objects, as well as counting instances.

    Attributes:
        prompt (str): The command prompt.
        __classes (set): A set of supported model classes.
    """
    prompt = "(hbnb) "
    __classes = {
        "Amenity",
        "BaseModel",
        "City",
        "Place",
        "Review",
        "State",
        "User"
    }

    def emptyline(self):
        """
        Handles an empty line input by doing nothing.
        """
        pass

    def default(self, input):
        """
        Handle unknown or complex commands that are not standard.
        It parses and delegates the commands based on specific syntax.

        Args:
            input (str): The input command.

        Returns:
            - bool: True if the command was executed successfully,
            False otherwise.
        """
        cmd_dict = {
            "all": self.do_all,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "count": self.do_count,
            "update": self.do_update
        }
        dot_search = re.search(r"\.", input)
        if dot_search is not None:
            list_arg = [input[:dot_search.span()[0]], input
                        [dot_search.span()[1]:]]
            dot_search = re.search(r"\((.*?)\)", list_arg[1])
            if dot_search is not None:
                action = [list_arg[1][:dot_search.span()[0]],
                          dot_search.group()[1:-1]]
                if action[0] in cmd_dict.keys():
                    call = "{} {}".format(list_arg[0], action[1])
                    return cmd_dict[action[0]](call)
        print("*** Unknown syntax: {}".format(input))
        return False

    def do_EOF(self, input):
        """
        Handle the EOF (End of File) command by printing a new line
        and returning True to exit the command loop.

        Args:
            input (str): The input command.

        Returns:
            bool: True to exit the command loop.
        """
        print("")
        return True

    def do_quit(self, input):
        """
        Handle the 'quit' command by returning True to exit the command loop.

        Args:
            input (str): The input command.

        Returns:
            bool: True to exit the command loop.
        """
        return True

    def do_create(self, input):
        """
        Create a new instance of a model class and print its unique
        identifier (id) to the console. The new instance is also
        saved to the database.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(list_arg[0])().id)
            storage.save()

    def do_show(self, input):
        """
        Show the string representation of an instance of a model
        class based on the provided class name and instance ID.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        obj_dict = storage.all()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict:
            print("** no instance found **")
        else:
            print(obj_dict["{}.{}".format(list_arg[0], list_arg[1])])

    def do_destroy(self, input):
        """
        Delete an instance of a model class based on the provided
        class name and instance ID. The instance is removed from
        the database.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        obj_dict = storage.all()
        if len(list_arg) == 0:
            print("** class name missing **")
        elif list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(list_arg) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
        else:
            del obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            storage.save()

    def do_all(self, input):
        """
        List all instances of a model class or all instances of all
        model classes if no class name is provided.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        if len(list_arg) > 0 and list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objl = []
            for object in storage.all().values():
                if len(list_arg) > 0 and list_arg[0] == object.\
                        __class__.__name__:
                    objl.append(object.__str__())
                elif len(list_arg) == 0:
                    objl.append(object.__str__())
            print(objl)

    def do_count(self, input):
        """
        Count the number of instances of a model class.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        count = 0
        for object in storage.all().values():
            if list_arg[0] == object.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, input):
        """
        Update the attributes of an instance of a model class based
        on the provided class name, instance ID, and attribute
        name-value pairs.

        Args:
            input (str): The input command.

        Returns:
            None
        """
        list_arg = tokenize(input)
        obj_dict = storage.all()

        if len(list_arg) == 0:
            print("** class name missing **")
            return False
        if list_arg[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(list_arg) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(list_arg[0], list_arg[1]) not in obj_dict.keys():
            print("** no instance found **")
            return False
        if len(list_arg) == 2:
            print("** attribute name missing **")
            return False
        if len(list_arg) == 3:
            try:
                type(eval(list_arg[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(list_arg) == 4:
            object = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            if list_arg[2] in object.__class__.__dict__.keys():
                valtype = type(object.__class__.__dict__[list_arg[2]])
                object.__dict__[list_arg[2]] = valtype(list_arg[3])
            else:
                object.__dict__[list_arg[2]] = list_arg[3]
        elif type(eval(list_arg[2])) == dict:
            object = obj_dict["{}.{}".format(list_arg[0], list_arg[1])]
            for k, v in eval(list_arg[2]).items():
                if (k in object.__class__.__dict__.keys() and
                        type(object.__class__.__dict__[k]) in {str,
                                                               int, float}):
                    valtype = type(object.__class__.__dict__[k])
                    object.__dict__[k] = valtype(v)
                else:
                    object.__dict__[k] = v
        storage.save()


def tokenize(input):
    """
    Tokenize the input string into a list of command tokens,
    considering the presence of curly braces and brackets.

    Args:
        input (str): The input command.

    Returns:
        list: A list of tokens extracted from the input string.
    """
    curly_braces = re.search(r"\{(.*?)\}", input)
    brackets = re.search(r"\[(.*?)\]", input)
    if curly_braces is None:
        if brackets is None:
            return [token.strip(",") for token in split(input)]
        else:
            token_res = split(input[:brackets.span()[0]])
            list = [token.strip(",") for token in token_res]
            list.append(brackets.group())
            return list
    else:
        token_res = split(input[:curly_braces.span()[0]])
        list = [token.strip(",") for token in token_res]
        list.append(curly_braces.group())
        return list


if __name__ == "__main__":
    HBNBCommand().cmdloop()
