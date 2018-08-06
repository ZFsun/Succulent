from django import template

from django.utils.html import format_html

# 注册到django的语法库
register = template.Library()


@register.simple_tag
def guess_page(current_page, loop_num):
    offset = abs(int(current_page) - int(loop_num))
    # 如果绝对值
    if offset < 2:
        if current_page == loop_num:
            page_ele = '''
                <li class="active"><a href="/hybapp/hybinfolist/%s">%s<span class="sr-only">(current)</span></a></li>
                ''' % (loop_num, loop_num)
        else:
            page_ele = '''
                <li class=""><a href="/hybapp/hybinfolist/%s">%s<span class="sr-only">(current)</span></a></li>
                ''' % (loop_num, loop_num)
        return format_html(page_ele)
    else:
        return ''