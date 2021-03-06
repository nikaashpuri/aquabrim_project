
from tastypie.api import Api
from django.conf.urls import patterns, include, url

'''

v1_api = Api(api_name='v1')
v1_api.register(DeviceResource())

'''
from machine.views import ControllerListView

urlpatterns = patterns('',
  # ...more URLconf bits here...
  # Then add:
  # url(r'^api/', include(v1_api.urls)),
  # url(r'^add_machine/', add_machine, name='add-machine'),
  # url(r'^add_machine_through_phone/', add_machine_through_phone, name='add-machine-through-phone'),
  url(r'^get/(?P<data_id>\d+)/command/$', 'machine.views.commandData'),
  url(r'^get/(?P<data_id>\d+)/command/submit/$', 'machine.views.submitData'),
  url(r'^get/(?P<data_id>\d+)/master_command/$', 'machine.views.masterCommandData'),
  url(r'^get/(?P<data_id>\d+)/master_command/submit/$', 'machine.views.masterSubmitData'),
  url(r'^get/(?P<data_id>\d+)/user_interface/$', 'machine.views.userInterface'),
  url(r'^get/(?P<data_id>\d+)/user_interface/tank-setting/$', 'machine.views.userInterfaceTankSetting'),
  url(r'^get/(?P<data_id>\d+)/user_interface/controller-setting/$', 'machine.views.userInterfaceControllerSetting'),
  url(r'^get/(?P<data_id>\d+)/user_interface/display-setting/$', 'machine.views.userInterfaceDisplaySetting'),
  url(r'^get/(?P<data_id>\d+)/user_interface/timer-setting/$', 'machine.views.userInterfaceTimerSetting'),

  url(r'^get/(?P<data_id>\d+)/user_interface/submit/$', 'machine.views.submitDataUIHome'),
  url(r'^get/(?P<data_id>\d+)/user_interface/tank-setting/submit/$', 'machine.views.submitDataUITank'),
  url(r'^get/(?P<data_id>\d+)/user_interface/controller-setting/submit/$', 'machine.views.submitDataUIController'),
  url(r'^get/(?P<data_id>\d+)/user_interface/display-setting/submit/$', 'machine.views.submitDataUIDisplay'),
  url(r'^get/(?P<data_id>\d+)/user_interface/timer-setting/submit/$', 'machine.views.submitDataUITimer'),


  url(r'^get/(?P<data_id>\d+)/$', 'machine.views.deviceData'),

  url(r'^get/(?P<data_id>\d+)/value/$', 'machine.views.changeViews'),
  url(r'^toggle/$', 'machine.views.list_change', name='device-list'),

  url(r'^$', ControllerListView.as_view(), name='device-list'),
  # url(r'^send_data_to_server/$', 'machine.views.collect_data_from_device'),
  url(r'^start_server/$', 'machine.views.activate_server'),
  url(r'^log/$', 'machine.views.generate_log'),
  # url(r'^send_data_to_device/$', 'machine.views.prepare_string_to_activate_command'),


)