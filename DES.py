# -*- coding: utf-8 -*-
"""
Created on Sat Dec 22 14:09:31 2018

@author: YURU
"""

from js2py.pyjs import *
# setting scope
var = Scope( JS_BUILTINS )
set_global_object(var)

# Code follows:
var.registers(['stringToHex', 'HexTostring', 'des', 'encMe', 'uncMe', 'des_createKeys'])
@Js
def PyJsHoisted_des_(beinetkey, message, encrypt, mode, iv, this, arguments, var=var):
    var = Scope({'beinetkey':beinetkey, 'message':message, 'encrypt':encrypt, 'mode':mode, 'iv':iv, 'this':this, 'arguments':arguments}, var)
    var.registers(['cbcright2', 'spfunction8', 'encrypt', 'message', 'm', 'loopinc', 'spfunction6', 'spfunction4', 'len', 'mode', 'cbcright', 'right', 'spfunction3', 'chunk', 'j', 'spfunction2', 'keys', 'spfunction5', 'cbcleft2', 'spfunction7', 'beinetkey', 'right1', 'iv', 'spfunction1', 'iterations', 'i', 'endloop', 'temp', 'temp2', 'cbcleft', 'right2', 'looping', 'left'])
    def PyJs_LONG_0_(var=var):
        return var.get('Array').create(Js(16843776), Js(0.0), Js(65536), Js(16843780), Js(16842756), Js(66564), Js(4), Js(65536), Js(1024), Js(16843776), Js(16843780), Js(1024), Js(16778244), Js(16842756), Js(16777216), Js(4), Js(1028), Js(16778240), Js(16778240), Js(66560), Js(66560), Js(16842752), Js(16842752), Js(16778244), Js(65540), Js(16777220), Js(16777220), Js(65540), Js(0.0), Js(1028), Js(66564), Js(16777216), Js(65536), Js(16843780), Js(4), Js(16842752), Js(16843776), Js(16777216), Js(16777216), Js(1024), Js(16842756), Js(65536), Js(66560), Js(16777220), Js(1024), Js(4), Js(16778244), Js(66564), Js(16843780), Js(65540), Js(16842752), Js(16778244), Js(16777220), Js(1028), Js(66564), Js(16843776), Js(1028), Js(16778240), Js(16778240), Js(0.0), Js(65540), Js(66560), Js(0.0), Js(16842756))
    var.put('spfunction1', PyJs_LONG_0_())
    def PyJs_LONG_1_(var=var):
        return var.get('Array').create((-Js(2146402272)), (-Js(2147450880)), Js(32768), Js(1081376), Js(1048576), Js(32), (-Js(2146435040)), (-Js(2147450848)), (-Js(2147483616)), (-Js(2146402272)), (-Js(2146402304)), (-Js(2147483648)), (-Js(2147450880)), Js(1048576), Js(32), (-Js(2146435040)), Js(1081344), Js(1048608), (-Js(2147450848)), Js(0.0), (-Js(2147483648)), Js(32768), Js(1081376), (-Js(2146435072)), Js(1048608), (-Js(2147483616)), Js(0.0), Js(1081344), Js(32800), (-Js(2146402304)), (-Js(2146435072)), Js(32800), Js(0.0), Js(1081376), (-Js(2146435040)), Js(1048576), (-Js(2147450848)), (-Js(2146435072)), (-Js(2146402304)), Js(32768), (-Js(2146435072)), (-Js(2147450880)), Js(32), (-Js(2146402272)), Js(1081376), Js(32), Js(32768), (-Js(2147483648)), Js(32800), (-Js(2146402304)), Js(1048576), (-Js(2147483616)), Js(1048608), (-Js(2147450848)), (-Js(2147483616)), Js(1048608), Js(1081344), Js(0.0), (-Js(2147450880)), Js(32800), (-Js(2147483648)), (-Js(2146435040)), (-Js(2146402272)), Js(1081344))
    var.put('spfunction2', PyJs_LONG_1_())
    def PyJs_LONG_2_(var=var):
        return var.get('Array').create(Js(520), Js(134349312), Js(0.0), Js(134348808), Js(134218240), Js(0.0), Js(131592), Js(134218240), Js(131080), Js(134217736), Js(134217736), Js(131072), Js(134349320), Js(131080), Js(134348800), Js(520), Js(134217728), Js(8), Js(134349312), Js(512), Js(131584), Js(134348800), Js(134348808), Js(131592), Js(134218248), Js(131584), Js(131072), Js(134218248), Js(8), Js(134349320), Js(512), Js(134217728), Js(134349312), Js(134217728), Js(131080), Js(520), Js(131072), Js(134349312), Js(134218240), Js(0.0), Js(512), Js(131080), Js(134349320), Js(134218240), Js(134217736), Js(512), Js(0.0), Js(134348808), Js(134218248), Js(131072), Js(134217728), Js(134349320), Js(8), Js(131592), Js(131584), Js(134217736), Js(134348800), Js(134218248), Js(520), Js(134348800), Js(131592), Js(8), Js(134348808), Js(131584))
    var.put('spfunction3', PyJs_LONG_2_())
    def PyJs_LONG_3_(var=var):
        return var.get('Array').create(Js(8396801), Js(8321), Js(8321), Js(128), Js(8396928), Js(8388737), Js(8388609), Js(8193), Js(0.0), Js(8396800), Js(8396800), Js(8396929), Js(129), Js(0.0), Js(8388736), Js(8388609), Js(1), Js(8192), Js(8388608), Js(8396801), Js(128), Js(8388608), Js(8193), Js(8320), Js(8388737), Js(1), Js(8320), Js(8388736), Js(8192), Js(8396928), Js(8396929), Js(129), Js(8388736), Js(8388609), Js(8396800), Js(8396929), Js(129), Js(0.0), Js(0.0), Js(8396800), Js(8320), Js(8388736), Js(8388737), Js(1), Js(8396801), Js(8321), Js(8321), Js(128), Js(8396929), Js(129), Js(1), Js(8192), Js(8388609), Js(8193), Js(8396928), Js(8388737), Js(8193), Js(8320), Js(8388608), Js(8396801), Js(128), Js(8388608), Js(8192), Js(8396928))
    var.put('spfunction4', PyJs_LONG_3_())
    def PyJs_LONG_4_(var=var):
        return var.get('Array').create(Js(256), Js(34078976), Js(34078720), Js(1107296512), Js(524288), Js(256), Js(1073741824), Js(34078720), Js(1074266368), Js(524288), Js(33554688), Js(1074266368), Js(1107296512), Js(1107820544), Js(524544), Js(1073741824), Js(33554432), Js(1074266112), Js(1074266112), Js(0.0), Js(1073742080), Js(1107820800), Js(1107820800), Js(33554688), Js(1107820544), Js(1073742080), Js(0.0), Js(1107296256), Js(34078976), Js(33554432), Js(1107296256), Js(524544), Js(524288), Js(1107296512), Js(256), Js(33554432), Js(1073741824), Js(34078720), Js(1107296512), Js(1074266368), Js(33554688), Js(1073741824), Js(1107820544), Js(34078976), Js(1074266368), Js(256), Js(33554432), Js(1107820544), Js(1107820800), Js(524544), Js(1107296256), Js(1107820800), Js(34078720), Js(0.0), Js(1074266112), Js(1107296256), Js(524544), Js(33554688), Js(1073742080), Js(524288), Js(0.0), Js(1074266112), Js(34078976), Js(1073742080))
    var.put('spfunction5', PyJs_LONG_4_())
    def PyJs_LONG_5_(var=var):
        return var.get('Array').create(Js(536870928), Js(541065216), Js(16384), Js(541081616), Js(541065216), Js(16), Js(541081616), Js(4194304), Js(536887296), Js(4210704), Js(4194304), Js(536870928), Js(4194320), Js(536887296), Js(536870912), Js(16400), Js(0.0), Js(4194320), Js(536887312), Js(16384), Js(4210688), Js(536887312), Js(16), Js(541065232), Js(541065232), Js(0.0), Js(4210704), Js(541081600), Js(16400), Js(4210688), Js(541081600), Js(536870912), Js(536887296), Js(16), Js(541065232), Js(4210688), Js(541081616), Js(4194304), Js(16400), Js(536870928), Js(4194304), Js(536887296), Js(536870912), Js(16400), Js(536870928), Js(541081616), Js(4210688), Js(541065216), Js(4210704), Js(541081600), Js(0.0), Js(541065232), Js(16), Js(16384), Js(541065216), Js(4210704), Js(16384), Js(4194320), Js(536887312), Js(0.0), Js(541081600), Js(536870912), Js(4194320), Js(536887312))
    var.put('spfunction6', PyJs_LONG_5_())
    def PyJs_LONG_6_(var=var):
        return var.get('Array').create(Js(2097152), Js(69206018), Js(67110914), Js(0.0), Js(2048), Js(67110914), Js(2099202), Js(69208064), Js(69208066), Js(2097152), Js(0.0), Js(67108866), Js(2), Js(67108864), Js(69206018), Js(2050), Js(67110912), Js(2099202), Js(2097154), Js(67110912), Js(67108866), Js(69206016), Js(69208064), Js(2097154), Js(69206016), Js(2048), Js(2050), Js(69208066), Js(2099200), Js(2), Js(67108864), Js(2099200), Js(67108864), Js(2099200), Js(2097152), Js(67110914), Js(67110914), Js(69206018), Js(69206018), Js(2), Js(2097154), Js(67108864), Js(67110912), Js(2097152), Js(69208064), Js(2050), Js(2099202), Js(69208064), Js(2050), Js(67108866), Js(69208066), Js(69206016), Js(2099200), Js(0.0), Js(2), Js(69208066), Js(0.0), Js(2099202), Js(69206016), Js(2048), Js(67108866), Js(67110912), Js(2048), Js(2097154))
    var.put('spfunction7', PyJs_LONG_6_())
    def PyJs_LONG_7_(var=var):
        return var.get('Array').create(Js(268439616), Js(4096), Js(262144), Js(268701760), Js(268435456), Js(268439616), Js(64), Js(268435456), Js(262208), Js(268697600), Js(268701760), Js(266240), Js(268701696), Js(266304), Js(4096), Js(64), Js(268697600), Js(268435520), Js(268439552), Js(4160), Js(266240), Js(262208), Js(268697664), Js(268701696), Js(4160), Js(0.0), Js(0.0), Js(268697664), Js(268435520), Js(268439552), Js(266304), Js(262144), Js(266304), Js(262144), Js(268701696), Js(4096), Js(64), Js(268697664), Js(4096), Js(266304), Js(268439552), Js(64), Js(268435520), Js(268697600), Js(268697664), Js(268435456), Js(262144), Js(268439616), Js(0.0), Js(268701760), Js(262208), Js(268435520), Js(268697600), Js(268439552), Js(268439616), Js(0.0), Js(268701760), Js(266240), Js(266240), Js(4160), Js(4160), Js(262208), Js(268435456), Js(268701696))
    var.put('spfunction8', PyJs_LONG_7_())
    var.put('keys', var.get('des_createKeys')(var.get('beinetkey')))
    var.put('m', Js(0.0))
    pass
    pass
    var.put('len', var.get('message').get('length'))
    var.put('chunk', Js(0.0))
    var.put('iterations', (Js(3.0) if (var.get('keys').get('length')==Js(32.0)) else Js(9.0)))
    if (var.get('iterations')==Js(3.0)):
        var.put('looping', (var.get('Array').create(Js(0.0), Js(32.0), Js(2.0)) if var.get('encrypt') else var.get('Array').create(Js(30.0), (-Js(2.0)), (-Js(2.0)))))
    else:
        var.put('looping', (var.get('Array').create(Js(0.0), Js(32.0), Js(2.0), Js(62.0), Js(30.0), (-Js(2.0)), Js(64.0), Js(96.0), Js(2.0)) if var.get('encrypt') else var.get('Array').create(Js(94.0), Js(62.0), (-Js(2.0)), Js(32.0), Js(64.0), Js(2.0), Js(30.0), (-Js(2.0)), (-Js(2.0)))))
    var.put('message', Js('\x00\x00\x00\x00\x00\x00\x00\x00'), '+')
    var.put('result', Js(''))
    var.put('tempresult', Js(''))
    if (var.get('mode')==Js(1.0)):
        def PyJs_LONG_8_(var=var):
            return ((((var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
        var.put('cbcleft', PyJs_LONG_8_())
        def PyJs_LONG_9_(var=var):
            return ((((var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('iv').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
        var.put('cbcright', PyJs_LONG_9_())
        var.put('m', Js(0.0))
    while (var.get('m')<var.get('len')):
        if var.get('encrypt'):
            var.put('left', ((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))))
            var.put('right', ((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))))
        else:
            def PyJs_LONG_10_(var=var):
                return ((((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            var.put('left', PyJs_LONG_10_())
            def PyJs_LONG_11_(var=var):
                return ((((var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('message').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            var.put('right', PyJs_LONG_11_())
        if (var.get('mode')==Js(1.0)):
            if var.get('encrypt'):
                var.put('left', var.get('cbcleft'), '^')
                var.put('right', var.get('cbcright'), '^')
            else:
                var.put('cbcleft2', var.get('cbcleft'))
                var.put('cbcright2', var.get('cbcright'))
                var.put('cbcleft', var.get('left'))
                var.put('cbcright', var.get('right'))
        var.put('temp', ((PyJsBshift(var.get('left'),Js(4.0))^var.get('right'))&Js(252645135)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(4.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('left'),Js(16.0))^var.get('right'))&Js(65535)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(16.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('right'),Js(2.0))^var.get('left'))&Js(858993459)))
        var.put('left', var.get('temp'), '^')
        var.put('right', (var.get('temp')<<Js(2.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('right'),Js(8.0))^var.get('left'))&Js(16711935)))
        var.put('left', var.get('temp'), '^')
        var.put('right', (var.get('temp')<<Js(8.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('left'),Js(1.0))^var.get('right'))&Js(1431655765)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(1.0)), '^')
        var.put('left', ((var.get('left')<<Js(1.0))|PyJsBshift(var.get('left'),Js(31.0))))
        var.put('right', ((var.get('right')<<Js(1.0))|PyJsBshift(var.get('right'),Js(31.0))))
        #for JS loop
        var.put('j', Js(0.0))
        while (var.get('j')<var.get('iterations')):
            try:
                var.put('endloop', var.get('looping').get((var.get('j')+Js(1.0))))
                var.put('loopinc', var.get('looping').get((var.get('j')+Js(2.0))))
                #for JS loop
                var.put('i', var.get('looping').get(var.get('j')))
                while (var.get('i')!=var.get('endloop')):
                    try:
                        var.put('right1', (var.get('right')^var.get('keys').get(var.get('i'))))
                        var.put('right2', ((PyJsBshift(var.get('right'),Js(4.0))|(var.get('right')<<Js(28.0)))^var.get('keys').get((var.get('i')+Js(1.0)))))
                        var.put('temp', var.get('left'))
                        var.put('left', var.get('right'))
                        def PyJs_LONG_12_(var=var):
                            return (((((var.get('spfunction2').get((PyJsBshift(var.get('right1'),Js(24.0))&Js(63)))|var.get('spfunction4').get((PyJsBshift(var.get('right1'),Js(16.0))&Js(63))))|var.get('spfunction6').get((PyJsBshift(var.get('right1'),Js(8.0))&Js(63))))|var.get('spfunction8').get((var.get('right1')&Js(63))))|var.get('spfunction1').get((PyJsBshift(var.get('right2'),Js(24.0))&Js(63))))|var.get('spfunction3').get((PyJsBshift(var.get('right2'),Js(16.0))&Js(63))))
                        var.put('right', (var.get('temp')^((PyJs_LONG_12_()|var.get('spfunction5').get((PyJsBshift(var.get('right2'),Js(8.0))&Js(63))))|var.get('spfunction7').get((var.get('right2')&Js(63))))))
                    finally:
                            var.put('i', var.get('loopinc'), '+')
                var.put('temp', var.get('left'))
                var.put('left', var.get('right'))
                var.put('right', var.get('temp'))
            finally:
                    var.put('j', Js(3.0), '+')
        var.put('left', (PyJsBshift(var.get('left'),Js(1.0))|(var.get('left')<<Js(31.0))))
        var.put('right', (PyJsBshift(var.get('right'),Js(1.0))|(var.get('right')<<Js(31.0))))
        var.put('temp', ((PyJsBshift(var.get('left'),Js(1.0))^var.get('right'))&Js(1431655765)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(1.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('right'),Js(8.0))^var.get('left'))&Js(16711935)))
        var.put('left', var.get('temp'), '^')
        var.put('right', (var.get('temp')<<Js(8.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('right'),Js(2.0))^var.get('left'))&Js(858993459)))
        var.put('left', var.get('temp'), '^')
        var.put('right', (var.get('temp')<<Js(2.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('left'),Js(16.0))^var.get('right'))&Js(65535)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(16.0)), '^')
        var.put('temp', ((PyJsBshift(var.get('left'),Js(4.0))^var.get('right'))&Js(252645135)))
        var.put('right', var.get('temp'), '^')
        var.put('left', (var.get('temp')<<Js(4.0)), '^')
        if (var.get('mode')==Js(1.0)):
            if var.get('encrypt'):
                var.put('cbcleft', var.get('left'))
                var.put('cbcright', var.get('right'))
            else:
                var.put('left', var.get('cbcleft2'), '^')
                var.put('right', var.get('cbcright2'), '^')
        if var.get('encrypt'):
            var.put('tempresult', var.get('String').callprop('fromCharCode', PyJsBshift(var.get('left'),Js(24.0)), (PyJsBshift(var.get('left'),Js(16.0))&Js(255)), (PyJsBshift(var.get('left'),Js(8.0))&Js(255)), (var.get('left')&Js(255)), PyJsBshift(var.get('right'),Js(24.0)), (PyJsBshift(var.get('right'),Js(16.0))&Js(255)), (PyJsBshift(var.get('right'),Js(8.0))&Js(255)), (var.get('right')&Js(255))), '+')
        else:
            var.put('tempresult', var.get('String').callprop('fromCharCode', (PyJsBshift(var.get('left'),Js(16.0))&Js(65535)), (var.get('left')&Js(65535)), (PyJsBshift(var.get('right'),Js(16.0))&Js(65535)), (var.get('right')&Js(65535))), '+')
        (var.put('chunk', Js(16.0), '+') if var.get('encrypt') else var.put('chunk', Js(8.0), '+'))
        if (var.get('chunk')==Js(512.0)):
            var.put('result', var.get('tempresult'), '+')
            var.put('tempresult', Js(''))
            var.put('chunk', Js(0.0))
    return (var.get('result')+var.get('tempresult'))
PyJsHoisted_des_.func_name = 'des'
var.put('des', PyJsHoisted_des_)
@Js
def PyJsHoisted_des_createKeys_(beinetkey, this, arguments, var=var):
    var = Scope({'beinetkey':beinetkey, 'this':this, 'arguments':arguments}, var)
    var.registers(['keys', 'righttemp', 'temp', 'lefttemp', 'shifts', 'beinetkey', 'n', 'j', 'iterations', 'm'])
    var.put('pc2bytes0', var.get('Array').create(Js(0.0), Js(4), Js(536870912), Js(536870916), Js(65536), Js(65540), Js(536936448), Js(536936452), Js(512), Js(516), Js(536871424), Js(536871428), Js(66048), Js(66052), Js(536936960), Js(536936964)))
    var.put('pc2bytes1', var.get('Array').create(Js(0.0), Js(1), Js(1048576), Js(1048577), Js(67108864), Js(67108865), Js(68157440), Js(68157441), Js(256), Js(257), Js(1048832), Js(1048833), Js(67109120), Js(67109121), Js(68157696), Js(68157697)))
    var.put('pc2bytes2', var.get('Array').create(Js(0.0), Js(8), Js(2048), Js(2056), Js(16777216), Js(16777224), Js(16779264), Js(16779272), Js(0.0), Js(8), Js(2048), Js(2056), Js(16777216), Js(16777224), Js(16779264), Js(16779272)))
    var.put('pc2bytes3', var.get('Array').create(Js(0.0), Js(2097152), Js(134217728), Js(136314880), Js(8192), Js(2105344), Js(134225920), Js(136323072), Js(131072), Js(2228224), Js(134348800), Js(136445952), Js(139264), Js(2236416), Js(134356992), Js(136454144)))
    var.put('pc2bytes4', var.get('Array').create(Js(0.0), Js(262144), Js(16), Js(262160), Js(0.0), Js(262144), Js(16), Js(262160), Js(4096), Js(266240), Js(4112), Js(266256), Js(4096), Js(266240), Js(4112), Js(266256)))
    var.put('pc2bytes5', var.get('Array').create(Js(0.0), Js(1024), Js(32), Js(1056), Js(0.0), Js(1024), Js(32), Js(1056), Js(33554432), Js(33555456), Js(33554464), Js(33555488), Js(33554432), Js(33555456), Js(33554464), Js(33555488)))
    var.put('pc2bytes6', var.get('Array').create(Js(0.0), Js(268435456), Js(524288), Js(268959744), Js(2), Js(268435458), Js(524290), Js(268959746), Js(0.0), Js(268435456), Js(524288), Js(268959744), Js(2), Js(268435458), Js(524290), Js(268959746)))
    var.put('pc2bytes7', var.get('Array').create(Js(0.0), Js(65536), Js(2048), Js(67584), Js(536870912), Js(536936448), Js(536872960), Js(536938496), Js(131072), Js(196608), Js(133120), Js(198656), Js(537001984), Js(537067520), Js(537004032), Js(537069568)))
    var.put('pc2bytes8', var.get('Array').create(Js(0.0), Js(262144), Js(0.0), Js(262144), Js(2), Js(262146), Js(2), Js(262146), Js(33554432), Js(33816576), Js(33554432), Js(33816576), Js(33554434), Js(33816578), Js(33554434), Js(33816578)))
    var.put('pc2bytes9', var.get('Array').create(Js(0.0), Js(268435456), Js(8), Js(268435464), Js(0.0), Js(268435456), Js(8), Js(268435464), Js(1024), Js(268436480), Js(1032), Js(268436488), Js(1024), Js(268436480), Js(1032), Js(268436488)))
    var.put('pc2bytes10', var.get('Array').create(Js(0.0), Js(32), Js(0.0), Js(32), Js(1048576), Js(1048608), Js(1048576), Js(1048608), Js(8192), Js(8224), Js(8192), Js(8224), Js(1056768), Js(1056800), Js(1056768), Js(1056800)))
    var.put('pc2bytes11', var.get('Array').create(Js(0.0), Js(16777216), Js(512), Js(16777728), Js(2097152), Js(18874368), Js(2097664), Js(18874880), Js(67108864), Js(83886080), Js(67109376), Js(83886592), Js(69206016), Js(85983232), Js(69206528), Js(85983744)))
    var.put('pc2bytes12', var.get('Array').create(Js(0.0), Js(4096), Js(134217728), Js(134221824), Js(524288), Js(528384), Js(134742016), Js(134746112), Js(16), Js(4112), Js(134217744), Js(134221840), Js(524304), Js(528400), Js(134742032), Js(134746128)))
    var.put('pc2bytes13', var.get('Array').create(Js(0.0), Js(4), Js(256), Js(260), Js(0.0), Js(4), Js(256), Js(260), Js(1), Js(5), Js(257), Js(261), Js(1), Js(5), Js(257), Js(261)))
    var.put('iterations', (Js(3.0) if (var.get('beinetkey').get('length')>=Js(24.0)) else Js(1.0)))
    var.put('keys', var.get('Array').create((Js(32.0)*var.get('iterations'))))
    var.put('shifts', var.get('Array').create(Js(0.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(1.0), Js(0.0)))
    var.put('m', Js(0.0))
    var.put('n', Js(0.0))
    #for JS loop
    var.put('j', Js(0.0))
    while (var.get('j')<var.get('iterations')):
        try:
            def PyJs_LONG_13_(var=var):
                return ((((var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            var.put('left', PyJs_LONG_13_())
            def PyJs_LONG_14_(var=var):
                return ((((var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(24.0))|(var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(16.0)))|(var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1)))<<Js(8.0)))|var.get('beinetkey').callprop('charCodeAt', (var.put('m',Js(var.get('m').to_number())+Js(1))-Js(1))))
            var.put('right', PyJs_LONG_14_())
            var.put('temp', ((PyJsBshift(var.get('left'),Js(4.0))^var.get('right'))&Js(252645135)))
            var.put('right', var.get('temp'), '^')
            var.put('left', (var.get('temp')<<Js(4.0)), '^')
            var.put('temp', ((PyJsBshift(var.get('right'),(-Js(16.0)))^var.get('left'))&Js(65535)))
            var.put('left', var.get('temp'), '^')
            var.put('right', (var.get('temp')<<(-Js(16.0))), '^')
            var.put('temp', ((PyJsBshift(var.get('left'),Js(2.0))^var.get('right'))&Js(858993459)))
            var.put('right', var.get('temp'), '^')
            var.put('left', (var.get('temp')<<Js(2.0)), '^')
            var.put('temp', ((PyJsBshift(var.get('right'),(-Js(16.0)))^var.get('left'))&Js(65535)))
            var.put('left', var.get('temp'), '^')
            var.put('right', (var.get('temp')<<(-Js(16.0))), '^')
            var.put('temp', ((PyJsBshift(var.get('left'),Js(1.0))^var.get('right'))&Js(1431655765)))
            var.put('right', var.get('temp'), '^')
            var.put('left', (var.get('temp')<<Js(1.0)), '^')
            var.put('temp', ((PyJsBshift(var.get('right'),Js(8.0))^var.get('left'))&Js(16711935)))
            var.put('left', var.get('temp'), '^')
            var.put('right', (var.get('temp')<<Js(8.0)), '^')
            var.put('temp', ((PyJsBshift(var.get('left'),Js(1.0))^var.get('right'))&Js(1431655765)))
            var.put('right', var.get('temp'), '^')
            var.put('left', (var.get('temp')<<Js(1.0)), '^')
            var.put('temp', ((var.get('left')<<Js(8.0))|(PyJsBshift(var.get('right'),Js(20.0))&Js(240))))
            var.put('left', ((((var.get('right')<<Js(24.0))|((var.get('right')<<Js(8.0))&Js(16711680)))|(PyJsBshift(var.get('right'),Js(8.0))&Js(65280)))|(PyJsBshift(var.get('right'),Js(24.0))&Js(240))))
            var.put('right', var.get('temp'))
            #for JS loop
            var.put('i', Js(0.0))
            while (var.get('i')<var.get('shifts').get('length')):
                try:
                    if var.get('shifts').get(var.get('i')):
                        var.put('left', ((var.get('left')<<Js(2.0))|PyJsBshift(var.get('left'),Js(26.0))))
                        var.put('right', ((var.get('right')<<Js(2.0))|PyJsBshift(var.get('right'),Js(26.0))))
                    else:
                        var.put('left', ((var.get('left')<<Js(1.0))|PyJsBshift(var.get('left'),Js(27.0))))
                        var.put('right', ((var.get('right')<<Js(1.0))|PyJsBshift(var.get('right'),Js(27.0))))
                    var.put('left', (-Js(15)), '&')
                    var.put('right', (-Js(15)), '&')
                    def PyJs_LONG_15_(var=var):
                        return (((((var.get('pc2bytes0').get(PyJsBshift(var.get('left'),Js(28.0)))|var.get('pc2bytes1').get((PyJsBshift(var.get('left'),Js(24.0))&Js(15))))|var.get('pc2bytes2').get((PyJsBshift(var.get('left'),Js(20.0))&Js(15))))|var.get('pc2bytes3').get((PyJsBshift(var.get('left'),Js(16.0))&Js(15))))|var.get('pc2bytes4').get((PyJsBshift(var.get('left'),Js(12.0))&Js(15))))|var.get('pc2bytes5').get((PyJsBshift(var.get('left'),Js(8.0))&Js(15))))
                    var.put('lefttemp', (PyJs_LONG_15_()|var.get('pc2bytes6').get((PyJsBshift(var.get('left'),Js(4.0))&Js(15)))))
                    def PyJs_LONG_16_(var=var):
                        return (((((var.get('pc2bytes7').get(PyJsBshift(var.get('right'),Js(28.0)))|var.get('pc2bytes8').get((PyJsBshift(var.get('right'),Js(24.0))&Js(15))))|var.get('pc2bytes9').get((PyJsBshift(var.get('right'),Js(20.0))&Js(15))))|var.get('pc2bytes10').get((PyJsBshift(var.get('right'),Js(16.0))&Js(15))))|var.get('pc2bytes11').get((PyJsBshift(var.get('right'),Js(12.0))&Js(15))))|var.get('pc2bytes12').get((PyJsBshift(var.get('right'),Js(8.0))&Js(15))))
                    var.put('righttemp', (PyJs_LONG_16_()|var.get('pc2bytes13').get((PyJsBshift(var.get('right'),Js(4.0))&Js(15)))))
                    var.put('temp', ((PyJsBshift(var.get('righttemp'),Js(16.0))^var.get('lefttemp'))&Js(65535)))
                    var.get('keys').put((var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)), (var.get('lefttemp')^var.get('temp')))
                    var.get('keys').put((var.put('n',Js(var.get('n').to_number())+Js(1))-Js(1)), (var.get('righttemp')^(var.get('temp')<<Js(16.0))))
                finally:
                        (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
        finally:
                (var.put('j',Js(var.get('j').to_number())+Js(1))-Js(1))
    return var.get('keys')
PyJsHoisted_des_createKeys_.func_name = 'des_createKeys'
var.put('des_createKeys', PyJsHoisted_des_createKeys_)
@Js
def PyJsHoisted_stringToHex_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['hexes', 'r', 's', 'i'])
    var.put('r', Js(''))
    var.put('hexes', var.get('Array').create(Js('0'), Js('1'), Js('2'), Js('3'), Js('4'), Js('5'), Js('6'), Js('7'), Js('8'), Js('9'), Js('a'), Js('b'), Js('c'), Js('d'), Js('e'), Js('f')))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('s').get('length')):
        try:
            var.put('r', (var.get('hexes').get((var.get('s').callprop('charCodeAt', var.get('i'))>>Js(4.0)))+var.get('hexes').get((var.get('s').callprop('charCodeAt', var.get('i'))&Js(15)))), '+')
        finally:
                (var.put('i',Js(var.get('i').to_number())+Js(1))-Js(1))
    return var.get('r')
PyJsHoisted_stringToHex_.func_name = 'stringToHex'
var.put('stringToHex', PyJsHoisted_stringToHex_)
@Js
def PyJsHoisted_HexTostring_(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['sxx', 'i', 'r', 's'])
    var.put('r', Js(''))
    #for JS loop
    var.put('i', Js(0.0))
    while (var.get('i')<var.get('s').get('length')):
        try:
            var.put('sxx', var.get('parseInt')(var.get('s').callprop('substring', var.get('i'), (var.get('i')+Js(2.0))), Js(16.0)))
            var.put('r', var.get('String').callprop('fromCharCode', var.get('sxx')), '+')
        finally:
                var.put('i', Js(2.0), '+')
    return var.get('r')
PyJsHoisted_HexTostring_.func_name = 'HexTostring'
var.put('HexTostring', PyJsHoisted_HexTostring_)
@Js
def encMe(s, this, arguments, var=var):
    var = Scope({'s':s, 'this':this, 'arguments':arguments}, var)
    var.registers(['s'])
    return var.get('stringToHex')(var.get('des')(Js('5/4fu618'), var.get('s'), Js(1.0), Js(0.0)))