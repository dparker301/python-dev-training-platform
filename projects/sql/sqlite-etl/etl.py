import sqlite3, csv, argparse, pathlib
DB = pathlib.Path(__file__).with_suffix('.db')
def get_conn(): return sqlite3.connect(DB)
def load_csv(path):
    with open(path) as f, get_conn() as conn:
        rdr = csv.DictReader(f); rows = list(rdr)
        conn.execute("drop table if exists employees")
        conn.execute("create table employees(id int, name text, department text, salary int)")
        conn.executemany("insert into employees values (:id,:name,:department,:salary)", rows)
        conn.commit(); print(f"Loaded {len(rows)} rows into {DB.name}")
def run_query(sql):
    with get_conn() as conn:
        cur = conn.execute(sql)
        for row in cur.fetchall(): print(row)
def export_csv(out_path, sql):
    with get_conn() as conn, open(out_path, 'w', newline='') as f:
        cur = conn.execute(sql); cols=[d[0] for d in cur.description]
        w=csv.writer(f); w.writerow(cols)
        for r in cur.fetchall(): w.writerow(r)
    print(f"Wrote results to {out_path}")
if __name__=="__main__":
    ap=argparse.ArgumentParser(); sub=ap.add_subparsers(dest="cmd")
    l=sub.add_parser("load"); l.add_argument("path")
    q=sub.add_parser("query"); q.add_argument("sql")
    e=sub.add_parser("export"); e.add_argument("out"); e.add_argument("sql")
    a=ap.parse_args()
    if a.cmd=="load": load_csv(a.path)
    elif a.cmd=="query": run_query(a.sql)
    elif a.cmd=="export": export_csv(a.out, a.sql)
    else: ap.print_help()
