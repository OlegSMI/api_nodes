from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register(r'cities', CityListAPIView)
router.register(r'specialties', SpecialtyListAPIView)
router.register(r'vacancies', VacancyListAPIView)

urlpatterns = []
urlpatterns += router.urls