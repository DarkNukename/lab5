from django.contrib import admin
from django.urls import path, include

from gate.my_views.emp_view import Emp_View
from gate.my_views.emps_view import Emps_View

from gate.my_views.work_view import Work_View
from gate.my_views.works_view import Works_View

from gate.my_views.pay_view import Pay_View
from gate.my_views.pays_view import Pays_View

urlpatterns = [
    
    path('works/', Works_View.as_view()),
    path('work/<uuid:work_uuid>', Work_View.as_view()),

    path('payments/', Pays_View.as_view()),
    path('payment/<uuid:pay_uuid>', Pay_View.as_view()),

    path('persons/', Emps_View.as_view()),
    path('person/<uuid:emp_uuid>', Emp_View.as_view()),

 


]
