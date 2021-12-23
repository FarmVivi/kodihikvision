import xbmcaddon

def getSettingString(setting_id):
    return xbmcaddon.Addon(id='plugin.farmvivi.hikvision').getSettingString(setting_id)

def getSettingInt(setting_id):
    return xbmcaddon.Addon(id='plugin.farmvivi.hikvision').getSettingInt(setting_id)
