@echo off
setlocal enabledelayedexpansion
echo *****************************************************
echo *
echo *   1. ui���ϸ��� �Է��ϼ���. Ȯ���� ����������.
echo *
set /p in=*   �� 
echo *
echo *
echo *   2. ��µ� py ������ �̸��� ������. Ȯ���� ����������.
echo *
set /p out=*   �� 
python -m PyQt5.uic.pyuic -x %in%.ui -o %out%.py
echo *
echo *   ################  ��ȯ �Ϸ��...  ################
echo *
echo *****************************************************
pause