# importing the user model, the bult-in user model
from django.contrib.auth.models import User

def project_context(request):
    context = {
        # keyword argument that be accessible in the templates that we're building
        'me': User.objects.first(),
    }
    return context