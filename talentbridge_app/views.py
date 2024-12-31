from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "user/index.html")


def about(request):
    return render(request, "user/about.html")

def services(request):
    return render(request, "user/services.html")


def faq(request):
    return render(request, "user/faq.html")


def team_details(request):
    return render(request, "user/team_details.html")


def jobs(request):
    return render(request, "user/jobs.html")


def history(request):
    return render(request, "user/history.html")


def project(request):
    return render(request, "user/project.html")


def contact(request):
    return render(request, "user/contact.html")



def blog(request):
    return render(request, "user/blog.html")


def contact(request):
    return render(request, "user/contact.html")


def blog(request):
    return render(request, "user/blog.html")


def blog_details(request):
    return render(request, "user/blog_details.html")

def project_details(request):
    return render(request, "user/project_details.html")