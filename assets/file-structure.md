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
│   └── ...
├── assets/                       ← static project files
│   ├── sop.md                    ← project sop
│   ├── file-structure.md         ← project file structure
│   └── ...
├── src/mw_pyhelper/              ← codebase files
│   ├── messaging                 ← helper/utilities about messaging
│   ├── network                   ← helper/utilities about network
│   ├── webbot                    ← helper/utilities about web bot
│   ├── cfgloader.py              ← common cfg loader
│   ├── logcfg.py                 ← common log cfg loader
│   ├── __init__.py               ← default package file that define package version
│   └── ...
├── pyproject.toml                ← python project definition
├── uv.lock                       ← uv lock file
└── xxxxx                         ← other project file (LICENSE, README, ... etc)

```