function setHostEntries([hashtable] $entries) { 
    $hostsFile = "$env:windir\System32\drivers\etc\hosts" 
    $newLines = @() 

    $c = Get-Content -Path $hostsFile 
    foreach ($line in $c) { 
     $bits = [regex]::Split($line, "\s+") 
     if ($bits.count -eq 2) { 
      $match = $NULL 
      ForEach($entry in $entries.GetEnumerator()) { 
       if($bits[1] -eq $entry.Key) { 
        $newLines += ($entry.Value + '  ' + $entry.Key) 
        Write-Host Replacing HOSTS entry for $entry.Key 
        $match = $entry.Key 
        break 
       } 
      } 
      if($match -eq $NULL) { 
       $newLines += $line 
      } else { 
       $entries.Remove($match) 
      } 
     } else { 
      $newLines += $line 
     } 
    } 

    foreach($entry in $entries.GetEnumerator()) { 
     Write-Host Adding HOSTS entry for $entry.Key 
     $newLines += $entry.Value + '  ' + $entry.Key 
    } 

    Write-Host Saving $hostsFile 
    Clear-Content $hostsFile 
    foreach ($line in $newLines) { 
     $line | Out-File -encoding ASCII -append $hostsFile 
    } 
} 

$entries = @{ 
    "vaxtpmde69.proteccion.com.co" = "172.30.57.12"
    "vostpmde37.proteccion.com.co" = "172.30.57.11"
    "vosdcbog04.proteccion.com.co" = "172.30.57.13:9459"
    "servicios.proteccion.com.co" = "172.30.57.14:4443"
    "apolo-qa.proteccion.com.co" = "172.30.57.15"
};
setHostEntries($entries) 