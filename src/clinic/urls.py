from django.urls import path

from clinic.views import RequisitesView, AboutView, LicensesView

urlpatterns = [
    path(
        route='requisites/',
        view=RequisitesView.as_view(),
        name='requisites',
    ),
    path(
        route='company/',
        view=AboutView.as_view(),
        name='company',
    ),
    path(
        route='licenses/',
        view=LicensesView.as_view(),
        name='licenses',
    ),
]