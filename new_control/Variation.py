from co_ import Variation,session


def create_variation(vtext, session):
    """
    在Variation表中创建新记录
    """
    new_variation = Variation(vtext=vtext)
    session.add(new_variation)
    session.commit()
    print(f"新变体记录创建成功, vcode: {new_variation.vcode}")
    return new_variation.vcode


def update_variation(vcode, vtext, session):
    """
    更新Variation表中的记录
    """
    variation = session.query(Variation).filter_by(vcode=vcode).first()
    if not variation:
        print(f"错误: 变体ID {vcode} 不存在!")
        return

    variation.vtext = vtext
    session.commit()
    print(f"变体ID {vcode} 更新成功!")


def get_all_variations(session):
    return session.query(Variation).all()

