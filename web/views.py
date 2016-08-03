# -*- coding: utf-8 -*-

from __future__ import division, print_function, unicode_literals

from korean import hangul
from django.shortcuts import render
from django.views.generic import View
from django.conf import settings


def pull(text):
    exploded = [list(hangul.split_char(c)) if hangul.is_hangul(c) else c for c in text]
    for i in range(len(exploded)):
        if i == 0:
            continue
        a = exploded[i - 1]
        b = exploded[i]
        if type(a) is list and type(b) is list:
            if not a[2] and b[0] != "ㅇ":
                next = b[0]
                if next == "ㅉ":
                    next = "ㅈ"
                elif next == "ㅃ":
                    next = "ㅂ"
                elif next == "ㄸ":
                    next = "ㄷ"
                a[2] = next
                b[0] = "ㅇ"
            elif a[2] == "ㄹ":
                if b[0] == "ㄱ":
                    a[2] = "ㄺ"
                elif b[0] == "ㅁ":
                    a[2] = "ㄻ"
                elif b[0] == "ㅍ":
                    a[2] = "ㄿ"
                b[0] = "ㅇ"
            elif a[2] == "ㄱ" and b[0] == "ㅅ":
                a[2] = "ㄳ"
                b[0] = "ㅇ"
            elif a[2] == "ㄴ" and b[0] == "ㅈ":
                a[2] = "ㄵ"
                b[0] = "ㅇ"
            elif a[2] == "ㅂ" and b[0] == "ㅅ":
                a[2] = "ㅄ"
                b[0] = "ㅇ"
            elif a[2] == "ㄹ":
                if b[0] == "ㅂ":
                    a[2] = "ㄼ"
                elif b[0] == "ㅅ":
                    a[2] = "ㄽ"
                elif b[0] == "ㅌ":
                    a[2] = "ㄾ"
                b[0] = "ㅇ"
    return "".join([hangul.join_char(c) if type(c) is list else c for c in exploded])


def view(request, view_name, **kwargs):
    context = {
        'view': view_name,
        'site': settings.SITE,
    }
    context.update(kwargs)
    return render(request, 'view/{}.html'.format(view_name), context)


class HomeView(View):

    def get(self, request, *args, **kwargs):
        return view(request, 'home')

    def post(self, request, *args, **kwargs):
        content = request.POST.get('content', "")
        len_content = len(content)
        if len_content > 10000:
            return view(request, 'home', content=content, message="10000자 이하 텍스트를 넣어주세요")
        return view(request, 'home', content=content, result=pull(content))
