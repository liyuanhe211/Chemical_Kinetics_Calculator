pushd %~dp0
powershell -Command "New-Item -ItemType HardLink -Path .\My_Lib_PyQt.py -Target ..\..\Python_Lib\My_Lib_PyQt.py"
pause