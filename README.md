# StateAxis Speculative Target Verification

Extension ID: `org.vllm-hust.stateaxis-speculative-decoding`

This MOD is the active, default-off ECPA boundary for the existing StateAxis
Qwen2.5-14B BF16 physical-B32 target-verification component from issue
[#7](https://github.com/Qixin-Gaoke/stateaxis/issues/7). It admits draft widths
K1-K8 and requires exact target logits/tokens.

## Deliberate boundary

This is not a complete online speculative decoder. The contract explicitly
excludes a proposal model, acceptance transaction, rollback transaction, and
online serving. The StateAxis host rejects online launch under this MOD and
accepts it only for assembly/component validation. Results from vLLM-HUST
vSpec or EAGLE checkpoints are not inherited.

```bash
python -m pip install .
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext extension check org.vllm-hust.stateaxis-speculative-decoding
VLLM_HUST_EXT_CONFIG=evidence/ecpa-contract-20261011/manager-config.json \
  vllm-hust-ext run --dry-run -- /bin/true
```

## Evidence boundary

Historical V163 real-NPU component tests were exact across five lifecycles and
showed 1.547x at K1 through 4.112x at K8. This is component-cost evidence only.
For the frozen prompt-lookup proposal, V168's optimistic serial upper bound was
only 1.016x-1.019x and no sample exceeded 1.05x, so it could not meet the 1.20x
admission gate. No online throughput gain is claimed. See [EVIDENCE.md](EVIDENCE.md).

## Validate

```bash
python -m pip install -e '.[test]'
ruff check .
ruff format --check .
pytest -q
python -m build
```

Maintainer: Shuhao Zhang (Tony), directly responsible; no advisor is declared.
