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

  #
  # /admin-home
  #

  # def admin_home(self):
  #   ''' Get adminHome parameters
  #   '''
  #   endpoint = 'admin-home/'
  #   return request(endpoint)

  #
  # /app-settings
  #

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

  #
  # /attachment
  #

  def attachment_list(self, **params):
    ''' Get attachment list
    '''
    endpoint = 'attachment/list'
    return self.request(endpoint, params=params)

  #
  # /bookmarks
  #

  def bookmarks_info(self, **params):
    ''' Get bookmarked info
    '''
    endpoint = 'bookmarks/info'
    return self.request(endpoint, params=params)

  def my_bookmarks(self, user_id, **params):
    ''' Get my bookmarked status
    '''
    endpoint = f'bookmarks/{user_id}'
    return self.request(endpoint, params=params)

  def bookmarks(self, **params):
    ''' Update bookmarked status
    '''
    endpoint = 'bookmarks/'
    return self.request(endpoint, methot='PUT', params=params)

  #
  # /customize_setting
  #

  # def customize_setting(self):
  #   ''' Get customize parameters
  #   '''
  #   endpoint = 'customize-setting/'
  #   return self.request(endpoint)

  # def customize_setting_layout(self):
  #   ''' Get layout
  #   '''
  #   endpoint = 'customize-setting/layout/'
  #   return self.request(endpoint)

  # def customize_setting_update_layout(self, **params):
  #   ''' Update layout
  #   '''
  #   endpoint = 'customize-setting/layout/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_theme_asset_path(self, **params):
  #   ''' Get theme asset path
  #   '''
  #   endpoint = 'customize-setting/theme/asset-path/'
  #   return self.request(endpoint, params=params)

  # def customize_setting_theme(self, **params):
  #   ''' Update theme
  #   '''
  #   endpoint = 'customize-setting/theme/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_function(self, **params):
  #   ''' Update function
  #   '''
  #   endpoint = 'customize-setting/function/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_highlight(self, **params):
  #   ''' Update highlight
  #   '''
  #   endpoint = 'customize-setting/highlight/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_customize_title(self, **params):
  #   ''' Update customizeTitle
  #   '''
  #   endpoint = 'customize-setting/customize-title/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_customize_header(self, **params):
  #   ''' Update customizeHeader
  #   '''
  #   endpoint = 'customize-setting/customize-header/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_customize_css(self, **params):
  #   ''' Update customizeCss
  #   '''
  #   endpoint = 'customize-setting/customize-css/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def customize_setting_customize_script(self, **params):
  #   ''' Update customizeScript
  #   '''
  #   endpoint = 'customize-setting/customize-script/'
  #   return self.request(endpoint, methot='PUT', params=params)
