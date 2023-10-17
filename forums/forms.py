from .models import Events,Notices, Forum, JoinReq
from django import forms

class ScheduleForm(forms.ModelForm):
    def __init__(self,user=None,*args,**kwargs):
        self.forum = user.mod_forums.all()
        super(ScheduleForm,self).__init__(*args,**kwargs)
        self.fields['forum'].queryset = self.forum
    class Meta():
        model = Events
        fields = ['forum', 'title', 'about', 'date', 'is_public', 'users_added']
        
class NoticeForm(forms.ModelForm):
    def __init__(self,user=None,*args,**kwargs):
        self.forum = user.mod_forums.all()
        super(NoticeForm,self).__init__(*args,**kwargs)
        self.fields['forum'].queryset = self.forum
    class Meta:
        model = Notices
        fields = ['forum','title','about']
        
class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name','about','is_public','pic']

    
class JoinReqForm(forms.ModelForm):
    class Meta:
        model = JoinReq
        fields = ['user']