from django.contrib import admin

from .models import Book, Author

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    fieldsets = [ 
                ("Book Details", {"fields" : ["title", "authors"]}),
                ("Reivew", {"fields" : ["is_favourite", "review", "reviewed_by", "date_reviewed"]}),
            ]
    readonly_fields = ("date_reviewed",)    # Make the fields readonly
    
    def book_authors(self, obj):
        return obj.list_authors()
        
    book_authors.short_description = "Author(s)"
    
    list_display = ("title", "book_authors", "date_reviewed", "is_favourite",)  # Displays the fields as the columns in a table
    list_editable = ("is_favourite",)
    list_display_links = ("title", "date_reviewed",)
    list_filter = ("title","is_favourite", )
    search_fields = ("title", "authors__name",)
    
    
# Register your models here.
#admin.site.register(Book)
# admin.site.register(Book, BookAdmin)  # Now this registration is done by the decorator
admin.site.register(Author)