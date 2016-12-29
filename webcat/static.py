from django.shortcuts import render_to_response


def index(http_request):
    return render_to_response('index.html')
