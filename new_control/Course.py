from co_ import Course, session,AssignQ
from sqlalchemy import or_


class Course1():
    def __init__(self):
        self.session = session

    def create_course(CName,CDes,Ccategory, session):
        """
        在Course表中创建新课程记录
        """
        new_course = Course(CName=CName,CDes=CDes,Ccategory=Ccategory)
        session.add(new_course)
        session.commit()
        return new_course.CNumber

    def get_course_num(cnumber, session):
        """
        查询Course表中的课程记录
        """
        course = session.query(Course).filter_by(CNumber=cnumber).first()

        if not course:
            return None

        return course

    def get_all_courses(session):
        """
        查询Course表中的课程记录
        """
        course = session.query(Course).all()

        return course

    def get_course_name(CName, session):
        """
        查询Course表中的课程记录
        """
        search_pattern = f"%{CName}%"
        courses = session.query(Course).filter(or_(Course.CName.like(search_pattern), Course.CNumber.like(search_pattern))).all()

        if not courses:
            return []

        return courses
