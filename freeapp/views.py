from django.shortcuts import render
from freeapp.models import *
from django.http import HttpResponseRedirect
import datetime
from django.db.models import Q
import os
# Create your views here.

def search(request):
	title=request.GET["title"]
	products=f_details_tb.objects.filter(Title__icontains=title,Status="Pending")
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"shop-fullwidth.html",{"products":products,"sr":sr})

def index(request):
	data=f_details_tb.objects.filter(Status="Pending")
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"index-3.html",{"data":data,"sr":sr})

def index2(request):
	return render(request,"index-3.html")

def index3(request):
	data=f_details_tb.objects.filter(Status="Pending")
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"index-3.html",{"data":data,"sr":sr})


def index4(request):
	return render(request,"index-3.html")

def index5(request):
	return render(request,"index-3.html")

def index6(request):
	return render(request,"index-3.html")

def about(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"about-us.html",{"sr":sr})

def tc(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"terms&condition.html",{"sr":sr})

def category_view(request):
	if request.method == 'GET' and 'cat' in request.GET:
		cat=request.GET['cat']
		category=category_tb.objects.filter(Name=cat)
		for x in category:
			catid=x.id
		data=f_details_tb.objects.filter(Catname=catid)
		category=category_tb.objects.all()
		sr=f_details_tb.objects.filter(Status="Pending")
		return render(request,"catlist_view.html",{"products":data,"category":category,"sr":sr})
	else:
		data=f_details_tb.objects.all()
		category=category_tb.objects.all()
		sr=f_details_tb.objects.filter(Status="Pending")
		return render(request,"catlist_view.html",{"products":data,"category":category,"sr":sr})


def selindex(request):
	category=category_tb.objects.all()
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"sellerindex.html",{"category":category,"sr":sr})
 
def contact(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.method=="POST":
		varname=request.POST['con_name']
		varemail=request.POST['con_email'] 
		varsubject=request.POST['con_subject']
		varfeed=request.POST['con_message']
		query=webreview_tb(Name=varname,Email=varemail,Subject=varsubject,Feedback=varfeed)
		query.save()
		return render(request,"contact-us.html",{"sr":sr})
	else:
		return render(request,"contact-us.html",{"sr":sr})


def shop(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	products=f_details_tb.objects.filter(Status="Pending") 
	return render(request,"shop-fullwidth.html",{"products":products,"sr":sr})

def admin_index(request):
	return render(request,"admin/index.html")


def buyer_register(request):
	if request.method=="POST":
		varfname=request.POST['FirstName']
		varemail=request.POST['EmailAddress'] 
		varpassword=request.POST['Password']
		vardistrict=request.POST['District']
		varphoneno=request.POST['phoneno']
		varaddress=request.POST['Address']
		check= buyer_reg_tb.objects.all().filter(Email=varemail)
		if check:
			return render(request,"login-register.html",{'error':'Email already registered'})
		else:
			query=buyer_reg_tb(Fname=varfname,Email=varemail,Password=varpassword,District=vardistrict,Phone=varphoneno,Address=varaddress)
			query.save()
			return render(request,"login-register.html",{'success':'sucessfully registered'})
	else:
		return render(request,"login-register.html")


# def user_profile_update(request):
#     if request.method=="POST":
#         ii=request.session['id']
# 		varfname=request.POST['FirstName']
# 		varemail=request.POST['EmailAddress'] 
# 		varpassword=request.POST['Password']
# 		vardistrict=request.POST['District']
# 		varphoneno=request.POST['phoneno']
# 		varaddress=request.POST['Address']
#         buyer_reg_tb.objects.filter(id=ii).update(Fname=varfname,Email=varemail,Password=varpassword,District=vardistrict,Phone=varphoneno,Address=varaddress)
#         var=buyer_reg_tb.objects.all().filter(id=ii)
#         return render(request,'profile.html',{"data":data})
#     else:
#         ii=request.session['id']
#         var=addcustomer_tb.objects.all().filter(id=ii)
#         return render(request,'profile_update.html',{'data':var})


def seller_register(request):
	if request.method=="POST":
		varfname=request.POST['FirstName']
		# varlname=request.POST['LastName']
		varemail=request.POST['EmailAddress'] 
		varpassword=request.POST['Password']
		# varcpassword=request.POST['ConfirmPassword']
		vardistrict=request.POST['District']
		# varpincode=request.POST['pincode']
		varphoneno=request.POST['phoneno']
		varaddress=request.POST['Address']
		check= seller_reg_tb.objects.all().filter(Email=varemail)
		if check:
			return render(request,"sellogin-register.html",{'error':'Email already registered'})
		else:
			query=seller_reg_tb(Fname=varfname,Email=varemail,Password=varpassword,District=vardistrict,Phone=varphoneno,Address=varaddress)
			query.save()
			return render(request,"sellogin-register.html",{'success':'sucessfully registered'})
	else:
		return render(request,"sellogin-register.html")


def Buyerlogin_check(request):
	if request.method=="POST":
		varemail=request.POST['EmailAddress']
		varpassword=request.POST['Password']
		check=buyer_reg_tb.objects.filter(Email=varemail,Password=varpassword)
		products=f_details_tb.objects.filter(Status="Pending")
		if check:
			for x in check:
				request.session["buid"]=x.id
				return render(request,"shop-fullwidth.html",{"success":"Login Sucess","products":products})
		else:
			return render(request,"login-register.html",{"error":"Invalid Details or Not Registered"})
	else:
		return render(request,"login-register.html")

def Sellerlogin_check(request):
	if request.method=="POST":
		varemail=request.POST['EmailAddress']
		varpassword=request.POST['Password']
		check=seller_reg_tb.objects.filter(Email=varemail,Password=varpassword)
		category=category_tb.objects.all()
		if check:
			for x in check:
				request.session["suid"]=x.id
				sid= request.session["suid"]
				bankcheck=bank_details_tb.objects.filter(Seller=sid)
				if bankcheck:
					return render(request,"sellerindex.html",{"success":"Login Sucess","category":category})
				else:
					return render(request,"sellerbank_details.html",{"message":"Please fill bank details"})
		else:
			return render(request,"sellogin-register.html",{"error":"Invalid Details or Not Registered"})
	else:
		return render(request,"sellogin-register.html")

def logout(request):
	if request.session.has_key("buid"):
		del request.session['buid']
		return HttpResponseRedirect('/')
	elif request.session.has_key("suid"):
		del request.session['suid']
		return HttpResponseRedirect('/')
	elif request.session.has_key("aid"):
		del request.session['aid']
		return HttpResponseRedirect('/')
	else:
		return HttpResponseRedirect('/')



def admin_login(request):
	bc=buyer_reg_tb.objects.all().count()
	sc=seller_reg_tb.objects.all().count()
	pc=f_details_tb.objects.all().count()
	cc=category_tb.objects.all().count()
	oc=f_bokking_tb.objects.all().count()
	ec=exchange_tb.objects.all().count()
	bac=bank_details_tb.objects.all().count()
	pac=payment_tb.objects.all().count()
	# data={"bc":bc,"sc":sc,"pc":pc,"cc":cc,"oc":oc,"ec":ec,"bac":bac,"pac":pac}
	if request.method=="POST":
		varemail=request.POST['Email']
		varpassword=request.POST['Password']
		check=admin_tb.objects.filter(Email=varemail,Password=varpassword)
		if check:
			for x in check:
				request.session["aid"]=x.id
				return render(request,"admin/index.html",{"bc":bc,"sc":sc,"pc":pc,"cc":cc,"oc":oc,"ec":ec,"bac":bac,"pac":pac,"success":"Login Sucess"})
		else:
			return render(request,"admin/auth-login.html",{"bc":bc,"sc":sc,"pc":pc,"cc":cc,"oc":oc,"ec":ec,"bac":bac,"pac":pac,"error":"Invalid Details or Not Registered"})
	else:
		return render(request,"admin/auth-login.html",{"bc":bc,"sc":sc,"pc":pc,"cc":cc,"oc":oc,"ec":ec,"bac":bac,"pac":pac})



def categories(request):
	if request.method=="POST":
		category=request.POST["list"]
		# price=request.POST["Price"]

		check=category_tb.objects.filter(Name=category)
		if check:
			return render(request,"admin/category_add.html")
		else:
			add=category_tb(Name=category)
			add.save()
			return render(request,"admin/category_add.html")
	else:
		return render(request,"admin/category_add.html")


def category_list_admin(request):
	dataset=category_tb.objects.all()
	return render(request,"admin/category_list_admin.html",{'dataset':dataset})

def category_delete_admin(request):
	cid=request.GET['cid']
	dataset=category_tb.objects.filter(id=cid).delete()
	return HttpResponseRedirect("/category_list_admin/")

def buyer_list_admin(request):
	dataset=buyer_reg_tb.objects.all()
	return render(request,"admin/buyer_list_admin.html",{'dataset':dataset})

def vreview(request):
	dataset=webreview_tb.objects.all()
	return render(request,"admin/viewreview.html",{'dataset':dataset})


def seller_list_admin(request):
	dataset=seller_reg_tb.objects.all()
	return render(request,"admin/seller_list_admin.html",{'dataset':dataset})

def product_list_admin(request):
	dataset=f_details_tb.objects.all()
	return render(request,"admin/product_list_admin.html",{'dataset':dataset})

def fbooking_list_admin(request):
	dataset=f_bokking_tb.objects.all()
	return render(request,"admin/fbooking_list_admin.html",{'dataset':dataset})

def Exchange_list_admin(request):
	dataset=exchange_tb.objects.all()
	return render(request,"admin/exglist_admin.html",{'dataset':dataset})

def Payment_list_admin(request):
	dataset=payment_tb.objects.all()
	return render(request,"admin/paylist_admin.html",{'dataset':dataset})

def Bankdetails_list_admin(request):
	dataset=bank_details_tb.objects.all()
	return render(request,"admin/Banklist_admin.html",{'dataset':dataset})

def product_details(request):
	if request.session.has_key("suid"):
		category=category_tb.objects.all()
		sr=f_details_tb.objects.filter(Status="Pending")
		if request.method=="POST":
			vartitle=request.POST['title']
			varcategory=request.POST['category']
			Date= datetime.datetime.now()
			varimage=request.FILES['image']
			vardescribtion=request.POST['description']
			varcategory=category_tb.objects.get(id=varcategory)
			vartype=request.POST['types']

			if vartype == "Paid stuff":
				varprice=request.POST['price']
				
			else:
				varprice="Free stuff"			
			Seller=request.session['suid']
			bankcheck=bank_details_tb.objects.filter(Seller=Seller)			
			Seller=seller_reg_tb.objects.get(id=Seller)

			
			check= f_details_tb.objects.filter(Seller=Seller,Title=vartitle,Describtion=vardescribtion,Catname=varcategory,Price=varprice)
			if bankcheck:

				if check:
					return render (request,"sellerindex.html",{"error":"allready submitted","category":category})
				else:
					query=f_details_tb(Seller=Seller,Title=vartitle,Catname=varcategory,Describtion=vardescribtion,File=varimage,Price=varprice,Status="Pending",Date=Date)
					query.save()
					return render (request,"sellerindex.html",{"message":"submitted","category":category})
			else:
				# query=f_details_tb(Seller=Seller,Title=vartitle,Catname=varcatname,Describtion=vardescribtion,File=varimage,Price=varprice,Status="Pending",Date=Date)

				return render(request,"sellerbank_details.html",{"message":"Please fill bank details to add products. Then add the products."})
		else:
			return render (request,"sellerindex.html",{"category":category,"sr":sr})
	else:
		return render(request,"sellogin-register.html")



def singleproduct_view(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	proid=request.GET['pid']
	dataset=f_details_tb.objects.filter(id=proid)
	return render(request,"single-product-tab-style-left.html",{'dataset':dataset,"sr":sr})


def fbooking(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key("buid"):
		proid=request.GET['pid']
		dataset=f_details_tb.objects.filter(id=proid)
		for x in dataset:
			Seller=x.Seller
		Buyer=request.session['buid']
		Buyer=buyer_reg_tb.objects.get(id=Buyer)
		proidd=f_details_tb.objects.get(id=proid)
		fdata=f_details_tb.objects.filter(id=proid)
		for x in fdata:
			ftype=x.Price
			fid=x.id

		# Seller=seller_reg_tb.objects.get(id=Seller)
		Date= datetime.datetime.now()
		check=f_bokking_tb.objects.filter(Seller=Seller,Buyer=Buyer,Free_details=proidd)
		if check:
			dataset=f_details_tb.objects.filter(id=proid)
			return render(request,"single-product-tab-style-left.html",{'dataset':dataset,"sr":sr}) 
		else:
			if ftype == "Free stuff":		
				query=f_bokking_tb(Seller=Seller,Buyer=Buyer,Free_details=proidd,Status="Booked",Date=Date)
				query.save()
				f_details_tb.objects.filter(id=fid).update(Status="Sold Out")
			else:
				query=f_bokking_tb(Seller=Seller,Buyer=Buyer,Free_details=proidd,Status="Pending",Date=Date)
				query.save()
			products=f_details_tb.objects.filter(Status="Pending")
			return render(request,"shop-fullwidth.html",{"products":products,"sr":sr})
	else:
		return render(request,"sellogin-register.html")


def myorder(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('buid'):
		bid=request.session['buid']
		dataset=f_bokking_tb.objects.filter(Buyer=bid)
		return render(request,"userbooking_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"login-register.html")


def orders(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('suid'):
		sid=request.session['suid']
		dataset=f_bokking_tb.objects.filter(Seller=sid,Status="Booked")
		return render(request,"sellerbooking_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"sellogin-register.html")

def booking(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.method=="POST":
		uid=request.session['buid']
		uidd=buyer_reg_tb.objects.get(id=uid)
		cdate=datetime.datetime.now().date()
		# oid=request.POST['oid']
		bid=request.POST['bid']
		fbid= f_bokking_tb.objects.get(id=bid)
		uidd=buyer_reg_tb.objects.get(id=uid)
		add=payment_tb(Freebook=fbid,Status="paid",Date=cdate)
		add.save()
		dataset=f_bokking_tb.objects.filter(id=bid)
		for x in dataset:
			fid=x.Free_details.id
		dataset=f_bokking_tb.objects.filter(id=bid).update(Status="Booked") 
		data=f_details_tb.objects.filter(id=fid).update(Status="Sold Out")
		bid=request.session['buid']
		dataset=f_bokking_tb.objects.filter(Buyer=bid)
		return render(request,"userbooking_view.html",{'dataset':dataset,"sr":sr})
	else:
		bid=request.GET['id']
		data=f_bokking_tb.objects.all().filter(id=bid)
		return render(request,"payment.html",{'data':data,"sr":sr})


def sellerapproval(request):
	alid=request.GET['apid']
	dataset=f_bokking_tb.objects.filter(id=alid)
	for x in dataset:
		fid=x.Free_details.id 
	data=f_details_tb.objects.filter(id=fid).update(Status="Approved")
	f_bokking_tb.objects.filter(Free_details=fid).update(Status="rejected")
	f_bokking_tb.objects.filter(id=alid).update(Status="Approved")
	return HttpResponseRedirect("/orders/")
	# sid=request.session['suid']
	# dataset=f_booking_tb.objects.filter(Seller=sid)
	# return render(request,"sellerbooking_view.html",{'dataset':dataset})

def exchange(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key("buid"):
		proid=request.GET['pid']
		dataset=f_details_tb.objects.filter(id=proid)
		for x in dataset:
			Seller=x.Seller
		Buyer=request.session['buid']
		Buyer=buyer_reg_tb.objects.get(id=Buyer)
		proidd=f_details_tb.objects.get(id=proid)
		# Seller=seller_reg_tb.objects.get(id=Seller)
		if request.method=="POST":
			products=f_details_tb.objects.filter(Status="Pending")
			vartitle=request.POST['title']
			varcategory=request.POST['category']
			Date= datetime.datetime.now()
			varimage=request.FILES['image']
			vardescribtion=request.POST['description']
			varcatname=category_tb.objects.get(id=varcategory)
			check= exchange_tb.objects.filter(Seller=Seller,Title=vartitle,Describtion=vardescribtion,Catname=varcatname,File=varimage)
			if check:
				return render (request,"shop-fullwidth.html",{"error":"allready submitted","category":category,"products":products,"sr":sr})
			else:
				query=exchange_tb(Seller=Seller,Buyer=Buyer,Free_details=proidd,Title=vartitle,Catname=varcatname,Describtion=vardescribtion,File=varimage,Status="Pending",Date=Date)
				query.save()
				return render (request,"shop-fullwidth.html",{"message":"submitted","products":products,"sr":sr})
		else:
			proid=request.GET['pid']
			category=category_tb.objects.all()
			return render(request,"exchange_form.html",{"pid":proid,"category":category,"sr":sr})
	else:
		return render(request,"exchange_form.html")

def exgsel(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('suid'):
		sid=request.session['suid']
		dataset=exchange_tb.objects.filter(Seller=sid)
		return render(request,"sel_exchange_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"sellogin-register.html")

def exguser(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('buid'):
		bid=request.session['buid']
		dataset=exchange_tb.objects.filter(Buyer=bid)
		return render(request,"user_exchange_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"login-register.html")

def ustep(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"userstep.html",{"sr":sr})

def sstep(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	return render(request,"sellerstep.html",{"sr":sr})

def payment(request):
	return render(request,"payment.html")

def uprofile(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	uid=request.session["buid"]
	data=buyer_reg_tb.objects.filter(id=uid)
	return render(request,"profile.html",{"data":data,"sr":sr})

def uprofile_edit(request):
	if request.method=="POST":
		varfname=request.POST['name']
		varemail=request.POST['email'] 
		vardistrict=request.POST['district']
		varphoneno=request.POST['phone']
		varaddress=request.POST['address']
		uid=request.session["buid"]
		buyer_reg_tb.objects.filter(id=uid).update(Fname=varfname,Email=varemail,District=vardistrict,Phone=varphoneno,Address=varaddress)
		# data=buyer_reg_tb.objects.filter(id=uid)
		return HttpResponseRedirect("/uprofile/")
	else:
		sr=f_details_tb.objects.filter(Status="Pending")
		uid=request.session["buid"]
		data=buyer_reg_tb.objects.filter(id=uid)
		return render(request,"profile_update.html",{"data":data,"sr":sr})


def sprofile(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	uid=request.session["suid"]
	data=seller_reg_tb.objects.filter(id=uid)
	return render(request,"sprofile.html",{"data":data,"sr":sr})

def sprofile_edit(request):
	if request.method=="POST":
		varfname=request.POST['name']
		varemail=request.POST['email'] 
		vardistrict=request.POST['district']
		varphoneno=request.POST['phone']
		varaddress=request.POST['address']
		uid=request.session["suid"]
		seller_reg_tb.objects.filter(id=uid).update(Fname=varfname,Email=varemail,District=vardistrict,Phone=varphoneno,Address=varaddress)
		# data=buyer_reg_tb.objects.filter(id=uid)
		return HttpResponseRedirect("/sprofile/")
	else:
		sr=f_details_tb.objects.filter(Status="Pending")
		uid=request.session["suid"]
		data=seller_reg_tb.objects.filter(id=uid)
		return render(request,"sprofile_update.html",{"data":data,"sr":sr})


def selBank(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key("suid"):
		category=category_tb.objects.all()

		if request.method=="POST":
			varaccno=request.POST['Accno']
			varifse=request.POST['ifse']
			varbank=request.POST['bank']
			varbranch=request.POST['branch']
			sid=request.session['suid']
			Seller=seller_reg_tb.objects.get(id=sid)
			check= bank_details_tb.objects.filter(Seller=Seller,account_number=varaccno,ifsecode=varifse,bank=varbank,branch=varbranch)
			if check:
				return render (request,"sellerindex.html",{"error":"already submitted","category":category,"sr":sr})
			else:
				query=bank_details_tb(Seller=Seller,account_number=varaccno,ifsecode=varifse,bank=varbank,branch=varbranch)
				query.save()
				return render (request,"sellerindex.html",{"message":"submitted","category":category,"sr":sr})
		else:
	 		return render(request,"sellerbank_details.html")

def selproducts_details(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('suid'):
		sid=request.session['suid']
		dataset=f_details_tb.objects.filter(Seller=sid)
		return render(request,"selprt_details.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"sellogin-register.html")

def selnotification(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('suid'):
		sid=request.session['suid']
		dataset=f_bokking_tb.objects.filter(Seller=sid,Status="Booked")
		return render(request,"snot_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"sellogin-register.html")

def usernotification(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	if request.session.has_key('buid'):
		bid=request.session['buid']
		dataset=f_bokking_tb.objects.filter(Buyer=bid,Status="Booked")
		return render(request,"unot_view.html",{'dataset':dataset,"sr":sr})	
	else:
		return render(request,"login-register.html")


def prd_delete(request):
	prd=request.GET['pid']
	dataset=f_details_tb.objects.filter(id=prd).delete()
	return HttpResponseRedirect("/selproducts_details/")


def prd_edit(request):
	sr=f_details_tb.objects.filter(Status="Pending")
	category=category_tb.objects.all()
	if request.method=="POST":
		vartitle=request.POST['title']
		varcategory=request.POST['category']
		Date= datetime.datetime.now()
		
		vardescribtion=request.POST['description']
		varcatname=category_tb.objects.get(id=varcategory)
		vartype=request.POST['types']
		prd=request.GET['pid']
		imgup=request.POST['imgup']

		if vartype == "Paid stuff":
			varprice=request.POST['price']
			
		else:
			varprice="Free stuff"
		if imgup == "Yes":
				varimage=request.FILES['image']
				oldrec=f_details_tb.objects.all().filter(id=prd)
				updrec=f_details_tb.objects.get(id=prd)
				for x in oldrec:
					imgurl=x.File.url
					pathtoimage=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))+imgurl
					if os.path.exists(pathtoimage):
						os.remove(pathtoimage)
						print('Successfully deleted')
				updrec.File=varimage
				updrec.save()			
		# Seller=request.session['suid']
		# bankcheck=bank_details_tb.objects.filter(Seller=Seller)			
		# Seller=seller_reg_tb.objects.get(id=Seller)

		data=f_details_tb.objects.filter(id=prd).update(Title=vartitle,Catname=varcatname,Describtion=vardescribtion,Price=varprice)
		return HttpResponseRedirect("/selproducts_details/")

	else:
		prd=request.GET['pid']
		data=f_details_tb.objects.filter(id=prd)
		category=category_tb.objects.all()
		return render(request,"product_update.html",{"data":data,"category":category,"sr":sr})


def exgapproval(request):
	prd=request.GET['pid']
	data=exchange_tb.objects.filter(id=prd).update(Status="Approved")
	return HttpResponseRedirect("/exgsel/")
