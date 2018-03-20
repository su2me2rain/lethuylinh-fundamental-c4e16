from pymongo import MongoClient

mongo_uri = 'mongodb://admin:admin@ds021182.mlab.com:21182/c4e'

#1. connect to database
client = MongoClient(mongo_uri)

#2. get database
db = client.get_default_database()

#3. Create a new document
html_content = """
Mượn lời dành tặng các bạn đồng môn C4E 16...
Ta không muốn những ngày trẻ, trở nên gầy gò xanh xao
Ta muốn là cánh chim nhỏ, giữa bầu trời trong xanh chao
Trong mắt của rất nhiều người ta rất điên và rất ương bướng
Lấy đam mê làm ánh mặt trời, để tâm hồn này không mất phương hướng
Ta đi theo bóng mặt trời, từ hạ tới hay đông về qua
Khi những đam mê, còn nồng cháy, thì con đường đó sẽ không hề xa.
"""
new_post = {
'title':'Đi theo bóng mặt trời',
'author':'Linh Thùy',
'Content':html_content
}

#4. Insert document into collection
db.posts.insert_one(new_post)
