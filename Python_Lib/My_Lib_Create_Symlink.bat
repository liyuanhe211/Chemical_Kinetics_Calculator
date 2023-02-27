pushd %~dp0
powershell -Command "New-Item -ItemType HardLink -Path .\My_Lib.py -Target ..\..\Python_Lib\My_Lib.py"
pause