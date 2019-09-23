# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/idlc/rt/idl/Event.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException

# value object
class Event(ValueObject):
    idlType = "idl.Event:1.0.0"

    def __init__(self, source):
        typecheck.is_remote_obj(source, AssertionError)

        self.source = source

    def encode(self):
        json = {}
        json['source'] = Interface.encode(self.source)
        return json

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            source = Interface.decode(json['source'], agent),
        )
        return obj

    def listElements(self):
        elements = ["source"]
        return elements
