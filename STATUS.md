# Migration compatibility checklist

Current target: Minecraft 1.21.11, Folia build 14, Java 25.

The CyoriaSMP server has switched engine; unsupported historical plugin JARs and their configuration data are retained in a backup/quarantine outside its plugin loading path. This is a staged **feature** migration, not full plugin parity.

## Priority blockers

1. Authentication: use upstream Folia-specific AuthMe build; verify chat/password/UUID/Bedrock handshakes.
2. World management: the [official Folia support request](https://github.com/Multiverse/Multiverse-Core/issues/2901) remains on hold; our fork's world lifecycle is incomplete and must stay out of the live plugin path.
3. Region claims: ProtectionStones port has unverified cross-region world changes. Keep protected access until tested.
4. Economy: ExcellentEconomy, ExcellentCrates, ExcellentEnchants, tokens/rewards need compatible builds with data integrity.
5. Custom core: CyoriaCore, CyoriaCycRuntime, AuthEyeLab and interactive/chat/TPA/Status modules require direct port.
6. Skript ecosystem: scripts and addons are not assumed compatible; port scripts into Java/CyoriaRuntime or audited DSL.
7. GUI and gameplay: DeluxeMenus, DecentHolograms, third-party mini-games and pet systems need test/port.

Only install an Artifact from a passing workflow after confirming plugin.yml explicitly supports Folia and runtime smoke tests; `folia-supported: true` alone is insufficient.

## Latest live startup check (2026-10-17)

- Folia 1.21.11 build 14 reached `Done` and the server reported online; there were 0 players during the check.
- The original ItemTag 3.7.7 failed to enable with an unsupported Bukkit scheduler call. The fork's CI artifact `itemtag-folia-development-12` is now active with `folia-supported: true`; it logged `ItemTag # Enabled (took 34 ms)` and the server reached `Done`. The original JAR is retained in rollback. This is startup-only; the port remains experimental.
- FancyNpcs skipped 19 saved NPCs because `lobby` was not loaded. The lobby world exists on disk and is in the retained Multiverse config, but no Multiverse-Core JAR is active. Its current Folia port is not safe to install yet.
- No player gameplay or multi-region plugin interaction was verified in this check.
