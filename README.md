# Rad Library Registry (`rad-lib`)

Official package registry and library repository for the **Rad Programming Language**.

## Packages

| Package | Version | Description | License |
| :--- | :--- | :--- | :--- |
| [`rad-tui`](packages/rad-tui/0.1.0) | `0.1.0` | Modern, double-buffered Terminal User Interface framework | MIT |
| [`rad-json`](packages/rad-json/0.1.0) | `0.1.0` | Pure Rad JSON DOM, parser, and serialization | MIT |

## Using Packages in Rad Projects

Declare dependencies in your project's `rad.toml`:

```toml
[dependencies]
rad-tui = "^0.1.0"
rad-json = "^0.1.0"
```

Then install them with the Rad package manager:

```bash
rad package install
```

Or add packages interactively:

```bash
rad add rad-tui
rad add rad-json
```

## Repository Structure

```text
rad-lib/
├── registry/
│   ├── config.json         # Registry transport & base configuration
│   ├── index.json          # Package catalog & version metadata
│   └── schema/             # JSON validation schemas
├── packages/
│   ├── rad-tui/0.1.0/      # rad-tui package source and manifest
│   └── rad-json/0.1.0/     # rad-json package source and manifest
└── examples/               # Working showcase applications
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [REGISTRY.md](REGISTRY.md) for package publishing guidelines.

## License

MIT © 2026 GamerxIOEPB
