from django.shortcuts import render,redirect
from django.http import HttpResponse

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='sam')
print('Successfully connected to database')
cur = conn.cursor()

def homepage(request):
    return render(request, 'user/home/home.html')


def dashboard(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        user_email = request.COOKIES['user_email']
        return render(request, 'user/home/dashboard.html')
    else:
        return redirect(logins)

def vdashboard(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        vendor_email = request.COOKIES['vendor_email']
        return render(request, 'vendor/dashboard/dash.html')
    else:
        return redirect(vlogins)


def contact(request):
    return render(request,'user/contact/contact.html')


def about(request):
    return render(request,'user/about/about.html')


def offer(request):
    cur.execute("SELECT * FROM `tb_offer`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request,'user/offer/offer.html', {'offer': data})


def feedbackadd(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        return render(request,'user/feedback/add.html')
    else:
        return redirect(logins)

def feedbackaddprocess(request):
    
        if request.method == 'POST':
            print(request.POST)
            user_id = request.session['user_id']
            feedbackdetails = request.POST['txt1']
            feedbackdate = request.POST['txt2']
            #userid = request.POST['txt3']
            vendorid = request.POST['txt4']
            cur.execute(" INSERT INTO `tb_feedback`(`feedback_details`,`feedback_date`,`user_id`,`vendor_id`) VALUES ('{}','{}','{}','{}')".format(feedbackdetails,feedbackdate,user_id,vendorid))
            conn.commit()
            return redirect(feedbackadd) 
        else:
            return redirect(feedbackadd)
    
def feedbackview(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):

        user_id = request.session['user_id']
        #cur.execute("Select * from tb_feedback")
        cur.execute('''SELECT    tb_feedback.feedback_id    , tb_feedback.feedback_details    , 
        tb_feedback.feedback_date    , tb_user.user_name    , tb_vendor.vendor_name FROM    tb_feedback    
        INNER JOIN tb_user         ON (tb_feedback.user_id = tb_user.user_id)    
        INNER JOIN tb_vendor         
        ON (tb_feedback.vendor_id = tb_vendor.vendor_id) where tb_feedback.user_id = '{}'
        '''.format(user_id))
        data = cur.fetchall()
        print(list(data))
        return render(request, 'user/feedback/view.html', {'feedbacks': data})
    else:
        return redirect(logins)


def bookingadd(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        return render(request,'user/booking/add.html')
    else:
        return redirect(logins)

def bookingaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        user_id = request.session['user_id']
        bstatus = request.POST['txt1']
        bmaster = request.POST['txt2']
        btime = request.POST['txt3']
        bdate = request.POST['txt4']
        bduration = request.POST['txt5']
        baddress = request.POST['txt6']
        #uid = request.POST['txt7']
        pid = request.POST['txt8']
        pcost = request.POST['txt9']
        cur.execute("INSERT INTO `tb_booking`(`booking_status`,`booking_master`,`booking_time`,`booking_date`,`booking_duration`,`booking_address`,`user_id`,`product_id`,`product_cost`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(bstatus,bmaster,btime,bdate,bduration,baddress,user_id,pid,pcost))
        conn.commit()
        return redirect(bookingadd) 
    else:
        return redirect(bookingadd)

def bookingview(request):
    if 'user_id' in request.COOKIES and request.session.has_key('user_id'):
        
        user_id = request.session['user_id']
        cur.execute('''SELECT    tb_booking.booking_id    , tb_booking.booking_status    , 
        tb_booking.booking_master    , tb_booking.booking_time    , tb_booking.booking_date    , 
        tb_booking.booking_duration    ,tb_booking.booking_address    , tb_user.user_name    , 
        tb_product.product_name ,tb_product.product_cost FROM    tb_booking    
        INNER JOIN  tb_user  ON (tb_booking.user_id = tb_user.user_id)    
        INNER JOIN tb_product        
        ON (tb_booking.product_id = tb_product.product_id) where tb_booking.user_id = '{}'
        '''.format(user_id))
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'user/booking/view.html', {'booking': data})
    else:
        return redirect(logins)


def forgot(request):
    return render(request,'user/login/forgot.html')

def forgotaddprocess(request):
    if request.method == 'POST':
        uemail=request.POST['txt1']
        cur.execute("SELECT * from tb_user where user_email = '{}' ".format(uemail)) 
        return redirect(forgot)

def vforgot(request):
    return render(request,'user/login/vforgot.html')

def vforgotaddprocess(request):
    if request.method == 'POST':
        vemail=request.POST['txt1']
        cur.execute("SELECT * from tb_vendor where vendor_email = '{}' ".format(vemail)) 
        return redirect(vforgot)


def productlisting(request):
    cur.execute("SELECT    tb_product.product_id    , tb_product.product_name    , tb_product.product_details    , tb_product.product_cost    , tb_product.product_quantity    , tb_product.product_note    , tb_product.product_image_path    , tb_subcategory.subcategory_name    , tb_vendor.vendor_name FROM    tb_product    INNER JOIN tb_subcategory         ON (tb_product.subcategory_id = tb_subcategory.subcategory_id)    INNER JOIN tb_vendor         ON (tb_product.vendor_id = tb_vendor.vendor_id);")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT     * from tb_subcategory")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    
    return render(request, 'user/product/listing.html', {'product': data,'subcategories': data1})

def productlistingbycategory(request,id):
    print(id)
    cur.execute("""SELECT    
    tb_product.product_id    , 
    tb_product.product_name    , 
    tb_product.product_details    , 
    tb_product.product_cost    , 
    tb_product.product_quantity    , 
    tb_product.product_note    , 
    tb_product.product_image_path    , 
    tb_subcategory.subcategory_name    , 
    tb_vendor.vendor_name FROM   
     tb_product    INNER JOIN tb_subcategory         
     ON (tb_product.subcategory_id = tb_subcategory.subcategory_id)    
     INNER JOIN tb_vendor ON (tb_product.vendor_id = tb_vendor.vendor_id) where tb_product.subcategory_id ={} """.format(id))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT     * from tb_subcategory")
    data1 = cur.fetchall()
    #return list(data)
    print(list(data1))
    return render(request, 'user/product/listing.html', {'product': data,'subcategories': data1})

def productdetails(request,id):
    print("------------------------------")
    print(id)
    cur.execute("select * from `tb_product` where `product_id` = {}".format(id))
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    return render(request, 'user/product/details.html', {'product': data}) 


def faq(request):
    cur.execute("SELECT * FROM `tb_faq`")
    data = cur.fetchall()
    print(list(data))
    return render(request,'user/faq/faq.html', {'faq': data})  


def logins(request):
    return render(request,'user/login/login.html')

def loginprocess(request):
    if request.method == 'POST':
        print(request.POST)
        user_email = request.POST['txt1']
        user_password = request.POST['txt2']
        print("Yes")
        cur.execute("select * from `tb_user` where user_email ='{}' and user_password  ='{}'".format(user_email,user_password))
        data = cur.fetchone()
        print(data)
        #Check Data is Present or not
        if data is not None:
            if len(data) > 0:
                #Fetch Data
                user_id = data[0]
                user_email = data[2]
                print(user_id)
                print(user_email)
                #Session Create Code
                request.session['user_id'] = user_id
                request.session['user_email'] = user_email
                #Session Create Code
                #Cookie Code
                response = redirect(dashboard)
                response.set_cookie('user_id', user_id)
                response.set_cookie('user_email', user_email)
                return response
                #Cookie Code
            else:
                return redirect(logins)
        return redirect(logins)
    else:
        return redirect(logins)

def register(request):
    return render(request,'user/login/register.html')

def registeraddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        uname = request.POST['txt1']
        uemail = request.POST['txt2']
        upass = request.POST['txt3']
        uadd = request.POST['txt4']
        uphoto = request.POST['txt5']
        udetails = request.POST['txt6']
        cur.execute("INSERT INTO `tb_user`(`user_name`,`user_email`,`user_password`,`user_address`,`user_photo`,`user_details`) VALUES ('{}','{}','{}','{}','{}','{}')".format(uname,uemail,upass,uadd,uphoto,udetails))
        conn.commit()
        return redirect(logins) 
    else:
        return redirect(register)


def vlogins(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        vendor_email = request.COOKIES['vendor_email']
        return render(request,'vendor/dashboard/dash.html')
    else:
        return render(request,'vendor/login/add.html')

def vloginprocess(request):
    if request.method == 'POST':
        print(request.POST)
        vendor_email = request.POST['txt1']
        vendor_password = request.POST['txt2']
        print("Yes")
        cur.execute("select * from `tb_vendor` where vendor_email ='{}' and vendor_password  ='{}'".format(vendor_email,vendor_password))
        data = cur.fetchone()
        print(data)
        #Check Data is Present or not
        if data is not None:
            if len(data) > 0:
                #Fetch Data
                vendor_id = data[0]
                vendor_email = data[2]
                vendor_name = data[1]
                print(vendor_id)
                print(vendor_email)
                #Session Create Code
                request.session['vendor_id'] = vendor_id
                request.session['vendor_email'] = vendor_email
                #Session Create Code
                #Cookie Code
                response = redirect(vdashboard)
                response.set_cookie('vendor_id', vendor_id)
                response.set_cookie('vendor_email', vendor_email)
                return response
                #Cookie Code
            else:
                return redirect(vlogins)
        return redirect(vlogins)
    else:
        return redirect(vlogins)

def vregister(request):
    return render(request,'user/login/vregister.html')

def vregisteraddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        vendorname = request.POST['text1']
        vendoremail = request.POST['text2']
        vendorpassword = request.POST['text3']
        vendorgender = request.POST['text4']
        vendoraddress = request.POST['text5']
        vendorimagepath = request.POST['text6']
        cur.execute("INSERT INTO `tb_vendor`(`vendor_name`,`vendor_email`,`vendor_password`,`vendor_gender`,`vendor_address`,`vendor_image_path`) VALUES ('{}','{}','{}','{}','{}','{}')".format(vendorname,vendoremail,vendorpassword,vendorgender,vendoraddress,vendorimagepath))
        conn.commit()
        return redirect(vlogins) 
    else:
        return redirect(vregister)


def logouts(request):
    
    del request.session['user_id']
    del request.session['user_email']
    response = redirect(logins)
    response.delete_cookie('user_id')
    response.delete_cookie('user_email')
    return response   