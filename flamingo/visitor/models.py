from django.db import models
from _utils.codes import createCharacterCode

###
'''
	SESSION MODEL:
	Collect the ip and timestamp each time a new session occurs. A session
	should end when the browser is closed.
'''
class Session(models.Model):
	ip = models.CharField(
		max_length = 15,
		default = '000.000.000.000'
	)
	timestamp = models.DateTimeField( auto_now_add = True )	

###
'''
	VISITOR MODEL:
	Create a cookie in the browser to assign a visitor code. This code will be
	used to track the number of sessions, as well as the total number of pages
	that have been visited.
'''
class Visitor(models.Model):
	visitorCode = models.CharField(
		max_length = 16,
		default = createCharacterCode(),
		unique = True
	)
	sessions = models.ManyToManyField(
		Session,
		on_delete = models.PROTECT,
	)
	sessionCount = models.IntegerField(
		default = 1
	)
	pageCount = models.IntegerField(
		default = 1
	)
	
	def __str__(self):
		return self.visitorCode

###
'''
	USER MODEL:
	A user profile is generated whenever a transaction occurs
'''
class User(models.Model):

	def __str__(self):
		return self.customerAccount.customerCode

###
'''
	CUSTOMER MODEL:
	When a transaction occurs with no user logged in, the information collected
	during the transaction will be used to create a customer account (tied to their
	email address) with a unique customer code, as well as a user profile that
	contains more information.
'''
class Customer(models.Model):
	customerCode = models.CharField(
		max_length = 16,
		default = createCharacterCode(),
		unique = True,
	)
	visitorAccounts = models.ManyToManyField(
		Visitor,
		on_delete = models.PROTECT,
	)
	email = models.EmailField()
	created = models.DateTimeField( auto_now_add = True )
	userProfile = models.ForeignKey(
		User,
		on_delete = models.PROTECT,
		null = False
	)