# Do NOT edit this file!
# It was generated by IdlC class idl.json.python.ProxyAsnVisitor.

#
# Section generated from "/home/nb/builds/gitlab/builds/1da4124e/0/gitlab/main/firmware/mkdist/tmp/build-pdu-px2-final/luaserviced/client/idl/LuaService.idl"
#

import raritan.rpc
from raritan.rpc import Interface, Structure, ValueObject, Enumeration, typecheck, DecodeException
import raritan.rpc.luaservice


# structure
class ScriptState(Structure):
    idlType = "luaservice.ScriptState:1.0.0"
    elements = ["execState", "exitType", "exitStatus"]

    def __init__(self, execState, exitType, exitStatus):
        typecheck.is_enum(execState, raritan.rpc.luaservice.ScriptState.ExecState, AssertionError)
        typecheck.is_enum(exitType, raritan.rpc.luaservice.ScriptState.ExitType, AssertionError)
        typecheck.is_int(exitStatus, AssertionError)

        self.execState = execState
        self.exitType = exitType
        self.exitStatus = exitStatus

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            execState = raritan.rpc.luaservice.ScriptState.ExecState.decode(json['execState']),
            exitType = raritan.rpc.luaservice.ScriptState.ExitType.decode(json['exitType']),
            exitStatus = json['exitStatus'],
        )
        return obj

    def encode(self):
        json = {}
        json['execState'] = raritan.rpc.luaservice.ScriptState.ExecState.encode(self.execState)
        json['exitType'] = raritan.rpc.luaservice.ScriptState.ExitType.encode(self.exitType)
        json['exitStatus'] = self.exitStatus
        return json

    # enumeration
    class ExecState(Enumeration):
        idlType = "luaservice.ScriptState.ExecState:1.0.0"
        values = ["STAT_NEW", "STAT_RUNNING", "STAT_TERMINATED", "STAT_RESTARTING"]

    ExecState.STAT_NEW = ExecState(0)
    ExecState.STAT_RUNNING = ExecState(1)
    ExecState.STAT_TERMINATED = ExecState(2)
    ExecState.STAT_RESTARTING = ExecState(3)

    # enumeration
    class ExitType(Enumeration):
        idlType = "luaservice.ScriptState.ExitType:1.0.0"
        values = ["EXIT_CODE", "SIGNAL"]

    ExitType.EXIT_CODE = ExitType(0)
    ExitType.SIGNAL = ExitType(1)

# structure
class ScriptOptions(Structure):
    idlType = "luaservice.ScriptOptions:2.0.0"
    elements = ["defaultArgs", "autoStart", "autoRestart"]

    def __init__(self, defaultArgs, autoStart, autoRestart):
        typecheck.is_bool(autoStart, AssertionError)
        typecheck.is_bool(autoRestart, AssertionError)

        self.defaultArgs = defaultArgs
        self.autoStart = autoStart
        self.autoRestart = autoRestart

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            defaultArgs = dict([(
                elem['key'],
                elem['value'])
                for elem in json['defaultArgs']]),
            autoStart = json['autoStart'],
            autoRestart = json['autoRestart'],
        )
        return obj

    def encode(self):
        json = {}
        json['defaultArgs'] = [dict(
            key = k,
            value = v)
            for k, v in self.defaultArgs.items()]
        json['autoStart'] = self.autoStart
        json['autoRestart'] = self.autoRestart
        return json

# structure
class Environment(Structure):
    idlType = "luaservice.Environment:2.0.0"
    elements = ["maxScriptMemoryGrowth", "maxAmountOfScripts", "amountOfScripts", "maxScriptSize", "maxAllScriptSize", "allScriptSize", "outputBufferSize", "restartInterval", "autoStartDelay"]

    def __init__(self, maxScriptMemoryGrowth, maxAmountOfScripts, amountOfScripts, maxScriptSize, maxAllScriptSize, allScriptSize, outputBufferSize, restartInterval, autoStartDelay):
        typecheck.is_int(maxScriptMemoryGrowth, AssertionError)
        typecheck.is_int(maxAmountOfScripts, AssertionError)
        typecheck.is_int(amountOfScripts, AssertionError)
        typecheck.is_int(maxScriptSize, AssertionError)
        typecheck.is_int(maxAllScriptSize, AssertionError)
        typecheck.is_int(allScriptSize, AssertionError)
        typecheck.is_int(outputBufferSize, AssertionError)
        typecheck.is_int(restartInterval, AssertionError)
        typecheck.is_int(autoStartDelay, AssertionError)

        self.maxScriptMemoryGrowth = maxScriptMemoryGrowth
        self.maxAmountOfScripts = maxAmountOfScripts
        self.amountOfScripts = amountOfScripts
        self.maxScriptSize = maxScriptSize
        self.maxAllScriptSize = maxAllScriptSize
        self.allScriptSize = allScriptSize
        self.outputBufferSize = outputBufferSize
        self.restartInterval = restartInterval
        self.autoStartDelay = autoStartDelay

    @classmethod
    def decode(cls, json, agent):
        obj = cls(
            maxScriptMemoryGrowth = json['maxScriptMemoryGrowth'],
            maxAmountOfScripts = json['maxAmountOfScripts'],
            amountOfScripts = json['amountOfScripts'],
            maxScriptSize = json['maxScriptSize'],
            maxAllScriptSize = json['maxAllScriptSize'],
            allScriptSize = json['allScriptSize'],
            outputBufferSize = json['outputBufferSize'],
            restartInterval = json['restartInterval'],
            autoStartDelay = json['autoStartDelay'],
        )
        return obj

    def encode(self):
        json = {}
        json['maxScriptMemoryGrowth'] = self.maxScriptMemoryGrowth
        json['maxAmountOfScripts'] = self.maxAmountOfScripts
        json['amountOfScripts'] = self.amountOfScripts
        json['maxScriptSize'] = self.maxScriptSize
        json['maxAllScriptSize'] = self.maxAllScriptSize
        json['allScriptSize'] = self.allScriptSize
        json['outputBufferSize'] = self.outputBufferSize
        json['restartInterval'] = self.restartInterval
        json['autoStartDelay'] = self.autoStartDelay
        return json

# interface
class Manager(Interface):
    idlType = "luaservice.Manager:2.0.1"

    NO_ERROR = 0

    ERR_INVALID_NAME = 1

    ERR_NO_SUCH_SCRIPT = 2

    ERR_MAX_SCRIPT_NUMBERS_EXCEEDED = 3

    ERR_MAX_SCRIPT_SIZE_EXCEEDED = 4

    ERR_MAX_ALL_SCRIPT_SIZE_EXCEEDED = 5

    ERR_NOT_TERMINATED = 6

    ERR_NOT_RUNNING = 7

    ERR_INVALID_ADDR = 8

    ERR_TOO_MANY_ARGUMENTS = 10

    ERR_ARGUMENT_NOT_VALID = 11

    class _setScript(Interface.Method):
        name = 'setScript'

        @staticmethod
        def encode(name, script, options):
            typecheck.is_string(name, AssertionError)
            typecheck.is_string(script, AssertionError)
            typecheck.is_struct(options, raritan.rpc.luaservice.ScriptOptions, AssertionError)
            args = {}
            args['name'] = name
            args['script'] = script
            args['options'] = raritan.rpc.luaservice.ScriptOptions.encode(options)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getScript(Interface.Method):
        name = 'getScript'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            script = rsp['script']
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_string(script, DecodeException)
            return (_ret_, script)

    class _getScriptNames(Interface.Method):
        name = 'getScriptNames'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = [x0 for x0 in rsp['_ret_']]
            for x0 in _ret_:
                typecheck.is_string(x0, DecodeException)
            return _ret_

    class _deleteScript(Interface.Method):
        name = 'deleteScript'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _setScriptOptions(Interface.Method):
        name = 'setScriptOptions'

        @staticmethod
        def encode(name, options):
            typecheck.is_string(name, AssertionError)
            typecheck.is_struct(options, raritan.rpc.luaservice.ScriptOptions, AssertionError)
            args = {}
            args['name'] = name
            args['options'] = raritan.rpc.luaservice.ScriptOptions.encode(options)
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getScriptOptions(Interface.Method):
        name = 'getScriptOptions'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            options = raritan.rpc.luaservice.ScriptOptions.decode(rsp['options'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(options, raritan.rpc.luaservice.ScriptOptions, DecodeException)
            return (_ret_, options)

    class _getEnvironment(Interface.Method):
        name = 'getEnvironment'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = raritan.rpc.luaservice.Environment.decode(rsp['_ret_'], agent)
            typecheck.is_struct(_ret_, raritan.rpc.luaservice.Environment, DecodeException)
            return _ret_

    class _getScriptOutput(Interface.Method):
        name = 'getScriptOutput'

        @staticmethod
        def encode(name, iAddr):
            typecheck.is_string(name, AssertionError)
            typecheck.is_long(iAddr, AssertionError)
            args = {}
            args['name'] = name
            args['iAddr'] = iAddr
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            oAddr = int(rsp['oAddr'])
            nAddr = int(rsp['nAddr'])
            oString = rsp['oString']
            more = rsp['more']
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_long(oAddr, DecodeException)
            typecheck.is_long(nAddr, DecodeException)
            typecheck.is_string(oString, DecodeException)
            typecheck.is_bool(more, DecodeException)
            return (_ret_, oAddr, nAddr, oString, more)

    class _clearScriptOutput(Interface.Method):
        name = 'clearScriptOutput'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _startScript(Interface.Method):
        name = 'startScript'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _startScriptWithArgs(Interface.Method):
        name = 'startScriptWithArgs'

        @staticmethod
        def encode(name, arguments):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            args['arguments'] = [dict(
                key = k,
                value = v)
                for k, v in arguments.items()]
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _terminateScript(Interface.Method):
        name = 'terminateScript'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            typecheck.is_int(_ret_, DecodeException)
            return _ret_

    class _getScriptState(Interface.Method):
        name = 'getScriptState'

        @staticmethod
        def encode(name):
            typecheck.is_string(name, AssertionError)
            args = {}
            args['name'] = name
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = rsp['_ret_']
            state = raritan.rpc.luaservice.ScriptState.decode(rsp['state'], agent)
            typecheck.is_int(_ret_, DecodeException)
            typecheck.is_struct(state, raritan.rpc.luaservice.ScriptState, DecodeException)
            return (_ret_, state)

    class _getScriptStates(Interface.Method):
        name = 'getScriptStates'

        @staticmethod
        def encode():
            args = {}
            return args

        @staticmethod
        def decode(rsp, agent):
            _ret_ = dict([(
                elem['key'],
                raritan.rpc.luaservice.ScriptState.decode(elem['value'], agent))
                for elem in rsp['_ret_']])
            return _ret_
    def __init__(self, target, agent):
        super(Manager, self).__init__(target, agent)
        self.setScript = Manager._setScript(self)
        self.getScript = Manager._getScript(self)
        self.getScriptNames = Manager._getScriptNames(self)
        self.deleteScript = Manager._deleteScript(self)
        self.setScriptOptions = Manager._setScriptOptions(self)
        self.getScriptOptions = Manager._getScriptOptions(self)
        self.getEnvironment = Manager._getEnvironment(self)
        self.getScriptOutput = Manager._getScriptOutput(self)
        self.clearScriptOutput = Manager._clearScriptOutput(self)
        self.startScript = Manager._startScript(self)
        self.startScriptWithArgs = Manager._startScriptWithArgs(self)
        self.terminateScript = Manager._terminateScript(self)
        self.getScriptState = Manager._getScriptState(self)
        self.getScriptStates = Manager._getScriptStates(self)