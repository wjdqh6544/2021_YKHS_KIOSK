@echo off
setlocal enabledelayedexpansion
echo *****************************************************
echo *
echo *   1. ui파일명을 입력하세요. 확장자 쓰지마세요.
echo *
set /p in=*   → 
echo *
echo *
echo *   2. 출력될 py 파일의 이름을 쓰세요. 확장자 쓰지마세요.
echo *
set /p out=*   → 
python -m PyQt5.uic.pyuic -x %in%.ui -o %out%.py
echo *
echo *   ################  변환 완료됨...  ################
echo *
echo *****************************************************
pause