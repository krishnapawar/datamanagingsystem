from django.shortcuts import render, get_object_or_404,redirect
from.models import contact
from django.contrib import messages
from django.views.generic import DeleteView
from django.views.generic.edit import UpdateView,CreateView,DeleteView,FormView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.contrib.auth.models import User
from mytask.forms import ContactForm
# Create your views here.
def insert(request):
	if request.method == 'POST':
		if request.POST['name'] and request.POST['contactno'] and request.POST['district']:
			context = contact()
			context.name = request.POST['name']
			context.contactno = request.POST['contactno']
			context.district = request.POST['district']
			context.save()
			messages.success(request,f'your information enter susseccful')
	return render(request,'mytask/insart.html')


def showsub(request):
	context =  contact.objects.all()
	return render(request,'mytask/show-subcribe.html',{'q':context})


class ContactDeleteView(LoginRequiredMixin,DeleteView):
	model = contact
	success_url = '/'


class ContactUpdate(LoginRequiredMixin,UpdateView):
    model = contact
    fields = ['name','contactno','district']
    template_name_suffix = '_update_form'


class ContactCreate(LoginRequiredMixin,CreateView):
	model = contact
	fields = ['name','contactno','district']


class ContactView(FormView):
    template_name = 'contact.html'
    form_class = ContactForm
    success_url = '/show/'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        return super().form_valid(form)


'''def update(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            district = form.cleaned_data['district']
            try:
                send_mail(name,district, ['admin@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "contact_form.html", {'w': form})

def successView(request):
    return HttpResponse('Success! Thank you for your message.')

def update(request,p):
	if request.method == 'POST':
		form = ContactUpdateForm(request.POST, instance=instance)
		if form.is_valid():
			form.save()
			return redirect('showsubcriber')
	else:
		instance = get_object_or_404(contact,id=p)
		form = ContactUpdateForm(instance)
		return render(request,'mytask/contact_form.html',{'w':form})'''

	