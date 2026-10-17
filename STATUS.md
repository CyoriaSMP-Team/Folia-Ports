# Migration compatibility checklist

Current target: Minecraft 1.21.11, Folia build 14, Java 25.

CyoriaSMP has switched engine. Unsupported historical plugin JARs and their configuration data are retained in a backup or quarantine outside the plugin loading path. This is a staged feature migration, not full plugin parity.

## Priority blockers

1. Authentication: the official AuthMe 6.0.1 Folia JAR enables, and FastLoginPlus recognizes its AuthMe hook. Startup also reports offline mode and direct connections. Password, premium UUID, proxy, and Java/Bedrock login flows still need a controlled real-client check.
2. World management: the Multiverse fork now skips Folia's unsupported Bukkit createWorld call instead of crashing. MoreFoWorld 1.13.3 loads the existing lobby during startup, and the latest empty-server check found all 19 lobby FancyNpcs. MoreFoWorld calls itself temporary and uses server internals; a RandomTeleportation component logged that it could not find lobby before the helper loaded it. cmi reload later succeeded with no new missing-lobby warning, but actual RTP and the next cold boot remain unverified. Portal, teleport, and other world lifecycle flows remain unverified.
3. Region claims: the ProtectionStones port has unverified cross-region world changes. Keep protected access until tested.
4. Economy: ExcellentEconomy, ExcellentCrates, ExcellentEnchants, tokens, and rewards need compatible builds with data integrity.
5. Custom core: CyoriaCore, CyoriaCycRuntime, AuthEyeLab, and interactive, chat, TPA, and status modules require direct port or runtime verification.
6. Skript ecosystem: scripts and addons are not assumed compatible; port scripts into Java/CyoriaRuntime or an audited DSL.
7. GUI and gameplay: DeluxeMenus, DecentHolograms, third-party mini-games, and pet systems need test or port.

Only install an artifact from a passing workflow after confirming plugin.yml explicitly supports Folia and running runtime smoke tests; folia-supported: true alone is insufficient.

## Latest live startup check (2026-10-18)

- Folia 1.21.11 build 14 reached Done and the server reported online with 0 players; the current start count is 31.
- AuthMe 6.0.1-b2770 enabled and initialized SQLite. FastLoginPlus detected AuthMe 6.0+, registered its Folia configure-phase listener, and hooked into AuthMe. The server's real Java and Bedrock login flows were not exercised.
- ItemTag's original 3.7.7 failed to enable with an unsupported Bukkit scheduler call in the earlier migration test. The fork's CI artifact itemtag-folia-development-12 remains installed in the live server, logs that it enabled, and the original JAR is retained in rollback. This is startup-only; the port remains experimental.
- Multiverse-Core CI artifact folia-1.21.11-17 from commit 7e5a7076 passed all 183 tests. It enabled without the prior global-region config error or the unsupported Bukkit world-creation exception. Its expected warning says it is waiting for an external world loader.
- MoreFoWorld 1.13.3 logged that it added lobby after Multiverse skipped autoload. mv list showed lobby, world, world_nether, and world_the_end. npc list showed 19 saved lobby NPCs, and FancyNpcs reported no missing-world errors.
- A RandomTeleportation component logged that it could not find lobby before MoreFoWorld loaded it. cmi reload returned success at 00:21:49 and logged that CMI configs and locale files reloaded; no later missing-lobby warning appeared. Runtime teleport behavior and a subsequent cold boot have not been checked.
- The previous live comparison found config.yml, worlds.yml, and anchors.yml byte-identical to their saved copies. No player gameplay, login, portal, or multi-region plugin interaction was verified.
