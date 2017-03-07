from django import template
from django.utils.safestring import mark_safe
register = template.Library()


# @register.filter
# def test_tag(data):
#     return data.upper()
#
#
# @register.simple_tag()
# def test_tag2(data):
#     return mark_safe("<h2> %s </h2>" % (data))


#前台调用评论的子函数，被下面调用，可以与下面的合二为一的
def insert_commnet_node(data_dic, margin_val):
    #这里传进来就是子评论了

    #子评论也开始初始化html
    html = ''

    #这里传进来就是子评论了，一样的也是评论实例，也有属性方法
    for p, v in data_dic.items():
        r = '''<div style="margin-left:%spx">
            <span>%s</span>
            <span>%s</span>
            <span>%s</span>
            </div>''' % (margin_val, p.comments, p.user,p.date)

        #这里如果还有子评论，又开始递归了。。。
        if v is not None:
            ##每个子评论的下一级评论也是加20的缩进
            r += insert_commnet_node(v, margin_val + 20)
        #加到html内容中
        html += r

    #返回子评论一大串
    return html


#后台已经生成了评论树，前台显示函数（前台显示也很复杂）
@register.simple_tag()
def build_comment_tree(tree_data):   #直接传进去后台生成的评论树

    #返回的html内容初始化
    html_ele = ''

    # 把评论树以字典的形式读出来，注意，这里的是评论实例，所以可以调用models（表结构中的属性），如p.date,p.commnets
    for p, v in tree_data.items():

        # 拼凑和html内容
        row = '''<div>
        <h1>%s</h1>
        <h2>%s</h2>
        <h3>%s</h3>
        </div>''' % (p.comments, p.user, p.date)

        #如果还有子评论，就去这个函数添加到底
        if v is not None:

            #这里每个顶级评论与次级评论，水平距离20px，返回时，父评论就带上了子评论

            row += insert_commnet_node(v, 20)

        #所有的评论内容实际 是 每个顶级评论（带着一帮小弟） 加起来。
        html_ele += row

    #返回safe后的html内容
    return mark_safe(html_ele)

