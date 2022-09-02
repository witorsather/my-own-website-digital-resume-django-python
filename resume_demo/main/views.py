from django.shortcuts import render
# want import messagens is when a form when a form is valid and when a form is saved, we will then to render a message, so that the message pops up
from django.contrib import messages
# import all of these different models create in file "models.py"
from .models import (
    UserProfile,
    Blog,
    Portfolio,
    Testimonial,
    Certificate
)

#using the generic views, template view list view form
from django.views import generic
from . forms import ContactForm

# Create your views here.
# these built-in form views they're all class-based views, but they're built specifically for a tasks that happen regularly
# for instance a list view you're rendering a list of objects so it just does all the hard graft in the background so you've got you can render
# a web page they say a form view with only two or three lines of code
class IndexView(generic.TemplateView):
    # our home page
    template_name = "main/index.html"

    # def mean = defining a function
    def get_context_data(self, **kwargs):
        # we can actually render for loop using uh template filters
        context = super().get_context_data(**kwargs)
        # we're calling testimonial objects and we're filtering everything where is active equals true of the "models.py"
        # is active defaults to true but if in admin we click it to be untrue or false then it will no appear in the "def get_context_data"
        testimonials = Testimonial.objects.filter(is_active=True)
        certificates = Certificate.objects.filter(is_active=True)
        blogs = Blog.objects.filter(is_active=True)
        portfolio = Portfolio.objects.filter(is_active=True)

        # now in index we can reference testimonials and that will be a list of objects that we can render
        context["testimonials"] = testimonials
        context["certificates"] = certificates
        context["blogs"] = blogs
        context["portfolio"] = portfolio
        return context

# contac view this is a form view
class ContactView(generic.FormView):
    template_name = "main/contact.html"
    form_class = ContactForm
    # success url this is where the user will be redirected when the form is valid
    success_url = "/"

    # we then call the form valid method
    def form_valid(self, form):
        # we save the form instance
        form.save()
        # we send this message here to user
        messages.success(self.request, 'Thank you. We will be in touch soon.')
        return super().form_valid(form)

class PortfolioView(generic.ListView):
    model = Portfolio
    template_name = "main/portfolio.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

# page portfolio with 10 objects disponible
class PortfolioDetailView(generic.DetailView):
    model = Portfolio
    # filter true portfolio
    template_name = "main/portfolio-detail.html"

# blogview identical to the portfolio view, difference is html files
class BlogView(generic.ListView):
    model = Blog
    template_name = "main/blog.html"
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = "main/blog-detail.html"
