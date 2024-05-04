"""
修改AssignQ
"""
from co_ import AssignQ, session, Course

def create_assignq(cname, qtext, category, picturename, session):
    """
    在AssignQ表中为指定课程创建新问题
    """
    # 获取指定课程
    course = session.query(Course).filter_by(CName=cname).first()

    if not course:
        print(f"错误: 课程名称 '{cname}' 不存在!")
        return None

    # 创建新问题
    new_question = AssignQ(course=course, qtext=qtext, category=category, picturename=picturename)
    session.add(new_question)
    session.commit()

    print(f"新问题创建成功, qid: {new_question.qid}")

    return new_question.qid

def update_assignq(qid, aid, qtext, category, picturename, session):
    """
    修改AssignQ表中的问题
    """
    # 查找要修改的问题
    question = session.query(AssignQ).filter_by(qid=qid).first()

    # 如果问题不存在
    if not question:
        print(f"错误: 问题ID {qid} 不存在!")
        return

    # 修改问题属性
    question.aid = aid
    question.qtext = qtext
    question.category = category
    question.picturename = picturename

    session.commit()
    print(f"问题ID {qid} 修改成功!")

def delete_assignq(qid, session):
    """
    删除AssignQ表中的问题
    """
    # 查找要删除的问题
    question = session.query(AssignQ).filter_by(qid=qid).first()

    # 如果问题不存在
    if not question:
        print(f"错误: 问题ID {qid} 不存在!")
        return

    # 删除问题
    session.delete(question)
    session.commit()
    print(f"问题ID {qid} 删除成功!")

def get_assignq(qid, session):
    """
    查询AssignQ表中的问题
    """
    # 查找问题
    question = session.query(AssignQ).filter_by(qid=qid).first()

    # 如果问题不存在
    if not question:
        print(f"错误: 问题ID {qid} 不存在!")
        return None

    return question

if __name__ == "__main__":
    # 创建新问题
    new_qid = create_assignq(100, "这是一个测试问题?", "计算机科学", "test.jpg", session)
    print(f"新问题qid: {new_qid}")

    # 修改问题
    update_assignq(new_qid, 101, "修改后的问题内容", "数学", "new.png", session)

    # 查询问题
    question = get_assignq(new_qid, session)
    print(f"问题信息: {question.aid}, {question.qtext}, {question.category}, {question.picturename}")

    # 删除问题
    delete_assignq(new_qid, session)