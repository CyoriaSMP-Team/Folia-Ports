# BetterTeams 5.1.6 Folia + DecentHolograms safety workaround

**Problem**: With DecentHolograms 2.10.2 present, BetterTeams 5.1.6 calls `Bukkit.getScheduler().scheduleSyncRepeatingTask` from `HologramManager.startUpdates()`, which throws `UnsupportedOperationException` on Folia 1.21.11 during plugin enable and disables BetterTeams.

**Interim workaround**: This auditable ASM patch changes **only** `BetterTeams.Main.setupHolograms():boolean` to return `false`, disabling BetterTeams' auxiliary hologram integration; team membership, chat and economy functionality remain untouched by this bytecode change. DecentHolograms itself is not modified. Do not regard this as a complete Folia port of BetterTeams.

## Build and verify

1. Obtain the original `BetterTeams-5.1.6.jar` from a legitimate source and save its SHA-256 and a backup.
2. Compile `PatchBetterTeams.java` with `asm-9.11.jar` and `asm-tree-9.11.jar` (compile-only dependencies).
3. Run `java -cp <asm-jar>:<asm-tree-jar>:. PatchBetterTeams <original.jar> <patched.jar>`.
4. Confirm the patched `setupHolograms()` returns `false` using `javap -classpath <patched.jar> -c -p com.booksaw.betterTeams.Main`.
5. Smoke-test with Folia 1.21.11 and DecentHolograms installed, using a disposable server and a copy of existing configs; validate on player login and team GUI before claiming full functionality.
6. Replace the original server JAR only after saving it and the entire `plugins/BetterTeams` data folder outside the plugin loading directory; restart and check for absence of `Error occurred while enabling BetterTeams`.

Production build deployed 2026-10-20: SHA-256 `995df9c50cec95c3d58aa116af14119501351fcf4560f9b9e6d3ccb5fab1a56f`. Backup location: `plugins/_rollback/betterteams-dh-folia-20261020`.

BetterTeams is MIT-licensed (Booksaw). This tool is independent source code; it does not distribute upstream or modified BetterTeams binaries.
