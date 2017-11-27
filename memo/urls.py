from django.conf.urls import url
from memo.views import MemoList,MemoDetail


urlpatterns = [
    url(r'^$', MemoList.as_view(), name='index'),
    url(r'^(?P<pk>\d+)/$', MemoDetail.as_view(), name='detail')
]
