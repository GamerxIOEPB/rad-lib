# Rad Registry Architecture & Standards

## Overview

The Rad package registry is a decentralized, Git-backed and static-HTTP-compatible registry.

## Version Immutability

Published versions in `packages/<name>/<version>/` are strictly append-only and cannot be altered or overwritten.

## Package Resolution

The package manager resolves semantic versions using:
- **Caret (`^0.1.0`)**: Compatible updates up to the next breaking version.
- **Tilde (`~0.1.0`)**: Patch-level updates only.
- **Exact (`=0.1.0` or `0.1.0`)**: Pin to specific immutable release.

## Lockfiles

Projects create a reproducible `rad.lock` specifying exact versions and cryptographic SHA-256 digests.
