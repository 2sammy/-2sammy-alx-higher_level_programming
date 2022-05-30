Hello World, Python!
This is the first project made with Python and consists of knowing some of its bases.

<b>Learning Objectives</b>
Why Python programming is awesome?
Who created Python?
Who is Guido van Rossum?
Where does the name Python come from?
What is the Zen of Python?
How to use the Python interpreter?
How to print text and variables using print?
How to use strings?
What are indexing and slicing in Python?
How to apply the syntax code of pycodestyle?


Tasks
Run Python file
Write a Shell script that runs a Python script.

The Python file name will be saved in the environment variable $PYFILE

Solution: 0-run

$ amonkeyprogrammer@ubuntu:~/py/0x00$ cat main.py 
#!/usr/bin/python3
print("Holberton School")

$ amonkeyprogrammer@ubuntu:~/py/0x00$ export PYFILE=main.py
$ amonkeyprogrammer@ubuntu:~/py/0x00$ ./0-run
Holberton School
$ amonkeyprogrammer@ubuntu:~/py/0x00$