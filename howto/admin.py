from django.contrib import admin
# import your model
from howto.models import Comment

# # set up automated slug creation
class CommentAdmin(admin.ModelAdmin):
    model = Comment
    list_display = ('name', 'description',)
    # prepopulated_fields = {'slug': ('name',)}

# # and register it
admin.site.register(Comment, CommentAdmin)
