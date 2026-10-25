# Copy the skills in this repo into an agent's skill folder.
#   .\scripts\install.ps1                      -> ~/.agents/skills        (OpenCode, global)
#   .\scripts\install.ps1 -Target claude       -> ~/.claude/skills        (Claude Code)
#   .\scripts\install.ps1 -Target project      -> ./.agents/skills        (current repo only)
#   .\scripts\install.ps1 -Path D:\app\.agents\skills
#   .\scripts\install.ps1 -All                 -> every skill (default: ask-free, copies all)
#   .\scripts\install.ps1 -Filter ffmpeg,seo   -> only folders matching these fragments
[CmdletBinding()]
param(
    [ValidateSet('opencode', 'claude', 'project')]
    [string]$Target = 'opencode',
    [string]$Path,
    [string[]]$Filter,
    [switch]$Force
)

$src = Join-Path (Split-Path -Parent $PSScriptRoot) 'skills'
if (-not (Test-Path $src)) { throw "skills folder not found: $src" }

$dest = if ($Path) { $Path }
    elseif ($Target -eq 'claude') { Join-Path $HOME '.claude\skills' }
    elseif ($Target -eq 'project') { Join-Path (Get-Location) '.agents\skills' }
    else { Join-Path $HOME '.agents\skills' }

New-Item -ItemType Directory -Force -Path $dest | Out-Null

$copied = 0
$skipped = 0
foreach ($dir in Get-ChildItem $src -Directory) {
    if ($Filter -and -not ($Filter | Where-Object { $dir.Name -like "*$_*" })) { continue }
    if (-not (Test-Path (Join-Path $dir.FullName 'SKILL.md'))) { continue }

    $target = Join-Path $dest $dir.Name
    if ((Test-Path $target) -and -not $Force) {
        $skipped++
        continue
    }
    Copy-Item -Recurse -Force $dir.FullName $target
    $copied++
}

Write-Host "Installed $copied skill(s) into $dest" -ForegroundColor Green
if ($skipped) { Write-Host "Skipped $skipped existing skill(s) - rerun with -Force to overwrite" -ForegroundColor Yellow }
Write-Host "Restart your agent session, then ask it to list the skills it can see."
