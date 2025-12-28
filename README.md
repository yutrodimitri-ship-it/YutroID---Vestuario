# 🎬 YUTRO Casting Studio v2.2

**Professional Wardrobe Prompt Generator for AI Casting Model Workflows**
**🆕 Now with Age-Appropriate Presets (50-80 years)**

Transform your casting model images with professional outfit presets and intelligent prompt generation for ComfyUI.

---

## ✨ Features

### 🎯 **Linear Architecture** (v2.1)
- **YUTRO → Image Model** (Direct mode - no LLM needed)
- **YUTRO → LLM → Image Model** (LLM_Enrich mode - creative variations)

### 👔 **30 Professional Presets** (20 + 10 Mature)
Curated outfit presets across 8 categories:

**ALL AGES (20 presets):**
- **Casual** (5): Smart Casual, Weekend Relaxed, Urban Streetwear, Summer Casual, Layered Casual
- **Formal/Business** (5): Business Professional, Executive Suit, Smart Business, Corporate Casual, Business Elegant
- **Sport/Active** (3): Athleisure, Sporty Active, Yoga Casual
- **Evening/Night** (3): Evening Elegant, Night Out, Cocktail Ready
- **Fashion/Editorial** (4): Minimalist Fashion, Streetwear Premium, Vintage Retro, Avant-Garde

**MATURE ADULTS (10 presets):**
- **Mature/Casual** (4): Coastal Grandma (55+), Eclectic Grandpa (60+), Soft Casual Comfort (50+), Garden Casual (60+)
- **Mature/Elegant** (3): Refined Classic (55+), Elegant Mature (60+), Silver Sophistication (65+)
- **Mature/Active** (2): Active Senior (55+), Wellness Casual (60+)
- **Mature/Evening** (1): Mature Evening Elegant (65+)

### 🔒 **4-Level Preservation System**
Critical for casting to maintain model identity:
- **Flexible**: Similar proportions (creative freedom)
- **Moderate**: Exact proportions (balanced approach)
- **Strong**: CRITICAL preservation ⭐ **RECOMMENDED for casting**
- **Maximum**: LOCKED identity (forensic accuracy)

### 🎨 **2 Generation Modes**

#### **Direct Mode** (No LLM needed)
Generates complete, optimized prompts ready for image models.

```
YUTRO Wardrobe Preset → Nano Banana Pro → Image
```

#### **LLM_Enrich Mode** (Creative variations)
Generates detailed instructions for LLM to create enriched prompts.

```
YUTRO Wardrobe Preset → LLM Node → Nano Banana Pro → Image
```

### 🎯 **Multi-Model Optimization**
- **Nano Banana Pro**: Direct instruction format
- **Seedream 4.5**: Transformation format with pose preservation
- **Generic**: Universal format for any image model

---

## 📥 Installation

### Option 1: Manual Installation (Recommended)

1. **Download** the latest release ZIP
2. **Extract** to your ComfyUI custom nodes folder:
   ```
   ComfyUI/custom_nodes/ComfyUI-YUTRO-CastingStudio-v2.1/
   ```
3. **Restart** ComfyUI
4. **Find node** at: `Add Node → YUTRO/Casting → YUTRO Wardrobe Preset 👔`

### Option 2: Git Clone

```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/ComfyUI-YUTRO-CastingStudio.git
cd ComfyUI-YUTRO-CastingStudio
# No dependencies to install!
```

### Verify Installation

After restarting ComfyUI, you should see:
```
============================================================
🎬 YUTRO CASTING STUDIO v2.1.0
============================================================
✅ Loaded: YUTRO Wardrobe Preset 👔
📁 Location: YUTRO/Casting
```

---

## 🎯 Age-Appropriate Presets Guide

### **Why Age Tags Matter**

Different age groups have different fashion needs:

| Age Range | Style Focus | Key Features |
|-----------|-------------|-------------|
| **20-49** | Trendy, fitted | Slim cuts, bold colors, modern aesthetics |
| **50-64** | Comfortable modern | Relaxed fits, soft fabrics, classic with updates |
| **65-79** | Timeless elegant | Natural fibers, dignified styling, practical comfort |
| **80+** | Maximum comfort | Easy wear, soft materials, functional design |

### **Mature Presets Overview**

#### **Coastal Grandma (55+)** 🌊
- **Vibe**: Nancy Meyers aesthetic, relaxed elegance
- **Key pieces**: Linen cardigan, wide-leg pants, straw tote
- **Perfect for**: Beachside brunch, casual gatherings, relaxed outdoor events

#### **Eclectic Grandpa (60+)** 🧥
- **Vibe**: Vintage charm, cozy nostalgia
- **Key pieces**: Argyle sweater vest, wool trousers, suede loafers
- **Perfect for**: Library visits, casual socials, comfortable everyday

#### **Soft Casual Comfort (50+)** 🧶
- **Vibe**: Comfortable dignity, approachable warmth
- **Key pieces**: Merino sweater, relaxed chinos, cashmere scarf
- **Perfect for**: Casual meetings, shopping, lunch with friends

#### **Garden Casual (60+)** 🌿
- **Vibe**: Practical cheerfulness, outdoor ease
- **Key pieces**: Cotton check shirt, elastic-waist pants, sun hat
- **Perfect for**: Gardening, outdoor markets, nature walks

#### **Refined Classic (55+)** 👔
- **Vibe**: Timeless sophistication, quiet confidence
- **Key pieces**: Soft-structure blazer, wool pants, silk pocket square
- **Perfect for**: Professional events, formal lunches, cultural outings

#### **Elegant Mature (60+)** 🎩
- **Vibe**: Distinguished polish, graceful presence
- **Key pieces**: Cashmere turtleneck, tailored trousers, overcoat
- **Perfect for**: Theater evenings, upscale dinners, formal gatherings

#### **Silver Sophistication (65+)** 💎
- **Vibe**: Graceful refinement, ageless elegance
- **Key pieces**: Silk blouse, wide-leg wool pants, pearl earrings
- **Perfect for**: Special occasions, elegant luncheons, refined social events

#### **Active Senior (55+)** 🏃
- **Vibe**: Energetic practicality, healthy lifestyle
- **Key pieces**: Quarter-zip pullover, stretch pants, walking sneakers
- **Perfect for**: Morning walks, light exercise, active outdoor activities

#### **Wellness Casual (60+)** 🧘
- **Vibe**: Healthy comfort, mindful ease
- **Key pieces**: Cotton henley, relaxed joggers, supportive shoes
- **Perfect for**: Wellness center, gentle yoga, health-focused activities

#### **Mature Evening Elegant (65+)** ✨
- **Vibe**: Dignified grace, refined evening presence
- **Key pieces**: Silk cardigan with pearls, merino turtleneck, gold jewelry
- **Perfect for**: Evening concerts, formal dinners, elegant celebrations

---

## 🚀 Quick Start

### Workflow 1: Direct Mode (No LLM)

**Simple 3-node workflow:**

```
┌─────────────────────────┐
│  YUTRO Wardrobe Preset │
├─────────────────────────┤
│ preset: Smart Casual    │
│ mode: Direct            │
│ preservation: Strong    │
│ OUTPUT: prompt ─────────┼──┐
└─────────────────────────┘  │
                             ↓
                  ┌──────────────────┐
                  │  Load Image      │
                  │  (base model)    │
                  └──────────────────┘
                             ↓
                  ┌──────────────────┐
                  │  Nano Banana Pro │
                  │  (generates img) │
                  └──────────────────┘
```

**Steps:**
1. Add `YUTRO Wardrobe Preset` node
2. Select `preset_name`: "Smart Casual"
3. Set `variation_mode`: "Direct"
4. Set `preservation_strength`: "Strong"
5. Connect `prompt` output to your image model
6. Run!

---

### Workflow 2: LLM_Enrich Mode (Creative Variations)

**4-node workflow with LLM:**

```
┌─────────────────────────┐
│  YUTRO Wardrobe Preset │
├─────────────────────────┤
│ preset: Business Pro    │
│ mode: LLM_Enrich        │
│ preservation: Maximum   │
│ OUTPUT: instruction ────┼──┐
└─────────────────────────┘  │
                             ↓
                  ┌──────────────────────┐
                  │  LLM Node            │
                  │  (Gemini/GPT/Ollama) │
                  │ OUTPUT: enriched ────┼──┐
                  └──────────────────────┘  │
                                            ↓
                                 ┌──────────────────┐
                                 │  Load Image      │
                                 └──────────────────┘
                                            ↓
                                 ┌──────────────────┐
                                 │  Nano Banana Pro │
                                 └──────────────────┘
```

**Steps:**
1. Add `YUTRO Wardrobe Preset` node
2. Select `preset_name`: "Business Professional"
3. Set `variation_mode`: "LLM_Enrich"
4. Set `preservation_strength`: "Maximum"
5. Add an LLM node (Gemini/GPT/Ollama)
6. Connect YUTRO `prompt` → LLM `input`
7. Connect LLM `output` → Image Model `prompt`
8. Run!

---

## 📚 Node Parameters

### Required Inputs

| Parameter | Type | Options | Default | Description |
|-----------|------|---------|---------|-------------|
| `preset_name` | Dropdown | 30 presets | "Smart Casual" | Professional outfit preset (look for age tags) |
| `preservation_strength` | Dropdown | Flexible, Moderate, Strong, Maximum | "Strong" | Body/face preservation level |
| `variation_mode` | Dropdown | Direct, LLM_Enrich | "Direct" | Generation mode |
| `target_model` | Dropdown | Nano Banana Pro, Seedream 4.5, Generic | "Nano Banana Pro" | Target image model |
| `gender_fit` | Dropdown | Auto, Male, Female, Unisex | "Auto" | Gender adjustment |

### Optional Inputs

| Parameter | Type | Description |
|-----------|------|-------------|
| `additional_notes` | STRING (multiline) | Custom details: accessories, fit, colors, brands |

### Output

| Output | Type | Description |
|--------|------|-------------|
| `prompt` | STRING | Complete prompt (Direct) or LLM instruction (LLM_Enrich) |

---

## 🎯 Use Cases

### 1. Professional Casting Portfolio

**Scenario:** Photographer needs consistent model across 20 different outfits.

**Solution:**
```
variation_mode: Direct
preservation_strength: Maximum
Loop through 20 presets
→ Same model, 20 different professional looks
```

---

### 2. Creative Fashion Exploration

**Scenario:** Designer wants unique variations of "Smart Casual" style.

**Solution:**
```
variation_mode: LLM_Enrich
llm_provider: Gemini Flash (free)
Run 50 times with different LLM seeds
→ 50 unique Smart Casual interpretations
```

---

### 3. Multi-Model Comparison

**Scenario:** Compare how different models handle same outfit.

**Solution:**
```
preset_name: Business Professional
variation_mode: Direct
preservation_strength: Strong

Test with:
- target_model: Nano Banana Pro
- target_model: Seedream 4.5
- target_model: Generic

→ Compare results across models
```

---

## 🔧 Advanced Usage

### Preservation Strength Guide

#### When to use each level:

| Strength | Use Case | Body Accuracy | Creative Freedom |
|----------|----------|---------------|------------------|
| **Flexible** | Concept exploration, moodboards | ~70% | High |
| **Moderate** | General portfolio work | ~85% | Medium |
| **Strong** | Professional casting ⭐ | ~95% | Low |
| **Maximum** | Contractual portfolios, catalogs | ~99% | Minimal |

**Casting Rule:** Always use **Strong** or **Maximum** when client needs to see the actual model.

---

### Additional Notes Examples

```
✅ Good examples:
- "add black leather belt"
- "oversized fit"
- "pastel colors"
- "Nike brand sneakers"
- "vintage accessories"

❌ Avoid:
- Complete outfit changes (use presets instead)
- Contradicting the preset style
```

---

### LLM Integration

#### Compatible LLM Nodes:

1. **ComfyUI-LLM** (Recommended)
   - Supports: OpenAI, Anthropic, Google
   - Installation: `git clone https://github.com/lllyasviel/ComfyUI-LLM.git`

2. **ComfyUI-Ollama** (Local/Free)
   - Supports: Qwen2.5, Mistral, LLaMA
   - Installation: `git clone https://github.com/stavsap/comfyui-ollama.git`
   - Recommended models:
     - `ollama pull qwen2.5:7b` (best for fashion)
     - `ollama pull mistral:7b` (general purpose)

3. **Custom LLM Node**
   - Any node that outputs `STRING` type works
   - Connect YUTRO `prompt` → LLM `input`
   - LLM processes instruction → outputs enriched prompt

---

## 📊 Example Outputs

### Direct Mode Output:
```
Dress this person in white dress shirt with rolled sleeves, navy blue 
chinos, brown leather loafers, minimalist silver watch, smart casual 
style, professional yet relaxed vibe. PRESERVE: exact body shape, 
muscle definition, body proportions, facial features, skin tone. 
This is a casting model showcase - identity accuracy is CRITICAL.
```

### LLM_Enrich Mode Output:
```
You are a professional fashion stylist creating detailed outfit prompts 
for AI image generation in casting photoshoots.

TASK: Generate a creative and detailed outfit prompt for the style 
category "Smart Casual".

BASE REFERENCE (use as inspiration, NOT exact copy):
- Category: Smart Casual (Casual)
- Base outfit: white dress shirt, navy chinos, brown loafers
- Style: smart casual
- Vibe: professional yet relaxed
- Typical occasions: office casual, business lunch, networking event

REQUIREMENTS:
1. Create a CREATIVE VARIATION of this outfit (do NOT copy exactly)
2. Vary: colors, textures, fabrics, materials, accessories, brands
3. MUST maintain the "smart casual" style and "professional yet relaxed" vibe
4. Gender fit: Male
5. Target image generation model: Nano Banana Pro

[... detailed instructions continue ...]

Generate the prompt now:
```

*LLM then generates enriched prompt like:*
```
Dress this person in sage green textured cotton shirt with subtle 
herringbone pattern and mother-of-pearl buttons, charcoal gray 
wool-blend trousers with subtle pinstripe, burgundy leather derby 
shoes with cap toe, woven cognac leather belt, brushed gold minimalist 
chronograph watch, smart casual style, refined and approachable vibe. 
PRESERVE: exact body shape, muscle definition, body proportions, 
facial features, skin tone. This is a casting model showcase - 
identity accuracy is CRITICAL.
```

---

## 🐛 Troubleshooting

### Issue: Preset not loading

**Solution:**
- Check `presets/wardrobe_presets_v2.json` exists
- Verify JSON syntax is valid
- Restart ComfyUI
- Node has fallback presets if file missing

---

### Issue: LLM_Enrich mode not working

**Possible causes:**
1. No LLM node connected
   - **Solution:** Add and connect an LLM node
2. LLM node output incompatible
   - **Solution:** Ensure LLM outputs `STRING` type
3. LLM node not generating prompt correctly
   - **Solution:** Check LLM temperature/settings

---

### Issue: Model slimming down/changing proportions

**Solution:**
- Increase `preservation_strength`: Moderate → Strong → Maximum
- Use `target_model` specific optimization
- Check image model's denoise_strength (keep < 0.5)

---

## 🗺️ Roadmap

### v2.3 (Planned)
- [ ] YUTRO Wardrobe Custom (piece-by-piece outfit builder)
- [ ] Batch processing mode
- [ ] Preset favorites system
- [ ] More mature presets (cultural diversity)

### v3.0 (Future)
- [ ] YUTRO Photoshoot Studio (poses, lighting, camera angles)
- [ ] YUTRO AI Wardrobe Agent (full LLM reasoning)
- [ ] Custom preset creator UI

---

## 📝 Changelog

See [CHANGELOG.md](CHANGELOG.md) for full version history.

---

## 🤝 Contributing

Contributions welcome! Please:
1. Fork the repository
2. Create a feature branch
3. Submit a pull request

---

## 📄 License

MIT License - See LICENSE file for details

---

## 🙏 Credits

- **Author:** YUTRO Casting Studio
- **Version:** 2.2.0
- **Architecture Design:** User feedback-driven (linear flow)
- **ComfyUI:** [ComfyUI Project](https://github.com/comfyanonymous/ComfyUI)

---

## 📧 Support

- **Issues:** [GitHub Issues](https://github.com/yourusername/ComfyUI-YUTRO-CastingStudio/issues)
- **Discussions:** [GitHub Discussions](https://github.com/yourusername/ComfyUI-YUTRO-CastingStudio/discussions)

---

## ⭐ If You Like This Project

- Star the repository
- Share with the community
- Report bugs/suggest features
- Contribute presets or improvements

---

**Made with ❤️ for the ComfyUI community**
