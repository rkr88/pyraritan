# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/libisys/src/idl/ModbusGatewayMgr.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.modbus


# interface
class GatewayMgr(Interface):
    idlType = "modbus.GatewayMgr:1.0.0"

    NO_ERROR = 0

    ERR_INVALID_PARAMS = 1

    # structure
    class RtuSettings(Structure):
        idlType = "modbus.GatewayMgr.RtuSettings:1.0.0"
        elements = ["defaultAddr", "speed", "parity"]

        def __init__(self, defaultAddr, speed, parity):
            typecheck.is_byte(defaultAddr, AssertionError)
            typecheck.is_int(speed, AssertionError)
            typecheck.is_byte(parity, AssertionError)

            self.defaultAddr = defaultAddr
            self.speed = speed
            self.parity = parity

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                defaultAddr = json['defaultAddr'],
                speed = json['speed'],
                parity = json['parity'],
            )
            return obj

        def encode(self):
            json = {}
            json['defaultAddr'] = self.defaultAddr
            json['speed'] = self.speed
            json['parity'] = self.parity
            return json

    # structure
    class Settings(Structure):
        idlType = "modbus.GatewayMgr.Settings:1.0.0"
        elements = ["rtu"]

        def __init__(self, rtu):
            typecheck.is_struct(rtu, raritan.rpc.modbus.GatewayMgr.RtuSettings, AssertionError)

            self.rtu = rtu

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                rtu = raritan.rpc.modbus.GatewayMgr.RtuSettings.decode(json['rtu'], agent),
            )
            return obj

        def encode(self):
            json = {}
            json['rtu'] = raritan.rpc.modbus.GatewayMgr.RtuSettings.encode(self.rtu)
            return json

    class _getSettings(Interface.Method):
        name = 'getSettings'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.modbus.GatewayMgr.Settings.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.modbus.GatewayMgr.Settings, DecodeException)
            return _ret_

    class _setSettings(Interface.Method):
        name = 'setSettings'

        @staticmethod
        def encode(settings):
            typecheck.is_struct(settings, raritan.rpc.modbus.GatewayMgr.Settings, AssertionError)
            args = {}
            args['settings'] = raritan.rpc.modbus.GatewayMgr.Settings.encode(settings)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(GatewayMgr, self).__init__(target, agent)
        self.getSettings = GatewayMgr._getSettings(self)
        self.setSettings = GatewayMgr._setSettings(self)
# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/libidl_client/topofw/powerlogic/idl/ModbusDevice.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.modbus


# interface
class Device(Interface):
    idlType = "modbus.Device:1.0.0"

    # structure
    class DeviceID(Structure):
        idlType = "modbus.Device.DeviceID:1.0.0"
        elements = ["vendor", "code", "version", "url", "name", "model", "app"]

        def __init__(self, vendor, code, version, url, name, model, app):
            typecheck.is_string(vendor, AssertionError)
            typecheck.is_string(code, AssertionError)
            typecheck.is_string(version, AssertionError)
            typecheck.is_string(url, AssertionError)
            typecheck.is_string(name, AssertionError)
            typecheck.is_string(model, AssertionError)
            typecheck.is_string(app, AssertionError)

            self.vendor = vendor
            self.code = code
            self.version = version
            self.url = url
            self.name = name
            self.model = model
            self.app = app

        @classmethod
        def decode(cls, json, agent):
            obj = cls(
                vendor = json['vendor'],
                code = json['code'],
                version = json['version'],
                url = json['url'],
                name = json['name'],
                model = json['model'],
                app = json['app'],
            )
            return obj

        def encode(self):
            json = {}
            json['vendor'] = self.vendor
            json['code'] = self.code
            json['version'] = self.version
            json['url'] = self.url
            json['name'] = self.name
            json['model'] = self.model
            json['app'] = self.app
            return json

    class _readDeviceIdentification(Interface.Method):
        name = 'readDeviceIdentification'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.modbus.Device.DeviceID.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.modbus.Device.DeviceID, DecodeException)
            return _ret_
    def __init__(self, target, agent):
        super(Device, self).__init__(target, agent)
        self.readDeviceIdentification = Device._readDeviceIdentification(self)
