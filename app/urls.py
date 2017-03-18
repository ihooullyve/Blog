from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^demo$', views.test, name="test"),
    url(r'^signup$', views.signup, name="signup"),
    url(r'^login$', views.login, name="login"),
    url(r'^add-blog$', views.add_blog, name="add_blog"),
    url(r'^list-all-blog$', views.list_all_blog, name="list_all_blog"),
    url(r'^detail-blog$', views.detail_blog, name="detail_blog"),
    url(r'^detail-blog/edit-blog$', views.edit_blog, name="edit_blog"),
    url(r'^detail-blog/delete$', views.delete_blog, name="delete_blog"),
    url(r'^home/upload-image$', views.upload_image, name="upload_image"),
    url(r'^home/add-blog$', views.add_blog, name="add_blog"),
    url(r'^search$', views.search, name="search"),
]
