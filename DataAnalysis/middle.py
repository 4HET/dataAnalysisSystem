from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect, render


class MyMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # if request.path == '/data_list' or request.path == '/data_preview':
        #     user_id = request.session.get("user_id")
        #     if user_id:
        #         return
        #     else :
        #         return redirect("/")
        return
        