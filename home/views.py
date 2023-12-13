from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
# from pyexpat.errors import messages
from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render, redirect, HttpResponse
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode

from blog.models import Post
from home.forms import btechforms, MScDfForms, mtechaiforms, mtechcsforms, pgdforms
from home.models import Contact
from home.models import btech, mtechcs, mtechai, mscdf, pgd
import settings
from .tokens import generate_token


# Create your views here.
def home(request):
    return render(request, 'home/home.html')
    # return HttpResponse("This is Home")


def user(request):
    return render(request, 'home/user.html')
    # return HttpResponse("This is Home")


def about(request):
    return render(request, 'home/about.html')
    # return HttpResponse("This is about")


def contact(request):
    # messages.error(request, 'Welcome to contact')
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        content = request.POST['content']
        # print(name,email,phone,content)3

        if (len(name) < 2 or len(email) < 3 or len(phone) < 10 or len(content) < 4):
            messages.error(request, 'Please fill the form correctly')
        else:
            contact = Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, 'Your message has been successfully sent')
    return render(request, 'home/contact.html')
    # return HttpResponse("This is contact")


# def contact(index):
#     return HttpResponse("This is contact")

def payment(request):
    return render(request, 'home/payment.html')


def search(request):
    query = request.GET['query']
    if len(query) > 78:
        allpost = Post.objects.none()
    else:
        allposttitel = Post.objects.filter(title__icontains=query)
        allpostcontent = Post.objects.filter(content__icontains=query)
        allpost = allposttitel.union(allpostcontent)

    if allpost.count() == 0:
        messages.warning(request, 'No search results found. Please refind your query')

    # allpost=Post.objects.all()
    params = {'allpost': allpost, 'query': query}
    return render(request, 'home/search.html', params)
    # return HttpResponse('This is search')


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64)
        myuser = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser, token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request, myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('home')
    else:
        return render(request, 'activation_failed.html')


def handlesignup(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        # Check for errorneous inputa
        if len(username) > 10:
            messages.error(request, 'Username must under 10 characters')
            return redirect('home')

        if not username.isalnum():
            messages.error(request, 'Username should only contain letters and numbers')
            return redirect('home')

        if pass1 != pass2:
            messages.error(request, 'Passwords do not match')
            return redirect('home')

        # Creat the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False

        myuser.save()
        messages.success(request, 'Your account has been created, Verify your acccount to login into System.')

        # Welcome Email
        # subject = "Welcome to College Management!!"
        # message = "Hello " + myuser.first_name + "!! \n" + "Welcome to CMS!! \nThank you for visiting our website. \n\nThanking You\nJeet & Darshan"        
        # from_email = settings.EMAIL_HOST_USER
        # to_list = [myuser.email]
        # send_mail(subject, message, from_email, to_list, fail_silently=True)

        # Email Address Confirmation Email
        # to_list = [myuser.email]

        current_site = get_current_site(request)
        from_email = settings.EMAIL_HOST_USER
        email_subject = "Confirm your Email at College Management System!!"
        message2 = render_to_string('email_confirmation.html', {

            'name': myuser.first_name,
            'domain': current_site.domain,
            # 'uid': urlsafe_base64_encode(myuser.pk),
            'uid': urlsafe_base64_encode(force_bytes(myuser.pk)),
            'token': generate_token.make_token(myuser)
        })

        to_list = [myuser.email]

        send_mail(email_subject, message2, from_email, to_list, fail_silently=True)

        return redirect('home')


    else:
        return HttpResponse('404 - Not Found')


def handlelogin(request):
    if request.method == 'POST':
        loginusername = request.POST['loginusername']
        loginpass = request.POST['loginpass']

        user = authenticate(username=loginusername, password=loginpass)
        # print(loginusername)
        # print(user['fname'])
        # print(request.POST['name'])
        # editempobj.name=request.POST['name']
        # print(user.password)
        # print(loginpass)
        if user is not None:
            login(request, user)
            displayresults = user
            messages.success(request, "Successfully Logged In")
            # return render(request, "home/user.html",{'data':displayresults})
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials, Please try agian')
            return redirect('home')

    return HttpResponse('404 - Not Found')


def handlelogout(request):
    # if request.method=='POST':
    logout(request)
    messages.success(request, "Successfully Logged Out")
    return redirect('home')
    # return HttpResponse("Logout")


def btecha(request, userid):
    username = User.objects.get(id=userid)
    if request.method == "GET":
        return render(request, 'btecha.html', {'data': username})
    elif request.method == "POST":
        print("what the hell")
        # try:
        try:
            todo = btech()
            todo.u_id_id = request.POST['u_id_id']
            todo.aadhar = request.POST['aadhar']
            todo.name = request.POST['name']
            todo.email = request.POST.get('email')
            todo.mobile = request.POST['mobile']
            todo.dob = request.POST['dob']
            todo.gender = request.POST['gender']
            todo.percent = request.POST['percent']
            todo.percentile = request.POST['percentile']
            todo.category = request.POST['category']
            todo.pincode = request.POST['pincode']

            myfile = request.FILES['jee']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.jee = uploaded_file_url

            myfile = request.FILES['marksheet']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.marksheet = uploaded_file_url

            myfile = request.FILES['sign']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.sign = uploaded_file_url

            myfile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.img = uploaded_file_url

            if (todo.category != 'OPEN'):
                myfile = request.FILES['certificate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                todo.certificate = uploaded_file_url

            todo.save()
            print("seriously")
            messages.success(request, "The application Is Saved Successfully")
        # except Exception as e:
        #     messages.success(request,"The course "+request.POST['courses_id']+"Is Already Inserted")
        except Exception as e:
            messages.success(request, "You have filled the form twice or you have filled the form incorrectly")
            return render(request, 'home/user.html')

    return render(request, 'home/user.html')


def bteche(request: HttpRequest, id):
    try:
        editempobj = btech.objects.get(u_id_id=id)
        return render(request, 'bteche.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can edit.")
        return render(request, 'home/user.html')


def btechv(request: HttpRequest, id):
    try:
        editempobj = btech.objects.get(u_id_id=id)
        return render(request, 'btechv.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can view your data.")
        return render(request, 'home/user.html')


def btechu(request: HttpRequest, id):
    editempobj = btech.objects.get(u_id_id=id)

    fo = btechforms(request.POST, instance=editempobj)
    print("yes")
    # editempobj.name=request.POST['name']
    # print(request.POST['img'])
    # if (request.FILES['img']!=''):
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['jee']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.jee = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['marksheet']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.marksheet = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['sign']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.sign = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        editempobj.gender = request.POST['gender']
    except:
        pass
    try:
        editempobj.category = request.POST['category']
    except:
        pass
    if fo.is_valid():
        print("no")
        fo.save()
        messages.success(request, 'record updated successfully ..!')
        #        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})
        return render(request, 'home/user.html')


def mtechcsa(request, userid):
    username = User.objects.get(id=userid)
    if request.method == "GET":
        return render(request, 'mtechcsa.html', {'data': username})
    elif request.method == "POST":
        print("what the hell")
        # try:
        try:
            todo = mtechcs()
            todo.u_id_id = request.POST['u_id_id']
            todo.aadhar = request.POST['aadhar']
            todo.name = request.POST['name']
            todo.email = request.POST.get('email')
            todo.mobile = request.POST['mobile']
            todo.dob = request.POST['dob']
            todo.gender = request.POST['gender']
            todo.cgpa = request.POST['cgpa']
            todo.gatescore = request.POST['gatescore']
            todo.category = request.POST['category']
            todo.pincode = request.POST['pincode']
            myfile = request.FILES['gate']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.gate = uploaded_file_url

            myfile = request.FILES['marksheet']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.marksheet = uploaded_file_url

            myfile = request.FILES['sign']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.sign = uploaded_file_url

            myfile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.img = uploaded_file_url

            if (todo.category != 'OPEN'):
                myfile = request.FILES['certificate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                todo.certificate = uploaded_file_url

            todo.save()
            print("seriously")
            # btech(u_id_id=u_id_id,marksheet=marksheet,jee=jee,aadhar=aadhar,courses_id=courses_id).save()
            messages.success(request, "The application Is Saved Successfully")
        # except Exception as e:
        #     messages.success(request,"The course "+request.POST['courses_id']+"Is Already Inserted")
        except Exception as e:
            messages.success(request, "You have filled the form twice or you have filled the form incorrectly")
            return render(request, 'home/user.html')
    return render(request, 'home/user.html')


def mtechcse(request: HttpRequest, id):
    try:
        editempobj = mtechcs.objects.get(u_id_id=id)
        return render(request, 'mtechcse.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can edit.")
        return render(request, 'home/user.html')


def mtechcsv(request: HttpRequest, id):
    try:
        editempobj = mtechcs.objects.get(u_id_id=id)
        return render(request, 'mtechcsv.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can view your data.")
        return render(request, 'home/user.html')
        # return render(request,'mtechcsv.html',{"data":editempobj})


def mtechcsu(request: HttpRequest, id):
    editempobj = mtechcs.objects.get(u_id_id=id)

    fo = mtechcsforms(request.POST, instance=editempobj)
    print("yes")

    try:
        myfile = request.FILES['gate']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.gate = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['marksheet']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.marksheet = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['sign']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.sign = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        editempobj.gender = request.POST['gender']
    except:
        pass
    try:
        editempobj.category = request.POST['category']
    except:
        pass
    if fo.is_valid():
        print("no")
        fo.save()
        messages.success(request, 'record updated successfully ..!')
        #        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})
        return render(request, 'home/user.html')


def mtechaia(request, userid):
    username = User.objects.get(id=userid)
    if request.method == "GET":
        return render(request, 'mtechaia.html', {'data': username})
    elif request.method == "POST":
        print("what the hell")
        # try:
        try:
            todo = mtechai()
            todo.u_id_id = request.POST['u_id_id']
            todo.aadhar = request.POST['aadhar']
            todo.name = request.POST['name']
            todo.email = request.POST.get('email')
            todo.mobile = request.POST['mobile']
            todo.dob = request.POST['dob']
            todo.gender = request.POST['gender']
            todo.cgpa = request.POST['cgpa']
            todo.gatescore = request.POST['gatescore']
            todo.category = request.POST['category']
            todo.pincode = request.POST['pincode']
            myfile = request.FILES['gate']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.gate = uploaded_file_url

            myfile = request.FILES['marksheet']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.marksheet = uploaded_file_url

            myfile = request.FILES['sign']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.sign = uploaded_file_url

            myfile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.img = uploaded_file_url

            if (todo.category != 'OPEN'):
                myfile = request.FILES['certificate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                todo.certificate = uploaded_file_url

            todo.save()
            print("seriously")
            # btech(u_id_id=u_id_id,marksheet=marksheet,jee=jee,aadhar=aadhar,courses_id=courses_id).save()
            messages.success(request, "The application Is Saved Successfully")
        # except Exception as e:
        #     messages.success(request,"The course "+request.POST['courses_id']+"Is Already Inserted")
        except Exception as e:
            messages.success(request, "You have filled the form twice or you have filled the form incorrectly")
            return render(request, 'home/user.html')
    return render(request, 'home/user.html')


def mtechaie(request: HttpRequest, id):
    try:
        editempobj = mtechai.objects.get(u_id_id=id)
        return render(request, 'mtechaie.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can edit your data.")
        return render(request, 'home/user.html')
        # return render(request,'mtechaie.html',{"data":editempobj})


def mtechaiv(request: HttpRequest, id):
    try:
        editempobj = mtechai.objects.get(u_id_id=id)
        return render(request, 'mtechaiv.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can view your data.")
        return render(request, 'home/user.html')


def mtechaiu(request: HttpRequest, id):
    editempobj = mtechai.objects.get(u_id_id=id)
    fo = mtechaiforms(request.POST, instance=editempobj)
    print("yes")
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['gate']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.gate = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['marksheet']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.marksheet = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['sign']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.sign = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        editempobj.gender = request.POST['gender']
    except:
        pass
    try:
        editempobj.category = request.POST['category']
    except:
        pass
    if fo.is_valid():
        print("no")
        fo.save()
        messages.success(request, 'record updated successfully ..!')
        #        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})
        return render(request, 'home/user.html')


def mscdfa(request, userid):
    username = User.objects.get(id=userid)
    if request.method == "GET":
        return render(request, 'mscdfa.html', {'data': username})
    elif request.method == "POST":
        print("what the hell")
        # try:
        try:
            todo = mscdf()
            todo.u_id_id = request.POST['u_id_id']
            todo.aadhar = request.POST['aadhar']
            todo.name = request.POST['name']
            todo.email = request.POST.get('email')
            todo.mobile = request.POST['mobile']
            todo.dob = request.POST['dob']
            todo.gender = request.POST['gender']
            todo.cgpa = request.POST['cgpa']
            todo.category = request.POST['category']
            todo.pincode = request.POST['pincode']

            myfile = request.FILES['marksheet']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.marksheet = uploaded_file_url

            myfile = request.FILES['sign']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.sign = uploaded_file_url

            myfile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.img = uploaded_file_url

            if (todo.category != 'OPEN'):
                myfile = request.FILES['certificate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                todo.certificate = uploaded_file_url

            todo.save()
            print("seriously")
            # btech(u_id_id=u_id_id,marksheet=marksheet,jee=jee,aadhar=aadhar,courses_id=courses_id).save()
            messages.success(request, "The application Is Saved Successfully")
        # except Exception as e:
        #     messages.success(request,"The course "+request.POST['courses_id']+"Is Already Inserted")
        except Exception as e:
            messages.success(request, "You have filled the form twice or you have filled the form incorrectly")
            return render(request, 'home/user.html')
    return render(request, 'home/user.html')


def mscdfe(request: HttpRequest, id):
    try:
        editempobj = mscdf.objects.get(u_id_id=id)
        return render(request, 'mscdfe.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can edit your data.")
        return render(request, 'home/user.html')


def mscdfv(request: HttpRequest, id):
    try:
        editempobj = mscdf.objects.get(u_id_id=id)
        return render(request, 'mscdfv.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can view your data.")
        return render(request, 'home/user.html')


def mscdfu(request: HttpRequest, id):
    editempobj = mscdf.objects.get(u_id_id=id)
    fo = MScDfForms(request.POST, instance=editempobj)
    print("yes")

    try:
        myfile = request.FILES['marksheet']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.marksheet = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['sign']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.sign = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        editempobj.gender = request.POST['gender']
    except:
        pass
    try:
        editempobj.category = request.POST['category']
    except:
        pass
    if fo.is_valid():
        print("no")
        fo.save()
        messages.success(request, 'record updated successfully ..!')
        #        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})
        return render(request, 'home/user.html')


def pgda(request, userid):
    username = User.objects.get(id=userid)
    if request.method == "GET":
        return render(request, 'pgda.html', {'data': username})
    elif request.method == "POST":
        print("what the hell")
        # try:
        try:
            todo = pgd()
            todo.u_id_id = request.POST['u_id_id']
            todo.aadhar = request.POST['aadhar']
            todo.name = request.POST['name']
            todo.email = request.POST.get('email')
            todo.mobile = request.POST['mobile']
            todo.dob = request.POST['dob']
            todo.gender = request.POST['gender']
            todo.cgpa = request.POST['cgpa']
            todo.category = request.POST['category']
            todo.pincode = request.POST['pincode']

            myfile = request.FILES['marksheet']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.marksheet = uploaded_file_url

            myfile = request.FILES['sign']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.sign = uploaded_file_url

            myfile = request.FILES['img']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            todo.img = uploaded_file_url

            if (todo.category != 'OPEN'):
                myfile = request.FILES['certificate']
                fs = FileSystemStorage()
                filename = fs.save(myfile.name, myfile)
                uploaded_file_url = fs.url(filename)
                todo.certificate = uploaded_file_url

            todo.save()
            print("seriously")
            # btech(u_id_id=u_id_id,marksheet=marksheet,jee=jee,aadhar=aadhar,courses_id=courses_id).save()
            messages.success(request, "The application Is Saved Successfully")
        # except Exception as e:
        #     messages.success(request,"The course "+request.POST['courses_id']+"Is Already Inserted")
        except Exception as e:
            messages.success(request, "You have filled the form twice or you have filled the form incorrectly")
            return render(request, 'home/user.html')
    return render(request, 'home/user.html')


def pgde(request: HttpRequest, id):
    try:
        editempobj = pgd.objects.get(u_id_id=id)
        return render(request, 'pgde.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can edit your data.")
        return render(request, 'home/user.html')


def pgdv(request: HttpRequest, id):
    try:
        editempobj = pgd.objects.get(u_id_id=id)
        return render(request, 'pgdv.html', {"data": editempobj})
    except Exception as e:
        messages.error(request, "Apply first then you can view your data.")
        return render(request, 'home/user.html')


def pgdu(request: HttpRequest, id):
    editempobj = pgd.objects.get(u_id_id=id)
    fo = pgdforms(request.POST, instance=editempobj)

    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['marksheet']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.marksheet = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['sign']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.sign = uploaded_file_url
    except:
        pass
    try:
        myfile = request.FILES['img']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        editempobj.img = uploaded_file_url
    except:
        pass
    try:
        editempobj.gender = request.POST['gender']
    except:
        pass
    try:
        editempobj.category = request.POST['category']
    except:
        pass

    print("no")
    print(fo.is_valid)
    if fo.is_valid():
        print("no")
        fo.save()
        messages.success(request, 'record updated successfully ..!')
    #        return render(request,'opdcomplain.html',{"opdcomplainmodel":Updateemp})
    return render(request, 'home/user.html')
