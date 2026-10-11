"""Physical-B32 target-verification-only activation contract."""

from dataclasses import asdict, dataclass

MOD_ID = "org.vllm-hust.stateaxis-speculative-decoding"


@dataclass(frozen=True, slots=True)
class SpeculativeDecodingConfig:
    enabled: bool = True
    scope: str = "qwen2.5-14b-bf16-physical-b32-target-verification-component"
    mode: str = "target_verification_component_only"
    physical_batch: int = 32
    draft_widths: tuple[int, ...] = (1, 2, 3, 4, 5, 6, 7, 8)
    target_logits_required: bool = True
    target_tokens_exact_required: bool = True
    proposal_model_included: bool = False
    acceptance_transaction_included: bool = False
    rollback_transaction_included: bool = False
    online_serving_included: bool = False
    fail_closed: bool = True

    def __post_init__(self) -> None:
        expected = {
            "enabled": True,
            "scope": "qwen2.5-14b-bf16-physical-b32-target-verification-component",
            "mode": "target_verification_component_only",
            "physical_batch": 32,
            "draft_widths": (1, 2, 3, 4, 5, 6, 7, 8),
            "target_logits_required": True,
            "target_tokens_exact_required": True,
            "proposal_model_included": False,
            "acceptance_transaction_included": False,
            "rollback_transaction_included": False,
            "online_serving_included": False,
            "fail_closed": True,
        }
        if asdict(self) != expected:
            raise ValueError(
                "speculative decoding requires the reviewed component-only contract"
            )


def speculative_decoding() -> SpeculativeDecodingConfig:
    return SpeculativeDecodingConfig()


__all__ = ["MOD_ID", "SpeculativeDecodingConfig", "speculative_decoding"]
