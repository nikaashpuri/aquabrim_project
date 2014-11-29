__author__ = 'nikaashpuri'

'''
from tastypie.resources import ModelResource
from machine.models import Device
from tastypie.authentication import ApiKeyAuthentication
from tastypie.authorization import Authorization
from django.contrib.auth.models import User

class DeviceResource(ModelResource):
    class Meta:
        queryset = Device.objects.all()
        resource_name = 'device'
        list_allowed_methods = ['get', 'post']
        authentication = ApiKeyAuthentication()
        authorization = Authorization()


    def obj_create(self, bundle, **kwargs):
        print 'here'
        return super(DeviceResource, self).obj_create(bundle, user=bundle.request.user)

    def get_object_list(self, request):
        print request.user
        return super(DeviceResource, self).get_object_list(request).filter(user=request.user)

'''