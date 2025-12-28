# YUTRO Casting Studio - Changelog

All notable changes to this project will be documented in this file.

## [2.3.0] - 2024-12-28

### 🚀 Qwen Image Edit 2509 Support

**Major Feature:** Added support for Qwen Image Edit 2509, optimized for the core use case of dressing models in minimal clothing while preserving identity.

#### Added
- **Qwen Image Edit 2509** as new target model option
- Specialized prompt optimization for Qwen's image editing capabilities
- Enhanced "dress-the-mannequin" preservation system for Qwen
- Model-specific preservation text generation

#### Changed
- **Default target_model**: Changed from "Nano Banana Pro" to "Qwen Image Edit 2509"
- **Default preservation_strength**: Changed from "Strong" to "Maximum" (recommended for casting workflow)
- Updated tooltips to highlight Qwen as BEST option for dressing minimal-clothing models
- Enhanced preservation instructions specifically for Qwen's architecture

#### Technical Details
- `_build_direct_prompt()`: Added Qwen case with "Add these clothes to this person" format
- `_get_preservation_text()`: Added conditional logic for Qwen-specific preservation
- `_get_model_prefix()`: Added "Add these clothes to this person: " prefix for Qwen
- `_build_llm_instruction()`: Updated context to emphasize "dressing a model in underwear"

#### Workflow Optimization
```
Input: Model in minimal clothing (underwear)
       ↓
YUTRO Node (v2.3):
  • preset: Any of 30 styles
  • target_model: "Qwen Image Edit 2509"
  • preservation: "Maximum"
       ↓
Qwen Image Edit Node
       ↓
Output: Fully dressed model (identical face/body)
```

---

## [2.2.0] - 2024-12-23

### 🎯 Age-Appropriate Presets Update

**Feature:** Added 10 professional presets specifically designed for mature adults (50-80 years).

#### Added - Mature/Casual (4 presets)
- **Coastal Grandma (55+)**: Relaxed elegance, Nancy Meyers aesthetic
- **Eclectic Grandpa (60+)**: Vintage charm, cozy nostalgia
- **Soft Casual Comfort (50+)**: Comfortable dignity, approachable warmth
- **Garden Casual (60+)**: Practical cheerfulness, outdoor ease

#### Added - Mature/Elegant (3 presets)
- **Refined Classic (55+)**: Timeless sophistication, quiet confidence
- **Elegant Mature (60+)**: Distinguished polish, graceful presence
- **Silver Sophistication (65+)**: Graceful refinement, ageless elegance

#### Added - Mature/Active (2 presets)
- **Active Senior (55+)**: Energetic practicality, healthy lifestyle
- **Wellness Casual (60+)**: Healthy comfort, mindful ease

#### Added - Mature/Evening (1 preset)
- **Mature Evening Elegant (65+)**: Dignified grace, refined evening presence

#### Technical
- Updated `wardrobe_presets_v2.json` with 10 new mature-focused presets
- Added `age_range` field to mature presets for clarity
- Total presets: 30 (20 general + 10 mature)

---

## [2.1.0] - 2024-12-20

### 🏗️ Linear Architecture Update

**Major Refactor:** Simplified architecture from 3-step to 2-step workflow.

#### Changed - Architecture
- **Old**: YUTRO → Variation Enhancer → LLM → Image Model
- **New**: YUTRO → Image Model (Direct) OR YUTRO → LLM → Image Model (LLM_Enrich)

#### Removed
- `variation_strength` parameter (replaced by `variation_mode`)
- Intermediate "Variation Enhancer" step
- Complexity of 3-step workflow

#### Added
- `variation_mode`: "Direct" or "LLM_Enrich"
- `target_model`: "Nano Banana Pro", "Seedream 4.5", "Generic"
- Direct prompt generation for image models (no LLM required for Direct mode)
- LLM instruction generation for LLM_Enrich mode

#### Benefits
- 50% faster workflow in Direct mode (skip LLM step)
- Clearer mental model: 2 distinct paths instead of 3 steps
- More control: choose when to use LLM enrichment
- Better prompts: model-specific optimization

---

## [2.0.0] - 2024-12-15

### 🎉 Initial Release

#### Features
- 20 professional wardrobe presets across 5 categories
- 4-level body preservation system
- 3-step variation system (Base → Variation → LLM)
- Multi-model support
- Gender fit adjustment
- Custom notes integration

#### Categories
- Casual (5 presets)
- Formal/Business (5 presets)
- Sport/Active (3 presets)
- Evening/Night (3 presets)
- Fashion/Editorial (4 presets)

---

## Version Comparison

| Version | Presets | Architecture | Models | Key Feature |
|---------|---------|--------------|--------|-------------|
| 2.0.0   | 20      | 3-step       | Generic | Initial release |
| 2.1.0   | 20      | 2-step (Linear) | 3 models | Simplified workflow |
| 2.2.0   | 30      | 2-step       | 3 models | Mature presets (50-80y) |
| 2.3.0   | 30      | 2-step       | 4 models | **Qwen support + casting optimization** |
