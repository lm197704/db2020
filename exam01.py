import pymysql
def main():
    conn=pymysql.connect(host='10.10.10.130',port=3306,
                         user='root',password='123456',
                         db='hrs',charset='utf8'
                         )
    print(conn)
    try:
        with conn.cursor() as cur:
            #插入数据
            #res=cur.execute('insert into tb_dept(dloc,dname) values("上海","bufneer")')

            #删除数据
            #loc=input('输入一个地方：')
            #res=cur.execute('delete from tb_dept where dloc=%s',(loc,))

            #更新数据
            dno=int(input('输入本门编号：'))
            dname=input('输入部门名称')

            res=cur.execute('update tb_dept set dname=%s,dloc=%s where dno=%s',(dname,'上海',dno))

            if res==1:
                print('成功！')
            conn.commit()
    except pymysql.MySQLError as err:
        print(err)
        conn.rollback()
    finally:
        conn.close()


if __name__ == '__main__':
    main()