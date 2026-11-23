#!/usr/bin/env python3
"""Fail-closed authentic Kane CLI NDJSON terminal validation."""
import json,sys
from pathlib import Path
p=Path(sys.argv[1])
if not p.is_file() or p.stat().st_size<20:raise SystemExit('GENUINE_KANE_LOG_MISSING')
last=None
for line in p.read_text(errors='replace').splitlines():
 try:rec=json.loads(line)
 except json.JSONDecodeError:continue
 if isinstance(rec,dict) and rec.get('type')=='run_end':last=rec
if not last:raise SystemExit('GENUINE_KANE_RUN_END_MISSING')
print('GENUINE_KANE_RESULT',last.get('status','unknown'))
if last.get('status')!='passed':raise SystemExit('GENUINE_KANE_NOT_PASSED')
