import sqlite3
cnt=sqlite3.connect('jeetdb.dp')

# cnt.execute('Create table Information(id integer,name varchar,city varchar)')
# print('table created')

# cnt.execute("""
#             insert into Information Values
#             (1,'jeet','Bhayavadar'),
#             (2,'kush','Vadali'),
#             (3,'Vasu','Rajkot')
#             """)
# print('record inserted successfully')
# cnt.commit()

# cursor=cnt.execute('select * from Information where id<3')
# for i in cursor:
#     print(i)

# sql_upd=""" Update Information set name='chako' where id=3"""
# cnt.execute(sql_upd)
# cursor=cnt.execute('select * from Information')
# for i in cursor:
#     print(i)

sql_del=""" Delete from Information where id=2"""
cnt.execute(sql_del)
cursor=cnt.execute('select * from Information')
for i in cursor:
    print(i)
    
