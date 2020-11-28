from django import forms

from blog.models import Comment


class EmailPostForm(forms.Form):
    nama = forms.CharField(max_length=25)
    email_dari = forms.EmailField()
    email_kepada = forms.EmailField()
    komentar = forms.CharField(required=False, widget=forms.Textarea)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('nama', 'email', 'isi')
