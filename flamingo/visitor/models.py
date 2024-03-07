from django.db import models
from _utils.codes import create_char_code

###
'''
	SESSION MODEL:
	Collect the ip and timestamp each time a new session occurs. A session
	should end when the browser is closed.
'''
class Session(models.Model):
	session_key = models.CharField(
		max_length = 50,
		default = create_char_code( length = 36 ),
	)
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
		default = create_char_code(),
		unique = True
	)
	sessions = models.ManyToManyField( Session	)
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
	CUSTOMER MODEL:
	When a transaction occurs with no user logged in, the information collected
	during the transaction will be used to create a customer account (tied to their
	email address) with a unique customer code, as well as a user profile that
	contains more information.
'''
class Customer(models.Model):
	customer_code = models.CharField(
		max_length = 16,
		default = create_char_code(length = 16),
		unique = True,
	)
	name = models.CharField( max_length = 100, default = 'name' )
	email = models.EmailField()
	visitor_ids = models.ManyToManyField( Visitor, null = True, default=None )
	created = models.DateTimeField( auto_now_add = True )

###
'''
	USER MODEL:
	A user profile is generated whenever a transaction occurs
'''
class User(models.Model):
	customer = models.ForeignKey(Customer, on_delete = models.CASCADE, default='')
	is_active = models.BooleanField(default = False)
	password = models.CharField(max_length = 100, default = 'password')
	last_login = models.DateTimeField( default = None )
	
	def __str__(self):
		return self.customer.name

###