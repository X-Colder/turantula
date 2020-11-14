# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session

engine = create_engine(
    "mysql+pymysql://root:dreamer2012@localhost:3306/turantula?charset=utf8",
    max_overflow=0,  # 超过连接池大小外最多创建的连接
    pool_size=5,  # 连接池大小
    pool_timeout=30,  # 池中没有线程最多等待的时间，否则报错
    pool_recycle=-1  # 多久之后对线程池中的线程进行一次连接的回收（重置）
)

SessionFactory = sessionmaker(bind=engine)
session = scoped_session(SessionFactory)


class TurantulaPipeline:
    def process_item(self, item, spider):
        return item



class TurantulaMysqlPipeline:
    def process_item(self, item, spider):
        sql = 'INSERT INTO fundinfo(fund_company_id, fund_company_name) VALUES("%s", "%s")' % (item['fund_company_id'], item['fund_company_name'])
        cursor = session.execute(sql)
        session.commit()
        session.remove()
        print(cursor.lastrowid)
