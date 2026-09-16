# Benchmarks

First-class comparative evaluation across engines.

**Evaluation** (`evaluation/`) = metrics for one run.
**Benchmarks** (this tree) = suites comparing engines (Paddle vs PARSeq vs TrOCR vs Qwen, …).

| Suite | Focus |
|-------|-------|
| `handwritten/` | Handwriting / prescription HTR |
| `printed/` | Printed documents |
| `mixed/` | Mixed print + handwriting |
| `robustness/` | Noise, blur, rotation, compression |
| `latency/` | Throughput / latency |

Runner interface: `aarogya_core.interfaces.BenchmarkRunner`.
