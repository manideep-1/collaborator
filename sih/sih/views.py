from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from django.contrib import messages
from collaborator.models import destination
from collaborator.models import destinationclient
from collaborator.models import destinationcompany
from django.core.files.storage import FileSystemStorage
import psycopg2
import PyPDF2 
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from io import StringIO
dests=destination.objects.all()

def handle_uploaded_file(f):   
    with open('media/'+f, 'wb+') as destination:   
        for chunk in f.chunks(): 
            destination.write(chunk)   
# Create your views here. 
def home_view(request): 
    context = {} 
    if request.POST: 
        form = destination(request.POST, request.FILES) 
        if form.is_valid(): 
            handle_uploaded_file(request.FILES["geeks_field"]) 
    else: 
        form = destination()
    context['form'] = form 
    return render(request, "afterlogindeveloper.html", context) 
def index(request):
    return render(request,"index.html")

def register(request):
    # if(request.method=='POST'):
        
    # return render(request,"register.html")
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        upload=request.FILES['resume']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=name).exists():
                messages.info(request,'username is already taken.')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists.')
                return redirect('register')
            else:
                fi=request.FILES['resume']
                print(fi.name)
                fs=FileSystemStorage()
                fs.save(fi.name,fi)
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                destobj=destination(name=name,email=email,mobile=mobile,password=password,upload='upload/'+upload.name)
                destobj.save()
                
                print("user saved")
              
        else:
            messages.info(request,'password not matching...')
            return redirect('register')
        return redirect('login')
    else:
        return render(request,"register.html")

    
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user login done")
            dests=destination.objects.all()
            return redirect('/afterlogindeveloper',{'dests':dests})
        else:
            messages.info(request,'invalid credentials.please give correct login details')
            print("invalid credentials")
            return redirect('login')
    else:
        return render(request,"login.html")  

def loginclient(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user login done")
            return redirect('/afterloginclient')
        else:
            messages.info(request,'invalid credentials.please give correct login details')
            print("gone")
            return redirect('loginclient')
    else:
        return render(request,"loginclient.html")  

def registerclient(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        req=request.POST['req']
        nametodisplay=request.POST['nametodisplay']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=name).exists():
                messages.info(request,'username is already taken.')
                return redirect('registerclient')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists.')
                return redirect('registerclient')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                destobj=destinationclient(name=name,email=email,mobile=mobile,password=password,req=req,nametodisplay=nametodisplay)
                destobj.save()
                print("user saved")
              
        else:
            messages.info(request,'password not matching...')
            return redirect('registerclient')
        return redirect('loginclient')
    else:
        return render(request,"registerclient.html")

def registercompany(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        password=request.POST['password']
        
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=name).exists():
                messages.info(request,'username is already taken.')
                return redirect('registercompany')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email already exists.')
                return redirect('registercompany')
            else:
                user=User.objects.create_user(username=name,email=email,password=password)
                user.save()
                destobj=destinationcompany(name=name,email=email,mobile=mobile)
                destobj.save()
                print("user saved")
              
        else:
            messages.info(request,'password not matching...')
            return redirect('registercompany')
        return redirect('logincompany')
    else:
        return render(request,"registercompany.html")

def logincompany(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            print("user login done")
            return redirect('/afterlogincompany')
        else:
            messages.info(request,'invalid credentials.please give correct login details')
            print("gone")
            return redirect('logincompany')
    else:
        return render(request,"logincompany.html")

def client(request):
    return render(request,"client.html")

def developer(request):
    return render(request,"developer.html")

def company(request):
    return render(request,"company.html")  

def afterreg(request):
    return render(request,"afterreg.html")

def afterlogincompany(request):
    return render(request,"afterlogincompany.html")

def afterlogindeveloper(request):
    current_user = request.user
    current_user=str(current_user)
    dests=destination.objects.all()
    # con = psycopg2.connect(user="postgres",password="2304",host="127.0.0.1",port="5432",database="registration1")

    

    # cur = con.cursor()
        

    #     # print(f"Number of rows updated: {cur.rowcount}")
    # for i in dests:
    #     if(i.name==current_user):
    #         print(i.upload)
    #         filer=str(i.upload)
    #         # print(filer)
    #         # if(filer=='upload/Manideep_Laxmishetty_IT1.pdf'):
    #         filer='C:/Users/Manideep/Desktop/sih/media/'+filer
    #         pdftext=convert_pdf_to_txt(filer)
    #         pdftext=pdftext.lower()
    #         # print(pdftext)
    #         l=['c','c++','java','python','html','css','javascript']
    #         found=[]
    #         for j in l:
    #             if(pdftext.find(j)):
    #                 found.append(j)
    #         # print(found)
    #         sfound=",".join(found)
    #         print(sfound)
    #         print(current_user)
    #         cur.execute("UPDATE PUBLIC.collaborator_destination SET skills=%s where name=%s", (sfound,current_user))
    #         print(f"Number of rows updated: {cur.rowcount}")
    return render(request,"afterlogindeveloper.html",{'dests':dests,'current_user':current_user})

def afterloginclient(request):
    current_user = request.user
    current_user=str(current_user)
    destc=destinationclient.objects.all()
    # print(dests)
    return render(request,"afterloginclient.html",{'dests':destc,'current_user':current_user})

def aftercd(request):
    dests=destination.objects.all()
    dic={}
    for i in dests:
        print(i.upload)
        filer=str(i.upload)
        # if(filer=='upload/Manideep_Laxmishetty_IT1.pdf'):
        filer='C:/Users/Manideep/Desktop/sih/media/'+filer
        pdftext=convert_pdf_to_txt(filer)
        pdftext=pdftext.lower()
           # print(pdftext)
        l=['c','c++','java','python','html','css','javascript','mysql','ms office', 'adobe xd','flash','windows','mac os','django','flask']
        found=[]
        for j in l:
            if(pdftext.find(j)!=-1):
               found.append(j)
        # print(found)
        sfound=",".join(found)
        dic[i.name]=sfound
    print(dic)
    return render(request,"aftercd.html",{'dests':dests,'dic':dic })

def aftercc(request):
    # current_user = request.user
    # current_user=str(current_user)
    # print(current_user)
    dests=destinationclient.objects.all()
    return render(request,"aftercc.html",{'dests':dests})

def notify(request):
    current_user = request.user
    current_user=str(current_user)
    print(current_user)
    name=str(request.POST['name'])
    # email=request.POST['email']
    # print(name)
    
    con = psycopg2.connect(user="postgres",password="2304",host="127.0.0.1",port="5432",database="registration1")

    with con:

        cur = con.cursor()
        cur.execute("UPDATE PUBLIC.collaborator_destination SET notification=%s where name=%s", (current_user,name))

        print(f"Number of rows updated: {cur.rowcount}")
        con.close()
    return render(request,"aftercd.html",{'dests':dests})

def notifyclient(request):
    dests=destinationclient.objects.all()
    current_user = request.user
    current_user=str(current_user)
    print(current_user)
    name=str(request.POST['name'])
    # organizationname=str(request.POST['organizationname'])
    con = psycopg2.connect(user="postgres",password="2304",host="127.0.0.1",port="5432",database="registration1")

    with con:

        cur = con.cursor()
        cur.execute("UPDATE PUBLIC.collaborator_destinationclient SET notification=%s where name=%s", (current_user,name))

        print(f"Number of rows updated: {cur.rowcount}")
    return render(request,"aftercc.html",{'dests':dests})

def test(request):
    
    # filename = 'D:/recent2ppf.pdf' 
    # #open allows you to read the file.
    # pdfFileObj = open(filename,'rb')
    # #The pdfReader variable is a readable object that will be parsed.
    # pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    # #Discerning the number of pages will allow us to parse through all the pages.
    # num_pages = pdfReader.numPages
    # count = 0
    # text = ""
    # #The while loop will read each page.
    # while count < num_pages:
    #     pageObj = pdfReader.getPage(count)
    #     count +=1
    #     text += pageObj.extractText()
    # #This if statement exists to check if the above library returned words. It's done because PyPDF2 cannot read scanned files.
    # if text != "":
    #     text = text
    # #If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text.
    # else:
    #     text = textract.process('D:/recent2ppf.pdf', method='tesseract', language='eng')
    # #Now we have a text variable that contains all the text derived from our PDF file. Type print(text) to see what it contains. It likely contains a lot of spaces, possibly junk such as '\n,' etc.
    # #Now, we will clean our text variable and return it as a list of keywords.
    # #The word_tokenize() function will break our text phrases into individual words.
    # tokens = word_tokenize(text)
    # #We'll create a new list that contains punctuation we wish to clean.
    # punctuations = ['(',')',';',':','[',']',',']
    # #We initialize the stopwords variable, which is a list of words like "The," "I," "and," etc. that don't hold much value as keywords.
    # stop_words = stopwords.words('english')
    # #We create a list comprehension that only returns a list of words that are NOT IN stop_words and NOT IN punctuations.
    # keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
    # print(keywords)
    # text = textract.process('media/upload/recent_2pp.pdf', method='pdfminer')
    # print(text)
    pdftext=convert_pdf_to_txt("C:/Users/Manideep/Desktop/sih/media/upload/recent_2pp.pdf")
    pdftext=pdftext.lower()
    print(pdftext)
    l=['c','c++','java','python']
    found=[]
    for i in l:
        if(pdftext.find(i)):
            found.append(i)
    print(found)
    return render(request,"test.html")

def convert_pdf_to_txt(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    # codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, laparams=laparams)
    fp = open(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    fp.close()
    device.close()
    retstr.close()
    return text