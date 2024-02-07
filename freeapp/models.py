
from django.db import models

# Create your models here.

class buyer_reg_tb(models.Model):
	Fname=models.CharField(max_length=100,null=False)
	# Lname=models.CharField(max_length=100,null=False)
	Email=models.CharField(max_length=100,null=False)
	Password=models.CharField(max_length=100,null=False)
	# Cpassword=models.CharField(max_length=100,null=False)

	Phone=models.CharField(max_length=15,null=False)
	Address=models.CharField(max_length=15,null=False)
	District=models.CharField(max_length=100,null=False)
	# Pincode=models.CharField(max_length=15,null=False)

class seller_reg_tb(models.Model):
	Fname=models.CharField(max_length=100,null=False)
	# Lname=models.CharField(max_length=100,null=False)
	Email=models.CharField(max_length=100,null=False)
	Password=models.CharField(max_length=100,null=False)
	# Cpassword=models.CharField(max_length=100,null=False)

	Phone=models.CharField(max_length=15,null=False)
	Address=models.CharField(max_length=15,null=False)
	District=models.CharField(max_length=100,null=False)
	# Pincode=models.CharField(max_length=15,null=False)

	
class bank_details_tb(models.Model):
	Seller=models.ForeignKey(seller_reg_tb, on_delete=models.CASCADE)
	account_number=models.CharField(max_length=100,null=False)
	ifsecode=models.CharField(max_length=100,null=False)
	bank=models.CharField(max_length=100,null=False)
	branch=models.CharField(max_length=100,null=False)




		

class category_tb(models.Model):
	Name=models.CharField(max_length=100,null=False)
		
class admin_tb(models.Model):
	Email=models.CharField(max_length=100,null=False)
	Password=models.CharField(max_length=100,null=False)

class f_details_tb(models.Model):
	Seller=models.ForeignKey(seller_reg_tb, on_delete=models.CASCADE)
	Title=models.CharField(max_length=100,null=False)
	Catname=models.ForeignKey(category_tb, on_delete=models.CASCADE)
	File=models.FileField(upload_to="freestuff_details")
	Describtion=models.CharField(max_length=300,null=False)
	Date=models.CharField(max_length=100,null=False)
	Price=models.CharField(max_length=100,null=False)
	Status=models.CharField(max_length=100,null=False)

class f_bokking_tb(models.Model):
	Buyer=models.ForeignKey(buyer_reg_tb, on_delete=models.CASCADE)
	Seller=models.ForeignKey(seller_reg_tb, on_delete=models.CASCADE)
	Free_details=models.ForeignKey(f_details_tb, on_delete=models.CASCADE)
	Date=models.CharField(max_length=100,null=False)
	Status=models.CharField(max_length=100,null=False)

class payment_tb(models.Model):
	Freebook=models.ForeignKey(f_bokking_tb, on_delete=models.CASCADE)
	Amount=models.CharField(max_length=100,null=False)
	Date=models.CharField(max_length=100,null=False)
	Status=models.CharField(max_length=100,null=False)

class exchange_tb(models.Model):
	Buyer=models.ForeignKey(buyer_reg_tb, on_delete=models.CASCADE)
	Seller=models.ForeignKey(seller_reg_tb, on_delete=models.CASCADE)
	Free_details=models.ForeignKey(f_details_tb, on_delete=models.CASCADE)
	Title=models.CharField(max_length=100,null=False)
	Catname=models.ForeignKey(category_tb, on_delete=models.CASCADE)
	File=models.FileField(upload_to="freestuff_details")
	Describtion=models.CharField(max_length=300,null=False)
	Date=models.CharField(max_length=100,null=False)
	Status=models.CharField(max_length=100,null=False)

class webreview_tb(models.Model):
	Name=models.CharField(max_length=100,null=False)
	Email=models.CharField(max_length=100,null=False)
	Subject=models.CharField(max_length=100,null=False)
	Feedback=models.CharField(max_length=100,null=False)