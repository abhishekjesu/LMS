# from django import forms
# from .models import BooksDB

# class BooksStore(forms.ModelForm):
#     class Meta:
#         model = BooksDB
#         fields = ['title', 'author', 'publisher', 'language' , 'copies']
#         widgets = {
#             'title': forms.TimeInput(attrs={'class':'form-control'}),
#             'author': forms.TimeInput(attrs={'class':'form-control'}),
#             'publisher': forms.TimeInput(attrs={'class':'form-control'}),
#             'language': forms.TimeInput(attrs={'class':'form-control'}),
#             'copies': forms.TimeInput(attrs={'class':'form-control'}),
#         }