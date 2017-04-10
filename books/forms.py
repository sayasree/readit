from django import forms
from .models import Book, Author

class ReviewForm(forms.Form):
    '''
    Form for reviewing a book
    '''
    is_favourite = forms.BooleanField( label='Favourite?', 
                                help_text="In your top 100 books all the time?", 
                                required=False)
                                
    review = forms.CharField(widget=forms.Textarea, min_length=10,
                    error_messages = {
                            'required' :  'Please enter your review',
                            'min_length' : 'Please write a review that has 10 characters (You have written (%show_value) characters)'
                        }
                        )
                        
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'authors']
        
    def clean(self):
        # Call the clean method of the super to maintain the main validation and error messages
        # super(BookForm, self).clean()   # This is older syntax
        super().clean()

        try:
            title = self.cleaned_data.get('title')
            authors = self.cleaned_data.get('authors')
            book = Book.objects.get(title=title, authors=authors)
            
            # If there is match, then the control comes here and it indicates that there a books with the same title and the authors and hence it is a duplicate
            raise forms.ValidationError("There book: {} by authors: {} already exists".format(title, book.list_authors()),
                                       code="BookExists")
        except Book.DoesNotExist:
            return self.cleaned_data
            
            
            

        
        