from django.contrib import admin
from .models import Todo, Customer, Flight, first_page


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'tel')  # 顯示欄位


admin.site.register(Customer, CustomerAdmin)  # 加入至Administration(管理員後台)


class FlightAdmin(admin.ModelAdmin):
    list_display = ('user', 'items', 'fromname', 'description', 'finish',
                    'pd_number', 'pd_content', 'pub_date', 'pd_weight', 'pd_profit', 'pd_photo')


admin.site.register(Flight)


class first_page_admin(admin.ModelAdmin):
    list_display = ()


admin.site.register(first_page)
