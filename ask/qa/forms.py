# -- coding: utf-8 --
from django import forms
from models import Question, Answer

class AskForm(forms.Form):
    title = forms.CharField(max_length=255, widget=forms.Textarea)
    text = forms.CharField(widget=forms.Textarea)
    
    def __init__(self, *args, **kwargs):
        super(AskForm, self).__init__(*args, **kwargs)
    def save(self):
        if self._user.is_authenticated():
            self.cleaned_data['author'] = self._user
        question = Question(**self.cleaned_data)
        question.save()
        return question
class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    def save(self):
        if self._user.is_authenticated():
            self.cleaned_data['author'] = self._user
        url = '/question/'+ str(self.cleaned_data['question'])+'/' # bad pracrtice hardcoded link
        self.cleaned_data['question'] = Question.objects.get(id=self.cleaned_data['question'])
        answer = Answer(**self.cleaned_data)
        answer.save()
        return url
#        return answer #why? fat controller?
class SignupForm(forms.Form):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=255)
    password = forms.CharField(max_length=255)
    
class LoginForm(forms.Form): 
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput, max_length=255)
   
