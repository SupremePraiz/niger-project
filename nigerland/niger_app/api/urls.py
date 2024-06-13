from django.urls import path

from .views import SurveyorList, SurveyorDetail, DocumentList, DocumentDetail, DocumentCreate, SurveyorDocument

urlpatterns = [
    path("surveyor/",SurveyorList.as_view(), name="surveyor"),
    path("surveyor/<int:pk>/",SurveyorDetail.as_view(), name="surveyordetail"),
    
    path("document/<int:pk>/surveyor/",DocumentList.as_view(), name="document"),
    path("document/detail/<int:pk>/",DocumentDetail.as_view(), name="documentdetail"),
    
    path("surveyor/document-create/", DocumentCreate.as_view(), name="documentcreate"),
    
    # path("document/<str:username>/",SurveyorDocument.as_view(), name="surveyordocument"),
    path("document/list/",SurveyorDocument.as_view(), name="surveyordocument"),
]


