"""shortner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import (
    include,
    path,
)

from shortner.views import (
    create,
    delete,
    edit,
    entries,
    go,
    login,
    logout,
    redirect_root,
    ShortnerAdmin,
    submit,
    thanks,
)

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),

    url(r'^$', redirect_root),

    url(r'^s/(?P<short>.+)$', go),

    url(r'^submit/$', submit),
    url(r'^thanks/(?P<short>.+)$', thanks),

    url(r'^entries/$', entries),
    url(r'^entries/create/$', create),
    url(r'^entries/(?P<short>.+)/edit/$', edit),
    url(r'^entries/(?P<short>.+)/delete/$', delete),

    path('admin/', include(ShortnerAdmin.urls())),
]
