
from random import choices
from django import forms
from .models import Registar1

class RegistrationForm(forms.ModelForm):
    class Meta:
        #GENDER_CHOICES = (
        #    ('M', 'Male'),
        #    ('F', 'Female'),
        #    ('O', 'Other'),
        #)
        
        #choice = forms.ChoiceField(label='Choice', choices=[('option1', 'Option 1'), ('option2', 'Option 2')])
        model = Registar1
        fields = ['first_name', 'last_name', 'b_year', 'card_id', 'passp', "gender", "pay", "class_user"]
        #gender = forms.ChoiceField(choices=GENDER_CHOICES)
       

# class UserForm(forms.Form):
#    first_name = forms.CharField(label='First Name', max_length=100)
#    last_name = forms.CharField(label='Last Name', max_length=100)
#    age = forms.IntegerField(label='Age')
    

#class GenderForm(forms.Form):
    #gender = forms.ChoiceField(label='Gender', choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])

        #widget = {
        #    "first_name": forms.TextInput(attrs={"placeholder": "Example Alex", "style": "width: 300px;"}),
        #    "last_name": forms.TextInput(attrs={"placeholder": "Example Alexs", "style": "width: 300px;"}),
        #    "b_year" : forms.TextInput(attrs={"placeholder": "Year Of Your berth", "style": "width: 300px; height: 200px;"}),
        #    "card_id" : forms.TextInput(attrs={"placeholder": "Example 58964GHL", "style": "width: 300px;"}),
        #} {{ form.as_p }}

# class UserInfoForm(forms.Form):
#    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Name', 'style': 'width: 300px;'}))
#    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder' :'Email', 'style': 'width: 300px;'}))


# class UserInfoForm(ModelForm):
#    class Meta:
#        model = User
#        fields = ['name', 'email']
#        widgets = {
#            'name': TextInput(attrs={
#                'class': "form-control",
#                'style': 'max-width: 300px;',
#                'placeholder': 'Name'
#                }),
#            'email': EmailInput(attrs={
#                'class': "form-control", 
#                'style': 'max-width: 300px;',
#                'placeholder': 'Email'
#                })
#        }


#<div class="container">
#    <h1>Form</h1>
#    <form action="{% url 'index' %}" method="post">
#        {% csrf_token %}
#    <div class="form-group">
#        {{ form.name }}
#    </div>
#    <div class="form-group">
#        {{ form.email }}
#    </div>
#    <div class="form-group">
#        <input class="btn btn-primary" type="submit" value="Submit">
#    </div>
#    </form>
#</div>