from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Myboard

def index(request):
    myboard_all = Myboard.objects.all().order_by('-id') # select * from Myboard
    print(myboard_all)
    return render(request, 'index.html', {'list': myboard_all})

def detail(request, idn):
    return render(request, 'detail.html', {'dto': Myboard.objects.get(id=idn)})

def update_form(request, idn):
    return render(request, 'update.html', {'dto':Myboard.objects.get(id=idn)})

def update_proc(request):
    mycontent = request.POST['mycontents']
    id = request.POST['id']
    mytitle = request.POST['mytitle']
    myname = request.POST['myname']

    myboard = Myboard.objects.filter(id=id)
    result_title = myboard.update(mytitle=mytitle)
    result_name = myboard.update(myname=myname)
    result_content = myboard.update(mycontent=mycontent)

    if result_title + result_name + result_content == 3:
        return redirect('/detail/' + id)
    else:
        return redirect('/updateform' + id)

def insert_form(request):
    return render(request, 'insert.html')

def insert_proc(request):
    myname = request.POST['myname']
    mytitle = request.POST['mytitle']
    mycontent = request.POST['mycontent']

    result = Myboard.objects.create(myname = myname, mytitle = mytitle,
                            mycontent = mycontent, mydate = timezone.now())

    print('==========================')
    print(result)
    print('==========================')

    if result :
        return redirect('index') #id 사용
    else :
        return redirect('insertform')

def delete_proc(request, id):
    result = Myboard.objects.filter(id = id).delete()

    print('==========================')
    print(result)
    print('==========================')

    return redirect('index')