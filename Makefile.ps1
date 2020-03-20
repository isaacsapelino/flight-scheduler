$CurrentDir = $(get-location).path
$PlanMigDir = Join-Path $CurrentDir -ChildPath "plan" | Join-Path -ChildPath "migrations"
$Test = Get-ChildItem -Path $PlanMigDir  *.py -recurse -exclude __init__.py | foreach { Remove-Item -Path $_.FullName }

Remove-Item .\db.sqlite3
