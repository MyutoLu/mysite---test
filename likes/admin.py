from django.contrib import admin
from .models import LikeCount, LikeRecord

@admin.register(LikeCount)
class LikeCountAdmin(admin.ModelAdmin):
    list_display = ('id','content_type','content_object','liked_num')

@admin.register(LikeRecord)
class LikeRecordtAdmin(admin.ModelAdmin):
    list_display = ('id','content_type','content_object','user')