from django.conf.urls import url

from .views import (
    ProductListView,
    # ProductCardView,
    # product_list_view,
    # ProductDetailView,
    # product_detail_view,
    # ProductFeaturedListView,
    ProductDetailSlugView,
    # ProductFeaturedDetailView,
    )

urlpatterns = [
    # url(r'^$', home_page),
    # url(r'^about/$', about_page),
	# url(r'^contact/$', contact_page),
    # url(r'^login/$', login_page),
    url(r'^$', ProductListView.as_view(), name='list'),
    # url(r'^$', ProductCardView.as_view()),
    # url(r'^products-fbv/$', product_list_view),
    # url(r'^products/(?P<pk>\d+)/$', ProductDetailView.as_view()),
    # url(r'^products-fbv/(?P<pk>\d+)/$', product_detail_view),  
    # url(r'^featured/$', ProductFeaturedListView.as_view()),
    # url(r'^featured/(?P<pk>\d+)/$', ProductFeaturedDetailView.as_view()),
    url(r'^(?P<slug>[\w-]+)/$', ProductDetailSlugView.as_view(), name='detail'), 
    # url(r'^register/$', register_page),
    # url(r'^admin/', admin.site.urls),
]

