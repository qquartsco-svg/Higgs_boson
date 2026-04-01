# BLOCKCHAIN_INFO

In this repository, “blockchain signature” does **not** mean an on-chain consensus system or smart contract.

Here it means the **file-level SHA-256 integrity manifest** stored at the repository root in `SIGNATURE.sha256`.

What it does guarantee:

- quick detection of release-surface changes
- comparison between a local copy and the published baseline
- integrity checks for package code, tests, scripts, and documentation

What it does not guarantee:

- cryptographic signing with private keys
- blockchain consensus validation
- on-chain persistence

Verify:

```bash
python3 scripts/verify_signature.py
```

Regenerate:

```bash
python3 scripts/generate_signature.py
```
