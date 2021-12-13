from django.contrib.auth import login, authenticate
from django.urls import reverse_lazy
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormMixin
from django.views.generic.edit import UpdateView

from .forms import CommentForm
from .forms import CustomUserCreationForm
from .forms import CustomUserUpdateForm
from .forms import SearchAllForm
from .forms import SearchMatchesForm
from .models import CustomUser


class SignUpView(CreateView):
    model = CustomUser
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy('edit')

    def form_valid(self, form):
        to_return = super().form_valid(form)

        page_form = form.save(commit=False)
        page_form.save()
        form.save_m2m()

        user = authenticate(
            username=form.cleaned_data["username"],
            password=form.cleaned_data["password1"],
        )
        login(self.request, user)
        return to_return


class ProfileView(DetailView):
    context_object_name = 'user'
    template_name = 'user_profile.html'
    model = CustomUser

    def get_object(self):
        return self.request.user


class EditView(UpdateView):
    model = CustomUser
    form_class = CustomUserUpdateForm
    template_name = 'edit.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user


class UserDetailView(DetailView, FormMixin):
    context_object_name = 'user'
    template_name = 'user.html'
    slug_field = 'username'
    slug_url_kwarg = 'username'
    model = CustomUser
    form_class = CommentForm

    def get_success_url(self):
        return reverse_lazy('detail', kwargs={'username': self.get_object().username})

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['form'] = CommentForm(initial={'for_user': self.object, 'author': self.request.user})
        return context

    def post(self, request, *args, **kwargs):
        form = self.get_form()

        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        form.save()
        return super(UserDetailView, self).form_valid(form)


class IndexView(ListView, FormMixin):
    context_object_name = 'users'
    template_name = 'index.html'
    model = CustomUser
    form_class = SearchAllForm
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = SearchAllForm(initial={
            'city': self.request.GET.get('city'),
            'knows': self.request.GET.get('knows'),
            'learns': self.request.GET.get('learns'),
        })
        return context

    def get_queryset(self):
        query_params = {}

        if self.request.user.is_authenticated:
            get_request = self.request.GET

            query = {
                'city': get_request.get('city'),
                'knows': get_request.get('knows'),
                'learns': get_request.get('learns'),
            }
            query_params = {field: constraint for field, constraint in query.items() if constraint}

        query_params['is_superuser'] = False
        return CustomUser.objects.exclude(username=self.request.user.username).filter(**query_params)


class MatchesView(ListView, FormMixin):
    context_object_name = 'users'
    template_name = 'matches.html'
    model = CustomUser
    form_class = SearchMatchesForm
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super(MatchesView, self).get_context_data(**kwargs)
        context['form'] = SearchMatchesForm(initial={
            'city': self.request.GET.get('city'),
            'knows': self.request.GET.get('knows')
        })
        return context

    def get_queryset(self):
        get_request = self.request.GET

        query = {
            'city': get_request.get('city'),
            'knows': get_request.get('knows'),
            'knows__in': self.request.user.learns.all(),
            'learns__in': self.request.user.knows.all()
        }

        query_params = {field: constraint for field, constraint in query.items() if constraint}
        query_params['is_superuser'] = False
        return CustomUser.objects.exclude(username=self.request.user.username).filter(**query_params)
