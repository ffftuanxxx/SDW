# 导入必要的库
from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session

# 创建一个Engine实例
engine = create_engine('mysql+pymysql://llm:2501004@47.109.73.150:3306/llm')

# 创建MetaData实例
metadata = MetaData()

# 反射数据库中的表
metadata.reflect(bind=engine)

# 使用automap基类
Base = automap_base(metadata=metadata)

# 使用反射的元数据加载所有表的信息
Base.prepare()

# connect to tables
User = Base.classes.User
AssignQ = Base.classes.AssignQ
Course = Base.classes.Course
HelpTopic = Base.classes.HelpTopic
LLM = Base.classes.LLM
Request = Base.classes.Request
Variation = Base.classes.Variation

# 创建session
session = Session(engine)
#
# # 使用模型进行查询
# users = session.query(User).all()
# for user in users:
#     print(user.email)  # 假设'user'表有一个'name'字段