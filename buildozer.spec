[app]
title = Gauravi AI
package.name = gauraviai
package.domain = org.papa
source.dir = .
# फालतू फाइलें हटा दीं ताकि बिल्ड फेल न हो
source.include_exts = py,png,jpg,ttf,fst
version = 1.1

requirements = python3,kivy,android,pyjnius

orientation = portrait

# सिर्फ सबसे ज़रूरी परमिशन अभी के लिए
android.permissions = INTERNET, CALL_PHONE, SEND_SMS, READ_CONTACTS, RECORD_AUDIO, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE

android.api = 33
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
