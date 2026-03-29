import os
import json
from anthropic import Anthropic
from config import (
    ANTHROPIC_API_KEY,
)

client = Anthropic(
    api_key=ANTHROPIC_API_KEY,
)
page = client.models.list()

print("=" * 100)
print("AVAILABLE CLAUDE MODELS")
print("=" * 100)

for i, model in enumerate(page.data, 1):
    print(f"\n{i}. {model.display_name}")
    print(f"   ID: {model.id}")
    print(f"   Created: {model.created_at.strftime('%Y-%m-%d')}")
    print(f"   Max Input Tokens: {model.max_input_tokens:,}")
    print(f"   Max Output Tokens: {model.max_tokens:,}")
    
    # Show key capabilities
    caps = model.capabilities
    print(f"   Capabilities:")
    print(f"     ✓ Batch: {caps.batch.supported}")
    print(f"     ✓ Code Execution: {caps.code_execution.supported}")
    print(f"     ✓ Image Input: {caps.image_input.supported}")
    print(f"     ✓ Thinking: {caps.thinking.supported}")
    if hasattr(caps.effort, 'max') and caps.effort.max.supported:
        print(f"     ✓ Effort Level: max")
    print()

print("=" * 100)