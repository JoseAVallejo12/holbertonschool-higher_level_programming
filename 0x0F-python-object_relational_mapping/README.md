# 0x0F. Python - Object-relational mapping

## Background Context
In this project, you will link two amazing worlds: Databases and Python!

In the first part, you will use the module MySQLdb to connect to a MySQL database and execute your SQL queries.

In the second part, you will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, your biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. You won’t write any SQL queries only Python code. Last thing, your code won’t be “storage type” dependent. You will be able to change your storage easily without re-writing your entire project.

Without ORM:
```
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
With an ORM:
```
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```
Do you see the difference? Cool, right?

The biggest difficulty with ORM is: The syntax!

Indeed, all of them have the same type of syntax, but not always. Please read tutorials and don’t read the entire documentation before starting, just jump on it if you don’t get something.

## Resources
Read or watch:

- [Object-relational mappers](https://intranet.hbtn.io/rltoken/IqdjUaZ31ZfP6eT-lTyUkA)
- [mysqlclient/MySQLdb documentation](https://intranet.hbtn.io/rltoken/rMJpVJ1_YjMWfvY00I7Kpw) (please don’t pay attention to _mysql)
- [MySQLdb tutorial](https://intranet.hbtn.io/rltoken/KskI6xMlQCYJyE0UVPJfKQ)
- [SQLAlchemy tutorial](https://intranet.hbtn.io/rltoken/9JWveMwNKe3IUErdEbDsUQ)
- [SQLAlchemy](https://intranet.hbtn.io/rltoken/E9dLS6Shaezq4ivnGxN_RA)
- [mysqlclient/MySQLdb](https://intranet.hbtn.io/rltoken/SSoBE3ckyGFi3NexCH3nuw)
- [Introduction to SQLAlchemy](https://intranet.hbtn.io/rltoken/I5bvhPGTOu3_-T-4jpN-hg)
- [Flask SQLAlchemy](https://intranet.hbtn.io/rltoken/UvaHESHeqlRA0Z0uQFi0_A)
- [10 common stumbling blocks for SQLAlchemy newbies](https://intranet.hbtn.io/rltoken/Zb8Yc2WycLLYX8gnLlwZKw)
- [Python SQLAlchemy Cheatsheet](https://intranet.hbtn.io/rltoken/XHPAX7-ydSou2BLWHII8Vw)
- [SQLAlchemy ORM Tutorial for Python Developers](https://intranet.hbtn.io/rltoken/aeLSQ039BhLhamU2BjqsOw) (Warning: This tutorial is with PostgreSQL, but the concept of SQLAlchemy is the same with MySQL)

## Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

## General
- Why Python programming is awesome (don’t forget to tweet today, with the hashtag #pythoniscool :))
- How to connect to a MySQL database from a Python script
- How to SELECT rows in a MySQL table from a Python script
- How to INSERT rows in a MySQL table from a Python script
- What ORM means
- How to map a Python Class to a MySQL table

## Requirements
General
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 14.04 LTS using python3 (version 3.4.3)
- Your files will be executed with MySQLdb version 1.3.x
- Your files will be executed with SQLAlchemy version 1.2.x
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the PEP 8 style (version 1.7.*)
- All your files must be executable
- The length of your files will be tested using wc
- All your modules should have a documentation (python3 -c 'print(__import__("my_module").__doc__)')
- All your classes should have a documentation (python3 -c 'print(__import__("my_module").MyClass.__doc__)')
- All your functions (inside and outside a class) should have a documentation (python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')
- You are not allowed to use execute with sqlalchemy
