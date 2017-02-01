from django.contrib import admin
from products.models import *

class ProductAdmin(admin.ModelAdmin):
	pass

class HistoryAdmin(admin.ModelAdmin):
	pass

class RecipeAdmin(admin.ModelAdmin):
	pass

class PreparationAdmin(admin.ModelAdmin):
	pass

class ProvenanceAdmin(admin.ModelAdmin):
	pass

class ImpactAdmin(admin.ModelAdmin):
	pass

class ProductPhotoAdmin(admin.ModelAdmin):
	pass

class HistoryPhotoAdmin(admin.ModelAdmin):
	pass

class RecipePhotoAdmin(admin.ModelAdmin):
	pass

class PreparationPhotoAdmin(admin.ModelAdmin):
	pass

class ImpactPhotoAdmin(admin.ModelAdmin):
	pass

class ProductTextAdmin(admin.ModelAdmin):
	pass

class HistoryTextAdmin(admin.ModelAdmin):
	pass

class RecipeTextAdmin(admin.ModelAdmin):
	pass

class PreparationTextAdmin(admin.ModelAdmin):
	pass

class ImpactTextAdmin(admin.ModelAdmin):
	pass

class ProductHeaderAdmin(admin.ModelAdmin):
	pass

class HistoryHeaderAdmin(admin.ModelAdmin):
	pass

class RecipeHeaderAdmin(admin.ModelAdmin):
	pass

class PreparationHeaderAdmin(admin.ModelAdmin):
	pass

class ImpactHeaderAdmin(admin.ModelAdmin):
	pass


admin.site.register(Product, ProductAdmin)
admin.site.register(History, HistoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Provenance, ProvenanceAdmin)
admin.site.register(Preparation, PreparationAdmin)
admin.site.register(Impact, ImpactAdmin)
admin.site.register(ProductPhoto, ProductPhotoAdmin)
admin.site.register(HistoryPhoto, HistoryPhotoAdmin)
admin.site.register(RecipePhoto, RecipePhotoAdmin)
admin.site.register(PreparationPhoto, PreparationPhotoAdmin)
admin.site.register(ImpactPhoto, ImpactPhotoAdmin)
admin.site.register(ProductText, ProductTextAdmin)
admin.site.register(HistoryText, HistoryTextAdmin)
admin.site.register(RecipeText, RecipeTextAdmin)
admin.site.register(PreparationText, PreparationTextAdmin)
admin.site.register(ImpactText, ImpactTextAdmin)
admin.site.register(ProductHeader, ProductHeaderAdmin)
admin.site.register(HistoryHeader, HistoryHeaderAdmin)
admin.site.register(RecipeHeader, RecipeHeaderAdmin)
admin.site.register(PreparationHeader, PreparationHeaderAdmin)
admin.site.register(ImpactHeader, ImpactHeaderAdmin)
