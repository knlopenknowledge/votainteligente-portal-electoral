from django.conf.urls import url
from organization_profiles.views import (OrganizationDetailView,
                                         OrganizationTemplateUpdateView,
                                         AyuranosView,
                                         ExtraPageUpdateView)


urlpatterns = [
    url(r'^update/extra_pages/(?P<pk>[\d]+)/?$', ExtraPageUpdateView.as_view(), name='update_extrapage'),
    url(r'^update/?$', OrganizationTemplateUpdateView.as_view(), name='update'),
    url(r'^(?P<slug>[-\w]+)/?$',
        OrganizationDetailView.as_view(),
        name='home'),
    url(r'^(?P<slug>[-\w]+)/ayudanos/?$',
        AyuranosView.as_view(),
        name='ayuranos'),
]
