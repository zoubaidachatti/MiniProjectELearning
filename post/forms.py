from django import forms
from .models import Post
#DataFlair
class PostCreate(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'

class UpdatePostForm(forms.ModelForm):

	class Meta:
		model = Post
		fields = [ 'title' , 'detail' , 'state' , 'logo' , 'category' ]

	def save(self, commit=True):
		post = self.instance
        
		post.state = self.cleaned_data['state']
		post.detail = self.cleaned_data['detail']
		post.title = self.cleaned_data['title']
		post.category = self.cleaned_data['category']
        

		if self.cleaned_data['logo']:
			post.logo = self.cleaned_data['logo']

		if commit:
			post.save()
		return post