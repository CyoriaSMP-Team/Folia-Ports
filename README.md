# CyoriaSMP Folia Ports

Community-visible work on Minecraft **Folia 1.21.11** interoperability. Each plugin fork derives from its **official upstream**; GitHub forks preserve the original project's license, attribution, and history.

**Important:** a green CI build is not certification of safe Folia region ownership. Check the `FOLIA_PORT_STATUS.md` in each fork and the open PRs before using a development artifact. Avoid enabling `folia-supported: true` until the port is actually safe.

## Official-upstream forks

| Project | Repository | Current stage |
|---|---|---|
| WorldEdit | [WorldEdit-Folia](https://github.com/CyoriaSMP-Team/WorldEdit-Folia) | CI passed, startup smoke-tested with WorldGuard; more multi-region tests needed |
| WorldGuard | [WorldGuard-Folia](https://github.com/CyoriaSMP-Team/WorldGuard-Folia) | CI passed, startup smoke-tested with WorldEdit; more region tests needed |
| ProtectionStones | [ProtectionStones-Folia](https://github.com/CyoriaSMP-Team/ProtectionStones-Folia) | Experimental source, CI passed, **Folia flag not enabled** |
| FastAsyncWorldEdit | [FAWE-Folia](https://github.com/CyoriaSMP-Team/FAWE-Folia) | Experimental source, CI passed, **Folia flag not enabled**; replaces WorldEdit |
| Multiverse-Core | [Multiverse-Core-Folia](https://github.com/CyoriaSMP-Team/Multiverse-Core-Folia) | Official fork, port pending |
| Skript | [Skript-Folia](https://github.com/CyoriaSMP-Team/Skript-Folia) | Official fork, port pending; CyoriaRuntime migration is another path |
| DeluxeMenus | [DeluxeMenus-Folia](https://github.com/CyoriaSMP-Team/DeluxeMenus-Folia) | Official fork, port pending |
| DecentHolograms | [DecentHolograms](https://github.com/CyoriaSMP-Team/DecentHolograms) | Official fork, Folia port pending |

## Public installation builds

The experimental branches use `folia/1.21.11`. Open the fork's **Actions → Folia 1.21.11 Build** page and download the development JAR artifact of a green run. **Never install a `*-sources.jar` or `*-javadoc.jar` as a plugin.** No automatic deployment onto public servers is configured.

## Maintenance

We track changes from official upstream, carry Folia-specific patches in separate development branches, and build on GitHub-hosted Actions. An automated daily upstream review has been configured; updates with unresolved merge conflicts, untested schedulers, or unsafe entity/world interactions are not automatically released.

Project issue reports should include: plugin and build SHA, Folia/Minecraft version, startup logs (redact secrets), steps to reproduce, and whether a player/world region was active when it failed. Contributions welcome under the upstream license.
