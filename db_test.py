import pymysql

#example1:
'''
#打开连接，并指定游标类型为字典类型
connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='gsys',charset='utf8mb4',cursorclass=pymysql.cursors.DictCursor)

try:
    #建立游标
    with connection.cursor() as cursor:
        sql = "select * from dat_reader;";
        #执行sql语句
        cursor.execute(sql);
        #result = cursor.fetchone();
        #获取sql执行结果
        result = cursor.fetchall();
        print(result);
        #因为没有设置默认提交，此处提交执行
        connection.commit();
finally:
    #关闭连接
    connection.close();
'''

#example2：创建数据库表
connection = pymysql.connect(host='127.0.0.1',port=3306,user='root',password='root',db='gsys',charset='utf8mb4'); #,cursorclass=pymysql.cursors.DictCursor

try:
    with connection.cursor() as cursor:

        #数据库表的创建
        '''
        cursor.execute("DROP TABLE IF EXISTS EMPLOYEE;");
        # 使用预处理语句创建表
        sql = """CREATE TABLE EMPLOYEE (
         FIRST_NAME  CHAR(20) NOT NULL,
         LAST_NAME  CHAR(20),
         AGE INT,  
         SEX CHAR(1),
         INCOME FLOAT );""";
        cursor.execute(sql);
        '''

        #数据库表记录的插入
        # SQL 插入语句
        '''
        sql = """INSERT INTO EMPLOYEE(FIRST_NAME,
         LAST_NAME, AGE, SEX, INCOME)
         VALUES ('Mac', 'Mohan', 20, 'M', 2000);"""
        '''
        """
        #使用参数形式
        fn = "Jack";
        ln = "Ma";
        a = 46;
        s = "m";
        i = 100000;'''

        sql = '''insert into employee(first_name,
        last_name,age,sex,income)
        values ("%s","%s",%d,"%s",%d)''';
        
        cursor.execute(sql % (fn,ln,a,s,i));
        #提交到数据库执行
        connection.commit();
        """

        sql = "select first_name,last_name,age,sex,income from employee;";
        cursor.execute(sql);
        len = cursor.rowcount;
        print(len);
        results = cursor.fetchall();
        #查询结果会按字母顺序排序
        for rows in results:
            fn = rows[0];
            ln = rows[1];
            a = rows[2];
            s = rows[3];
            i = rows[4];
            #print("test");
            print("first_name: %s,last_name: %s,age: %d,sex: %s,income: %d" % (fn,ln,a,s,i));
except:
    #如果发生错误，则执行回滚
    connection.rollback();
    print("rollback");
finally:
    connection.close();

