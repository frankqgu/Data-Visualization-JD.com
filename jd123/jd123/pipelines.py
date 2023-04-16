import pymysql

def dbHandle():
    conn = pymysql.connect(
        host = "localhost",
        user = "root",
        passwd = "toxicreaperz",
        charset = "utf8",
        use_unicode = False
    )
    return conn

class Jd123Pipeline(object):
    #填入你的地址
    def process_item(self, item, spider):
        dbObject = dbHandle()
        cursor = dbObject.cursor()
        cursor.execute("USE spider")
        #插入数据库
        sql = "INSERT INTO jd(用户名,评论,星级,评论时间) VALUES (%s,%s,%s,%s)"
        try:
            cursor.execute(sql,
                           (item['nickname'], item['content'], item['score'],item['time']))
            cursor.connection.commit()
        except BaseException as e:
            print("错误在这里>>>>>>>>>>>>>", e, "<<<<<<<<<<<<<错误在这里")
            dbObject.rollback()
        return item


