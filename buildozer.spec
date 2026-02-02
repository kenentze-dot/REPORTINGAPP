[app]
title = Enercapita Scanner
package.name = enercapitaddr
package.domain = org.rigtool
source.dir = .
source.include_exts = py,png,jpg,kv,xlsm
requirements = python3, kivy==2.2.1, openpyxl, pandas, jnius, pillow

# Important Permissions
android.permissions = CAMERA, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
orientation = portrait
fullscreen = 1

[buildozer]
log_level = 2
warn_on_root = 1
