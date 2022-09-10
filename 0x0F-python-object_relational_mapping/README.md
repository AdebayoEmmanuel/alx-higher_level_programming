**Background Context**

In this project, I will link two amazing worlds: Databases and Python!

In the first part, I will use the module MySQLdb to connect to a MySQL database and execute my SQL queries.

In the second part, I will use the module SQLAlchemy (don’t ask me how to pronounce it…) an Object Relational Mapper (ORM).

The biggest difference is: no more SQL queries! Indeed, the purpose of an ORM is to abstract the storage to the usage. With an ORM, the biggest concern will be “What can I do with my objects” and not “How this object is stored? where? when?”. I won’t write any SQL queries only Python code. Last thing, my code won’t be “storage type” dependent. I will be able to change my storage easily without re-writing my entire project.

	* Without ORM:
```bash
conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
```
	* With an ORM:
```bash
engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format("root", "root", "my_db"), pool_pre_ping=True)
Base.metadata.create_all(engine)

session = Session(engine)
for state in session.query(State).order_by(State.id).all(): # HERE: no SQL query, only objects!
    print("{}: {}".format(state.id, state.name))
session.close()
```

Do you see the difference? Cool, right?
