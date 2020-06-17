import pymysql
def main():
    conn = pymysql.connect(host='10.10.10.130', port=3306,
                           user='root', password='123456',
                           db='hrs', charset='utf8',cursorclass=pymysql.cursors.DictCursor)

    try:
        with conn.cursor() as cur:
            cur.execute('select dno,dname,dloc from tb_dept')
            #print(cur.fetchall())
            '''
            注意以下的区别，cur是游标类型，取过一次，向下移动
            cur.fetchone()
            cur.fetchmany(2)
            cur.fetchall()
            默认的游标类型在conn初始化中：cursorclass=Cursor，默认是元组类型，
            可以修改为字典类型，便于按字段名提取
            
            '''
            '''
            for row in cur.fetchall():
                print(f'部门编号：{row[0]}')
                print(f'部门地点：{row[1]}')
                print(f'部门名称：{row[2]}')            
            '''
            for row in cur.fetchall():
                print(row['dno'])
                print(row['dname'])
                print(row['dloc'])


    except pymysql.MySQLError as err:
        print(err)
    finally:
        conn.close()


if __name__ == '__main__':
    main()