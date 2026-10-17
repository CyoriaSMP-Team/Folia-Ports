# CyoriaSMP Folia Ports

Community-visible work on Minecraft **Folia 1.21.11** interoperability. Each plugin fork derives from its **official upstream**; GitHub forks preserve the original project's license, attribution, and history.

See [STATUS.md](STATUS.md) for current migration blockers and [CATALOG.md](CATALOG.md) for the plugin JAR inventory and observed failures.

**Important:** neither a green CI build nor `folia-supported: true` certifies safe Folia region ownership. The marker only allows loading. Check each fork's `FOLIA_PORT_STATUS.md` before use; experimental builds may enable the marker for authorized testing while still having unverified paths.

## Official-upstream forks

| Project | Repository | Current stage |
|---|---|---|
| WorldEdit | [WorldEdit-Folia](https://github.com/CyoriaSMP-Team/WorldEdit-Folia) | CI passed, startup smoke-tested with WorldGuard; more multi-region tests needed |
| WorldGuard | [WorldGuard-Folia](https://github.com/CyoriaSMP-Team/WorldGuard-Folia) | CI passed, startup smoke-tested with WorldEdit; more region tests needed |
| ProtectionStones | [ProtectionStones-Folia](https://github.com/CyoriaSMP-Team/ProtectionStones-Folia) | Experimental prerelease `v2.10.7-folia.1`; startup and isolated claim lifecycle passed; multi-region safety remains unverified |
| FastAsyncWorldEdit | [FAWE-Folia](https://github.com/CyoriaSMP-Team/FAWE-Folia) | Experimental source, CI passed, **Folia flag not enabled**; replaces WorldEdit |
| Multiverse-Core | [Multiverse-Core-Folia](https://github.com/CyoriaSMP-Team/Multiverse-Core-Folia) | Existing worlds load via MoreFoWorld; `/mv create` still fails because Folia throws from `Bukkit.createWorld` |
| Skript | [Skript-Folia](https://github.com/CyoriaSMP-Team/Skript-Folia) | Official fork, port pending; CyoriaRuntime migration is another path |
| DeluxeMenus | [DeluxeMenus-Folia](https://github.com/CyoriaSMP-Team/DeluxeMenus-Folia) | Official fork, port pending |
| DecentHolograms | [DecentHolograms](https://github.com/CyoriaSMP-Team/DecentHolograms) | Official fork, Folia port pending |

## Other published plugins

| Project | Repository | Current stage |
|---|---|---|
| CyoriaMOTDGuard | [CyoriaMOTDGuard-Folia](https://github.com/CyoriaSMP-Team/CyoriaMOTDGuard-Folia) | Experimental prerelease `v1.0.2-folia.1`; live Java and RakNet status checks passed; one status client channel remains unverified |
| CyoriaInteractiveChat | [CyoriaInteractiveChat](https://github.com/CyoriaSMP-Team/CyoriaInteractiveChat) | Experimental prerelease `v0.1.5-folia.1`; CI and live startup passed; isolated Leaf chat/GUI flow passed; live Folia player interaction remains unverified |

## Public installation builds

The experimental branches use `folia/1.21.11`. Open the fork's **Actions → Folia 1.21.11 Build** page and download the development JAR artifact of a green run. **Never install a `*-sources.jar` or `*-javadoc.jar` as a plugin.** No automatic deployment onto public servers is configured.

## Maintenance

We track changes from official upstream, carry Folia-specific patches in separate development branches, and build on GitHub-hosted Actions. The daily workflow records upstream default-branch SHAs. Configured forks use a reusable daily sync workflow that merges upstream changes into a review branch and opens a pull request only after the repository build passes. It targets the Folia branch when one exists, otherwise the fork's default branch. It never merges or deploys. Updates with conflicts or unsafe entity/world interactions still require manual review.

Project issue reports should include: plugin and build SHA, Folia/Minecraft version, startup logs (redact secrets), steps to reproduce, and whether a player/world region was active when it failed. Contributions welcome under the upstream license.
