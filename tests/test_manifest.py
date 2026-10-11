import hashlib
import json
from pathlib import Path

import pytest
from vllm_hust_ext.manifest import activation_blocker, load_manifest

import stateaxis_speculative_decoding
from stateaxis_speculative_decoding import (
    SpeculativeDecodingConfig,
    speculative_decoding,
)


def test_manifest_is_active_and_hash_bound() -> None:
    package = Path(stateaxis_speculative_decoding.__file__).parent
    repo = package.parents[1]
    path = package / "vllm-hust-extension-v0.3.json"
    manifest = load_manifest(path)
    assert manifest.bundle_id == "org.vllm-hust.stateaxis-speculative-decoding"
    assert manifest.schema_version == "0.3-experimental"
    assert activation_blocker(manifest) is None
    raw = json.loads(path.read_text())
    expected = raw["activation"]["additional_config"]["stateaxis_mod"][
        "manifest_sha256"
    ]
    actual = hashlib.sha256((repo / "RESEARCH_MANIFEST.json").read_bytes()).hexdigest()
    assert actual == expected


def test_contract_cannot_gain_online_speculation_authority() -> None:
    assert speculative_decoding() == SpeculativeDecodingConfig()
    with pytest.raises(ValueError, match="reviewed component-only contract"):
        SpeculativeDecodingConfig(online_serving_included=True)
