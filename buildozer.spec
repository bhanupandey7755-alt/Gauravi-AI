[app]
# ऐप का नाम और जानकारी
title = Gauravi AI
package.name = gauraviai
package.domain = org.gauravi
source.dir = .

# इसमें py, png, और ttf (फॉन्ट) तीनों शामिल हैं
source.include_exts = py,png,jpg,kv,atlas,ttf
version = 1.0

# ऐप का आइकॉन और शुरूआती फोटो (जो आपने अपलोड की है)
icon.filename = %(source.dir)s/logo.png
presplash.filename = %(source.dir)s/logo.png

# आवाज़ (Voice) और Android सिस्टम के तालमेल के लिए ज़रूरी लाइब्रेरीज़
# pyjnius से ऐप एंड्रॉइड की असली आवाज़ का इस्तेमाल कर पाएगी
requirements = python3, kivy, pyjnius, android

# परमिशन: इंटरनेट और आवाज़ रिकॉर्ड करने के लिए
android.permissions = INTERNET, RECORD_AUDIO, MODIFY_AUDIO_SETTINGS

# स्क्रीन सेटिंग्स
orientation = portrait
fullscreen = 1

# एंड्रॉइड वर्जन और आर्किटेक्चर (नये फोंस के लिए arm64-v8a ज़रूरी है)
android.arch = arm64-v8a
android.api = 31
android.minapi = 21

# बिल्ड को साफ़ रखने के लिए
[buildozer]
log_level = 2
warn_on_root = 1
