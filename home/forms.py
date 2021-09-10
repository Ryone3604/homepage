from django import forms
from django.core.mail import EmailMessage

class InquiryForm(forms.Form):
    name = forms.CharField(label='お名前', max_length=30)
    email = forms.EmailField(label='メールアドレス')
    inquiry = forms.CharField(label='お問い合わせ内容',widget=forms.Textarea(attrs={'cols':80,'rows':10}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        inquiry = self.cleaned_data['inquiry']
        
        message = EmailMessage(subject=name + "からの問い合わせ",
                                body=inquiry,
                                from_email=email,
                                to=["0927ryota.Sgmail.com"],
                                cc=[email])
        message.send()
    