from django.shortcuts import render
from rest_framework import views
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view()
def internal(request):
    return Response("internal")

@api_view()
def external(external):
    return Response("external")

@api_view()
def cached(request):
    return Response("cached")