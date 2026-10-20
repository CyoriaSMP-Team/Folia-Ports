# CyoriaSMP Folia parity audit — 20 October 2026

## Scope

Reference: **last Leaf startup 17 Oct**, `2026-10-17-7.log.gz`, 111 plugin initializations (17 Paper, 94 Bukkit). First Folia startup had 64 (12 Paper, 52 Bukkit). Folia at 17:29 on 20 Oct had **80** (15 Paper, 65 Bukkit). During this audit, production added **DecentHolograms 2.10.2** and **SkBee 3.25.4**, confirmed **82** plugin initializations with server online after the second restart (15 Paper + 67 Bukkit). BetterTeams, DecentHolograms and SkBee all enabled; Skript loaded. The comparison is by exact plugin name, not a guarantee of equivalent features.

## Restored on 20 Oct

- **DecentHolograms 2.10.2 official**: Folia 1.21.11 boot smoke passed; Production read 10 original hologram definitions. Backup: `plugins/_rollback/decentholograms-official-20261020`.
- **SkBee 3.25.4 official**: Folia 1.21.11 with Cyoria Skript 2.17 boot smoke passed; 528 elements loaded. Scoreboard and world creator elements intentionally disabled on Folia. Backup: `plugins/_rollback/skbee-folia-20261020`.
- **BetterTeams 5.1.6 compatibility hotfix**: old `setupHolograms()` scheduler integration crashes on Folia when DecentHolograms installed. One-method bytecode patch disables **only BetterTeams' hologram integration**; BetterTeams and DecentHolograms both enabled successfully in isolated smoke and live production. Original JAR and YAML backups: `plugins/_rollback/betterteams-dh-folia-20261020`.

## Still absent by exact plugin name

| Plugin | Status / caution |
|---|---|
| AxiomPaper | Requires Folia-safe artifact and feature/data validation; not deployed |
| BannerMOTDplus | MiniMOTD / CyoriaMOTDGuard provide MOTD; banner-specific output unverified |
| ChatColor2 | Requires Folia-safe artifact and feature/data validation; not deployed |
| ChatGames | Requires Folia-safe artifact and feature/data validation; not deployed |
| CyoriaAuthEyeLab | CyoriaCore AuthMeUI/auth extensions running; EyeLab-specific behavior unverified |
| CyoriaCycRuntime | CyoriaCore .cyc embedded runtime active; standalone runtime not restored |
| CyoriaTPA | CMI TPA functions potentially available; custom CyoriaTPA behavior unverified |
| DailyRewards | Requires Folia-safe artifact and feature/data validation; not deployed |
| DeluxeTags | Requires Folia-safe artifact and feature/data validation; not deployed |
| DiSky | Requires Folia port and secure Discord token/webhook migration; current script has unresolved DiSky syntax |
| ExcellentCrates | Requires Folia-safe artifact and feature/data validation; not deployed |
| ExcellentEconomy | Current economy uses CMI/Vault; balances require separate migration check |
| ExcellentEnchants | Requires Folia-safe artifact and feature/data validation; not deployed |
| FarmProtect | Requires Folia-safe artifact and feature/data validation; not deployed |
| FastAsyncWorldEdit | Cyoria FAWE fork remains experimental; do not replace working WorldEdit without world/selection audit |
| FlareTokens | Requires Folia-safe artifact and feature/data validation; not deployed |
| Floodgate-Skript | Requires Folia-safe artifact and feature/data validation; not deployed |
| FreeCoinFlip | Requires Folia-safe artifact and feature/data validation; not deployed |
| LagFixer | Requires Folia-safe artifact and feature/data validation; not deployed |
| MimiVouchers | Requires Folia-safe artifact and feature/data validation; not deployed |
| P2PSmokeTest | Diagnostic smoke-test plugin, not production feature |
| PetKuEngSus | Requires Folia-safe artifact and feature/data validation; not deployed |
| PhatLoots | Requires Folia-safe artifact and feature/data validation; not deployed |
| ProtectionStonesMenu | Requires Folia-safe artifact and feature/data validation; not deployed |
| ProtocolLib2PacketEvents | Requires Folia-safe artifact and feature/data validation; not deployed |
| RedeemDialog | Requires Folia-safe artifact and feature/data validation; not deployed |
| SkBriggy | SkBriggy 1.7.0 (1.21.11) paper-plugin.yml lacks folia-supported flag; do not force |
| Themis | GrimAC active; anti-cheat rule parity unverified |
| VirtualStorage | Requires Folia-safe artifact and feature/data validation; not deployed |
| WorldGuardExtraFlags | Requires Folia-safe artifact and feature/data validation; not deployed |
| bosssummoner | Requires Folia-safe artifact and feature/data validation; not deployed |
| rerollex | Requires Folia-safe artifact and feature/data validation; not deployed |
| skript-db | No verified Folia-compatible 1.21.11 addon build |
| skript-worldguard | Skript native WorldGuard hook loaded; addon-specific syntax unverified |
| skript-yaml | Folia fork exists but no audited, published release |

## Deployment policy / acceptance gates

1. Do not use `folia-supported: true` alone as compatibility evidence. Verify ownership-safe scheduler and actual Folia runtime behavior.
2. Smoke test Java 25 / Folia 1.21.11 with required dependencies, command/event paths, player moves between regions, login/logout, and errors; preserve config/data backups.
3. **No uncontrolled economy conversion.** `ExcellentEconomy`, `ExcellentCrates`, `ExcellentEnchants`, tokens, vouchers and shops may persist sensitive player balances/items; export and reconcile before attempting reinstall.
4. **No parallel WorldEdit/FAWE installation** until replacement path and functionality are tested.
5. Incomplete scripts still refer to Discord DiSky structures and SkBriggy tab completion. Remove or port unsafe constructs; never copy exposed bot/webhook credentials from scripts.
6. The module catalog's prior `On live Folia?` values are historical; this dated audit reflects the current parity effort.

## Next gate

The goal is *feature parity*, not matching 111 JARs. Validate the high-priority unimplemented features against player workflows and only restore plugins where no supported replacement exists.
