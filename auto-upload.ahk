^!a::
RunWait,%A_ScriptDir%\QQSnapShot.exe
return

^!s::
cmd = python %A_ScriptDir%\qi.py
Run,%comspec% /c %cmd%





