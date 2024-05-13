from co_ import HelpTopic, session
def create_helptopic(title, topicq, topica, cnumber, session):
    """
    在 HelpTopic 表中创建新帮助主题
    """
    new_topic = HelpTopic(title=title, topicq=topicq, topica=topica, CNumber=cnumber)  # 添加 CNumber
    session.add(new_topic)
    session.commit()
    print(f"新帮助主题创建成功, topic_id: {new_topic.topic_id}")
    return new_topic.topic_id


def get_helptopic(topic_id, session):
    """
    查询HelpTopic表中的帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return None
    return topic

def update_helptopic(topic_id, title, topicq, topica, session):
    """
    更新HelpTopic表中的帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return

    topic.title = title
    topic.topicq = topicq
    topic.topica = topica

    session.commit()
    print(f"主题ID {topic_id} 更新成功!")

def delete_helptopic(topic_id, session):
    """
    从HelpTopic表中删除帮助主题
    """
    topic = session.query(HelpTopic).filter_by(topic_id=topic_id).first()
    if not topic:
        print(f"错误: 主题ID {topic_id} 不存在!")
        return

    session.delete(topic)
    session.commit()
    print(f"主题ID {topic_id} 删除成功!")


def get_all_helptopics(session):
    return session.query(HelpTopic).all()


