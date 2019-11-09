from django.contrib import admin
from .models import User, Tweet
from django import forms


class FormTweetAdmin(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FormTweetAdmin, self).__init__(*args, **kwargs)

    def clean(self):
        tweet = self.cleaned_data.get('content')
        if len(tweet) > 140:
            raise forms.ValidationError(f'Tweet length has exceeded!, maximum length is 140 characters.',
                                        code='length exceeded')
        return self.cleaned_data

    def save(self, commit=True):
        super(FormTweetAdmin, self).save(commit=commit)


class UserAdmin(admin.ModelAdmin):
    list_display = ('name', 'email')


class TweetAdmin(admin.ModelAdmin):
    list_display = ('username', 'content', 'date_time')
    form = FormTweetAdmin


admin.site.register(User, UserAdmin)
admin.site.register(Tweet, TweetAdmin)
