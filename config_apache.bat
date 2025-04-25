@echo off

REM === CONFIGURE THESE VARIABLES ===

set APACHE_HOME=C:\Apache24

set PROJECT_DIR=C:\MyProject

set PYTHON_HOME=C:\Users\YourUser\AppData\Local\Programs\Python\Python311

set VENV_SCRIPTS=%PYTHON_HOME%\Scripts

set WSGI_SCRIPT=%PROJECT_DIR%\your_project\wsgi.py

set HTTPD_CONF=%APACHE_HOME%\conf\httpd.conf

REM === SETUP PYTHON ENV ===

set PATH=%VENV_SCRIPTS%;%PATH%

REM === CLEAN PREVIOUS WSGI CONFIG ===

findstr /V "mod_wsgi_autogen" "%HTTPD_CONF%" > "%HTTPD_CONF%.tmp"

move /Y "%HTTPD_CONF%.tmp" "%HTTPD_CONF%" >nul

REM === APPEND mod_wsgi config ===

echo Generating mod_wsgi config...

mod_wsgi-express module-config > mod_wsgi_config.txt

echo Inserting mod_wsgi config into httpd.conf...

(for /f "delims=" %%l in (mod_wsgi_config.txt) do echo %%l >> "%HTTPD_CONF%")

REM === ADD WSGI ALIASES AND PERMISSIONS ===

echo Adding WSGI app configuration...

(

echo ^# mod_wsgi_autogen

echo WSGIScriptAlias / "%WSGI_SCRIPT%"

echo ^<Directory "%PROJECT_DIR%\your_project"^>

echo     ^<Files wsgi.py^>

echo         Require all granted

echo     ^</Files^>

echo ^</Directory^>

) >> "%HTTPD_CONF%"

REM === START APACHE WITHOUT SERVICE ===

echo Starting Apache manually...

"%APACHE_HOME%\bin\httpd.exe" -k start -f "%HTTPD_CONF%"

echo Apache started. Press any key to stop.

pause

echo Stopping Apache...

"%APACHE_HOME%\bin\httpd.exe" -k stop -f "%HTTPD_CONF%"

echo Done.
