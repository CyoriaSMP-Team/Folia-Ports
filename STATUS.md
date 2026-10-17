# Migration compatibility checklist

Current target: Minecraft 1.21.11, Folia build 14, Java 25.

CyoriaSMP has switched engine. Unsupported historical plugin JARs and their configuration data are retained in a backup or quarantine outside the plugin loading path. This is a staged feature migration, not full plugin parity.

## Priority blockers

1. Authentication: the official AuthMe 6.0.1 Folia JAR enables, and FastLoginPlus recognizes its AuthMe hook. Startup also reports offline mode and direct connections. Password, premium UUID, proxy, and Java/Bedrock login flows still need a controlled real-client check.
2. World management: the Multiverse fork skips Folia's unsupported Bukkit createWorld call and waits for an external loader. MoreFoWorld 1.13.3 uses server internals; after adding optional Paper load ordering ahead of CMI, the 2026-10-18 cold boot loaded lobby before CMI and the missing-lobby warning did not recur. The four worlds and 19 lobby FancyNpcs were listed. Actual RTP, portals, player teleports, and other world lifecycle flows remain unverified.
3. Region claims: the ProtectionStones port has unverified cross-region world changes. Keep protected access until tested.
4. Economy: ExcellentEconomy, ExcellentCrates, ExcellentEnchants, tokens, and rewards need compatible builds with data integrity.
5. Custom core: CyoriaCore's private Folia port now builds and passes a live startup smoke test; its player commands and gameplay paths remain untested. CyoriaCycRuntime, AuthEyeLab, and interactive, chat, TPA, and status modules still need direct port or runtime verification.
6. Skript ecosystem: scripts and addons are not assumed compatible; port scripts into Java/CyoriaRuntime or an audited DSL.
7. GUI and gameplay: DeluxeMenus, DecentHolograms, third-party mini-games, and pet systems need test or port.
8. MOTD: `CyoriaMOTDGuard` is disabled by its hard `BannerMOTDplus` dependency. A staged BannerMOTDPlus 2.0.0 JAR matches the official Modrinth SHA-512, but its `plugin.yml` lacks Folia's required `folia-supported: true` marker. Modrinth lists Paper, Purpur, BungeeCord, and Velocity and marks the project ARR; do not publish a modified copy without maintainer permission. Keep MiniMOTD as the working fallback until a Folia-ready release or source permission is available.

Only install an artifact from a passing workflow after confirming plugin.yml explicitly supports Folia and running runtime smoke tests; folia-supported: true alone is insufficient.

## Latest live startup check (2026-10-18)

- Folia 1.21.11 build 14 reached Done and the server reported online with 0 of 50 players; the current start count is 34.
- AuthMe 6.0.1-b2770 enabled and initialized SQLite. FastLoginPlus detected AuthMe 6.0+, registered its Folia configure-phase listener, and hooked into AuthMe. The server's real Java and Bedrock login flows were not exercised.
- CyoriaCore 3.0.5-standalone-authme was built from the private source with `folia-supported: true` and installed as a live smoke test. It enabled AuthMeFIX/AuthMeUI, connected to MySQL, started its voice and HTTP services, and reported four `.cyc` runtime scripts enabled with zero failed or dependency-blocked. Core startup logged no errors; player commands, payments, redemption, login, and voice gameplay paths remain untested. Its previous JAR remains as `plugins/CyoriaCore.previous-folia-smoke.disabled` for rollback.
- WorldGuard-Folia 7.0.17+bb6504f and WorldEdit 7.4.7-SNAPSHOT enabled together. `/rg list -w world` reached the read-only region listing, and `/we version` responded. Region edits, protection checks around a player, and cross-region interactions remain untested.
- ItemTag's original 3.7.7 failed to enable with an unsupported Bukkit scheduler call in the earlier migration test. The fork's CI artifact itemtag-folia-development-12 remains installed in the live server, logs that it enabled, and the original JAR is retained in rollback. This is startup-only; the port remains experimental.
- Multiverse-Core CI artifact folia-1.21.11-17 from commit 7e5a7076 passed all 183 tests. It enabled without the prior global-region config error or the unsupported Bukkit world-creation exception. Its expected warning says it is waiting for an external world loader.
- On the latest cold boot, MoreFoWorld 1.13.3 loaded before CMI and logged that it added lobby. mv list showed lobby, world, world_nether, and world_the_end. npc list showed 19 saved lobby NPCs plus modeltest in world. No lobby-missing RandomTeleportation warning appeared in this startup log.
- The preceding boot had produced a RandomTeleportation missing-lobby warning; cmi reload then succeeded at 00:21:49. The new load order prevented that warning from recurring on cold boot. Actual RTP behavior was not exercised.
- The previous live comparison found config.yml, worlds.yml, and anchors.yml byte-identical to their saved copies. No player gameplay, login, portal, or multi-region plugin interaction was verified.
