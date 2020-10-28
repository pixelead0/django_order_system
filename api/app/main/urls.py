# Django
from django.urls import path

# Django REST Framework
from rest_framework.routers import DefaultRouter

# Views
# from app.people import viewsets


router = DefaultRouter()

# router.register(r'people', viewsets.PersonViewSet)
# router.register(r"groups", viewsets.GroupListAPIView)
# router.register(r"address_type", viewsets.AddressTypeViewSet)
# router.register(r"business_line", viewsets.BusinessLineViewSet)
# router.register(r"civil_status", viewsets.CivilStatusViewSet)
# router.register(r"document_type", viewsets.DocumentTypeViewSet)
# router.register(r"person_type", viewsets.PersonTypeViewSet)
# router.register(r"recommended", viewsets.RecommendedViewSet)
# router.register(r"roles_type", viewsets.RolesTypeViewSet)

# urlpatterns = router.urls

# urlpatterns += [
#      path('people/<person>/documents/', viewsets.DocumentPersonListCreate.as_view()),
#      path('people/<person>/documents/<pk>/', viewsets.DocumentPersonRetrieveUpdateDestroy.as_view()),
#      path('people/<person>/address/', viewsets.AddressPersonListCreate.as_view()),
#      path('people/<person>/address/<pk>/', viewsets.AddressPersonRetrieveUpdateDestroy.as_view()),

#      # Insurance
#      path('people/<person>/insurers/', viewsets.InsuranceListCreate.as_view()),
#      path('people/<insurance>/promoters/', viewsets.PromoterListCreate.as_view()),
#      path('people/<insurance>/promoters/<pk>/', viewsets.PromoterRetrieveUpdateDestroy.as_view()),
#      path('people/<promoter>/managers/', viewsets.ManagerListCreate.as_view()),
#      path('people/<promoter>/managers/<pk>/', viewsets.ManagerRetrieveUpdateDestroy.as_view()),
#      path('people/<manager>/agents/', viewsets.AgentListCreate.as_view()),
#      path('people/<manager>/agents/<pk>/', viewsets.AgentRetrieveUpdateDestroy.as_view()),
#      path('people/<agent>/associates/', viewsets.AssociateListCreate.as_view()),
#      path('people/<agent>/associates/<pk>/', viewsets.AssociateRetrieveUpdateDestroy.as_view()),

#      path('people/<person>/agent_warrant/', viewsets.AgentWarrantListCreate.as_view()),
#      path('people/<person>/agent_warrant/<pk>/', viewsets.AgentWarrantRetrieveUpdateDestroy.as_view()),
#      path('people/<person>/agent_policy/', viewsets.AgentPolicyListCreate.as_view()),
#      path('people/<person>/agent_policy/<pk>/', viewsets.AgentPolicyRetrieveUpdateDestroy.as_view()),
#      path('people/<moral_person>/agent_moral_guardian/', viewsets.AgentMoralGuardianListCreate.as_view()),
#      path('people/<moral_person>/agent_moral_guardian/<pk>/', viewsets.AgentMoralGuardianRetrieveUpdateDestroy.as_view()),
# ]
