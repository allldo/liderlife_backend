from django.urls import path, include

from items import views

urlpatterns = [
    path('team/', views.TeamView.as_view()),
    path('full_team/', views.FullTeamInfo.as_view()),
    path('programm/main/', views.ProgrammsFullInfo.as_view()),
    path('small_programms/', views.ProgrammsSmallInfo.as_view()),
    path('form_programms/', views.ProgrammsFormInfo.as_view()),
    path('smeni/<int:pk>/', views.GetSmenaInfo.as_view()),

    # sliders

    path('get/main/photos/', views.GetMainSoloSlider.as_view()),
    path('get/main/galery/', views.GetMainGalery.as_view()),

    path('reserve/post/', views.PostReserve.as_view()),

    path('get/mainText/', views.GetTextMain.as_view()),


    path('get/template/<int:pk>/', views.GetTemplateObject.as_view()),

    path('slg/programm/<slug:slug>/', views.GetSlugProgramm.as_view()),
    path('programm/get/<int:pk>/', views.GetProgramm.as_view()),

    path('send_email_new_reserve/', views.send_email_new_reserve),
    path('send_email_new_reserve_client/', views.send_email_new_reserve_client),
    
    path('email/callback', views.send_email_callback_client)
]