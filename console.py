#!/usr/bin/python3

import cmd
import re
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Class to the command Line"""

    prompt = "(hbnb) "
    classes = {"BaseModel", "City", "State",
               "Amenity", "User", "Review", "Place"}

    def do_EOF(self, line):
        """Method that exist the program
        """
        return True

    def do_quit(self, line):
        """Method that exist the program
        """
        return True

    def emptyline(self):
        pass

    def do_create(self, line):
        """Method that create a new object
        """
        try:
            obj = eval("{}()".format(line))
            obj.save()
            print("{}".format(obj.id))
        except NameError:
            print("** class doesn't exist **")
        except AttributeError:
            print("** class name missing **")

    def do_show(self, line):
        """Prints the string representation of an
        instance based on the class name and id
        """
        arg = line.split()
        try:
            if not arg:
                raise SyntaxError()
            if arg[0] not in self.classes:
                raise NameError()
            if len(arg) < 2:
                raise IndexError()
            obj = "{}.{}".format(arg[0], arg[1])
            dic = storage.all()
            if obj in dic:
                print(dic[obj])
            else:
                raise KeyError()
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        """
        arg = line.split()
        try:
            if not arg:
                raise SyntaxError()
            if arg[0] not in self.classes:
                raise NameError()
            if len(arg) < 2:
                raise IndexError()
            obj = "{}.{}".format(arg[0], arg[1])
            dic = storage.all()
            if obj in dic:
                dic.pop(obj)
                storage.save()
            else:
                raise KeyError()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all
        instances based or not on the class name
        """
        clas = line.split()
        objs = storage.all()
        objs_list = []
        if not clas:
            for key, value in objs.items():
                objs_list.append(str(value))
            print(objs_list)
            return None
        if clas[0] and not clas[0] in self.classes:
            print("** class doesn't exist **")
            return None

        for key, value in objs.items():
            if clas[0] == value.__class__.__name__:
                objs_list.append(str(value))
        print(objs_list)

    def do_count(self, line):
        """Method that counts the instance of a class
        """
        count = 0
        clas = line.split()
        objs = storage.all()
        if not clas[0] in self.classes:
            print("** class doesn't exist **")
            return None
        for key, value in objs.items():
            if value.__class__.__name__ == clas[0]:
                count += 1
        print(count)
    def do_update(self, line):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """
        commands = line.split()
        objs = storage.all()
        if not commands:
            print("** class name missing **")
            return None
        if not commands[0] in self.classes:
            print("** class doesn't exist **")
            return None
        if len(commands) < 4:
            if len(commands) < 2:
                print("** instance id missing **")
            elif len(commands) < 3:
                print("** attribute name missing **")
            elif len(commands) < 4:
                print("** value missing **")
            return None
        key = "{}.{}".format(commands[0], commands[1])
        if key not in objs:
            print("** no instance found **")
            return None
        obj = objs[key]

        try:
            obj.__dict__[commands[2]] = eval(commands[3])
            obj.save()
        except Exception:
            obj.__dict__[commands[2]] = commands[3]
            obj.save()
            
    def remove(self, line_list):
        line_list = str(line_list).replace("update(", "")
        line_list = str(line_list).replace("show(", "")
        line_list = str(line_list).replace("destroy(", "")
        line_list = line_list.split(',')
        string = ""
        for i in range(len(line_list)):
            line_list[i] = re.sub(r"[^a-zA-Z0-9-_]", "", line_list[i])
            string += line_list[i]
            string += " "
        return(string)
    def default(self, line):
        l_list = line.split('.')
        if len(l_list) >= 2:
            if l_list[1] == "all()":
                self.do_all(l_list[0])
            if l_list[1] == "count()":
                self.do_count(l_list[0])
            elif l_list[1][:4] == "show":
                self.do_show(self.remove(l_list))
            elif l_list[1][:7] == "destroy":
                self.do_destroy(self.remove(l_list))
        else:
            cmd.Cmd.default(self, line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
