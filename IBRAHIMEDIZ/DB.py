import sqlite3 as sql

class VetDB():
    def __init__(self):
        self.db = sql.connect(r"DB\VETOTO.db")
        self.cur = self.db.cursor()

    def eyaletGetir(self):
        sorgu = """
        SELECT EYALET_ID,ID
            FROM ST_EYALET 
        WHERE ST_EYALET.EYALET_ID LIKE 'C%' OR 
            ST_EYALET.EYALET_ID LIKE 'N%'
            """
        return self.cur.execute(sorgu).fetchall()
    
    def SecilieyaletGetir(self,ID):
        sorgu = """
                       SELECT EYALET_ADI,ID
                
                FROM eyalet_alt
                WHERE EYID = {}
            """.format(ID)
        return self.cur.execute(sorgu).fetchall()




    def __del__(self):
        self.cur.close()
        self.db.close()

