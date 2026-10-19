from module import dbConfig

def getAll(param = ""):
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        
        cursor.close()
        mydb.close()
        return True
        
    except:
        return False
        
    finally:
        pass


def insertData(visina,teza,itm):
    sql = """
    INSERT INTO dnevnik (datumcas,visina,teza,itm)
    VALUES (now(), {},{},{});
    """.format(visina,teza,itm)
    try:
        mydb = dbConfig.dbConnect()
        cursor = mydb.cursor()
        cursor.execute(sql)
        mydb.commit()
        vrniID = cursor.lastrowid
        return vrniID
    except:
        return -1
    finally:
        cursor.close()
        mydb.close()