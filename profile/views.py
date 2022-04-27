from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import UserProfile
from .forms import ContactForm


def profile(request):
    """ Returns Profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)
    confirm_msg = ''

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            confirm_msg = 'Saved Successfully'

    form = ContactForm(instance=user_profile)
    
    template = 'profile/profile.html'
    context = {
        'user_profile': user_profile,
        'form': form,
        'confirm_msg': confirm_msg
    }
    return render(request, template, context)