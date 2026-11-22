#!/usr/bin/env python3
import json
import hashlib
import os
import sys

def main():
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    index_path = os.path.join(repo_root, "registry", "index.json")

    if not os.path.isfile(index_path):
        sys.exit(f"Error: registry index not found at {index_path}")

    with open(index_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    pkgs = data.get("packages", {})
    if not pkgs:
        sys.exit("Error: No packages found in registry/index.json")

    errors = 0
    checked = 0

    for name, pkg in sorted(pkgs.items()):
        pkg_name = pkg.get("name")
        if pkg_name != name:
            print(f"[FAIL] Package key '{name}' does not match inner name '{pkg_name}'")
            errors += 1

        for field in ("latest", "versions", "releases"):
            if field not in pkg:
                print(f"[FAIL] Package '{name}' missing required field '{field}'")
                errors += 1

        releases = pkg.get("releases", {})
        for ver, rel in releases.items():
            if rel.get("version") != ver:
                print(f"[FAIL] Release key '{ver}' does not match inner version in '{name}'")
                errors += 1

            rel_path = rel.get("path", "")
            pkg_dir = os.path.join(repo_root, rel_path)
            if not os.path.isdir(pkg_dir):
                print(f"[FAIL] Path '{rel_path}' does not exist for '{name}' {ver}")
                errors += 1
                continue

            rad_toml = os.path.join(pkg_dir, "rad.toml")
            if not os.path.isfile(rad_toml):
                print(f"[FAIL] rad.toml missing in '{pkg_dir}'")
                errors += 1
                continue

            with open(rad_toml, "rb") as tf:
                actual_chk = hashlib.sha256(tf.read()).hexdigest()

            expected_chk = rel.get("checksum", "")
            if actual_chk != expected_chk:
                print(f"[FAIL] Checksum mismatch for '{name}' {ver}: expected {expected_chk}, calculated {actual_chk}")
                errors += 1
            else:
                checked += 1

    if errors > 0:
        print(f"\nValidation failed with {errors} error(s).")
        sys.exit(1)

    print(f"Validation successful: verified {len(pkgs)} packages and {checked} release checksums.")

if __name__ == "__main__":
    main()
