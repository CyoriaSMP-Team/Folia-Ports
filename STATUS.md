# Migration compatibility checklist

Current target: Minecraft 1.21.11, Folia build 14, Java 25.

The CyoriaSMP server has switched engine; unsupported historical plugin JARs and their configuration data are retained in a backup/quarantine outside its plugin loading path. This is a staged **feature** migration, not full plugin parity.

## Priority blockers

1. Authentication: use upstream Folia-specific AuthMe build; verify chat/password/UUID/Bedrock handshakes.
2. World management: the [official Folia support request](https://github.com/Multiverse/Multiverse-Core/issues/2901) remains on hold. The Multiverse test fork is installed; its global-region config error is fixed, but Folia 1.21.11's `CraftServer.createWorld(WorldCreator)` still throws `UnsupportedOperationException`. The `lobby` world and its 19 FancyNpcs remain unavailable.
3. Region claims: ProtectionStones port has unverified cross-region world changes. Keep protected access until tested.
4. Economy: ExcellentEconomy, ExcellentCrates, ExcellentEnchants, tokens/rewards need compatible builds with data integrity.
5. Custom core: CyoriaCore, CyoriaCycRuntime, AuthEyeLab and interactive/chat/TPA/Status modules require direct port.
6. Skript ecosystem: scripts and addons are not assumed compatible; port scripts into Java/CyoriaRuntime or audited DSL.
7. GUI and gameplay: DeluxeMenus, DecentHolograms, third-party mini-games and pet systems need test/port.

Only install an Artifact from a passing workflow after confirming plugin.yml explicitly supports Folia and runtime smoke tests; `folia-supported: true` alone is insufficient.

## Latest live startup check (2026-10-17)

- Folia 1.21.11 build 14 reached `Done` and the server reported online; there were 0 players during the check.
- The original ItemTag 3.7.7 failed to enable with an unsupported Bukkit scheduler call. The fork's CI artifact `itemtag-folia-development-12` is now active with `folia-supported: true`; it logged `ItemTag # Enabled (took 34 ms)` and the server reached `Done`. The original JAR is retained in rollback. This is startup-only; the port remains experimental.
- Multiverse-Core CI artifact `folia-1.21.11-12` (`cfe4362e18cc3dd8bb1df2881d9665eb8c0b6a2f7babc7751eb52ed08a3d0aba`) passed all 183 tests and is installed. After restart the server returned online with 0 players; the plugin enabled and the previous global-region config error was gone. `lobby` remains unloaded because Folia throws `UnsupportedOperationException` from `CraftServer.createWorld(WorldCreator)`, so FancyNpcs still skips its 19 lobby NPCs. `config.yml`, `worlds.yml`, `anchors.yml`, and the 186 MB lobby world match their saved copies.
- FancyNpcs skipped all 19 saved NPCs because `lobby` was not loaded. No player gameplay or multi-region plugin interaction was verified in this check.
