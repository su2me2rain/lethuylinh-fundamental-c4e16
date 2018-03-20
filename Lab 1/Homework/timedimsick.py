from gmail import GMail, Message
from random import choice
import datetime

gmail = GMail('linhltt3131990@gmail.com','31/3/1990')

reasons = ['đi công tác','ốm nặng','đau bụng','chán đời','buồn ngủ']
html_content = """
<p>Dear Tuấn Anh &amp; Qu&yacute;,</p>
<p>Chị xin ph&eacute;p nghỉ buổi học sắp tới v&igrave; {{reason}}. Chị sẽ nghe lại b&agrave;i giảng v&agrave; l&agrave;m b&agrave;i tập đầy đủ.&nbsp;</p>
<p>Cảm ơn em,</p>
<p>Chị Linh!</p>
<p><em><strong>P/S:</strong> Đi học C4E rất vui ^^ Nếu kh&ocirc;ng v&igrave; bận kh&ocirc;ng sắp xếp được th&igrave; chắc chắn chị sẽ kh&ocirc;ng nghỉ đ&acirc;u&nbsp;<img src="http://htmleditor.tools/tinymce465/plugins/emoticons/img/smiley-laughing.gif" alt="laughing" /></em></p>
"""

word = choice(reasons)
html_content_new = html_content.replace('{{reason}}',word)

#send
while True:
    t = datetime.datetime.now().strftime('%I %p')
    if t == '07 AM':
        msg = Message('Đơn xin nghỉ học', to='techkidsc4e16@gmail.com',html=html_content_new)
        gmail.send(msg)
        break
