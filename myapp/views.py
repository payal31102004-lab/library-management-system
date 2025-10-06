import datetime

from django.db.models import F
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.defaultfilters import title, first

from myapp.models import admintbl, manage_book_tbl, manage_member_tbl, issue_return_tbl, return_book_tbl


# Create your views here.
def adminlogin(request):
    return render(request, 'adminlogin.html')
def admin_login_code(request):
    if request.method == 'POST':
        a=request.POST.get('username')
        b=request.POST.get('password')
        data=admintbl.objects.filter(username=a).first()
        if not data:
            return HttpResponse("username wrong")
        elif data.password == b:
            request.session['admin']=a
            return redirect("../dashboard")
        else:
            HttpResponse("password wrong")
    else:
        return redirect("../")

def dashboard(request, curdate=None):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect("../")
    else:
        bookdata=manage_book_tbl.objects.count()
        totalmember=manage_member_tbl.objects.count()
        issuedata=issue_return_tbl.objects.count()
        returndata=return_book_tbl.objects.count()
        curdate=datetime.date.today()
        getdata=issue_return_tbl.objects.filter(issuedate=curdate).filter()
        return render(request, "dashboard.html",{"show":bookdata,"show1":totalmember,"show2":issuedata,"show3":returndata,"getdata":getdata})

def manage_books(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect("../dashboard")
    else:
        data=manage_book_tbl.objects.all()
        return render(request, 'manage_books.html',{'show':data})

def manage_books_code(request):
    if request.method == 'POST':
        a=request.POST.get('title')
        b=request.POST.get('author')
        c=request.POST.get('category')
        d=request.POST.get('total_copies')
        e=request.POST.get('available_copies')
        manage_book_tbl.objects.create(title=a,author=b,category=c,total_copies=d,available_copies=e)
        return redirect("../manage_books")

    else:
        return redirect("../manage_books")
def manage_members(request):
    sesid=request.session.get('admin')
    if not sesid:
        return redirect("../")
    else:
        data=manage_member_tbl.objects.all()
        return render(request, 'manage_members.html',{'show':data})

def manage_members_code(request):
    if request.method == 'POST':
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('membership_date')
        manage_member_tbl.objects.create(name=a,email=b,phone=c,members_date=d)
        return redirect("../manage_members")
    else:
        return redirect("../manage_members")

def manage_books_delete(request,id):
    manage_book_tbl.objects.get(id=id).delete()
    return redirect("../manage_books")

def manage_books_edit(request,id):
    data=manage_book_tbl.objects.filter(id=id).first()
    return render(request, 'manage_books_edit.html',{'show':data})

def manage_books_update(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        a=request.POST.get('title')
        b=request.POST.get('author')
        c=request.POST.get('category')
        d=request.POST.get('total_copies')
        e=request.POST.get('available_copies')
        manage_book_tbl.objects.filter(id=id).update(title=a,author=b,category=c,total_copies=d,available_copies=e)
        return redirect("../manage_books")
    else:
        return redirect("../")

def manage_members_delete(request,id):
    manage_member_tbl.objects.get(id=id).delete()
    return redirect("../manage_members")

def manage_members_edit(request,id):
    data=manage_member_tbl.objects.filter(id=id).first()
    return render(request, 'manage_members_edit.html',{'show':data})
def manage_members_update(request):
    if request.method == 'POST':
        id=request.POST.get('id')
        a=request.POST.get('name')
        b=request.POST.get('email')
        c=request.POST.get('phone')
        d=request.POST.get('membership_date')
        manage_member_tbl.objects.filter(id=id).update(name=a,email=b,phone=c,members_date=d)
        return redirect("../manage_members")
    else:
        return redirect("../")

def issue_return(request):
   data=manage_book_tbl.objects.all()
   data1=manage_member_tbl.objects.all()
   data2=issue_return_tbl.objects.all()
   data3=return_book_tbl.objects.all()
   return render(request, 'issue_return.html',{'show':data,'show1':data1,'show2':data2,'show3':data3})
def issue_return_code(request):
    if request.method == 'POST':
        a=request.POST.get('member_id')
        b=request.POST.get('book_id')
        c=request.POST.get('due_date')
        date=datetime.date.today()
        issue_return_tbl.objects.create(memberid=a,bookid=b,duedate=c,issuedate=date)
        data=manage_book_tbl.objects.filter(title=b).first()
        if data.total_copies=='0':
            return HttpResponse("book out of stock")
        else:
            manage_book_tbl.objects.filter(title=b).update(total_copies=F('total_copies')-1)
            return redirect("../issue_return")
    else:
        return redirect("../")

def return_book_code(request):
    if request.method == 'POST':
        a=request.POST.get('member_id')
        b=request.POST.get('book_id')
        date=datetime.date.today()
        return_book_tbl.objects.create(memberid=a,bookid=b,returndate=date)
        manage_book_tbl.object.filter(title=b).update(total_copies=F('total_copies')+1)
        return redirect("../issue_return")
        return HttpResponse("data save")
    else:
        # return HttpResponse("error")
        return redirect("../issue_return")

def reports(request):
    return render(request, 'reports.html')



















