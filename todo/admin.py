from django.contrib import admin
from .models import Todo,Customer,Flight



class TodoAdmin(admin.ModelAdmin):
    list_display = ('title','name', 'finish', 'created')


admin.site.register(Todo, TodoAdmin)

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'tel')  # 顯示欄位
admin.site.register(Customer, CustomerAdmin)  # 加入至Administration(管理員後台)


class FlightAdmin(admin.ModelAdmin):
	list_display = ('user', 'items', 'fromname', 'description', 'finish',  'pd_number', 'pd_content', 'pub_date', 'pd_weight', 'pd_profit')
		
admin.site.register(Flight)

