from django.contrib import admin
from .models import Medicine, Order

# Admin for Medicine Model
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'cost', 'brand', 'cure_for', 'image_preview')  # Display fields
    search_fields = ('name', 'brand')  # Search by name and brand
    list_filter = ('brand',)  # Filter by brand
    
    def image_preview(self, obj):
        if obj.image:
            return f"<img src='{obj.image.url}' width='50' height='50' />"
        return "-"
    image_preview.allow_tags = True
    image_preview.short_description = 'Image Preview'

# Admin for Order Model
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'medicine',)  # Display fields
    search_fields = ('patient__name', 'medicine__name')  # Search patient and medicine names
      # Filter by order date

# Register models to admin site
admin.site.register(Medicine, MedicineAdmin)
admin.site.register(Order, OrderAdmin)
