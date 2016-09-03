#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""SqlAlchemy example"""

import sqlite3

# conn = sqlite3.connect(":memory:")
conn = sqlite3.connect('tutorial5.db')
cursor = conn.cursor()

cursor.execute(
    "create table if not exists x (a integer, b integer, PRIMARY KEY (a))")

for i in range(1000000):
    cursor.execute("insert into x (a, b) values ({0}, {0})".format(i))


# cursor.execute('select * from x limit 1000, 10;')

# for row in cursor:
#     print(row)

# cursor.close()
# conn.close()
