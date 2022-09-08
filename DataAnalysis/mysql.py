import pymysql


def mysql(sql, ty=0):
    conn = pymysql.connect(host="localhost",user="root", port=3306, passwd="123456", database="sheji")
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    if ty==1:
        data = cur.fetchall()
        cur.close()
        conn.close()
        return data
    else:
        cur.close()
        conn.close()
        return