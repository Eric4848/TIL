from django.shortcuts import render, redirect
from .models import MyBoard
from django.utils import timezone
from django.core.paginator import Paginator


def index(request):
    myboard_all = MyBoard.objects.all().order_by('-id')

    paginator = Paginator(myboard_all, 5)  # 5개마다 paging한다
    page_num = request.GET.get('page', '1')  # page값이 없으면 1, 1자리가 page번호

    page_obj = paginator.get_page(page_num)  # page에 맞는 모델

    print("-----count-----")
    print(page_obj.count)  # 총 게시물 수

    print("-----page-----")
    print(page_obj.number)

    print("-----num_page-----")
    print(page_obj.paginator.num_pages)

    print("-----total page range-----")
    print(page_obj.paginator.page_range)

    print("-----is next, prev-----")
    print(page_obj.has_next())
    print(page_obj.has_previous())

    try:
        print("-----next page null = error-----")
        print(page_obj.next_page_number)

        print("-----prev page null = error-----")
        print(page_obj.previous_page_number)
    except:
        pass

    print("-----start_index-----")
    print(page_obj.start_index())

    print("-----end_index-----")
    print(page_obj.end_index())

    return render(request, 'index.html', {'list': page_obj})


def insert_form(request):
    return render(request, 'insert_form.html')


def insert_proc(request):
    name = request.POST['myname']
    title = request.POST['mytitle']
    content = request.POST['mycontent']

    result = MyBoard.objects.create(myname=name, mytitle=title,
                                    mycontent=content, mydate=timezone.now())
    if result:
        return redirect('/')
    else:
        return redirect('insert_form')


def detail(request, id):
    return render(request, 'detail.html', {'dto': MyBoard.objects.get(id=id)})


def delete(request, id):
    result = MyBoard.objects.get(id=id).delete()
    print(result)
    if result[0]:
        return redirect('/')
    else:
        return redirect('/detail/id')


def updateform(request, id):
    return render(request, 'update.html', {'dto': MyBoard.objects.get(id=id)})


def updateres(request, id):
    idn = request.POST['id']
    newname = request.POST['myname']
    newtitle = request.POST['mytitle']
    newcontent = request.POST['mycontents']

    myboard = MyBoard.objects.filter(id=id)
    updatename = myboard.update(myname=newname)
    updatetitle = myboard.update(mytitle=newtitle)
    updatecontent = myboard.update(mycontent=newcontent)

    if updatename + updatetitle + updatecontent == 3:
        return redirect('/detail/' + str(id))  # 주소에는 문자열만 가능
    else:
        return redirect('/updateform/' + idn)
