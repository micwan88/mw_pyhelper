# Project File Structure

```

Project Folder
├── CLAUDE.md
├── .claude/rules/                ← claude code project rules
│   ├── python-rules.md           ← python specific rules
│   └── xxxx
├── tasks/
│   ├── story-1-r1-template.md    ← request template
│   ├── story-{id}-r{rev}.md      ← request with `unique ID` and `revision` from user
│   ├── xxxx-plan-{id}-r{rev}.md  ← work plan correspond to `unique ID + revision` request
│   ├── xxxx-note.md              ← lessons capture by agent
│   ├── ...
│   └── archived/                 ← archive folder for tasks related files
├── assets/                       ← static project files
│   ├── file-structure.md         ← project file structure
│   ├── sop.md                    ← project sop
│   └── ...
├── src/mw_pyhelper/              ← codebase files
│   ├── messaging                 ← helper/utilities about messaging
│   ├── network                   ← helper/utilities about network
│   ├── webbot                    ← helper/utilities about web bot
│   ├── cfgloader.py              ← common cfg loader
│   ├── logcfg.py                 ← common log cfg loader
│   ├── __init__.py               ← default package file that define package version
│   └── ...
├── tests/unit/                   ← unittest files (offline tests)
│   ├── messaging/xxxx1                     
│   └── ...
├── tests/integration/            ← integration test files
│   ├── messaging/xxxx1                     
│   └── ...
├── pyproject.toml                ← python project definition
├── uv.lock                       ← uv lock file
└── xxxxx                         ← other project file (LICENSE, README, ... etc)

```