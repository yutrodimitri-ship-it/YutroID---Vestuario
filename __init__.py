"""
YUTRO Casting Studio - ComfyUI Custom Nodes
Professional wardrobe and casting workflow tools for AI-generated model photography.

Version: 2.3.0
Author: YUTRO
License: MIT
"""

from .nodes.yutro_wardrobe_preset import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
__version__ = "2.3.0"

print("=" * 60)
print("🎬 YUTRO CASTING STUDIO v2.3.0")
print("=" * 60)
print("✅ Loaded: YUTRO Wardrobe Preset 👔")
print("📁 Location: YUTRO/Casting")
print("")
print("🆕 v2.3 Features:")
print("  • Qwen Image Edit 2509 support (BEST for dressing models)")
print("  • Optimized for minimal-clothing → full outfit workflow")
print("  • Enhanced 'dress-the-mannequin' preservation system")
print("  • 30 professional presets (20 general + 10 mature)")
print("  • 4 target models: Nano, Seedream, Qwen, Generic")
print("")
print("🎯 Primary Use Case:")
print("  Take model in underwear → Dress in professional outfit")
print("  → Preserve 100% face/body features")
print("")
print("📖 Quick Start:")
print("  1. Add Node → YUTRO/Casting → YUTRO Wardrobe Preset")
print("  2. Select preset + target_model: 'Qwen Image Edit 2509'")
print("  3. Set preservation_strength: 'Maximum' (recommended)")
print("  4. Connect to Qwen Image Edit node")
print("  5. Input: Model in minimal clothing")
print("  6. Output: Fully dressed model (same face/body)")
print("")
print("🔗 Workflow: [Model in underwear] → [YUTRO] → [Qwen] → [Dressed model]")
print("=" * 60)
