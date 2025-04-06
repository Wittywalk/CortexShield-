[app]

title = CortexShield
package.name = cortexshield
package.domain = org.wittywalk
version = 1.0

source.dir = .
source.main = run_all_processes.py

requirements = python3,kivy,requests==2.28.1,termcolor==1.1.0,loguru==0.5.3,psutil==5.9.1,simplejson==3.17.6,schedule==1.1.0,cython==0.29.24,pyjnius==1.3.0,pillow==8.4.0,setuptools==56.0.0

android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,WAKE_LOCK,FOREGROUND_SERVICE,RECEIVE_BOOT_COMPLETED

icon.filename = /storage/emulated/0/Downloads/CortexShield.png

source.include_exts = py,txt,png,jpg,json,sh
include_patterns = *.py,*.json,*.sh

orientation = portrait
fullscreen = 0
log_enable = 1

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools_version = 33.0.2

android.private_storage = True
android.copy_libs = 1
use_pip = True

source.include_dirs = ./lib,./logs,./bin,./modules,./scripts,./backups,./CortexShield
android.include_dirs = /data/data/com.termux/files/usr/include
android.library_dirs = /usr/lib/aarch64-linux-gnu

android.add_libs = ./lib/libz.so,./lib/libz.so.1,./lib/libz.so.1.3.1

# GitHub repo can be linked via comments or used in metadata (this has no effect on build)
# GitHub Repository: https://github.com/Wittywalk/CortexShield
# Add the supported architectures
android.arch = armeabi-v7a arm64-v8a
# (Optional) You can leave this blank unless you have a custom run command
custom_command =





