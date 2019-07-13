import sqlite3
import os
# from orm import IntegerField, StringField, Model

# os.makedirs('./', exist_ok=True)
db = r'D:/flask.db'

def select(sql,args,size=None):
    # Select
    global db
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql,args)
            if size is None:
                return cursor.fetchone()
            else:
                return cursor.fetchmany(size)
        except:
            raise
        finally:
            cursor.close()

def execute(sql,args):
    # Insert, Update, Delete
    global db
    with sqlite3.connect(db) as conn:
        cursor = conn.cursor()
        try:
            cursor.execute(sql, args)
            affected = cursor.rowcount
            return affected
        except:
            raise
        finally:
            cursor.close()
