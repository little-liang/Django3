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
        bbs_obj.head_img = "static/imgs/upload/%s" % (filename)
        print("图片路径为", bbs_obj.head_img)
        bbs_obj.save()
        return bbs_obj


    def update(self):
        pass


def handle_upload_file(request, file_obj):
    upload_dir = '%s/%s' % (settings.BASE_DIR, settings.FileUploadDir)
    #if not os.path.isdir(upload_dir):
    #    os.mkdir(upload_dir)


    with open('%s/%s' % (upload_dir, file_obj.name), 'wb') as destination:
        for chunk in file_obj.chunks():
            destination.write(chunk)

    print('上传的图片路径', '-->', upload_dir)
    return file_obj.name


##查询父评论树的子评论逻辑处理，递归思想
def recursive_search(data_dic, comment):

    ##把父评论字典循环，这里就会把评论的key拿出来。
    for parent, v in data_dic.items():

        ##如果传进去的  子评论的父亲属性（自己认为的父评论）     是  父评论字典的 父评论
        # print(parent)
        if parent == comment.parent_comment:



            #在这个父评论建一个新的子字典，字典的key就是子评论
            data_dic[parent][comment] = {}
            # print("find parent of [%s],done!" % (comment))

            #找到了就不用往下走了，直接本次查找退出
            break

        else:
            # print("can't find  [%s]'s parent,going to 下一级" % (comment))

            #如果这个子评论的属性（父评论）与目前的父评论不等

            #这里开始了递归,把整个评论树少一级放进去（半成品，但是评论的父评论一定有，不然子评论没办法创建）
            recursive_search(data_dic[parent], comment)


##查询评论数方法，其实就是 把 所有评论弄成一个字典，父评论与子评论就是 通过key连接，是key，是的，没错
def build_comments_tree(request):
    ##把某一个文章找出来，这里固定死了，第一个文章（这样做只是测试）
    bbs_obj = models.Article.objects.first()

    #评论树的字典
    tree_dic = {}

    ##查询开始！！！把某一个文章的所有评论查出来，循环每一个评论，找出所有评论的子评论
    for comment in bbs_obj.comment_set.select_related():
        # print("目前正在找。。。。", comment)
        ##如果该评论没有父评论，就建立一个父评论，顶级key，如文章《你好》 顶级评论，A{}，B{}
        if not comment.parent_comment:
            tree_dic[comment] = {}

        else:
            ##如果该评论有父评论，开始找他的父评论，这里逻辑是，把顶级父评论A{}和本次评论（大多数为子评论）传进去，出来就是评论树（A { A1 {A-1}, A2}）
            recursive_search(tree_dic, comment)


    # print("最后", tree_dic)
    # for k, v in tree_dic.items():
    #     print(k, "--->", v)

    return tree_dic