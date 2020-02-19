#!/usr/bin/python3

import cmd
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """Class to the command Line"""

    prompt ="(hbnb) "
    classes = {"BaseModel"}
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
        """Prints the string representation of an instance based on the class name and id
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
        """Prints all string representation of all instances based or not on the class name
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

            
    def do_update(self):
        """Updates an instance based on the class name and id by adding or updating attribute
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
