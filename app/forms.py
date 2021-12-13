from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import UserCreationForm

from .models import Comment
from .models import CustomUser
from .models import Subject


class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('username', 'email', 'city', 'knows', 'learns')

    learns = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Subject.objects.all(),
        required=True
    )

    knows = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Subject.objects.all(),
        required=True
    )


class CustomUserUpdateForm(UserChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserUpdateForm, self).__init__(*args, **kwargs)
        del self.fields['password']

    class Meta(UserChangeForm):
        model = CustomUser
        fields = (
            'username', 'email', 'first_name', 'last_name', 'description', 'image', 'city', 'knows',
            'learns'
        )

    learns = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Subject.objects.all(),
        required=True
    )

    knows = forms.ModelMultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Subject.objects.all(),
        required=True
    )


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', 'for_user', 'author')
        widgets = {
            'for_user': forms.HiddenInput(),
            'author': forms.HiddenInput(),
        }


class SearchAllForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchAllForm, self).__init__(*args, **kwargs)
        self.fields['knows'].label = 'Find people who knows'
        self.fields['learns'].label = 'Find people who learns'
        self.fields['city'].label = 'Show instructors from'

    class Meta:
        model = CustomUser
        fields = ('knows', 'learns', 'city')

    knows = forms.ModelChoiceField(
        Subject.objects.all(),
        required=False
    )
    learns = forms.ModelChoiceField(
        Subject.objects.all(),
        required=False
    )


class SearchMatchesForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchMatchesForm, self).__init__(*args, **kwargs)
        self.fields['knows'].label = 'I want to learn'
        self.fields['city'].label = 'Show matches from'

    class Meta:
        model = CustomUser
        fields = ('knows', 'city')

    knows = forms.ModelChoiceField(
        Subject.objects.all(),
        required=False
    )
