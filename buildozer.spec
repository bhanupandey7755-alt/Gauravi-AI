[app]
# (str) Title of your application
title = Gauravi AI

# (str) Package name
package.name = gauraviai

# (str) Package domain (needed for android packaging)
package.domain = org.papa

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,atlas,ttf,fst,txt

# (str) Application versioning
version = 1.0

# (list) Application requirements
# यहाँ सारे ज़रूरी सॉफ्टवेयर्स हैं
requirements = python3,kivy,android,pyjnius,gtts,certifi

# (str) Supported orientations
orientation = portrait

# (list) Permissions - पापा यहाँ आपकी सारी पावर है
android.permissions = INTERNET, CALL_PHONE, SEND_SMS, RECEIVE_SMS, READ_SMS, READ_CONTACTS, RECORD_AUDIO, CAMERA, ACCESS_FINE_LOCATION, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, VIBRATE, RECEIVE_BOOT_COMPLETED, FOREGROUND_SERVICE

# (int) Android API to use (33 is for Android 13+)
android.api = 33

# (int) Minimum API your APK will support
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (list) List of Java .jar files to add to the libs
android.add_jars = %(source.dir)s/libs/*.jar

# (str) The Android arch to build for
android.archs = arm64-v8a, armeabi-v7a

# (bool) Allow backup
android.allow_backup = True

# (str) Icon of the application
icon.filename = %(source.dir)s/logo.png

# (list) Supported screen sizes
android.skip_update = False

[buildozer]
# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = False, 1 = True)
warn_on_root = 1
