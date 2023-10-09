<h1 align="center"><b>0x00. AIRBNB CLONE - THE CONSOLE</b></h1>
<div align="center"><code>Group project</code> <code>Python</code> <code>OOP</code></div>

# Background Context
<details>
<summary><h3>Welcome to the AirBnB clone project!</h3></summary>

Before starting, please read the AirBnB concept page.

<h4>First step: Write a command interpreter to manage your AirBnB objects.</h4>

This is the first step towards building your first full web application: the **AirBnB clone**. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called `BaseModel`) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (`User`, `State`, `City`, `Place`…) that inherit from `BaseModel`
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine
</details>

<details>
<summary><h3>What’s a command interpreter?</h3></summary>

Do you remember the Shell? It’s exactly the same but limited to a specific use-case. In our case, we want to be able to manage the objects of our project:
- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object
</details>


# Resources
<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/66">Python packages</a></b></summary>


</details>

<details>
<summary><b><a href="https://intranet.alxswe.com/concepts/74">AirBnB clone</a></b></summary>


</details>

<details>
<summary><b><a href="https://docs.python.org/3.8/library/cmd.html">cmd module</a></b></summary>


</details>

<details>
<summary><b><a href="https://pymotw.com/2/cmd/">cmd module in depth</a></b></summary>


</details>

<details>
<summary><b>packages </b>concept page</summary>


</details>

<details>
<summary><b><a href="https://docs.python.org/3.8/library/uuid.html">uuid module</a></b></summary>


</details>

<details>
<summary><b><a href="https://docs.python.org/3.8/library/datetime.html">datetime</a></b></summary>


</details>

<details>
<summary><b><a href="https://docs.python.org/3.8/library/unittest.html#module-unittest">unittest module</a></b></summary>


</details>

<details>
<summary><b><a href="https://yasoob.me/2013/08/04/args-and-kwargs-in-python-explained/">args/kwargs</a></b></summary>


</details>

<details>
<summary><b><a href="https://www.pythonsheets.com/notes/python-tests.html">Python test cheatsheet</a></b></summary>


</details>

<details>
<summary><b><a href="https://wiki.python.org/moin/CmdModule">cmd module wiki page</a></b></summary>


</details>

<details>
<summary><b><a href="https://realpython.com/python-testing/">python unittest</a></b></summary>


</details>


<!-- **man or help:**
- `` -->

# Learning Objectives
<details>
<summary><b><a href=" ">How to create a Python package</a></b></summary>


</details>

<details>
<summary><b><a href=" ">How to create a command interpreter in Python using the cmd module</a></b></summary>


</details>

<details>
<summary><b><a href=" ">What is Unit testing and how to implement it in a large project</a></b></summary>


</details>

<details>
<summary><b><a href=" ">How to serialize and deserialize a Class</a></b></summary>


</details>

<details>
<summary><b><a href=" ">How to write and read a JSON file</a></b></summary>


</details>

<details>
<summary><b>How to manage <code>datetime</code></b></summary>


</details>

<details>
<summary><b>What is an <code>UUID</code></b></summary>


</details>

<details>
<summary><b>What is <code>*args</code> and how to use it</b></summary>


</details>

<details>
<summary><b>What is <code>**kwargs</code> and how to use it</b></summary>


</details>

<details>
<summary><b><a href=" ">How to handle named arguments in a function</a></b></summary>


</details>

# Requirements
<details>
<summary><h3>Python Scripts</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version `2.8.*`)
- All your files must be executable
- The length of your files will be tested using `wc`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
</details>

<details>
<summary><h3>Python Unit Tests</h3></summary>

- Allowed editors: `vi`, `vim`, `emacs`
- All your files should end with a new line
- All your test files should be inside a folder `tests`
- You have to use the [unittest module](https://docs.python.org/3.4/library/unittest.html#module-unittest)
- All your test files should be python files (extension: `.py`)
- All your test files and folders should start by `test_`
- Your file organization in the tests folder should be the same as your project
- e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
- e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
- All your tests should be executed by using this command: `python3 -m unittest discover tests`
- You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
- All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`)
- All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`)
- All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case
</details>


<details>
<summary><h3>GitHub</h3></summary>

**There should be one project repository per group. If you clone/fork/whatever a project repository with the same name before the second deadline, you risk a 0% score.**
</details>

# More Info
<details>
<summary><h3>Execution</h3></summary>

Your shell should work like this in interactive mode:
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C)
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: `$ echo "python3 -m unittest discover tests" | bash`

<br>
<img src="https://github.com/codenvibes/AirBnB_clone/blob/master/pics/img1_0x00.AIRBNB_CLONE-THE%20CONSOLE.png">
</details>

# Video library
<div><video autoplay="" poster="https://hbtn-vod-input-prod.s3-accelerate.amazonaws.com/ALX/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812/16966eb2f1a059c5e0282d5588288e5729446ea17fbf4e1f4fca0867d788f812.jpg?response-content-disposition=attachment%3B&amp;X-Amz-Algorithm=AWS4-HMAC-SHA256&amp;X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20231009%2Fus-east-1%2Fs3%2Faws4_request&amp;X-Amz-Date=20231009T071246Z&amp;X-Amz-Expires=14400&amp;X-Amz-SignedHeaders=host&amp;X-Amz-Signature=373e77ec8a61a0599efc69b488ba49f41f1be2da0f5e1290d254b063eaab483f" src="blob:https://intranet.alxswe.com/7d360758-2084-4631-9c07-b10531e6c6d0"></video></div>

# Tasks
<details>
<summary>

### 0. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 1. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 2. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 3. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 4. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 5. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 6. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 7. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 8. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 9. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 10. 
`mandatory`

File: []()
</summary>


</details>

<details>
<summary>

### 11. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 12. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 13. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 14. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 15. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 16. 
`#advanced`

File: []()
</summary>


</details>

<details>
<summary>

### 17. 
`#advanced`

File: []()
</summary>


</details>

