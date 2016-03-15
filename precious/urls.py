from django.conf.urls import include, url

# Import views.py
from . import views

urlpatterns = [

    # Homepage
    url(r'^$', views.homepage, name='homepage'),

    # Create Post
    url(r'^new_post/$', views.new_post, name='new_post'),

	# Create Post
    url(r'^new_category/$', views.new_category, name='new_category'),

    # Create Category
    url(r'^new_category/$', views.new_category, name='new_category'),

    # Create GeneralText
    url(r'^new_general_text/(?P<pk>[0-9]+)/$', views.new_general_text, name='new_general_text'),

    # Create GeneralFile
    url(r'^new_general_file/(?P<pk>[0-9]+)/$', views.new_general_file, name='new_general_file'),

    # Look Post in details
    url(r'^detail_post/(?P<pk>[0-9]+)/$', views.detail_post, name='detail_post'),

    # Edit existing Post
    url(r'^edit_post/(?P<pk>[0-9]+)/$', views.edit_post, name='edit_post'),

    # Edit existing GeneralText
    url(r'^edit_general_text/(?P<pk>[0-9]+)/(?P<pks>[0-9]+)/$', views.edit_general_text, name='edit_general_text'),

    # Edit existing GeneralText
    url(r'^edit_general_file/(?P<pk>[0-9]+)/(?P<pks>[0-9]+)/$', views.edit_general_file, name='edit_general_file'),

    # AJAX search
    url(r'^post_search/$', views.post_search, name='post_search'),

    # AJAX Category search
    url(r'^category_text_search/$', views.category_text_search, name='category_text_search'),

    # Delete Post
    url(r'^delete_post/(?P<pk>[0-9]+)/$', views.delete_post, name='delete_post'),

    # Delete GeneralText
    url(r'^delete_general_text/(?P<pk>[0-9]+)/(?P<ppk>[0-9]+)/$', views.delete_general_text, name='delete_general_text'),

    # Delete GeneralFile
    url(r'^delete_general_file/(?P<pk>[0-9]+)/(?P<ppk>[0-9]+)/$', views.delete_general_file, name='delete_general_file'),
]
