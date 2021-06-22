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

    elif methot == 'DELETE':
      return requests.delete(url, headers=headers, params=payload).json()

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

  #
  # /export
  #
  def export_status(self):
    ''' Get properties of stored zip files for export
    '''
    endpoint = 'export/status/'
    return self.request(endpoint)

  # WIP
  # def export(self, body):
  #   ''' Generate zipped jsons for collections
  #   '''
  #   endpoint = 'export/'
  #   return self.request(endpoint, methot='POST', params=body)

  def export_delete(self, file_name):
    ''' Delete the file
    '''
    endpoint = f'export/{file_name}'
    return self.request(endpoint, methot='DELETE')

  #
  # /healthcheck
  #
  def healthcheck(self, **params):
    ''' Check whether the server is healthy or not
    '''
    endpoint = 'healthcheck/'
    return self.request(endpoint, params=params)

  #
  # /import
  #
  def import_(self):
    ''' Get import settings params
    '''
    endpoint = 'import/'
    return self.request(endpoint)

  def import_status(self, **params):
    ''' Import a collection from a zipped json
    '''
    endpoint = 'import/status'
    return self.request(endpoint, params=params)

  # WIP
  # def import_collection(self, **params):
  #   ''' Import a collection from a zipped json
  #   '''
  #   endpoint = 'import/'
  #   return self.request(endpoint, methot='POST', params=params)

  # WIP
  # def import_upload(self, **params):
  #   ''' Upload a zip file
  #   '''
  #   endpoint = '/import/upload'
  #   return self.request(endpoint, params=params)

  def import_delete(self):
    ''' Delete all zip files
    '''
    endpoint = 'import/all/'
    return self.request(endpoint, methot='DELETE')

  #
  # /markdown
  #
  # def markdown_setting(self):
  #   ''' Get markdown parameters
  #   '''
  #   endpoint = 'markdown-setting/'
  #   return self.request(endpoint)

  # def markdown_setting_lineBreak(self, **params):
  #   ''' Update lineBreak setting
  #   '''
  #   endpoint = 'markdown-setting/lineBreak/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def markdown_setting_indent(self, **params):
  #   ''' Update indent setting
  #   '''
  #   endpoint = 'markdown-setting/indent/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def markdown_setting_presentation(self, **params):
  #   ''' Update presentation
  #   '''
  #   endpoint = 'markdown-setting/presentation/'
  #   return self.request(endpoint, methot='PUT', params=params)

  # def markdown_setting_xss(self, **params):
  #   ''' Update xss
  #   '''
  #   endpoint = 'markdown-setting/xss/'
  #   return self.request(endpoint, methot='PUT', params=params)

  #
  # /mongo
  #
  # def mongo_collections(self):
  #   ''' Get mongodb collections names
  #   '''
  #   endpoint = 'mongo/collections/'
  #   return self.request(endpoint)

  #
  # /notification-setting
  #
  def notification_setting(self):
    ''' Get notification paramators
    '''

    endpoint = 'notification-setting/'
    return self.request(endpoint)

  def notification_setting_slack_configuration(self, **param):
    ''' Update slack configuration setting
    '''
    endpoint = 'notification-setting/slack-configuration/'
    return self.request(endpoint, methot='PUT', params=param)

  def notification_setting_user_notification(self, **params):
    ''' Add user notification setting
    '''
    endpoint = 'notification-setting/user-notification/'
    return self.request(endpoint, methot='POST', params=params)

  def notification_setting_delete_user_notification(self, _id):
    ''' Delete user trigger notification pattern
    '''
    endpoint = f'notification-setting/user-notification/{_id}/'
    return self.request(endpoint, methot='DELETE')
