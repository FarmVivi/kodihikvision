import settings
from resources.lib import hikvisionapi


def getCamera():
    return hikvisionapi.Client(
        'http://' + settings.getSettingString('api_ip') +
        ':' + str(settings.getSettingInt('api_port')),
        settings.getSettingString('api_username'), settings.getSettingString('api_password'))


def move(pan, tilt, zoom, duration):
    xml = """<?xml version="1.0" encoding="UTF-8"?>
    <PTZData version="2.0" xmlns="http://www.hikvision.com/ver20/XMLSchema">
    <pan>{pan}</pan>
    <tilt>{tilt}</tilt>
    <zoom>{zoom}</zoom>
    <Momentary>
    <duration>{duration}</duration>
    </Momentary>
    </PTZData>""".format(pan=pan, tilt=tilt, zoom=zoom, duration=duration)
    getCamera().PTZCtrl.channels[1].momentary(method='put', data=xml)


def pressed_right():
    move(settings.getSettingInt('ptz_speed_pressed_pan'),
         0, 0, settings.getSettingInt('ptz_duration_pan'))


def pressed_left():
    move(-settings.getSettingInt('ptz_speed_pressed_pan'),
         0, 0, settings.getSettingInt('ptz_duration_pan'))


def pressed_up():
    move(0, settings.getSettingInt('ptz_speed_pressed_tilt'),
         0, settings.getSettingInt('ptz_duration_tilt'))


def pressed_down():
    move(0, -settings.getSettingInt('ptz_speed_pressed_tilt'),
         0, settings.getSettingInt('ptz_duration_tilt'))


def pressed_zoom_in():
    move(0, 0, settings.getSettingInt('ptz_speed_pressed_zoom'),
         settings.getSettingInt('ptz_duration_zoom'))


def pressed_zoom_out():
    move(0, 0, -settings.getSettingInt('ptz_speed_pressed_zoom'),
         settings.getSettingInt('ptz_duration_zoom'))


def held_right():
    move(settings.getSettingInt('ptz_speed_held_pan'), 0,
         0, settings.getSettingInt('ptz_duration_pan'))


def held_left():
    move(-settings.getSettingInt('ptz_speed_held_pan'),
         0, 0, settings.getSettingInt('ptz_duration_pan'))


def held_up():
    move(0, settings.getSettingInt('ptz_speed_held_tilt'),
         0, settings.getSettingInt('ptz_duration_tilt'))


def held_down():
    move(0, -settings.getSettingInt('ptz_speed_held_tilt'),
         0, settings.getSettingInt('ptz_duration_tilt'))


def held_zoom_in():
    move(0, 0, settings.getSettingInt('ptz_speed_held_zoom'),
         settings.getSettingInt('ptz_duration_zoom'))


def held_zoom_out():
    move(0, 0, -settings.getSettingInt('ptz_speed_held_zoom'),
         settings.getSettingInt('ptz_duration_zoom'))
