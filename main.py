# coding=utf-8

import sys

import xbmc
import xbmcaddon

from resources.lib.libs import hikvisionapi
from resources.lib import kodilogging

# Keep this file to a minimum, as Kodi
# doesn't keep a compiled copy of this
ADDON = xbmcaddon.Addon()
kodilogging.config()

# Parameters
hikvision_ip = ADDON.getSettingString('hikvision_ip')
hikvision_port = ADDON.getSettingInt('hikvision_port')
hikvision_rtsp_port = ADDON.getSettingInt('hikvision_rtsp_port')
hikvision_username = ADDON.getSettingString('hikvision_username')
hikvision_password = ADDON.getSettingString('hikvision_password')

# Connect to camera
cam = hikvisionapi.Client('http://' + hikvision_ip + ':' + str(hikvision_port), hikvision_username, hikvision_password)

# Play RTSP video feed
xbmc.Player().play(
    'rtsp://' + hikvision_username + ':' + hikvision_password + '@' + hikvision_ip + ':' + str(hikvision_rtsp_port))
