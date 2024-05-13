import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.utils import formataddr

def send_email_with_image(receivers, subject, content, image_path):
    """发送包含图片的邮件

    Args:
        receivers (list): 收件人邮箱地址列表
        subject (str): 邮件主题
        content (str): 邮件内容
        image_path (str): 图片路径

    Returns:
        bool: 邮件是否发送成功
    """
    sender = '2879907402@qq.com'
    password = 'wyectrxugvevdeca'
    try:
        # 创建一个MIMEMultipart对象，代表整个邮件
        msg = MIMEMultipart()
        msg['From'] = formataddr(['From nicead.top', sender])
        msg['Subject'] = subject

        # 添加文本内容
        msg.attach(MIMEText(content, 'plain', 'utf-8'))

        # 添加图片附件
        with open(image_path, 'rb') as f:
            mime = MIMEImage(f.read())
            mime.add_header('Content-Disposition', 'attachment', filename=image_path)
            msg.attach(mime)

        # 连接邮箱服务器并登录
        server = smtplib.SMTP_SSL('smtp.qq.com', 465)
        server.login(sender, password)

        # 发送邮件
        for receiver in receivers:
            msg['To'] = formataddr(['FK', receiver])
            server.sendmail(sender, [receiver], msg.as_string())

        server.quit()
        return True
    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    receivers = ['r130026041@mail.uic.edu.cn']
    subject = '色色'
    content = '请看'
    image_path = 'C:\\Users\\1\\Pictures\\Camera Roll\\7.png'  # 图片文件路径

    if send_email_with_image(receivers, subject, content, image_path):
        print('邮件发送成功')
    else:
        print('邮件发送失败')
