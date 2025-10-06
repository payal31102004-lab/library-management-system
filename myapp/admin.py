from django.contrib import admin

from myapp.models import admintbl, manage_book_tbl, manage_member_tbl, issue_return_tbl, return_book_tbl

# Register your models here.
admin.site.register(admintbl)
admin.site.register(manage_book_tbl)
admin.site.register(manage_member_tbl)
admin.site.register(issue_return_tbl)
admin.site.register(return_book_tbl)