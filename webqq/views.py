from django.shortcuts import render, HttpResponse
from webqq import models, utils
import json, datetime
# Create your views here.


# 全局字典，检测是否有数据，这个用来应对不同进程的queue保存的数据不一样。
global_msg_dic = {}


def dashboard(request):

    # print(models.QQGroup.name)

    #单独建立一个 templates webqq项目,里面放置对应的 webqq的html内容
    return render(request, 'webqq/dashboard.html')


def send_msg(request):
    print("okoko")
    print(request.POST)
    data = request.POST.get("data")
    print(json.loads(data))

    #序列化python能认识的字典
    data = json.loads(data)

    # #给数据打上时间戳
    data['date'] = datetime.datetime.now().strftime("%Y%m%d %H%M%S")

    #数据从前端取出
    to_id = data.get('to_id')
    contact_type = data.get('contact_type')
    user_obj = models.bbs_models.UserProfile.objects.get(id=to_id)

    #如果给单个人发消息
    if contact_type == 'single':

    ##开始调用关于消息的类，多用这种，面向对象
        if not to_id in global_msg_dic:
            global_msg_dic[to_id] = utils.Chat()

        global_msg_dic[to_id].msg_queue.put(data)

        print("Push msg [%s] into user [%s] queue" % (data['msg'], user_obj))


    return HttpResponse("ddddddddddddddddd")


#把后台收到的消息扔
def get_msg(request):
    uid = request.GET.get('uid')
    if uid:
        res = []

        #没有就创建一个
        if not uid in global_msg_dic:
            global_msg_dic[uid] = utils.Chat()


        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided!"))