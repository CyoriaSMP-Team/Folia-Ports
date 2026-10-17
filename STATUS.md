# Migration compatibility checklist

Current target: Minecraft 1.21.11, Folia build 14, Java 25.

The CyoriaSMP server has switched engine; unsupported historical plugin JARs and their configuration data are retained in a backup/quarantine outside its plugin loading path. This is a staged **feature** migration, not full plugin parity.

## Priority blockers

1. Authentication: use upstream Folia-specific AuthMe build; verify chat/password/UUID/Bedrock handshakes.
2. World management: Multiverse-Core has no verified Folia port yet.
3. Region claims: ProtectionStones port has unverified cross-region world changes. Keep protected access until tested.
4. Economy: ExcellentEconomy, ExcellentCrates, ExcellentEnchants, tokens/rewards need compatible builds with data integrity.
5. Custom core: CyoriaCore, CyoriaCycRuntime, AuthEyeLab and interactive/chat/TPA/Status modules require direct port.
6. Skript ecosystem: scripts and addons are not assumed compatible; port scripts into Java/CyoriaRuntime or audited DSL.
7. GUI and gameplay: DeluxeMenus, DecentHolograms, third-party mini-games and pet systems need test/port.

Only install an Artifact from a passing workflow after confirming plugin.yml explicitly supports Folia and runtime smoke tests; `folia-supported: true` alone is insufficient.
