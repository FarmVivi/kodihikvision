import xbmc
import xbmcaddon

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()

# Get RTSP settings
rtsp_ip = ADDON.getSettingString('rtsp_ip')
rtsp_port = ADDON.getSettingInt('rtsp_port')
rtsp_username = ADDON.getSettingString('rtsp_username')
rtsp_password = ADDON.getSettingString('rtsp_password')
rtsp_path = ADDON.getSettingString('rtsp_path')

# Generate RTSP url
rtsp_url = 'rtsp://'
if(rtsp_username != ''):
    rtsp_url += rtsp_username
    if(rtsp_password != ''):
        rtsp_url += ':' + rtsp_password
    rtsp_url += '@'
rtsp_url += rtsp_ip + ':' + str(rtsp_port)
if(rtsp_path != ''):
    rtsp_url += '/' + rtsp_path

# Play RTSP video feed
xbmc.Player().play(rtsp_url)
