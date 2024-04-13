from django.shortcuts import render,redirect
from django.http import HttpResponse

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='sam')
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.

def master(request):
    return render(request,'vendor/master.html')


def dash(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        return render(request,'vendor/dashboard/dash.html')   
    else:
        return redirect(home)

def home(request):
    return render(request, 'vendor/login/add.html')


def bookingadd(request):
    cur.execute("SELECT * FROM `tb_user`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tb_product`")
    datas = cur.fetchall()
    #return list(datas)
    print(list(datas))
    return render(request,'admin/booking/add.html', {'user': data, 'product' : datas})

def bookingaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        bstatus = request.POST['txt1']
        bmaster = request.POST['txt2']
        btime = request.POST['txt3']
        bdate = request.POST['txt4']
        bduration = request.POST['txt5']
        baddress = request.POST['txt6']
        uid = request.POST['txt7']
        pid = request.POST['txt8']
        pcost = request.POST['txt9']
        cur.execute("INSERT INTO `tb_booking`(`booking_status`,`booking_master`,`booking_time`,`booking_date`,`booking_duration`,`booking_address`,`user_id`,`product_id`,`product_cost`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}','{}')".format(bstatus,bmaster,btime,bdate,bduration,baddress,uid,pid,pcost))
        conn.commit()
        return redirect(bookingadd) 
    else:
        return redirect(bookingadd)

def bookingview(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        
        vendor_id = request.session['vendor_id']
        cur.execute(''' SELECT    tb_booking.booking_id    , tb_booking.booking_status    ,
        tb_booking.booking_master    , tb_booking.booking_time    , tb_booking.booking_date    ,
        tb_booking.booking_duration    ,tb_booking.booking_address    , tb_user.user_name    , 
        tb_product.product_name ,tb_product.product_cost FROM    tb_booking    
        INNER JOIN tb_user        ON (tb_booking.user_id = tb_user.user_id)    
        INNER JOIN tb_product        
        ON (tb_booking.product_id = tb_product.product_id);''')
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'vendor/booking/view.html', {'booking': data})
    else:
        return redirect(home)

def bookingdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_booking` where `booking_id` = {}".format(id))
    conn.commit()
    return redirect(bookingview)

def bookingedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_booking` where `booking_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("select * from `tb_user`".format(id))
    datas = cur.fetchall()
    #return list(data)
    print(list(datas))
    cur.execute("select * from `tb_product`".format(id))
    datasa = cur.fetchall()
    #return list(data)
    print(list(datasa))
    return render(request, 'admin/booking/edit.html', {'booking': data, 'user': datas , 'product': datasa})   

def bookingupdate(request):
    if request.method == 'POST':
        print(request.POST)
        bid = request.POST['txt0']
        bstatus = request.POST['txt1']
        bmaster = request.POST['txt2']
        btime = request.POST['txt3']
        bdate = request.POST['txt4']
        bduration = request.POST['txt5']
        uid = request.POST['txt6']
        pid = request.POST['txt7']
        cur.execute("update `tb_booking` set `booking_status` ='{}', `booking_master` ='{}', `booking_time` ='{}',`booking_date` ='{}', `booking_duration` ='{}', `user_id` ='{}', `product_id` ='{}' where `booking_id`='{}'".format(bstatus,bmaster,btime,bdate,bduration,uid,pid,bid))
        conn.commit()
        return redirect(bookingview) 
    else:
        return redirect(bookingview)


def productadd(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        cur.execute("SELECT * FROM `tb_subcategory`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        #cur.execute("SELECT * FROM `tb_vendor`")
        #datas = cur.fetchall()
        #return list(data)
        #print(list(datas))
        return render(request,'vendor/product/add.html', {'subcategories': data})
    else:
        return redirect(home)

def productaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        vendor_id = request.session['vendor_id']
        pname = request.POST['txt1']
        pdetails = request.POST['txt2']
        pcost = request.POST['txt3']
        pqty = request.POST['txt4']
        pnote = request.POST['txt5']
        pimapt = request.POST['txt6']
        sid = request.POST['txt7']
        #vid = request.POST['txt8']
        cur.execute("INSERT INTO `tb_product`(`product_name`,`product_details`,`product_cost`,`product_quantity`,`product_note`,`product_image_path`,`subcategory_id`,`vendor_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(pname,pdetails,pcost,pqty,pnote,pimapt,sid,vendor_id))
        conn.commit()
        return redirect(productadd) 
    else:
        return redirect(productadd)

def productview(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        
        vendor_id = request.session['vendor_id']
        cur.execute(''' SELECT    tb_product.product_id    , tb_product.product_name    , 
        tb_product.product_details    , tb_product.product_cost    ,tb_product.product_cost_3  ,  
        tb_product.product_cost_6  ,  tb_product.product_cost_12  ,   tb_product.product_cost_24  ,  
        tb_product.product_quantity    , tb_product.product_note    , tb_product.product_image_path    , 
        tb_subcategory.subcategory_name    , tb_vendor.vendor_name FROM    tb_product    
        INNER JOIN tb_subcategory         ON (tb_product.subcategory_id = tb_subcategory.subcategory_id)    
        INNER JOIN tb_vendor         
        ON (tb_product.vendor_id = tb_vendor.vendor_id) where tb_product.vendor_id = '{}'
        '''.format(vendor_id))
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'vendor/product/view.html', {'product': data})
    else:
        return redirect(home)

def productdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_product` where `product_id` = {}".format(id))
    conn.commit()
    return redirect(productview)

def productedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_product` where `product_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("select * from `tb_subcategory`".format(id))
    datas = cur.fetchall()
    #return list(data)
    print(list(datas))
    cur.execute("select * from `tb_vendor`".format(id))
    datasa = cur.fetchall()
    #return list(data)
    print(list(datasa))
    return render(request, 'admin/product/edit.html', {'product': data, 'subcategories': datas , 'vendor': datasa})   

def productupdate(request):
    if request.method == 'POST':
        print(request.POST)
        pid = request.POST['txt0']
        pname = request.POST['txt1']
        pdetails = request.POST['txt2']
        pcost = request.POST['txt3']
        product_cost_3 = request.POST['txt4']
        product_cost_6 = request.POST['txt5']
        product_cost_12 = request.POST['txt6']
        product_cost_24 = request.POST['txt7']
        pqty = request.POST['txt8']
        pnote = request.POST['txt9']
        pimapt = request.POST['txt10']
        sid = request.POST['txt11']
        vid = request.POST['txt12']
        cur.execute("update `tb_product` set `product_name` ='{}', `product_details` ='{}', `product_cost` ='{}',`product_cost_3` ='{}',`product_cost_6` ='{}',`product_cost_12` ='{}',`product_cost_24` ='{},`product_quantity` ='{}', `product_note` ='{}', `product_image_path` ='{}', `subcategory_id` ='{}', `vendor_id` ='{}' where `product_id`='{}'".format(pname,pdetails,pcost,product_cost_3,product_cost_6,product_cost_12,product_cost_24,ppqty,pnote,pimapt,sid,vid,pid))
        conn.commit()
        return redirect(productview) 
    else:
        return redirect(productview)


def feedbackadd(request):
    cur.execute("SELECT * FROM `tb_user`")
    data = cur.fetchall()
    #return list(data)
    print(list(data))
    cur.execute("SELECT * FROM `tb_vendor`")
    datas = cur.fetchall()
    #return list(datas)
    print(list(datas))
    return render(request,'admin/feedback/add.html', {'user': data, 'vendor': datas})

def feedbackaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        feedbackdetails = request.POST['text1']
        feedbackdate = request.POST['text2']
        userid = request.POST['text3']
        vendorid = request.POST['text4']
        cur.execute("INSERT INTO `tb_feedback`(`feedback_details`,`feedback_date`,`user_id`,`vendor_id`) VALUES ('{}','{}','{}','{}')".format(feedbackdetails,feedbackdate,userid,vendorid))
        conn.commit()
        return redirect(feedbackadd) 
    else:
        return redirect(feedbackadd)

def feedbackview(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):

        vendor_id = request.session['vendor_id']
        cur.execute(''' SELECT    tb_feedback.feedback_id    , tb_feedback.feedback_details    , 
        tb_feedback.feedback_date    , tb_user.user_name    , tb_vendor.vendor_name FROM    tb_feedback    
        INNER JOIN tb_user         ON (tb_feedback.user_id = tb_user.user_id)    
        INNER JOIN tb_vendor         ON (tb_feedback.vendor_id = tb_vendor.vendor_id) where tb_feedback.vendor_id = '{}'
        '''.format(vendor_id))
        data = cur.fetchall()
        print(list(data))
        return render(request, 'vendor/feedback/view.html', {'feedbacks': data})
    else:
        return redirect(home)

def feedbackdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_feedback` where `feedback_id` = {}".format(id))
    conn.commit()
    return redirect(feedbackview)

def feedbackedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_feedback` where `feedback_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("select * from `tb_user`".format(id))
    datas = cur.fetchall()
    #return list(data)
    print(list(datas))
    cur.execute("select * from `tb_vendor`".format(id))
    datasa = cur.fetchall()
    #return list(data)
    print(list(datasa))
    return render(request, 'admin/feedback/edit.html', {'feedback': data, 'user': datas , 'vendor': datasa})   

def feedbackupdate(request):
    if request.method == 'POST':
        print(request.POST)
        fid = request.POST['text0']
        fdetails = request.POST['text1']
        fdate = request.POST['text2']
        uid = request.POST['text3']
        vid = request.POST['text4']
        cur.execute("update `tb_feedback` set `feedback_details` ='{}', `feedback_date` ='{}', `user_id` ='{}', `vendor_id` ='{}' where `feedback_id`='{}'".format(fdetails,fdate,uid,vid,fid))
        conn.commit()
        return redirect(feedbackview) 
    else:
        return redirect(feedbackview)


def register(request):
    return render(request,'vendor/login/register.html')

def registerprocess(request):
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
        return redirect(home) 
    else:
        return redirect(register)


def loginchange(request):
    if 'vendor_id' in request.COOKIES and request.session.has_key('vendor_id'):
        return render(request,'vendor/login/change.html')
    else:
        return redirect(home)


def loginforgot(request):
    return render(request,'vendor/login/forgot.html')


def slogout(request):

    del request.session['vendor_id']
    del request.session['vendor_email']
    response = redirect(home)
    response.delete_cookie('vendor_id')
    response.delete_cookie('vendor_email')
    return response