from co_ import Course, session
def create_course(help_id, cname, qid, session):
    """
    在Course表中创建新课程记录
    """
    new_course = Course(Help_id=help_id, CName=cname, qid=qid)
    session.add(new_course)
    session.commit()
    print(f"新课程记录创建成功, cnumber: {new_course.CNumber}")
    return new_course.CNumber

def update_course(cnumber, help_id, cname, qid, session):
    """
    修改Course表中的课程记录
    """
    course = session.query(Course).filter_by(CNumber=cnumber).first()

    if not course:
        print(f"错误: 课程记录ID {cnumber} 不存在!")
        return

    course.Help_id = help_id
    course.CName = cname
    course.qid = qid

    session.commit()
    print(f"课程记录ID {cnumber} 修改成功!")

def delete_course(cnumber, session):
    """
    删除Course表中的课程记录
    """
    course = session.query(Course).filter_by(CNumber=cnumber).first()

    if not course:
        print(f"错误: 课程记录ID {cnumber} 不存在!")
        return

    session.delete(course)
    session.commit()
    print(f"课程记录ID {cnumber} 删除成功!")

def get_course(cnumber, session):
    """
    查询Course表中的课程记录
    """
    course = session.query(Course).filter_by(CNumber=cnumber).first()

    if not course:
        print(f"错误: 课程记录ID {cnumber} 不存在!")
        return None

    return course

def get_all_courses(session):
    return session.query(Course).all()

if __name__ == "__main__":
    # 创建新课程记录
    new_cnumber = create_course(1, "计算机导论", "cs101", session)
    print(f"新课程记录cnumber: {new_cnumber}")

    # 修改课程记录
    update_course(new_cnumber, 2, "数据结构", "cs201", session)

    # 查询课程记录
    course = get_course(new_cnumber, session)
    print(f"课程信息: {course.Help_id}, {course.CName}, {course.qid}")

    # 删除课程记录
    delete_course(new_cnumber, session)