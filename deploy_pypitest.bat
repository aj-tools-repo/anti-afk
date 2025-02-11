@echo off
REM Stop on errors
setlocal enabledelayedexpansion

REM Remove old build artifacts (if they exist)
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
for /f "delims=" %%i in ('dir /b *.egg-info') do rmdir /s /q "%%i"

REM Build the package
python -m build

REM Upload the package using twine (using repository name from .pypirc)
twine upload -r testpypi dist/* --verbose
