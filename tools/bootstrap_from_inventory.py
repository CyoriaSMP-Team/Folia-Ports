#!/usr/bin/env python3
"""Run locally with sanitized plugin-plan.json to initialize module metadata."""
from pathlib import Path
import json,re,sys
root=Path(__file__).resolve().parents[1]
if len(sys.argv)!=2:raise SystemExit('Usage: bootstrap_from_inventory.py /absolute/path/plugin-plan.json')
plan=json.loads(Path(sys.argv[1]).read_text())
upstreams={
'ProtectionStones':'https://github.com/CyoriaSMP-Team/ProtectionStones-Folia',
'FastAsyncWorldEdit':'https://github.com/CyoriaSMP-Team/FAWE-Folia',
'WorldGuard':'https://github.com/CyoriaSMP-Team/WorldGuard-Folia',
'Multiverse-Core':'https://github.com/CyoriaSMP-Team/Multiverse-Core-Folia',
'MoreFoWorld':'https://github.com/CyoriaSMP-Team/MoreFoWorld-Folia',
'Skript':'https://github.com/CyoriaSMP-Team/Skript-Folia',
'DeluxeMenus':'https://github.com/CyoriaSMP-Team/DeluxeMenus-Folia',
'DecentHolograms':'https://github.com/CyoriaSMP-Team/DecentHolograms-Folia',
'CyoriaCore':'https://github.com/CyoriaSMP-Team/CyoriaCore',
'PetKuEngSus':'https://github.com/CyoriaSMP-Team/PetKuEngSus',
'ProtocolLib2PacketEvents':'https://github.com/CyoriaSMP-Team/ProtocolLib2PacketEvents',
'AuthMe':'https://github.com/AuthMe/AuthMeReloaded',
'FastLoginPlus':'https://github.com/Hayston1001/FastLoginPlus',
}
custom={'CyoriaCore','CyoriaAuthEyeLab','CyoriaCycRuntime','CyoriaInteractiveChat','CyoriaStatusEmbed','CyoriaTPA','BannerMOTDplus','P2PSmokeTest'}
addon_deps={'SkBee','ProtectionStonesMenu','CyoriaMOTDGuard','InteractiveChatDiscordSrvAddon'}
byname={x['name']:x for x in plan['plugins']}
for name in ['WorldEdit','WorldGuard','FastAsyncWorldEdit','ProtectionStones','AuthMe','FastLoginPlus']:
    byname.setdefault(name,{'name':name,'folia':True})
byname.setdefault('WorldEdit',{'name':'WorldEdit','folia':True})
for name,item in sorted(byname.items()):
    slug=re.sub(r'[^a-z0-9]+','-',name.lower()).strip('-')
    # Avoid exposing private code by linking a public-only status rather than its restricted repo URL.
    if name=='CyoriaCore':origin='private:CyoriaSMP-Team/CyoriaCore'
    else:origin=upstreams.get(name,'pending official source verification')
    t=('cyoria-private' if name=='CyoriaCore' else 'custom-public' if name in custom else 'official-folia' if name in ('AuthMe','FastLoginPlus') else 'upstream-fork' if name in upstreams else 'third-party')
    installed=bool(item.get('folia',False))
    if name in ('AuthMe','FastLoginPlus'):installed=True
    if name=='WorldEdit':installed=True
    if name in ('ProtectionStones','FastAsyncWorldEdit'):installed=False
    if name in ('InteractiveChat','InteractiveChatDiscordSrvAddon','MythicMobs','EconomyShopGUI','CyoriaMOTDGuard'):
        state='blocked'
    elif name in ('ProtectionStones','FastAsyncWorldEdit','Multiverse-Core','Skript','DeluxeMenus','DecentHolograms'):
        state='experimental'
    elif installed:state='active'
    else:state='planned'
    entry={'name':name,'slug':slug,'type':t,'state':state,'installed_on_folia':installed,'source':origin,
           'target':'Folia 1.21.11','build_proves_folia_safety':False,
           'notes':item.get('reason','') if not installed else ''}
    d=root/'modules'/slug;d.mkdir(parents=True,exist_ok=True)
    f=d/'module.json'
    if not f.exists():f.write_text(json.dumps(entry,ensure_ascii=False,indent=2)+'\n')
print('Initialized',len(byname),'module records')
