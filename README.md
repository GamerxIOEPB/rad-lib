# Rad Library Registry (`rad-lib`)

Official package registry and library repository for the **Rad Programming Language**.

## Packages

| Package | Version | Description | License |
| :--- | :--- | :--- | :--- |
| [`rad-args`](packages/rad-args/0.1.0) | `0.1.0` | Declarative CLI argument parsing library with subcommands, flags, and options | MIT |
| [`rad-http`](packages/rad-http/0.1.0) | `0.1.0` | Lightweight HTTP/1.1 client and micro-server in pure Rad | MIT |
| [`rad-json`](packages/rad-json/0.1.0) | `0.1.0` | Pure Rad JSON DOM, parser, and serialization | MIT |
| [`rad-math`](packages/rad-math/0.1.0) | `0.1.0` | 2D/3D vectors, matrices, and geometry math in pure Rad | MIT |
| [`rad-test`](packages/rad-test/0.1.0) | `0.1.0` | Ergonomic unit testing harness with assertions and colored reporting | MIT |
| [`rad-tui`](packages/rad-tui/0.1.0) | `0.1.0` | Modern, double-buffered Terminal User Interface framework | MIT |

## Using Packages in Rad Projects

Declare dependencies in your project's `rad.toml`:

```toml
[dependencies]
rad-args = "^0.1.0"
rad-http = "^0.1.0"
rad-json = "^0.1.0"
rad-math = "^0.1.0"
rad-test = "^0.1.0"
rad-tui = "^0.1.0"
```

Then install them with the Rad package manager:

```bash
rad package install
```

Or add packages interactively:

```bash
rad add rad-args
rad add rad-http
rad add rad-json
rad add rad-math
rad add rad-test
rad add rad-tui
```

## Repository Structure

```text
rad-lib/
├── registry/
│   ├── config.json         # Registry transport & base configuration
│   ├── index.json          # Package catalog & version metadata
│   └── schema/             # JSON validation schemas
├── packages/
│   ├── rad-args/0.1.0/    # CLI argument parsing library
│   ├── rad-http/0.1.0/    # HTTP client/server library
│   ├── rad-json/0.1.0/    # JSON parser/serializer library
│   ├── rad-math/0.1.0/    # Math and geometry library
│   ├── rad-test/0.1.0/    # Testing framework
│   ├── rad-tui/0.1.0/     # TUI framework
│   └── ...
├──────────────────────
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) and [REGISTRY.md](REGISTRY.md) for package publishing guidelines.

## License

MIT © 2026 GamerxIOEPB
