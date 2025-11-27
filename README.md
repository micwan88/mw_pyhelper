# mw_pyhelper

A set of python helper classes / utilities from MicWan

### Command to build and check
``` bash
#Build
uv build

#Check the packages (under UV venv)
twine check dist/*

#or using UV
uv run --locked twine check dist/*
```