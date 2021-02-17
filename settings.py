from xml.dom import minidom


def getSetting(setting_id):
    #TODO Change this
    #settingsfile = minidom.parse('special://userdata/addon_data/plugin.farmvivi.hikvision/settings.xml')
    settingsfile = minidom.parse('/storage/.kodi/userdata/addon_data/plugin.farmvivi.hikvision/settings.xml')
    items = settingsfile.getElementsByTagName('setting')

    for elem in items:
        if elem.attributes['id'].value == setting_id:
            return elem.firstChild.data
