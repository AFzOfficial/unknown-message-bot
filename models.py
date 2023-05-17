import sqlite3

db = 'unknowns.db'

conn = sqlite3.connect(db)

def init() -> None:
    c = conn.cursor()

    c.execute('''
    CREATE TABLE IF NOT EXISTS unknowns (
    
    id               INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    real_id          TEXT NOT NULL,
    unknown_id       TEXT NOT NULL

    )
    ''')


    conn.commit()
    c.close()


init()




def add_unknown(real_id: str, unknown_id: str) -> bool:
    c = conn.cursor()

    try:
        c.execute("INSERT INTO unknowns (real_id, unknown_id) VALUES (?, ?)", (real_id, unknown_id, ))
        conn.commit()

        return True

    except sqlite3.Error as e:
        print(e)
        return None

    finally:
        c.close()





def get_unknown_with_real_id(real_id: str) -> tuple:
    c = conn.cursor()
    try:
        c.execute(f'SELECT real_id, unknown_id FROM unknowns WHERE real_id = ?', (real_id,))
        row = c.fetchone()

        return row
    
    except sqlite3.Error as e:
        print(e)
        return None
    
    finally:
        c.close()



def get_unknown_with_unknown_id(unknown_id: str) -> tuple:
    c = conn.cursor()
    try:
        c.execute(f'SELECT real_id, unknown_id FROM unknowns WHERE unknown_id = ?', (unknown_id,))
        row = c.fetchone()

        return row
    
    except sqlite3.Error as e:
        print(e)
        return None
    
    finally:
        c.close()





def get_all_unknowns() -> list:
    c = conn.cursor()
    try:
        c.execute(f'SELECT id, real_id, unknown_id FROM unknowns ORDER BY id DESC') # LIMIT 100
        rows = c.fetchall()

        return rows
    
    except sqlite3.Error as e:
        print(e)
        return None
    
    finally:
        c.close()





def delete_unknown_with_real_id(real_id: str) -> bool:

    if get_unknown_with_real_id(real_id):

        c = conn.cursor()

        try: 
            # c.execute(f'DELETE FROM donates') # Delete All
            c.execute(f'DELETE FROM unknowns WHERE real_id = ?', (real_id, ))
            conn.commit()

            return True
        
        except sqlite3.Error as e:
            print(e)
            return None
        
        finally:
            c.close()
    
    return None



def update_unknown_id(unknown_id: str, real_id: str) -> bool:

    if get_unknown_with_real_id(real_id):

        c = conn.cursor()

        try: 
            # c.execute(f'DELETE FROM donates') # Delete All
            c.execute(f'UPDATE unknowns SET unknown_id = ? WHERE real_id = ?', (unknown_id, real_id, ))
            conn.commit()

            return True
        
        except sqlite3.Error as e:
            print(e)
            return None
        
        finally:
            c.close()
    
    return None




