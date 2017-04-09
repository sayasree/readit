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
        