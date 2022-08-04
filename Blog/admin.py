from django.contrib import admin
from Blog.models import Post, Tag, Comment
#from django_summernote.admin import SummernoteModelAdmin
# Register your models here.





# class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
#     list_display = ('title', 'slug', 'author',  'schedule_date', 'approved',)
#     search_field = ('title', 'slug', 'author', 'schedule_date', 'approved',)


#     summernote_fields = ('content',)


admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)