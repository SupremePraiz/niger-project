from django.urls import path

from .views import SurveyorList, SurveyorDetail, DocumentList, DocumentDetail, DocumentCreate, SurveyorDocument

urlpatterns = [
    path("survey/",SurveyorList.as_view(), name="surveyor"),
    path("survey/<int:pk>/",SurveyorDetail.as_view(), name="surveyordetail"),
    
    path("document/<int:pk>/survey/",DocumentList.as_view(), name="document"),
    path("document/detail/<int:pk>/",DocumentDetail.as_view(), name="documentdetail"),
    
    path("document/<int:pk>/survey-create/", DocumentCreate.as_view(), name="documentcreate"),
    
    # path("document/<str:username>/",SurveyorDocument.as_view(), name="surveyordocument"),
    path("document/list/",SurveyorDocument.as_view(), name="surveyordocument"),
]


