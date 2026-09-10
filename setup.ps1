$ErrorActionPreference = "Stop"

$python = Join-Path $PSScriptRoot "venv\Scripts\python.exe"
if (-not (Test-Path -LiteralPath $python)) {
    py -3 -m venv (Join-Path $PSScriptRoot "venv")
}

& $python -m pip install -r (Join-Path $PSScriptRoot "requirements.txt")

$pythonVersion = & $python -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')"
if ([version]$pythonVersion -ge [version]"3.13") {
    & $python -m pip install --no-deps resemblyzer
}

if ((& $python -c "import sys; print(int(sys.version_info >= (3, 13)))") -eq "1") {
    & $python -m pip install --no-deps resemblyzer
}

Write-Host "SnapClass dependencies are installed."
