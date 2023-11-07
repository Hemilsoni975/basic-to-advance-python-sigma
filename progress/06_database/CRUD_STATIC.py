import psycopg2
import psycopg2.extras

hostname = 'localhost'  # hostname of postgres
port_id = 5432  # port of postgres
database = 'testdb'  # database name
username = 'postgres'  # username of postgres
pwd = 'admin123'  # password of postgres

conn = None
cur = None

try:
    conn = psycopg2.connect(
        host=hostname,
        dbname=database,
        port=port_id,
        user=username,
        password=pwd)

    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)

    # deleting the table if exist in the database

    cur.execute('DROP TABLE IF EXISTS emp')

    #  creating a table

    create_script = """ CREATE TABLE IF NOT EXISTS emp(
                        e_id int4 primary key,
                        e_name varchar(50),
                        salary int8,
                        dept_id varchar(30))"""
    cur.execute(create_script)

    # inserting the data in table

    insert_script = 'INSERT INTO emp(e_id, e_name, salary, dept_id) VALUES (%s,%s,%s,%s)'
    insert_values = [(101, 'hemil', 55000, 'D1'), (102, 'mit', 100000, 'D2'), (103, 'umang', 50000, 'D3')]
    for record in insert_values:
        cur.execute(insert_script, record)

    # updating the values of table

    update_script = 'UPDATE emp SET salary = salary + (salary * 0.5)'
    cur.execute(update_script)

    # deleting the value from table

    delete_script = 'DELETE from emp where e_name = %s '
    delete_record = ('umang',)
    cur.execute(delete_script, delete_record)

    # fetching all the datas from emp table

    cur.execute('SELECT * from emp')
    for record in cur.fetchall():
        print(record)
        print(record['e_name'], record['salary'])

    conn.commit()  # this is the main function as it stores all values of database.

except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
