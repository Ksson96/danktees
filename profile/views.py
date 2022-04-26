from django.shortcuts import render, get_object_or_404
from .models import UserProfile


def profile(request):
    """ Returns Profile """
    user_profile = get_object_or_404(UserProfile, user=request.user)

    template = 'profile/profile.html'
    context = {
        'user_profile': user_profile
    }
    return render(request, template, context)