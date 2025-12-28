"""
YUTRO Casting Studio - ComfyUI Custom Nodes
Professional wardrobe and casting workflow tools for AI-generated model photography.

Version: 2.2.0
Author: YUTRO
License: MIT
"""

from .nodes.yutro_wardrobe_preset import NODE_CLASS_MAPPINGS, NODE_DISPLAY_NAME_MAPPINGS

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
__version__ = "2.2.0"

print("=" * 60)
print("🎬 YUTRO CASTING STUDIO v2.2.0")
print("=" * 60)
print("✅ Loaded: YUTRO Wardrobe Preset 👔")
print("📁 Location: YUTRO/Casting")
print("")
print("🆕 v2.2 Features:")
print("  • 30 professional presets (20 + 10 mature)")
print("  • Age-appropriate styles: (50+), (55+), (60+), (65+)")
print("  • Coastal Grandma, Eclectic Grandpa, Silver Sophistication")
print("  • Linear architecture (YUTRO → LLM → Image Model)")
print("  • 4-level preservation system")
print("")
print("📖 Quick Start:")
print("  1. Add Node → YUTRO/Casting → YUTRO Wardrobe Preset")
print("  2. Select preset (look for age tags like '55+')")
print("  3. Choose mode: Direct or LLM_Enrich")
print("  4. Connect to image model or LLM node")
print("")
print("=" * 60)
