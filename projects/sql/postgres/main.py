import psycopg2, os
conn = psycopg2.connect(host=os.getenv("PGHOST","localhost"),user=os.getenv("PGUSER","app"),
    password=os.getenv("PGPASSWORD","app"),dbname=os.getenv("PGDATABASE","appdb"),port=int(os.getenv("PGPORT","5432")))
cur = conn.cursor()
cur.execute("create table if not exists greetings(id serial primary key, msg text)")
cur.execute("insert into greetings(msg) values ('hello postgres')")
conn.commit()
cur.execute("select count(*) from greetings"); print("greetings rows:", cur.fetchone()[0])
cur.close(); conn.close()
