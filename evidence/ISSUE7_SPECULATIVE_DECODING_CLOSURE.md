# Issue #7: speculative decoding closure

> **Document role: point-in-time report, not current repository status or a task
> assignment.** Current classification and priorities live only in
> [`NATIVE_ENGINE_STATUS.md`](../../NATIVE_ENGINE_STATUS.md).

Issue #7 is closed for the currently available Native candidate. The target-verification component is valid, but the frozen prompt-lookup proposal cannot meet the issue's 20% eager throughput advance gate even under an optimistic zero-integration-cost bound.

## Evidence chain

The V163 real-NPU B32 target-verification component passed logits/token correctness for draft widths 1 through 8. Its median component speedup increased from 1.547x at K1 to 4.112x at K8. This establishes a useful target primitive, not an online speculative decoder: no proposal model, acceptance transaction, rollback, scheduler accounting, or serving protocol was included.

V164/V165 evaluated prompt lookup over recorded continuations. The best training projection predicted only 1.0946x target-only speedup; held-out target-only headroom was 10.294%. Neither included full integration cost.

V166/V167 then modeled and measured suffix decoding at physical B32. Across 14 frozen waves, the candidate won 0 times; median target-only speedup was 0.7027x and median serial speedup including proposer CPU was 0.6958x.

V168 is the decisive upper bound. It assumes every extra draft-verification row and all scheduler/integration work are free while retaining only one base target pass and measured proposer CPU. Even then, target-only speedup is exactly 1.0323x and serial speedup ranges from 1.0164x to 1.0187x; 0 of 14 samples exceed 1.05x. A production implementation cannot reach the preregistered 1.20x gate under this candidate.

The repository has no frozen DSpark/EAGLE draft checkpoint, tokenizer mapping, or proposal execution artifact. Issue #7 explicitly forbids hardware performance work without those identities. Adding protocol/state transactions for prompt lookup would therefore integrate a candidate already proven unable to cross the gate.

## Decision

- Preserve V163 as accepted real-NPU component-cost evidence.
- Preserve V164--V168 as feasibility and negative-bound evidence.
- Keep speculative mode rejected by the protocol worker and default-off.
- Do not add proposal/acceptance/rollback protocol fields for this failed candidate.
- Make no online throughput, HBM, graph, or vLLM-HUST claim.
- Close Issue #7. A future DSpark/EAGLE attempt requires an available frozen draft checkpoint, new identity/preregistration, and must not reuse prompt-lookup projections as performance evidence.

## Frozen evidence hashes

- V163 NPU component audit: `91d936e8167f2945c6bfa8fee2907ad2057195b5eecce0a15ae0168a10bdf2d3`
- V164 target-cost projection: `2c09ade0249e56ae2b0fc8159aa5ef648a2739b210d955e113d9364cb3c6b9f1`
- V165 held-out policy: `9b1a716c83300a51a4892047cf9477937114ee33052c7c3685eef0e000fb4561`
- V166 held-out suffix feasibility: `d5cc226e5b1fd35233bce8833d469771688bca34b77fcdb7b6a614a3904b0230`
- V167 physical-B32 CPU/proposal result: `5c90ec5116d1b82656f404f637c0cdf171f409b4894a9a56a908974ac42222c1`
- V168 free-verification upper bound: `7ed963732ee6a6e0d5dd64faf23092a12218c4e7c8deb00351f6be7d490a2d33`
