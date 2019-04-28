$name = Read-Host 'Enter Remote Computer Name:'

Invoke-Command -ComputerName $name `
{Set-ItemProperty `
-Path 'HKLM:\System\CurrentControlSet\Control\Terminal Server'`
-Name "fDenyTSConnections" -Value 1; `
Enable-NetFirewallRule -DisplayGroup "Remote Desktop"}