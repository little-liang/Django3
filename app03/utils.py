from app03 import models
from Django3 import settings
class ArticleGen(object):
    def __init__(self, request):
        self.request = request

    def parse_data(self):
        form_data = {
            'title': self.request.POST.get('title'),
            'content': self.request.POST.get('content'),
            'category_id': 1,  #为什么必须用category_id 其他就不行，看下面，这里就是从前端的name="summary"，拿到数据而已
            'summary': self.request.POST.get('summary'),
            'author_id': self.request.user.userprofile.id,
            'head_img': '',
        }
        return form_data


    def create(self):
        self.data = self.parse_data()
        bbs_obj = models.Article(**self.data)  ##这里是上面用其他的字典key传不进来的原因，用Article类只能用Article
        #自己带的key（外键表可以有外键表属性，回去测测）
        bbs_obj.save()

        filename = handle_upload_file(self.request, self.request.FILES['head_img'])
        bbs_obj.head_img = "imgs/upload/%s" % (filename)
        bbs_obj.save()
        return bbs_obj


    def update(self):
        pass


def handle_upload_file(request, file_obj):
    upload_dir = '%s/%s' % (settings.BASE_DIR, settings.FileUploadDir)
    #if not os.path.isdir(upload_dir):
    #    os.mkdir(upload_dir)
    print('-->', file_obj)

    with open('%s/%s' % (upload_dir, file_obj.name), 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)


    return file_obj.name