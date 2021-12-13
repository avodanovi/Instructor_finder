INSTRUCTOR FINDER

Django web application

The purpose of this web application is to help people exchange their knowledge.
It works like a social network. User can make their profile, check the fields of interest that
user knows and wants to learn, look at other people profiles, find people who poses some kind 
of knowldege that interests him. 



#STARTING APPLICATION
To start application navigate to instructor_finder directory in terminal and type command
- python manage.py runserver

On adress http://127.0.0.1:8000/ you can access the application.

This is run ona a Django development server.




MODELS
# models.py

CostumUser 
 -inherits django.contrib.auth.models.AbstarctUser
 -added attributes: description, image, city, knows, learns

Subject 
 -represents knowledge
 -1 attribute: name

City
 -represents users city
 -1 attribute: name
Comment:
 -represents comment on users profile
 -3 attributes: text, author, for_user

After makeing changes in models it is necessary to apply them on database. 
Navigate to instructor_finder directory in terminal and type command
- python manage.py makemigrations
- python manage.py migrate


FORMS
# forms.py

CostumUserCreationForm
 -creating user
 -inherits django.contrib.auth.forms.UserCreationForm
 -additional fields: learns, knows

CostumUserUpdateForm
 -updating users information
 -inherits django.contrib.auth.forms.UserChangeForm
 -additional fields: learns, knows 

CommentForm
 -writing comment on users profile
 -fields: text, for_user, author

SearchAllUsers
 -search profiles
 -fields: knows,learns, city

SearchMatchesForm
 -finding a profile that is a match for a user
 

VIEWS

#views.py

SignUpView
 -creating a user
 -inherits django.views.generic.edit.CreateView
 -model: CostumUser
 -form: CustomUserCreationForm
 -template: 'signup.html'

ProfileView
 -shows detailed profile
 -inherits django.views.generic.edit.DetailView
 -model: CostumUser
 -template: 'user_profile.html'

EditView
 -update user profile information
 -inherits django.views.generic.edit.CreateView
 -model: CostumUser
 -form: CostumUserUpdateForm
 -template: 'edit.html'

UserDetailView
 -shows detailed user profile
 -inherits  django.views.generic.edit.FormMixin, django.views.generic.edit.DetailView
 -model: CostumUser
 -form: CommentForm
 -template: 'user.html'


IndexView
 -show search results
 -inherits  django.views.generic.edit.FormMixin, django.views.generic.list.ListView
 -model: CostumUser
 -form: SearchAllForm
 -template: 'index.html'

MatchesView
 -show user matches
 -inherits  django.views.generic.edit.FormMixin, django.views.generic.list.ListView
 -model: CostumUser
 -form: SearchMatchesForm
 -template: 'matches.html'

TEMPLATES

-Dajngo template extending
-implemented using DTL(Django Template Language)
-Design: HTML,CSS,Bootstrap,django-crispy-forms


URL
#urls.py
 -file maneaging URL-s



ADMINISTRATION

#admin.py

-integrated automatic Django admin interface
-http://127.0.0.1:8000/admin/login/?next=/admin/

To create administrator profile navigate to instructor_finder directory in terminal and type command
- python manage.py superuser
and enter username and password
 








