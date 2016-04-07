import sys
from cx_Freeze import setup, Executable
import os

##
##def include_files1():
##        path_base = "C:\\Python34\\Lib\\site-packages\\python-dateutil-2.4.2\\dateutil\\"
##        skip_count = len(path_base)
##        zip_includes = [(path_base, "dateutil")]
##        for root, sub_folders, files in os.walk(path_base):
##            for file_in_root in files:
##                zip_includes.append(
##                        ("{}".format(os.path.join(root, file_in_root)),
##                         "{}".format(os.path.join("dateutil", root[skip_count:], file_in_root))
##                        ) 
##                )
##        return zip_includes
##
##
##packages = []
##includefiles = [('C:\\Python34\\Lib\\fractions.py','fractions.py')]
##
##build_exe_options = { "packages" : packages ,'include_files':includefiles , "zip_includes": include_files1()}


setup(
    name = "Creep Data Filter",
    version = "1.0",
    description = "Creep Data Filter Exe",
    #options = {"build_exe": build_exe_options },
    executables = [Executable("Main.py", base = "console")])
