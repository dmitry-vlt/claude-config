#!/usr/bin/env python3
import json
import sys

payload = json.load(sys.stdin)
tool_input = payload.get("tool_input", {}) or {}
cmd = tool_input.get("command", "") or ""

safe_prefixes = [
    "python -c ",
    "python3 -c ",
    "pytest",
    "python -m pytest",
    "python3 -m pytest",
]

safe_substrings = [
    "from scripts.ingest_test.cli import parse_args",
    "subprocess.run(['python', '-m', 'scripts.ingest_test', '--help']",
    "subprocess.run([\"python\", \"-m\", \"scripts.ingest_test\", \"--help\"]",
]

is_safe_python_cli_test = (
    any(cmd.startswith(p) for p in safe_prefixes)
    and any(s in cmd for s in safe_substrings)
)

if is_safe_python_cli_test:
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PermissionRequest",
            "decision": {
                "behavior": "allow"
            }
        }
    }))
    sys.exit(0)

# Let Claude show the normal permission prompt for everything else.
sys.exit(0)