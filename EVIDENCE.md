# Evidence index

- [`ISSUE7_SPECULATIVE_DECODING_CLOSURE.md`](evidence/ISSUE7_SPECULATIVE_DECODING_CLOSURE.md): retained StateAxis V163-V168 closure. V163 validates the physical-B32 K1-K8 target-verification component; V168 rejects the frozen prompt-lookup candidate's online admission case.
- [`ecpa-contract-20261011/RESULT.json`](evidence/ecpa-contract-20261011/RESULT.json): active Manifest 0.3 / ECPA component admission, host identity separation, Rust and C++ contract tests, and current evidence boundary.
- [`historical-v163-v168/`](evidence/historical-v163-v168/): all six frozen
  component, projection, held-out feasibility, proposer-cost and optimistic
  bound records with a repo-local SHA-256 manifest.

The positive component result is not an online speculative-decoding result.
No vLLM-HUST vSpec or EAGLE evidence is inherited. A future online StateAxis
candidate requires separately frozen proposer, tokenizer, acceptance,
rollback, lifecycle, exactness, and matched serving identities.
