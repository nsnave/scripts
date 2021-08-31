Rem User Variables
set netid=ate4

Rem Constant Variables
set remoteserver=node.zoo.cs.yale.edu
set menutext=SCP to Zoo
set command1=cmd.exe /c \"scp -r %%1 ate4@node.zoo.cs.yale.edu:~/scp\"
set command2=cmd.exe /c \"scp -r %%V ate4@node.zoo.cs.yale.edu:~/scp\"

Rem Adds registry keys for context menu
REG ADD "HKEY_CURRENT_USER\Software\Classes\*\shell\%menutext%\command" /d "%command1%" /f
REG ADD "HKEY_CURRENT_USER\Software\Classes\directory\shell\%menutext%\command" /d "%command2%" /f
REG ADD "HKEY_CURRENT_USER\Software\Classes\directory\Background\shell\%menutext%\command" /d "%command2%" /f

pause
