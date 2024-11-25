from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, label="Имя пользователя")
    email = forms.EmailField(label="Электронная почта")
    password = forms.CharField(widget=forms.PasswordInput, label="Пароль")


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100, label="Ваше имя")
    email = forms.EmailField(label="Электронная почта")
    message = forms.CharField(widget=forms.Textarea, label="Сообщение")  


class BookForm(forms.Form):
    name_book = forms.CharField(max_length=200, label="Название книги")
    author = forms.CharField(max_length=100, label="Автор книги") 