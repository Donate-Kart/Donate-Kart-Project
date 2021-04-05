from django.urls import include, path

from classroom.views import classroom, students, teachers

app_name = "classroom"

urlpatterns = [
    path('', classroom.home, name='home'),
    path('donor/', students.QuizListView.as_view(), name='inventory'),
    path('', include('classroom.urls')),
    path('donor/add_item', students.AddItemView.as_view(), name='add_item'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', classroom.SignUpView.as_view(), name='signup'),
    path('ngo/', students.NGOQuizListView.as_view(), name='ngo_home'),
    path('accounts/signup/student/', students.SignUpView.as_view(), name='donor_signup'),
    path('accounts/signup/teacher/', students.NGOSignUpView.as_view(), name='ngo_signup'),
    path('donor/ngo_list', students.TakenQuizListView.as_view(), name='ngo_list'),
    path('ngo/donor_list', students.DonorListView.as_view(), name='donor_list'),
    path('activate/<uidb64>/<token>/', classroom.activate, name='activate'),
    path('donor/edit_profile', students.EditProfileView.as_view(), name='edit_profile'),
    path('donor/view_profile', students.UserProfileView.as_view(), name='view_profile'),
    path('ngo/<donorid>/order/', students.OrderView.as_view(), name='order'),
    path('donor/edit_profile_ngo', students.EditProfileNGOView.as_view(), name='edit_profile_ngo'),
    path('ngo/order_complete', students.update, name='order_complete'),
]
