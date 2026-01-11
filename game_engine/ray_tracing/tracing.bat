@echo off
:loop
lua tracing.lua
timeout /t 1 >nul
goto loop
