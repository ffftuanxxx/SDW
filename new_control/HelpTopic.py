from co_ import HelpTopic, session

class helpTopic2():
    def create_helptopic(title, topicq, topica, cnumber,session):
        """
        在 HelpTopic 表中创建新帮助主题
        """
        new_topic = HelpTopic(title=title, topicq=topicq, topica=topica, CNumber=cnumber)  # 添加 CNumber
        session.add(new_topic)
        session.commit()
        return new_topic.topic_id

    def get_all_helptopics(session):
        return session.query(HelpTopic).all()


