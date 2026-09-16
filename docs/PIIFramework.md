# PII Framework

Metadata-only PII flags (`PIIStatus`, `PIIMetadata`) on versions/samples:

- `unknown` | `contains_phi` | `redacted` | `verified_safe`
- booleans for name/address/phone/signature/hospital/barcode/QR

**No redaction implementation** in Phase 3. Explorer can filter on `pii_status`.
