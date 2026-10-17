#!/usr/bin/env python3
"""Build the public Folia module catalog from nonsensitive per-plugin metadata."""
from pathlib import Path
import json, re, sys
root=Path(__file__).resolve().parents[1]
mods=[]
for f in sorted((root/'modules').glob('*/module.json')):
    data=json.loads(f.read_text())
    for field in ('name','slug','state','type','installed_on_folia','source'):
        assert field in data,(f,field)
    assert data['slug']==f.parent.name
    assert data['state'] in {'active','experimental','blocked','testing','planned','replaced'}
    assert data['type'] in {'official-folia','upstream-fork','cyoria-private','third-party','custom-public'}
    assert isinstance(data['installed_on_folia'],bool)
    mods.append(data)
assert len(set(m['slug'] for m in mods))==len(mods)
mods.sort(key=lambda m:(not m['installed_on_folia'],m['name'].lower()))
rows=['# CyoriaSMP Folia 1.21.11 module catalog','','This registry is not a claim that every listed plugin is safe. **Runtime tests outrank `folia-supported` flags and CI green checks.**','','| Module | Type | Current state | On live Folia? | Source / work |','|---|---|---|---|---|']
for m in mods:
    src=m['source']; link=f'[Code]({src})' if src.startswith('https://') else src
    rows.append(f"| {m['name']} | {m['type']} | {m['state']} | {'Yes' if m['installed_on_folia'] else 'No'} | {link} |")
rows.extend(['',f"**Tracked modules: {len(mods)}. Installed: {sum(m['installed_on_folia'] for m in mods)}. Experimental/blocked: {sum(m['state'] in ('experimental','blocked') for m in mods)}.**",'', '### Rules','- Prefer verified official Folia releases and retain original license/credits.','- For open-source upstreams, fork from official upstream, preserve attribution, port, test on Folia, and keep the plugin binary name where practical.','- For privately maintained Cyoria code, keep the source private unless the owner explicitly publishes it.','- When `folia-supported` is absent, do not flip the flag without auditing region/entity schedulers, other thread access and shared data.','- GitHub Actions builds development artifacts but does not deploy to the live server.','- Record failures even if the plugin advertises Folia support.',''])
text='\n'.join(rows)
path=root/'CATALOG.md'
if '--check' in sys.argv:
    if not path.exists() or path.read_text()!=text:
        raise SystemExit('CATALOG.md is out of date: run python3 tools/generate_catalog.py')
else:
    path.write_text(text)
print(f'OK {len(mods)} modules, {sum(m["installed_on_folia"] for m in mods)} active-on-server flags')
