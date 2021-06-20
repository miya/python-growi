import json
import requests


class API:
  def __init__(self, growi_url, access_token, time_out=3.5):
    self.growi_url = growi_url
    self.access_token = access_token
    self.time_out = time_out

  def request(self, endpoint, methot='GET', params=None):
    api = '_api/v3'
    url = f'{self.growi_url}/{api}/{endpoint}'
    headers = {'content-type': 'application/json'}
    payload = {'access_token': self.access_token}
    if params:
      payload.update(params)

    if methot == 'GET':
      return requests.get(url, headers=headers, params=payload, timeout=self.time_out).json()

    elif methot == 'POST':
      return requests.post(url, headers=headers, data=json.dumps(payload), timeout=self.time_out).json()

    elif methot == 'PUT':
      return requests.put(url, headers=headers, data=json.dumps(payload), timeout=self.time_out).json()

  # def admin_home(self):
  #   ''' Get adminHome parameters
  #   '''
  #   endpoint = 'admin-home/'
  #   return request(endpoint)

  def app_settings(self):
    ''' Get app setting params
    '''
    endpoint = 'app-settings/'
    return self.request(endpoint)

  # def app_settings_app_setting(self, **params):
  #   ''' Update app setting
  #   '''
  #   endpoint = 'app-settings/app-setting/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def app_settings_site_url_setting(self, **params):
  #   ''' Update site url setting
  #   '''
  #   endpoint = 'app-settings/site-url-setting'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def app_settings_smtp_setting(self, **params):
  #   ''' Update smtp setting
  #   '''
  #   endpoint = 'app-settings/smtp-setting/'
  #   return request(endpoint, method='PUT', params=params)

  # def app_settings_smtp_test(self, **params):
  #   ''' Send test mail for smtp
  #   '''
  #   endpoint = 'app-settings/smtp-test/'
  #   return request(endpoint, method='POST', params=params)

  # def app_settings_ses_setting(self, **params):
  #   ''' Update ses setting
  #   '''
  #   endpoint = 'app-settings/ses-setting/'
  #   return request(endpoint, methot='PUT', params=params)

  # def app_settings_file_upload_setting(self, **params):
  #   ''' Update fileUploadSetting
  #   '''
  #   endpoint = 'app-settings/file-upload-setting/'
  #   return request(endpoint, method='PUT', params=params)

  # def app_settings_plugin_setting(self, **params):
  #   ''' Update plugin setting
  #   '''
  #   endpoint = 'app-settings/plugin-setting'
  #   return request(endpoint, method='PUT', params=params)