import pymysql
db = pymysql.connect("localhost", "root", "admin", "test1")#admin为自己数据库密码，test1为自己cmd中创建的数据库名
cursor = db.cursor()
cursor.execute("drop table if exists fin;") #如果存在fin表时候先删除
sql = '''create table fin
	(
		id int unsigned not null auto_increment primary key,
		姓名 char(100) not null,
		性别 char(4) not null,
		年龄 tinyint unsigned not null,
		电话 char(13) null default "-"
	);'''
cursor.execute(sql)
name = '李白'
sex = '男'
age = '20'
tel = '123456789'
sql = "insert into fin (姓名,性别,年龄,电话) values ('%s','%s','%s','%s');" % (name, sex, age, tel)
cursor.execute(sql)
#为了遵循mysql语法也可以用以下两句字符串拼接
#sql = 'insert into fin  (姓名,性别,年龄,电话) values (\"'+name+'\",\"'+sex+'\",\"'+age+'\",\"'+tel+'\");'
#cursor.execute(sql)
db.commit()
db.close()
