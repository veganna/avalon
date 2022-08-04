from django.http import JsonResponse
from django.shortcuts import render
from django.views import View
from .models import *
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.core.paginator import Paginator
from Blog.models import Post
# Create your views here.

class galleryView(View):
    def get(self,request):
        serve = nftItem.objects.all().order_by('?')[0:10]
        context ={
            "session": request.session,
            "objects": serve
        }

        returner = render(request, 'mainsite/gallery.html', context)
        returner['Content-Security-Policy'] = "frame-ancestors 'self' "
        return returner

carouselDefault = 6
class carouselView(View):
    def get(self,request):
        serve = nftItem.objects.all().order_by('-id')

        page = Paginator(serve, carouselDefault)
        page_number = request.GET.get('page')
        serve = page.get_page(1)



        context ={
            "session": request.session,
            "objects": serve
        }

        returner = render(request, 'mainsite/carousel.html', context)
        returner['Content-Security-Policy'] = "frame-ancestors 'self' "
        return returner
    def post(self,request):
        serve = nftItem.objects.all().order_by('-id')
        response = request.POST

        page = Paginator(serve, carouselDefault)
        page_number = response['page']
        serve = page.get_page(page_number)


        context ={
            "session": request.session,
            "objects": serve
        }

        returner = render(request, 'mainsite/carousel.html', context)
        returner['Content-Security-Policy'] = "frame-ancestors 'self' "
        return returner       



class collectionItemView(View):
    def get(self,request, id):
        serve = nftItem.objects.all().order_by('-id')

        page = Paginator(serve, carouselDefault)
        page_number = request.GET.get('page')
        serve = page.get_page(1)
        context ={
            "session": request.session,
            "object": nftItem.objects.filter(id = id)[0],
            "serve":serve
        }
        return render(request, 'mainsite/collectionItem.html', context)    

class collectionView(View):
    def get(self,request):

        context ={
            "session": request.session,
            "objects":nftItem.objects.all().order_by('-id')
        }
        return render(request, 'mainsite/collection.html', context)

class indexView(View):
    def get(self,request):
        posts = Post.objects.all().order_by('-id')[0:2]


        serve = nftItem.objects.all().order_by('-id')

        page = Paginator(serve, carouselDefault)
        page_number = request.GET.get('page')
        serve = page.get_page(1)

        context ={
            "session": request.session,
            "Posts":posts,
            "objects":roadMapModel.objects.all().order_by('id'),
            "gallery":nftItem.objects.all().order_by('?')[0:10],
            "Team": nftTeam.objects.all().order_by('id'),
            "serve":serve
        }
        returner = render(request, 'mainsite/index.html', context)
        returner['Content-Security-Policy'] = "frame-ancestors 'self' "
        return returner

class termsView(View):
    def get(self, request):
        context = {
            "session": request.session
        }
        return render(request,'mainsite/terms.html', context)

class policyView(View):
    def get(self, request):
        context = {
            "session": request.session
        }
        return render(request,'mainsite/policy.html', context)


class aboutView(View):
    def get(self,request):
        context ={
            "session": request.session,
        }
        return render(request, 'mainsite/about.html', context)

class roadMapView(View):
    def get(self,request):
        context ={
            "session": request.session,
            "objects":roadMapModel.objects.all()
        }
        return render(request, 'mainsite/roadmap.html', context)

class faqView(View):
    def get(self,request):

        context ={
            "session": request.session,
            "objects":faqCategories.objects.all()
        }
        return render(request, 'mainsite/faq.html', context)

class contactView(View):
    def get(self,request):
        
        context ={
            "session": request.session,
            "subjects":contactSubjects.objects.all()
        }
        return render(request, 'mainsite/contact.html', context)

    def post(self, request):
        code= 500
        message= 'Something went wrong!'

        answ = request.POST

        try:
            if answ['key'] == 'submit':
                if answ['fullName'] == '':
                    code = -1
                    message = 'Type your name.'
                    raise
                if answ['email'] == '':
                    code = -2
                    message = 'Type your email.'
                    raise
                if answ['subject'] == '0':
                    code = -3
                    message = 'Select a subject'
                    raise
                if answ['message'] == '':
                    code = -4
                    message = 'Type your message'
                    raise
                try:
                    validate_email(answ['email'])
                except:
                    code = -2
                    message = 'Invalid Email.'
                    raise
                subject = contactSubjects.objects.filter(id = int(answ['subject']))[0]
                contactMessages(
                    nameField = answ['fullName'][0:255],
                    mailField = answ['email'][0:255],
                    subjectField = subject,
                    messageField = answ['message']
                ).save()
                code = 1
                message = "Thank-you! We will contact you soon!"

        except:
            pass
        print(code)
        print(message)
        return JsonResponse({
            "code": code,
            "message": message
        })