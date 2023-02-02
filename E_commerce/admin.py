from django.contrib import admin

# Register your models here.
from E_commerce.models import Product,Customer,Brand,CostomerPanDetail,Order,OrderProduct

admin.site.register(Product)
admin.site.register(Customer)
admin.site.register(Brand)
admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(CostomerPanDetail)
