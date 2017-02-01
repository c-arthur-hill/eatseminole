from django.db import models
from django.conf import settings

class Product(models.Model):
	name = models.CharField(max_length=512)
	slug = models.SlugField()
	description = models.CharField(max_length=1024)
	sales = models.IntegerField()
	price = models.DecimalField(max_digits=7, decimal_places=2, null=True, blank=True)
	#booleans used for matrix
	meat = models.BooleanField(default=False)
	MEAT_CHOICES = (
	('PO', 'Pork'),
	('BF', 'Beef'),
	('CH', 'Chicken'),
	('OT', 'Other'),
	('NA', 'Not Meat'),
	)
	meat_type = models.CharField(max_length=2, choices=MEAT_CHOICES, default='PO',)
	vegan = models.BooleanField(default=False)
	vegetarian = models.BooleanField(default=False)
	vegetable_heavy = models.BooleanField(default=False)
	low_sugar = models.BooleanField(default=False)
	gluten_free = models.BooleanField(default=False)
	lasts_a_week = models.BooleanField(default=False)
	lasts_a_month = models.BooleanField(default=False)
	low_preparation = models.BooleanField(default=False)
	#affiliated models
	producer = models.ForeignKey('Producer', on_delete=models.CASCADE, null=True, blank=True)
	history = models.OneToOneField('History', on_delete=models.CASCADE, null=True, blank=True)
	recipes = models.ManyToManyField('Recipe', null=True, blank=True)
	provenance = models.ForeignKey('Provenance', on_delete=models.CASCADE, null=True, blank=True)
	pairings = models.ManyToManyField('self', null=True, blank=True)
	same_producer = models.ManyToManyField('self', null=True, blank=True)
	preparation = models.ForeignKey('Preparation', on_delete=models.CASCADE, null=True, blank=True)
	environmental_impact = models.ForeignKey('Impact', on_delete=models.CASCADE, null=True, blank=True)


class Producer(models.Model):
	user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Article(models.Model):
	#base class for other articles
	title = models.CharField(max_length=512)
	slug = models.SlugField()
	description = models.CharField(max_length=1024)
	
class History(Article):
	#was this product originally from here
	heritage = models.BooleanField(default=False)	

class Recipe(Article):
	#prep time in minutes, difficulty: 1-10
	prep_time = models.IntegerField()
	dificulty = models.SmallIntegerField()

class Provenance(Article):
	#links in the distribution chain
	people_supported = models.SmallIntegerField()
		
class Preparation(Article):
	#prep time in minutes, difficulty: 1-10
	prep_time = models.IntegerField()
	difficulty = models.SmallIntegerField()

class Impact(Article):
	#an all in rating of how environmentally sustainable
	rating = models.SmallIntegerField()
	
class Photo(models.Model):
	#path used for s3 path, priority for position in article
	image = models.ImageField(upload_to='pictures/', null=True, blank=True)
	priority = models.IntegerField()
	alt = models.CharField(max_length=256)
	description = models.CharField(max_length=512)

class ProductPhoto(Photo):
	product = models.ForeignKey('Product')

class HistoryPhoto(Photo):
	history = models.ForeignKey('History')

class RecipePhoto(Photo):
	recipe = models.ForeignKey('Recipe')

class PreparationPhoto(Photo):
	preparation = models.ForeignKey('Preparation')

class ImpactPhoto(Photo):
	impact = models.ForeignKey('Impact')

class Text(models.Model):
	#text used for paragraph(s), priority for position in article
	text = models.TextField()
	priority = models.IntegerField()
	
class ProductText(Text):
	product = models.ForeignKey('Product')

class HistoryText(Text):
	history = models.ForeignKey('History')

class RecipeText(Text):
	recipe = models.ForeignKey('Recipe')

class PreparationText(Text):
	preparation = models.ForeignKey('Preparation')

class ImpactText(Text):
	impact = models.ForeignKey('Impact')

class Header(models.Model):
	#headers, priority used for position in article
	header = models.CharField(max_length=512)
	priority = models.IntegerField()

class ProductHeader(Header):
	product = models.ForeignKey('Product')

class HistoryHeader(Header):
	history = models.ForeignKey('History')

class RecipeHeader(Header):
	recipe = models.ForeignKey('Recipe')

class PreparationHeader(Header):
	preparation = models.ForeignKey('Preparation')

class ImpactHeader(Header):
	impact = models.ForeignKey('Impact')


