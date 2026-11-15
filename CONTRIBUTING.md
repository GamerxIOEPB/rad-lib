# Contributing to the Rad Library Registry

Thank you for contributing to the Rad package ecosystem!

## Package Guidelines

1. **Pure Native Rad**: All packages must be written in pure Rad without unvetted C++ or foreign runtimes.
2. **Immutable Releases**: Package versions are immutable once published. Bug fixes and features must bump semantic versioning (`major.minor.patch`).
3. **Tests & Examples**: Packages must complete comprehensive unit tests and runnable examples.
4. **Manifest Compliance**: Packages must include a valid `rad.toml` conforming to `registry/schema/package.json`.

## Publication Process

1. Validate package contents:
   ```bash
   rad publish --dry-run
   ```
2. Submit a pull request or publish with:
   ```bash
   rad publish --confirm
   ```
