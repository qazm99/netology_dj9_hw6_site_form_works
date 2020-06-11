from django.contrib import admin

from .models import Car, Review
from .forms import ReviewAdminForm


class CarAdmin(admin.ModelAdmin):
    fields = ("brand", "model", "review_count")
    list_display = ("model", "brand", "review_count")
    list_filter = ("brand", "model")
    search_fields = ("brand", "model")


class ReviewAdmin(admin.ModelAdmin):
    form = ReviewAdminForm
    list_display = ("car", "title")
    list_filter = ("car", "title")
    search_fields = ("car", "title")
    ordering = ("-title",)


admin.site.register(Car, CarAdmin)
admin.site.register(Review, ReviewAdmin)
