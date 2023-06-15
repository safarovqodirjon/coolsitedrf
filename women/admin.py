from django.contrib import admin
from .models import Women, Category


# Register your models here.
@admin.register(Women)
class WomenAdmin(admin.ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass
