# Holberton School AirBnB project - The console
![AirBnB clone logo](https://i.blogs.es/360edc/airbnb/450_1000.jpg)

This project consist on make a console of the clone of the AirBnB page.
The project is fully written in python programming language.
It objective is to understand the file manage, persistance in a program and the first step of a basic clone of the AirBnB web application

## Synopsis
This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…
Each task is linked and will help you to:

* put in place a parent class (called **BaseModel**) to take care of the initialization, serialization and deserialization of your future instances
* create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
* create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
* create the first abstracted storage engine of the project: File storage.
* create all unittests to validate all our classes and storage engine

## Getting Started
Shell work like this in interactive mode:

$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
$

But also in non-interactive mode:

$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
----------------------------------------
EOF  help  quit
(hbnb)
$

---

### Installing
Clone the repository of the project from Github. This repository contain the console and all classes.
https://github.com/luismedinaeng/AirBnB_clone
### Commands
These are the interpreter commands:

### quit
* Exit the program (also you can use EOF). **Usage:** quit


### help
* Show the documentation of a command and their documantacion status. **Usage:** help (for documantation status) - help <command name> (for comand documantation)


### create
* Creates a new instance of a HBNB class, saves it (to the JSON file) and prints the id. **Usage:** create <class name>


### show
* Prints the string representation of an instance based on the class name and id. **Usage:** show <class name> <instance id> or <class name>.show("<instance id>")


### destroy
* Deletes an instance based on the class name and id (save the change into the JSON file). **Usage:** destroy <class name> <instance id> or <class name>.destroy("<instance id>")


### all
* Prints all string representation of all instances based or not on the class name. **Usage:** all (for all instances), all <class name> or <class name>.all() (for all instances of a class)


### update
* Updates an instance based on the class name and id by adding or updating attribute (save the change into the JSON file). **Usage:** update <class name> <instance id> <attribute name> "<attribute value>" or <class name>.update(<instance id>, <attribute name>, <attribute value>) or <class name>.update(<instance id>, <dictionary representation>) (for update an instance based on his ID with a dictionary)

---
## Built with
Ubuntu 14.04, Emacs, Vim and Python3.

## Authors

|               |                       |
| ---------     | --------              |
| Nicolas Gomez | negomezte@unal.edu.co |
| Luis Medina   | malf95@hotmail.com    |
