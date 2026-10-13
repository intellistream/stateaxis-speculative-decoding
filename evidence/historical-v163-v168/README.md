# Historical V163-V168 evidence chain

These six files are byte-for-byte copies of the frozen StateAxis issue #7
evidence chain. `SHA256SUMS` reproduces the hashes recorded in the closure.

V163 is real-NPU component evidence: target verification was exact across five
lifecycles and improved from 1.547x at K1 to 4.112x at K8. V164-V168 evaluate
the available prompt-lookup proposer. The decisive V168 optimistic bound makes
all extra verification and integration work free, yet serial speedup is only
1.0164x-1.0187x and 0/14 samples exceed 1.05x, below the 1.20x admission gate.

Thus the target primitive is useful, but this proposer cannot justify an
online speculative decoder. No online throughput result is claimed.
