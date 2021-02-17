import settings
import hikvisionapi


def getCamera():
    return hikvisionapi.Client(
        'http://' + settings.getSetting('hikvision_ip') + ':' + settings.getSetting('hikvision_port'),
        settings.getSetting('hikvision_username'), settings.getSetting('hikvision_password'))


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
    move(int(settings.getSetting('ptz_speed_pressed_pan')), 0, 0, int(settings.getSetting('ptz_duration_pan')))


def pressed_left():
    move(-int(settings.getSetting('ptz_speed_pressed_pan')), 0, 0, int(settings.getSetting('ptz_duration_pan')))


def pressed_up():
    move(0, int(settings.getSetting('ptz_speed_pressed_tilt')), 0, int(settings.getSetting('ptz_duration_tilt')))


def pressed_down():
    move(0, -int(settings.getSetting('ptz_speed_pressed_tilt')), 0, int(settings.getSetting('ptz_duration_tilt')))


def pressed_zoom_in():
    move(0, 0, int(settings.getSetting('ptz_speed_pressed_zoom')), int(settings.getSetting('ptz_duration_zoom')))


def pressed_zoom_out():
    move(0, 0, -int(settings.getSetting('ptz_speed_pressed_zoom')), int(settings.getSetting('ptz_duration_zoom')))


def held_right():
    move(int(settings.getSetting('ptz_speed_held_pan')), 0, 0, int(settings.getSetting('ptz_duration_pan')))


def held_left():
    move(-int(settings.getSetting('ptz_speed_held_pan')), 0, 0, int(settings.getSetting('ptz_duration_pan')))


def held_up():
    move(0, int(settings.getSetting('ptz_speed_held_tilt')), 0, int(settings.getSetting('ptz_duration_tilt')))


def held_down():
    move(0, -int(settings.getSetting('ptz_speed_held_tilt')), 0, int(settings.getSetting('ptz_duration_tilt')))


def held_zoom_in():
    move(0, 0, int(settings.getSetting('ptz_speed_held_zoom')), int(settings.getSetting('ptz_duration_zoom')))


def held_zoom_out():
    move(0, 0, -int(settings.getSetting('ptz_speed_held_zoom')), int(settings.getSetting('ptz_duration_zoom')))
