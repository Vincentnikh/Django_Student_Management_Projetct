from django.urls import path

from Studentapp import views

urlpatterns=[
    path('reg',views.reg_fun,name='reg'),  #3.it will redirect to register.html page
    path('regdata',views.regdata_fun),     #4.it will create superuser account
    path('',views.log_fun,name='log'),     #1.it will display login.html page
    path('logdata',views.logdata_fun),      #2.it will read the data and verify is that user is superuser or not
    path('home',views.home_fun,name='home'),  #5.it will return to home html page
    path('add_students',views.addstudent_fun,name='add'), #6.
    path('readdata',views.readdata_fun),       #7.it will insert record into student table
    path('display',views.display_fun,name='display'),     #8.it will display student table data in display.html file
    path('update/<int:id>',views.update_fun,name='up'),   #9.it will update student data
    path('delete/<int:id>',views.delete_fun,name='del'),    #10.it will delete the record fron student table
    path('log_out',views.log_out_fun,name='log_out')
]