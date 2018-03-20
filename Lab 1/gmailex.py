from gmail import GMail, Message
from random import choice

gmail = GMail('linhltt3131990@gmail.com','31/3/1990')

reasons = ['ốm','đau bụng','chán đời','buồn ngủ']
html_content = """
<p>Dear Tuấn Anh,</p>
<p>H&ocirc;m nay l&agrave; ng&agrave;y 18/3 v&igrave; {{reason}} n&ecirc;n chị xin ph&eacute;p được nghỉ học. Mong em đồng &yacute;.&nbsp;</p>
<p><span style="color: #800080; background-color: #cc99ff;"><strong><em>P/S: Nếu kh&ocirc;ng đồng &yacute; cũng chịu th&ocirc;i. Tặng em b&agrave;i h&aacute;t: <a href="https://www.youtube.com/watch?v=CJJJ8Vyv3ZA" style="color: #800080; background-color: #cc99ff;">link</a></em></strong></span></p>
<p>Chị Linh!</p>
"""
word = choice(reasons)
html_content_new = html_content.replace('{{reason}}',word)

#placeholder
msg = Message('Đơn xin nghỉ học', to='techkidsc4e16@gmail.com',html=html_content_new)
gmail.send(msg)
