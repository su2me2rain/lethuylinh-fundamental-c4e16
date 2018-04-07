from models.service import Service
import mlab
import random
from random import randint, choice
from faker import Faker

mlab.connect()

fake = Faker()

images = [
    'http://kenh14cdn.com/zoom/420_264/2017/13-1492264643804-79-0-452-599-crop-1492264873963.png',
    'https://s-media-cache-ak0.pinimg.com/originals/01/e0/0f/01e00f327ae3207f3a52e63795051c33.jpg',
    'https://i.pinimg.com/originals/19/80/38/19803858c32df480d55373508ddc674e.jpg',
    'http://k14.vcmedia.vn/2016/12316599-1674025576202318-4319954128171260713-n-1449513478480-1453796376563.jpg',
    'https://i.pinimg.com/originals/4f/cb/cf/4fcbcfba41b57f38b5d6ad0509644e2e.jpg',
    'https://s-media-cache-ak0.pinimg.com/originals/b3/05/93/b305933a3368991d851fad6a8e7a16cb.jpg',
    'http://blog.sieuthilamdep.com/wp-content/uploads/2016/05/B%E1%BA%ADt-M%C3%AD-Nh%E1%BB%AFng-Ki%E1%BB%83u-T%C3%B3c-D%C3%A0i-Xo%C4%83n-%C4%90%E1%BA%B9p-C%E1%BB%A7a-C%C3%B4-N%C3%A0ng-Xinh-%C4%90%E1%BA%B9p-Chipu-8.jpg',
    'http://img.tinbaihay.net/ThumbImages/01/8chi/8-chieu-lam-dep-xu-han-hot-nhat-hien-nay-efdc_450.jpg',
    'https://i.pinimg.com/originals/4e/0d/c7/4e0dc73dc10c6d49e97f861acec05321.jpg',
    'https://kenh14cdn.com/thumb_w/600/vAlPVSnI3KlTFY5PiLWE2U51feyJY/Image/2015/02/10389297_846275135437005_8550045073008497228_n-1ebec.jpg'
]

descriptions =[
    'Ngoan ngoãn', 'lễ phép', 'thông minh', 'đáng yêu', 'chơi game giỏi', 'hát hay', 'thích chụp ảnh', 'nấu ăn ngon'
]

def random_measure():
    measure = [0,0,0]
    measure[0] = randint(70,100)
    measure[1] = randint(55,90)
    measure[2] = randint(70,110)
    return measure

#create a document
for i in range(20):
    print('running')
    new_service = Service(name = fake.name(),
                            image = choice(images),
                            description = random.sample(set(descriptions), 3),
                            measurement = random_measure(),
                            yob = randint(1995,2000),
                            gender = 0,
                            height = randint(150,180),
                            phone = fake.phone_number(),
                            address = fake.address(),
                            status = choice([True, False]))
    new_service.save()
