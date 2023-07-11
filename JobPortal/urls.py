from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home'),                                                       # Landing page
    path('register/<str:role>',registerUser,name='register'),                        # registation page
    path('login/<str:role>',loginUser,name='login'),                                 # login page for 3 roles
    path('logout/',logoutUser,name='logout'),                                        # logout page
    path('adminpage/',adminpage,name='adminpage'),                                   # admin landing page
    path('addhr/',Addhr ,name='addhr'),                                              # add hr page user
    path("edit_admin_hr/<int:pk>",edit_admin_hr, name="edit_admin_hr"),              # edit admin page user
    path("delete_admin_user/<int:pk>",delete_admin_user, name="delete_admin_user"),  # delete admin page user
    path('hrview/',hrview,name='hrview'),                                            # HR landing page
    path('addjob/',Addjob ,name='addjob'),                                           # add job page
    path("edit_hr_job/<int:pk>",edit_job_hr, name="edit_hr_job"),                    # edit job page
    path("delete_hr_job/<int:pk>",delete_hr_job, name="delete_hr_job"),              # delete job page
    path('candidateview/',CompanyPage,name='candidateview'),                         # candidate landing page
    path('apply/<int:company_id>',applyPage ,name='apply'),                          # apply for job page
    path('appliedjobs/',appliedjobs,name='appliedjobs'),                             # view applied job page
]