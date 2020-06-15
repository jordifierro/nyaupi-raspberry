from tinydb import TinyDB

def table():
    return TinyDB('db.json').table('status')

def status():
    return table().all()[0]

def initialize_db():
    table().purge()
    table().insert({'door_open': False, 'alarm_active': False})

def is_door_open():
    return status()['door_open']

def is_alarm_active():
    return status()['alarm_active']

def set_door_open(is_open):
    table().update({'door_open': is_open})

def set_alarm_active(is_active):
    table().update({'alarm_active': is_active})

if __name__ == '__main__':
    if len(table().all()) == 0:
        print('Initializing database...')
        initialize_db()
    print(status())
