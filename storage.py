import sqlite3

def connection():
    return sqlite3.connect('nyaupi.db')

def status_table_exists():
    c = connection()
    cursor = c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='STATUS' ''')
    exists = (cursor.fetchone()[0] == 1)
    c.commit()
    c.close()
    return exists

def initialize_db():
    c = connection()
    c.execute('''CREATE TABLE STATUS
         (ID INT PRIMARY KEY     NOT NULL,
         ALARM_ACTIVE    INT     NOT NULL,
         DOOR_OPEN       INT     NOT NULL);''')
    c.execute("INSERT INTO STATUS (ID,ALARM_ACTIVE,DOOR_OPEN) VALUES (1, 0, 0)");
    c.commit()
    c.close()

def status():
    c = connection()
    cursor = c.execute("SELECT ID, ALARM_ACTIVE, DOOR_OPEN from STATUS where ID = 1")
    element = cursor.fetchone()
    result = {"alarm_active": bool(element[1]), "door_open": bool(element[2])}
    c.close()
    return result

def is_door_open():
    return status()['door_open']

def is_alarm_active():
    return status()['alarm_active']

def set_door_open(is_open):
    c = connection()
    c.execute("UPDATE STATUS set DOOR_OPEN = {} where ID = 1".format(int(is_open)))
    c.commit()
    c.close()

def set_alarm_active(is_active):
    c = connection()
    c.execute("UPDATE STATUS set ALARM_ACTIVE = {} where ID = 1".format(int(is_active)))
    c.commit()
    c.close()

if __name__ == '__main__':
    if not status_table_exists():
        print('Initializing database...')
        initialize_db()
    print(status())
