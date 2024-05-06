from co_ import Course, session
from sqlalchemy import or_
def create_course(CName,CDes,Ccategory, session):
    """
    在Course表中创建新课程记录
    """
    new_course = Course(CName=CName,CDes=CDes,Ccategory=Ccategory)
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

def get_course_num(cnumber, session):
    """
    查询Course表中的课程记录
    """
    course = session.query(Course).filter_by(CNumber=cnumber).first()

    if not course:
        print(f"错误: 课程记录ID {cnumber} 不存在!")
        return None

    return course

def get_course_name(CName, session):
    """
    查询Course表中的课程记录
    """
    search_pattern = f"%{CName}%"
    courses = session.query(Course).filter(or_(Course.CName.like(search_pattern), Course.CNumber.like(search_pattern))).all()

    if not courses:
        print(f"错误: 没有找到与 '{CName}' 相关的课程记录!")
        return []

    return courses
if __name__ == "__main__":
    # 创建新课程记录
    new_cnumber = create_course(1, "计算机导论", "cs101", session)
    print(f"新课程记录cnumber: {new_cnumber}")

    # 修改课程记录
    update_course(new_cnumber, 2, "数据结构", "cs201", session)

    # # 查询课程记录
    # course = get_course(new_cnumber, session)
    # print(f"课程信息: {course.Help_id}, {course.CName}, {course.qid}")

    # 删除课程记录
    delete_course(new_cnumber, session)