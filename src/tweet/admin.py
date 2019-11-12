from django.contrib import admin
from .models import Tweet
from django import forms


class FormTweetAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormTweetAdmin, self).__init__(*args, **kwargs)

    def clean(self):
        tweet = self.cleaned_data.get('content')
        username = self.cleaned_data.get('username')

        if tweet is None:
            raise forms.ValidationError(f'Tweet cannot be blank', code='blank tweet')
        if username is None:
            raise forms.ValidationError(f'User cannot be blank', code='user blank')

        return self.cleaned_data

    def save(self, commit=True):
        return super(FormTweetAdmin, self).save(commit=commit)


class TweetAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'date_time')
    form = FormTweetAdmin


admin.site.register(Tweet, TweetAdmin)