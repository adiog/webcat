# -*- coding: utf-8 -*-

"""
This file is a part of webcat project.
Copyright (c) 2016 Aleksander Gajewski <adiog@brainfuck.pl>.
"""
import json

from django.http import JsonResponse

from theory.Category import Category


def render(http_request):
    print(http_request.body.decode())
    json_request = json.loads(http_request.body.decode('utf-8'))
    try:
        category = Category(objects=json_request['objects'].split(' '), morphisms=json_request['morphisms'].split(' '))
    except RuntimeError:
        return JsonResponse({'status': 'failure'})
    return JsonResponse({'status': 'success', 'render': category.render()})


