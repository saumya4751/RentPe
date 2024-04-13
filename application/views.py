from django.shortcuts import render,redirect
from django.http import HttpResponse

import mysql.connector as mcdb
conn = mcdb.connect(host="localhost", user="root", passwd="", database='sam')
print('Successfully connected to database')
cur = conn.cursor()

# Create your views here.

def master(request):
    return render(request,'admin/master.html')

def home(request):
    return render(request, 'admin/login/add.html')

def dash(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/dashboard/dash.html')
    else:
        return redirect(home)


def adminadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/sammy/add.html')
    else:
        return redirect(home)

def adminaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        aname = request.POST['txt1']
        aemail = request.POST['txt2']
        apassword = request.POST['txt3']
        cur.execute("INSERT INTO `tb_admin`(`admin_name`,`admin_email`,`admin_password`) VALUES ('{}','{}','{}')".format(aname,aemail,apassword))
        conn.commit()
        return redirect(adminadd) 
    else:
        return redirect(adminadd)

def adminview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_admin`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/sammy/view.html', {'admin': data})
    else:
        return redirect(home)

def admindelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_admin` where `admin_id` = {}".format(id))
    conn.commit()
    return redirect(adminview)

def adminedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_admin` where `admin_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/sammy/edit.html', {'admin': data})   

def adminupdate(request):
    if request.method == 'POST':
        print(request.POST)
        aid = request.POST['txt0']
        aname = request.POST['txt1']
        aemail = request.POST['txt2']
        apassword = request.POST['txt3']
        cur.execute("update `tb_admin` set `admin_name` ='{}', `admin_email` ='{}', `admin_password` ='{}' where `admin_id`='{}'".format(aname,aemail,apassword,aid))
        conn.commit()
        return redirect(adminview) 
    else:
        return redirect(adminview)


def faqadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/FAQ/add.html')
    else:
        return redirect(home)

def faqaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        fques = request.POST['txt1']
        fans = request.POST['txt2']
        cur.execute("INSERT INTO `tb_faq`(`faq_question`,`faq_answer`) VALUES ('{}','{}')".format(fques,fans))
        conn.commit()
        return redirect(faqadd) 
    else:
        return redirect(faqadd)

def faqview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_faq`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/FAQ/view.html', {'faq': data})
    else:
        return redirect(home)

def faqdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_faq` where `faq_id` = {}".format(id))
    conn.commit()
    return redirect(faqview)

def faqedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_faq` where `faq_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/FAQ/edit.html', {'faq': data})   

def faqupdate(request):
    if request.method == 'POST':
        print(request.POST)
        fid = request.POST['txt0']
        fques = request.POST['txt1']
        fans = request.POST['txt2']
        cur.execute("update `tb_faq` set `faq_question` ='{}', `faq_answer` ='{}' where `faq_id`='{}'".format(fques,fans,fid))
        conn.commit()
        return redirect(faqview) 
    else:
        return redirect(faqview)


def bookingadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_user`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        cur.execute("SELECT * FROM `tb_product`")
        datas = cur.fetchall()
        #return list(datas)
        print(list(datas))
        return render(request,'admin/booking/add.html', {'user': data, 'product' : datas})
    else:
        return redirect(home)

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
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT    tb_booking.booking_id    , tb_booking.booking_status    , tb_booking.booking_master    , tb_booking.booking_time    , tb_booking.booking_date    , tb_booking.booking_duration    ,tb_booking.booking_address    , tb_user.user_name    , tb_product.product_name ,tb_product.product_cost FROM    tb_booking    INNER JOIN tb_user        ON (tb_booking.user_id = tb_user.user_id)    INNER JOIN tb_product        ON (tb_booking.product_id = tb_product.product_id);")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/booking/view.html', {'booking': data})
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


def categoryadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/category/add.html')
    else:
        return redirect(home)

def categoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        catname = request.POST['txt1']
        cur.execute("INSERT INTO `tb_category`(`category_name`) VALUES ('{}')".format(catname))
        conn.commit()
        return redirect(categoryadd) 
    else:
        return redirect(categoryadd)

def categoryview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_category`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'admin/category/view.html', {'categories': data})
    else:
        return redirect(home)

def categorydelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_category` where `category_id` = {}".format(id))
    conn.commit()
    return redirect(categoryview)

def categoryedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_category` where `category_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/category/edit.html', {'categories': data})   

def categoryupdate(request):
    if request.method == 'POST':
        print(request.POST)
        catid = request.POST['txt1']
        catname = request.POST['txt2']
        cur.execute("update `tb_category` set `category_name` ='{}' where `category_id`='{}'".format(catname,catid))
        conn.commit()
        return redirect(categoryview) 
    else:
        return redirect(categoryview)


def subcategoryadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_category`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'admin/subcategory/add.html', {'categories': data})
    else:
        return redirect(home)
   
def subcategoryaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        subname = request.POST['txt1']
        catid = request.POST['txt2']
        cur.execute("INSERT INTO `tb_subcategory`(`subcategory_name`,`category_id`) VALUES ('{}','{}')".format(subname,catid))
        conn.commit()
        return redirect(subcategoryadd) 
    else:
        return redirect(subcategoryadd)

def subcategoryview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT     tb_subcategory.subcategory_id     , tb_subcategory.subcategory_name     , tb_category.category_name FROM tb_category    INNER JOIN tb_subcategory       ON (tb_category.category_id = tb_subcategory.category_id);")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'admin/subcategory/view.html', {'subcategories': data})
    else:
        return redirect(home)

def subcategorydelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_subcategory` where `subcategory_id` = {}".format(id))
    conn.commit()
    return redirect(subcategoryview)

def subcategoryedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_subcategory` where `subcategory_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("select * from `tb_category`".format(id))
    datas = cur.fetchall()
    #return list(data)
    print(list(datas))
    return render(request, 'admin/subcategory/edit.html', {'subcategories': data, 'categories': datas})   

def subcategoryupdate(request): 
    if request.method == 'POST':
        print(request.POST)
        subid = request.POST['txt0']
        subname = request.POST['txt1']
        catid = request.POST['txt2']
        cur.execute("update `tb_subcategory` set `subcategory_name` ='{}', `category_id` ='{}' where `subcategory_id`='{}'".format(subname,catid,subid))
        conn.commit()
        return redirect(subcategoryview) 
    else:
        return redirect(subcategoryview)


def imageadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_product`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/image/add.html', {'product': data})
    else:
        return redirect(home)

def imageaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        pid = request.POST['txt1']
        iname = request.POST['txt2']
        cur.execute("INSERT INTO `tb_image`(`product_id`,`image_name`) VALUES ('{}','{}')".format(pid,iname))
        conn.commit()
        return redirect(imageadd) 
    else:
        return redirect(imageadd)

def imageview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT    tb_image.image_id    , tb_product.product_name    , tb_image.image_name FROM    tb_image    INNER JOIN tb_product        ON (tb_image.product_id = tb_product.product_id);")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'admin/image/view.html', {'image': data})
    else:
        return redirect(home)

def imagedelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_image` where `image_id` = {}".format(id))
    conn.commit()
    return redirect(imageview)

def imageedit(request,id):
     
    print(id)
    cur.execute("select * from `tb_image` where `image_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    cur.execute("select * from `tb_product`".format(id))
    datas = cur.fetchall()
    #return list(data)
    print(list(datas))
    return render(request, 'admin/image/edit.html', {'image': data, 'product': datas})   

def imageupdate(request):
    if request.method == 'POST':
        print(request.POST)
        iid = request.POST['txt0']
        pid = request.POST['txt1']
        iname = request.POST['txt2']
        cur.execute("update `tb_image` set `product_id` ='{}', `image_name` ='{}' where `image_id`='{}'".format(pid,iname,iid))
        conn.commit()
        return redirect(imageview) 
    else:
        return redirect(imageview)


def offeradd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/offer/add.html')
    else:
        return redirect(home)

def offeraddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        otitle = request.POST['txt1']
        odetails = request.POST['txt2']
        ostartdate = request.POST['txt3']
        oenddate = request.POST['txt4']
        cur.execute("INSERT INTO `tb_offer`(`offer_title`,`offer_details`,`offer_start_date`,`offer_end_date`) VALUES ('{}','{}','{}','{}')".format(otitle,odetails,ostartdate,oenddate))
        conn.commit()
        return redirect(offeradd) 
    else:
        return redirect(offeradd)

def offerview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_offer`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/offer/view.html', {'offer': data})
    else:
        return redirect(home)

def offerdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_offer` where `offer_id` = {}".format(id))
    conn.commit()
    return redirect(offerview)

def offeredit(request,id):
     
    print(id)
    cur.execute("select * from `tb_offer` where `offer_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/offer/edit.html', {'offer': data})   

def offerupdate(request):
    if request.method == 'POST':
        print(request.POST)
        oid = request.POST['txt0']
        otitle = request.POST['txt1']
        odetails = request.POST['txt2']
        ostartdate = request.POST['txt3']
        oenddate = request.POST['txt4']
        cur.execute("update `tb_offer` set `offer_title` ='{}', `offer_details` ='{}', `offer_start_date` ='{}',`offer_end_date` ='{}' where `offer_id`='{}'".format(otitle,odetails,ostartdate,oenddate,oid))
        conn.commit()
        return redirect(offerview) 
    else:
        return redirect(offerview)


def productadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_subcategory`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        cur.execute("SELECT * FROM `tb_vendor`")
        datas = cur.fetchall()
        #return list(data)
        print(list(datas))
        return render(request,'admin/product/add.html', {'subcategories': data, 'vendor': datas})
    else:
        return redirect(home)

def productaddprocess(request):
    if request.method == 'POST':
        print(request.POST)
        pname = request.POST['txt1']
        pdetails = request.POST['txt2']
        pcost = request.POST['txt3']
        pqty = request.POST['txt4']
        pnote = request.POST['txt5']
        pimapt = request.POST['txt6']
        sid = request.POST['txt7']
        vid = request.POST['txt8']
        cur.execute("INSERT INTO `tb_product`(`product_name`,`product_details`,`product_cost`,`product_quantity`,`product_note`,`product_image_path`,`subcategory_id`,`vendor_id`) VALUES ('{}','{}','{}','{}','{}','{}','{}','{}')".format(pname,pdetails,pcost,pqty,pnote,pimapt,sid,vid))
        conn.commit()
        return redirect(productadd) 
    else:
        return redirect(productadd)

def productview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT    tb_product.product_id    , tb_product.product_name    , tb_product.product_details    , tb_product.product_cost    ,tb_product.product_cost_3  ,  tb_product.product_cost_6  ,  tb_product.product_cost_12  ,   tb_product.product_cost_24  ,  tb_product.product_quantity    , tb_product.product_note    , tb_product.product_image_path    , tb_subcategory.subcategory_name    , tb_vendor.vendor_name FROM    tb_product    INNER JOIN tb_subcategory         ON (tb_product.subcategory_id = tb_subcategory.subcategory_id)    INNER JOIN tb_vendor         ON (tb_product.vendor_id = tb_vendor.vendor_id);")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request, 'admin/product/view.html', {'product': data})
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


def useradd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/user/add.html')
    else:
        return redirect(home)

def useraddprocess(request):
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
        return redirect(useradd) 
    else:
        return redirect(useradd)

def userview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_user`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        return render(request,'admin/user/view.html', {'user': data})
    else:
        return redirect(home)

def userdelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_user` where `user_id` = {}".format(id))
    conn.commit()
    return redirect(userview)

def useredit(request,id):
     
    print(id)
    cur.execute("select * from `tb_user` where `user_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/user/edit.html', {'user': data})   

def userupdate(request):
    if request.method == 'POST':
        print(request.POST)
        uid = request.POST['txt0']
        uname = request.POST['txt1']
        uemail = request.POST['txt2']
        upass = request.POST['txt3']
        uadd = request.POST['txt4']
        uphoto = request.POST['txt5']
        udetails = request.POST['txt6']
        cur.execute("update `tb_user` set `user_name` ='{}', `user_email` ='{}', `user_password` ='{}',`user_address` ='{}', `user_photo` ='{}', `user_details` ='{}' where `user_id`='{}'".format(uname,uemail,upass,uadd,uphoto,udetails,uid))
        conn.commit()
        return redirect(userview) 
    else:
        return redirect(userview)


def feedbackadd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_user`")
        data = cur.fetchall()
        #return list(data)
        print(list(data))
        cur.execute("SELECT * FROM `tb_vendor`")
        datas = cur.fetchall()
        #return list(datas)
        print(list(datas))
        return render(request,'admin/feedback/add.html', {'user': data, 'vendor': datas})
    else:
        return redirect(home)

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
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT    tb_feedback.feedback_id    , tb_feedback.feedback_details    , tb_feedback.feedback_date    , tb_user.user_name    , tb_vendor.vendor_name FROM    tb_feedback    INNER JOIN tb_user         ON (tb_feedback.user_id = tb_user.user_id)    INNER JOIN tb_vendor         ON (tb_feedback.vendor_id = tb_vendor.vendor_id);")
        data = cur.fetchall()
        print(list(data))
        return render(request, 'admin/feedback/view.html', {'feedbacks': data})
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


def vendoradd(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        return render(request,'admin/vendor/add.html')
    else:
        return redirect(home)

def vendoraddprocess(request):
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
        return redirect(vendoradd) 
    else:
        return redirect(vendoradd)

def vendorview(request):
    if 'admin_id' in request.COOKIES and request.session.has_key('admin_id'):
        cur.execute("SELECT * FROM `tb_vendor`")
        data = cur.fetchall()
        print(list(data))
        return render(request, 'admin/vendor/view.html', {'vendor': data})
    else:
        return redirect(home)

def vendordelete(request,id):
     
    #id = request.GET['id']
    #id = User.objects.get(id=id)
    print(id)
    cur.execute("delete from `tb_vendor` where `vendor_id` = {}".format(id))
    conn.commit()
    return redirect(vendorview)

def vendoredit(request,id):
     
    print(id)
    cur.execute("select * from `tb_vendor` where `vendor_id` = {}".format(id))
    data = cur.fetchone()
    #return list(data)
    print(list(data))
    return render(request, 'admin/vendor/edit.html', {'vendor': data})   

def vendorupdate(request):
    if request.method == 'POST':
        print(request.POST)
        vendorid = request.POST['text0']
        vendorname = request.POST['text1']
        vendoremail = request.POST['text2']
        vendorpassword = request.POST['text3']
        vendorgender = request.POST['text4']
        vendoraddress = request.POST['text5']
        vendorimagepath = request.POST['text7']
        cur.execute("update `tb_vendor` set `vendor_name` ='{}', `vendor_email` ='{}', `vendor_password` ='{}',`vendor_gender` ='{}', `vendor_address` ='{}', `vendor_image_path` ='{}' where `vendor_id`='{}'".format(vendorname,vendoremail,vendorpassword,vendorgender,vendoraddress,vendorimagepath,vendorid))
        conn.commit()
        return redirect(vendorview) 
    else:
        return redirect(vendorview)


def loginadd(request):
    return render(request,'admin/login/add.html')


def loginprocess(request):
    if request.method == 'POST':
        print(request.POST)
        admin_email = request.POST['txt1']
        admin_password = request.POST['txt2']
        print("Yes")
        cur.execute("select * from `tb_admin` where admin_email ='{}' and admin_password  ='{}'".format(admin_email,admin_password))
        data = cur.fetchone()
        print(data)
        #Check Data is Present or not
        if data is not None:
            if len(data) > 0:
                #Fetch Data
                admin_id = data[0]
                admin_email = data[2]
                print(admin_id)
                print(admin_email)
                #Session Create Code
                request.session['admin_id'] = admin_id
                request.session['admin_email'] = admin_email
                #Session Create Code
                #Cookie Code
                response = redirect(dash)
                response.set_cookie('admin_id', admin_id)
                response.set_cookie('admin_email', admin_email)
                return response
                #Cookie Code
            else:
                return redirect(loginadd)
        return redirect(loginadd)
    else:
        return redirect(loginadd)


def loginchange(request):
    return render(request,'admin/login/change.html')


def loginforgot(request):
    return render(request,'admin/login/forgot.html')


def slogout(request):
    del request.session['admin_id']
    del request.session['admin_email']
    response = redirect(loginadd)
    response.delete_cookie('admin_id')
    response.delete_cookie('admin_email')
    return response