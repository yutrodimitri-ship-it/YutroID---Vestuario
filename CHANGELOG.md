# YUTRO Casting Studio - Changelog

All notable changes to this project will be documented in this file.

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

#### Key Features
- **Visual age tags**: (50+), (55+), (60+), (65+) in preset names
- **Comfort-first design**: Elastic waists, soft fabrics, relaxed fits
- **Age-appropriate styling**: Natural fibers, classic colors, dignified aesthetics
- **Practical accessories**: Large dial watches, comfortable shoes, functional bags

#### Technical
- Total presets: **30** (20 original + 10 mature)
- New category field: `age_range` in JSON
- Backward compatible with existing workflows

---

## [2.1.0] - 2024-12-23

### 🚀 Major Architecture Change - Linear Flow

**Breaking Change:** Complete redesign based on user feedback for better workflow clarity.

#### Added
- **Linear Architecture**: YUTRO → LLM → Image Model (simple, clear data flow)
- **Direct Mode**: Generate complete prompts without LLM (plug & play)
- **LLM_Enrich Mode**: Generate instructions for external LLM nodes to enrich prompts
- **4-Level Preservation System**:
  - Flexible: Similar proportions (creative freedom)
  - Moderate: Exact proportions (balanced)
  - Strong: CRITICAL preservation (recommended for casting)
  - Maximum: LOCKED identity (maximum accuracy)
- 20 professional outfit presets across 5 categories
- Multi-model optimization (Nano Banana Pro, Seedream 4.5, Generic)
- Gender fit adjustment system
- Additional notes field for custom details

#### Changed
- **Removed internal LLM client** (now uses external LLM nodes only)
- Removed `variation_mode: Local` (simplified to Direct/LLM_Enrich)
- Improved tooltip documentation
- Cleaner separation of concerns

#### Technical
- Zero external dependencies (LLM handled by external nodes)
- Professional error handling
- Fallback presets if JSON fails
- Comprehensive inline documentation

---

## [2.0.0] - 2024-12-22

### Initial Professional Release

#### Added
- 20 curated professional outfit presets
- Multi-model prompt optimization
- Identity preservation system
- Additional notes integration
- Professional tooltips
- Comprehensive testing (32/32 tests passed)

#### Features
- Preset categories: Casual, Formal/Business, Sport/Active, Evening/Night, Fashion/Editorial
- Target models: Nano Banana Pro, Seedream 4.5, Generic
- Gender fit: Auto, Male, Female, Unisex
- Fluid additional notes integration

---

## [1.2.0] - 2024-12-21

### Internal Testing Release

#### Added
- Visual separators in presets
- Improved field logic with visual prefixes
- Internal validation improvements

---

## [1.1.0] - 2024-12-20

### Beta Release

#### Added
- Basic preset system
- Initial wardrobe generation logic
- README documentation

---

## [1.0.0] - 2024-12-19

### Alpha Release

#### Added
- Initial project structure
- Basic node framework
- Proof of concept
