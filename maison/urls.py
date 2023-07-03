from django.urls import path, include, re_path
from maison import views
from maison.views import *
from rest_framework import routers

router = routers.DefaultRouter()

# router.register(r'list_house',views.ListHouseView, 'task')
# router.register(r'create_house',views.CreateHouseView, 'task')
# router.register(r'<pk>/update_house',views.UpdateHouseView, 'task')
# router.register(r'<pk>/delete_house',views.DeleteHouseView, 'task')
# router.register(r'list_meuble',views.ListMeubleView, 'task')
# router.register(r'create_meuble',views.CreateMeubleView, 'task')
# router.register(r'<pk>/update_meuble',views.UpdateMeubleView, 'task')
# router.register(r'<pk>/delete_meuble',views.DeleteMeubleView, 'task')

router.register(r'house',views.houseView, 'task')
router.register(r'meuble',views.meubleView, 'task')


urlpatterns = [
    path('api/', include(router.urls)),
    path('list_house',views.ListHouseView.as_view(), name='house'),
    path('houses',views.searchHouseView.as_view(), name='searchhouse'),
    path('create_house/',views.CreateHouseView.as_view(), name='create_house'),
    path('<pk>/update_house/',views.UpdateHouseView.as_view(), name='house_update'),
    path('<pk>/delete_house/',views.DeleteHouseView.as_view(), name='house_delete'),
    
    path('list_meuble',views.ListMeubleView.as_view(), name='meuble'),
    path('meubles',views.searchMeubleView.as_view(), name='searchmeuble'),
    path('create_meuble/',views.CreateMeubleView.as_view(), name='create_meuble'),
    path('<pk>/update_meuble/',views.UpdateMeubleView.as_view(), name='update_meuble'),
    path('<pk>/delete_meuble/',views.DeleteMeubleView.as_view(), name='delete_meuble'),

]