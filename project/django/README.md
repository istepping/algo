# django web框架项目
## Django 2.0 新URL配置
[](https://www.cnblogs.com/feixuelove1009/p/8399338.html)
``
urlpatterns=[
   path('articles/2003/',view.special_case_2003),
   path('articles/<int:year>/',view.year), # view.year(request,year)
]
``