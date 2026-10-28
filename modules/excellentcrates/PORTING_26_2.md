# ExcellentCrates v7 — Folia 26.2 compatibility assessment

**Status: planned / not installable as a verified Folia 26.2 build.** This is research and a porting checklist, **not a plugin release**. Do not add an unverified JAR to the public CyoriaSMP plugin load path or assume that `folia-supported: true` makes a plugin region-thread safe.

## Verified source state (2026-10-28)

- Upstream project: [nulli0n/ExcellentCrates-spigot](https://github.com/nulli0n/ExcellentCrates-spigot), whose public default branch still contains **6.6.1** (not the published v7.2.0 code).
- Published **ExcellentCrates 7.2.0**, released 2026-10-16, supports **Paper/Spigot Minecraft 26.2**, but [official compatibility documentation](https://nightexpressdev.com/excellentcrates/) explicitly excludes Folia. [Release notes](https://nightexpressdev.com/excellentcrates/releases/v7-2-0/).
- Strongest found v7 starting point: [FluffyworldMC/ExcellentCrates-v7-folia](https://github.com/FluffyworldMC/ExcellentCrates-v7-folia), commit `dfa60d3b412c2dec66f738f198696076fe402baf` (2026-10-10). That fork declares **7.1.0**, **Java 25**, `io.papermc.paper:paper-api:26.1.2.build.+`, `NightCore 2.16.7`, and `UniversalScheduler 0.1.7`; both plugin metadata files set `folia-supported: true`. No GitHub Release was found for this fork. **26.2 compilation and runtime functionality have not been verified.**
- Previous v6 Folia forks (e.g. FreshSMP, GemstoneGG) are *not* replacements for the rewritten v7 architecture. Avoid claiming feature parity based on them.
- The current [NightCore 2.16.7](https://hangar.papermc.io/NightExpress/nightcore/versions) lists Minecraft 26.2 and its current [Modrinth page](https://modrinth.com/project/Y4NRwMW5) advertises Folia, but dependency compatibility alone does not establish ExcellentCrates runtime safety.
- Source is GPL-3.0; preserve upstream copyright, license, attribution, and accessible corresponding source on any redistributed fork.

## Porting work

1. Obtain a **legally distributable 7.2.0 source baseline** and reconcile changes between the v7.1.0 Folia fork and 7.2.0 (particularly sorting, API, and asynchronous physical-key fixes). Do **not** falsely label a 7.1.0 build as 7.2.0.
2. Compile against **Folia/Paper API 26.2** using **Java 25**. Update pinned dependencies and test available version-specific APIs. Build the plugin's shaded artifact and verify dependency loading; do not install the thin, sources, or javadoc JAR.
3. Audit all player/entity operations for **entity scheduler ownership**; crate-block/world/particle/hologram operations for **region scheduler ownership**; global state for safe synchronization or the global region scheduler; and database/network work for safe async execution. Avoid Bukkit's ordinary global scheduler and cross-region direct reads/writes.
4. Verify crate opening is atomic under concurrent access (physical/virtual keys, balance and cost deductions, cooldowns and limits, inventory space, rewards, commands). Preserve all existing crate definitions, player state and transaction history.
5. Test startup, shutdown, disconnects, UI editor, menus/animations, previews, key giving, placing/removing crate blocks, holograms, reward sorting, permission checks, integrations (Vault, PlayerPoints, PlaceholderAPI, PacketEvents, custom items), and cross-region use. Run concurrent opening and reload/restart/data restore tests.

## Release gates

- [ ] Source baseline and GPL notices verified.
- [ ] 7.2.0 parity proven (or clearly label reduced 7.1.0 compatibility).
- [ ] Build succeeds on Java 25 / Folia 26.2 with reproducible artifact.
- [ ] Correct region/entity scheduler audit passes; no known illegal cross-thread accesses.
- [ ] Runtime smoke tests and player concurrency tests pass on an isolated Folia 26.2 server.
- [ ] Backup + data migration/rollback verified for crate data, virtual keys and reward history.
- [ ] Only then enable the artifact on production; record exact JAR hash, build SHA and tested dependencies.

Tracking parent: [Folia-Ports issue #5](https://github.com/CyoriaSMP-Team/Folia-Ports/issues/5). Existing production inventory targets Folia 1.21.11; **this 26.2 research does not authorize upgrading the live server**.
