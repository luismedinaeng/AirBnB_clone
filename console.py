#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """Class to the command Line"""

    prompt ="(hbnb) "

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
        try:
            arg = line.split
            if not args:
                raise SyntaxError()
            if args[0] not in self.my_classes:
                raise NameError()
            if len(args) < 2:
                raise IndexError()
            obj = "{}.{}".format(arg[0], arg[1])
            dic = storage.all()
            if obj in dict_objs:
                print(dict_objs[obj])
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

    def do_destroy(self):
        """Deletes an instance based on the class name and id
        """
    def do_all(self):
        """Prints all string representation of all instances based or not on the class name
        """
    def do_update(self):
        """Updates an instance based on the class name and id by adding or updating attribute
        """
if __name__ == '__main__':
    HBNBCommand().cmdloop()
