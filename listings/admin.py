from django.contrib import admin
from .models import Listing
# Register your models here.
class ListingAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
    list_display_links = ('id', 'title')
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode', 'price')
    list_per_page = 25
#커스토마이즈 애드민 스터프 포 리스팅 앱
#models.py에서 데이터베이스에 들어간 테이블 모델을 만들었으면 이곳에서 레지스터를 하면 로컬호스트 애드민에서 볼수있음.
admin.site.register(Listing, ListingAdmin)