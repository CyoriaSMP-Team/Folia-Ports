# CyoriaSMP Folia Ports

Community-visible work on Minecraft **Folia 1.21.11** interoperability. Each plugin fork derives from its **official upstream**; GitHub forks preserve the original project's license, attribution, and history.

See [STATUS.md](STATUS.md) for current migration blockers and [CATALOG.md](CATALOG.md) for the plugin JAR inventory and observed failures.

**Important:** neither a green CI build nor `folia-supported: true` certifies safe Folia region ownership. The marker only allows loading. Check each fork's `FOLIA_PORT_STATUS.md` before use; experimental builds may enable the marker for authorized testing while still having unverified paths.

## Official-upstream forks

| Project | Repository | Current stage |
|---|---|---|
| WorldEdit | [WorldEdit-Folia](https://github.com/CyoriaSMP-Team/WorldEdit-Folia) | [Experimental prerelease v7.4.7-folia.1](https://github.com/CyoriaSMP-Team/WorldEdit-Folia/releases/tag/v7.4.7-folia.1); startup and /we version passed; navigation and multi-region edits need testing |
| WorldGuard | [WorldGuard-Folia](https://github.com/CyoriaSMP-Team/WorldGuard-Folia) | [Experimental prerelease v7.0.17-folia.1](https://github.com/CyoriaSMP-Team/WorldGuard-Folia/releases/tag/v7.0.17-folia.1); startup and read-only region listing passed; edits and multi-region behavior need testing |
| ProtectionStones | [ProtectionStones-Folia](https://github.com/CyoriaSMP-Team/ProtectionStones-Folia) | Experimental prerelease `v2.10.7-folia.1`; startup and isolated claim lifecycle passed; multi-region safety remains unverified |
| FastAsyncWorldEdit | [FAWE-Folia](https://github.com/CyoriaSMP-Team/FAWE-Folia) | Experimental source, CI passed, **Folia flag not enabled**; replaces WorldEdit |
| Multiverse-Core | [Multiverse-Core-Folia](https://github.com/CyoriaSMP-Team/Multiverse-Core-Folia) | [Experimental prerelease `folia-1.21.11-18`](https://github.com/CyoriaSMP-Team/Multiverse-Core-Folia/releases/tag/folia-1.21.11-18); 183 tests and live create/import/cold-boot-load smoke passed through MoreFoWorld 1.13.4; create exceeded the 5-second watchdog threshold, and player/cross-region flows remain unverified |
| MoreFoWorld | [MoreFoWorld-Folia](https://github.com/CyoriaSMP-Team/MoreFoWorld-Folia) | [Experimental prerelease `v1.13.4-folia.1`](https://github.com/CyoriaSMP-Team/MoreFoWorld-Folia/releases/tag/v1.13.4-folia.1); exposes `createWorld(WorldCreator)` for Folia integrations; empty-world create/import/load passed, but synchronous NMS and player lifecycle risks remain |
| Skript | [Skript-Folia](https://github.com/CyoriaSMP-Team/Skript-Folia) | Official fork, port pending; CyoriaRuntime migration is another path |
| DeluxeMenus | [DeluxeMenus-Folia](https://github.com/CyoriaSMP-Team/DeluxeMenus-Folia) | Official fork, port pending |
| DecentHolograms | [DecentHolograms](https://github.com/CyoriaSMP-Team/DecentHolograms) | Official fork, Folia port pending |

## Other published plugins

| Project | Repository | Current stage |
|---|---|---|
| CyoriaMOTDGuard | [CyoriaMOTDGuard-Folia](https://github.com/CyoriaSMP-Team/CyoriaMOTDGuard-Folia) | Experimental prerelease `v1.0.3-folia.2`; CI, live startup, Java protocol 774/47 status responses passed; management protocol 127 cannot expose its channel |
| CyoriaInteractiveChat | [CyoriaInteractiveChat](https://github.com/CyoriaSMP-Team/CyoriaInteractiveChat) | Experimental prerelease `v0.1.5-folia.1`; CI and live startup passed; isolated Leaf chat/GUI flow passed; live Folia player interaction remains unverified |

## Public installation builds

Use the fork's **Releases** page for experimental prereleases. Development builds are under **Actions → Folia 1.21.11 Build**. Download the server JAR artifact; **never install a `*-sources.jar` or `*-javadoc.jar` as a plugin.** No automatic deployment onto public servers is configured.

## Maintenance

We track changes from official upstream, carry Folia-specific patches in separate development branches, and build on GitHub-hosted Actions. The daily workflow records upstream default-branch SHAs. Configured forks use a reusable daily sync workflow that merges upstream changes into a review branch and opens a pull request only after the repository build passes. It targets the Folia branch when one exists, otherwise the fork's default branch. It never merges or deploys. Updates with conflicts or unsafe entity/world interactions still require manual review.

The sync workflow builds upstream changes in a read-only job, then recreates the verified merge on a fresh runner with PR-write permission. Pull requests still need a human review; enabling Actions approval permission at the organization level does not make a successful build proof of Folia safety.

Project issue reports should include: plugin and build SHA, Folia/Minecraft version, startup logs (redact secrets), steps to reproduce, and whether a player/world region was active when it failed. Contributions welcome under the upstream license.
