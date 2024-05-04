import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_email(receivers, subject, content):
    """发送邮件

    Args:
        sender (str): 发件人邮箱地址
        password (str): 发件人邮箱授权码
        receivers (list): 收件人邮箱地址列表
        subject (str): 邮件主题
        content (str): 邮件内容

    Returns:
        bool: 邮件是否发送成功
    """
        # 读取环境变量中的敏感信息 发送邮箱账户和对应授权码
    sender = '2879907402@qq.com'
    password = 'ljwjlubzknpmdgad'
    try:
        # 构造邮件对象
        msg = MIMEText(content, 'plain', 'utf-8')
        msg['From'] = formataddr(['From nicead.top', sender])
        msg['Subject'] = subject

        # 连接邮箱服务器并登录
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, password)

        # 发送邮件
        for receiver in receivers:
            msg['To'] = formataddr(['FK', receiver])
            server.sendmail(sender, [receiver], msg.as_string())

        server.quit()
        return True
    except Exception:
        return False


if __name__ == '__main__':

    # 设置收件人列表和邮件内容
    receivers = ['r130026041@mail.uic.edu.cn','r130026100@mail.uic.edu.cn']
    subject = '验证码'
    content = '验证码为：您是sb'

    # 发送邮件
    if send_email( receivers, subject, content):
        print('邮件发送成功')
    else:
        print('邮件发送失败')
