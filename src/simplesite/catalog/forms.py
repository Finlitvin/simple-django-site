from django.forms import ModelForm
#from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username']



#class AddBookForm(ModelForm):
#    class Meta:
#        model = Book
#        fields = ['title', 'about_text',]