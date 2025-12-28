# 🎬 YUTRO Casting Studio v2.3

**Professional Wardrobe Prompt Generator for AI Casting Model Workflows**
**🆕 Now with Qwen Image Edit 2509 Support**

Transform your casting model images with professional outfit presets and intelligent prompt generation for ComfyUI. **Optimized for dressing models in minimal clothing while preserving 100% of their identity.**

---

## ✨ What's New in v2.3

### 🎯 **Qwen Image Edit 2509 Integration**
- **NEW Model Support**: Qwen Image Edit 2509 (now default and recommended)
- **Optimized for Core Use Case**: Dressing models in underwear → Full professional outfit
- **Enhanced Preservation**: "Dress-the-mannequin" system locks face/body features
- **Better Results**: Superior identity preservation compared to other models

### 🔄 **Workflow**
```
[Model in Underwear/Minimal Clothing]
            ↓
[YUTRO Wardrobe Preset v2.3]
  • Select outfit preset
  • Target: Qwen Image Edit 2509
  • Preservation: Maximum
            ↓
[Qwen Image Edit 2509 Node]
            ↓
[Fully Dressed Model]
  (Same face, same body, new outfit)
```

---

## 🎯 Features

### 🏗️ **Linear Architecture** (v2.1+)
- **YUTRO → Image Model** (Direct mode - no LLM needed)
- **YUTRO → LLM → Image Model** (LLM_Enrich mode - creative variations)

### 👔 **30 Professional Presets** (20 General + 10 Mature)
Curated outfit presets across 8 categories:

**ALL AGES (20 presets):**
- **Casual** (5): Smart Casual, Weekend Relaxed, Urban Streetwear, Summer Casual, Layered Casual
- **Formal/Business** (5): Business Professional, Executive Suit, Smart Business, Corporate Casual, Business Elegant
- **Sport/Active** (3): Athleisure, Sporty Active, Yoga Casual
- **Evening/Night** (3): Evening Elegant, Night Out, Cocktail Ready
- **Fashion/Editorial** (4): Minimalist Fashion, Streetwear Premium, Vintage Retro, Avant-Garde

**MATURE/SENIOR (10 presets for 50-80 years):**
- **Mature/Casual** (4): Coastal Grandma (55+), Eclectic Grandpa (60+), Soft Casual Comfort (50+), Garden Casual (60+)
- **Mature/Elegant** (3): Refined Classic (55+), Elegant Mature (60+), Silver Sophistication (65+)
- **Mature/Active** (2): Active Senior (55+), Wellness Casual (60+)
- **Mature/Evening** (1): Mature Evening Elegant (65+)

### 🛡️ **4-Level Body Preservation System**
Fine-tune how much of the original model's features to preserve:

| Level | Description | Use Case |
|-------|-------------|----------|
| **Flexible** | Similar proportions | Creative freedom, artistic variations |
| **Moderate** | Exact proportions | Balanced approach |
| **Strong** | Critical preservation | Standard casting work |
| **Maximum** | Locked identity | **Dressing models in underwear (RECOMMENDED)** |

### 🤖 **4 Target Model Options**
- **Qwen Image Edit 2509** ⭐ **(NEW & RECOMMENDED)** - Best for adding clothing to minimal-dress models
- **Nano Banana Pro** - Direct instruction format
- **Seedream 4.5** - Transformation format
- **Generic** - Universal format for any model

### 🎨 **2 Generation Modes**
- **Direct**: Complete prompt ready for image model (fast, no LLM needed)
- **LLM_Enrich**: Instruction for LLM to generate creative variations (connect LLM node)

### 👥 **Gender Fit Adjustment**
- Auto (default) / Male / Female / Unisex
- Automatically adapts outfit descriptions

### 📝 **Custom Notes Support**
Add your own details:
- Accessories: "add leather belt", "silver watch"
- Fit adjustments: "oversized fit", "slim cut"
- Colors: "pastel colors", "earth tones"
- Brands: "Nike sneakers", "Gucci belt"

---

## 📦 Installation

### Method 1: ComfyUI Manager (Recommended)
1. Open ComfyUI Manager
2. Search for "YUTRO Casting Studio"
3. Click Install
4. Restart ComfyUI

### Method 2: Manual Installation
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/YUTRO-Casting-Studio.git
cd YUTRO-Casting-Studio
pip install -r requirements.txt
```

### Method 3: Git Clone
```bash
cd ComfyUI/custom_nodes/
git clone https://github.com/yourusername/YUTRO-Casting-Studio.git
```

---

## 🚀 Quick Start

### **Basic Workflow (Recommended for Casting Models)**

**Scenario:** You have a model/character in underwear, want to dress them in professional outfits.

1. **Add the Node**
   - Right-click → Add Node → YUTRO/Casting → YUTRO Wardrobe Preset 👔

2. **Configure Settings**
   ```
   preset_name: "Smart Casual" (or any of 30 presets)
   preservation_strength: "Maximum" ⭐ (CRITICAL for identity preservation)
   variation_mode: "Direct"
   target_model: "Qwen Image Edit 2509" ⭐ (BEST results)
   gender_fit: "Auto"
   additional_notes: "" (optional)
   ```

3. **Connect to Qwen Image Edit 2509**
   ```
   [Load Image] (model in underwear)
         ↓
   [YUTRO Wardrobe Preset] → prompt output
         ↓
   [Qwen Image Edit 2509]
         ↓
   [Save Image] (fully dressed model)
   ```

4. **Try Different Outfits**
   - Change `preset_name` to try different styles
   - Model's face and body stay identical
   - Only the outfit changes

---

## 💡 Usage Examples

### Example 1: Corporate Headshots
```
Input: Model in underwear
Preset: "Business Professional"
Target: Qwen Image Edit 2509
Preservation: Maximum
Output: Model in charcoal suit, white shirt, ready for LinkedIn
```

### Example 2: Fashion Portfolio
```
Input: Model in underwear
Preset: "Minimalist Fashion"
Target: Qwen Image Edit 2509
Preservation: Maximum
Output: Model in oversized white tee + black trousers, editorial style
```

### Example 3: Senior Portrait
```
Input: Senior model in underwear
Preset: "Coastal Grandma (55+)"
Target: Qwen Image Edit 2509
Preservation: Maximum
Output: Model in cream linen cardigan + beige pants, relaxed elegance
```

### Example 4: Creative Variation with LLM
```
Preset: "Urban Streetwear"
Mode: "LLM_Enrich"
Target: Qwen Image Edit 2509

Flow: YUTRO → LLM (creates variation) → Qwen (applies outfit)
Output: Unique streetwear interpretation maintaining style/vibe
```

---

## 🎯 Best Practices

### ✅ **DO:**
- ✅ Use **"Maximum" preservation** when dressing models in minimal clothing
- ✅ Use **"Qwen Image Edit 2509"** for best identity preservation
- ✅ Start with a clear, well-lit photo of model in underwear
- ✅ Try multiple presets to build a complete wardrobe portfolio
- ✅ Use "additional_notes" for fine-tuning specific details
- ✅ Use **Direct mode** for speed, **LLM_Enrich** for creativity

### ❌ **DON'T:**
- ❌ Use "Flexible" preservation for casting models (identity will drift)
- ❌ Expect perfect results with low-quality input images
- ❌ Over-complicate "additional_notes" (keep them simple and specific)

---

## 🔧 Advanced Features

### **Model Comparison**

| Model | Strength | Best For | Preservation Quality |
|-------|----------|----------|---------------------|
| **Qwen Image Edit 2509** ⭐ | Superior editing | **Dressing minimal-clothing models** | ⭐⭐⭐⭐⭐ Excellent |
| Nano Banana Pro | Direct instructions | General outfit changes | ⭐⭐⭐⭐ Very Good |
| Seedream 4.5 | Transformations | Style transfers | ⭐⭐⭐ Good |
| Generic | Universal | Any model | ⭐⭐⭐ Good |

### **Preservation Levels Explained**

**For Qwen Image Edit 2509:**
- **Flexible**: "Preserve overall facial features and body proportions while adding outfit"
- **Moderate**: "Preserve face and body shape exactly. Only add the clothing"
- **Strong**: "PRESERVE IDENTITY: Face, body proportions, pose, skin tone. ONLY add outfit items"
- **Maximum**: "CRITICAL CASTING MODE: LOCK ALL BASE FEATURES. Think: same person, just dressed. Zero changes except clothing"

### **LLM_Enrich Mode Workflow**

```
[YUTRO Node]
  • Mode: "LLM_Enrich"
  • Preset: "Smart Casual"
      ↓
  [Generates LLM instruction]
      ↓
[LLM Node] (ComfyUI-LLM, Ollama, etc.)
  • Receives instruction
  • Creates creative outfit variation
  • Maintains style/vibe from preset
      ↓
  [Enriched prompt with creative details]
      ↓
[Qwen Image Edit 2509]
      ↓
[Styled model with unique outfit]
```

---

## 🛠️ Technical Details

### **Architecture**
- **Language**: Python 3.9+
- **Dependencies**: None (pure Python, JSON-based presets)
- **ComfyUI Integration**: Standard custom node structure
- **Preset Storage**: JSON file (`presets/wardrobe_presets_v2.json`)

### **Node Specifications**
- **Category**: `YUTRO/Casting`
- **Display Name**: `YUTRO Wardrobe Preset 👔`
- **Return Type**: `STRING` (prompt text)
- **Output Node**: No (prompt generator)

### **File Structure**
```
YUTRO-Casting-Studio/
├── __init__.py              # Node registration (v2.3)
├── nodes/
│   └── yutro_wardrobe_preset.py  # Main node class
├── presets/
│   └── wardrobe_presets_v2.json  # 30 outfit presets
├── README.md                # This file
├── CHANGELOG.md             # Version history
├── LICENSE                  # MIT License
└── requirements.txt         # Empty (no external deps)
```

---

## 🤝 Use Cases

### **1. Casting Portfolio Generation**
Create complete wardrobe portfolios from a single model photo:
- Corporate headshots (10 variations)
- Casual lifestyle shots (5 variations)
- Evening wear (3 variations)
- Sports/active wear (3 variations)

### **2. Fashion E-commerce**
Generate product mockups with consistent model:
- Same model wearing different outfits
- Consistent body proportions across catalog
- Rapid prototyping of clothing combinations

### **3. Character Design for Games/Film**
Explore wardrobe options for characters:
- Base character in underwear
- Try 30 different outfit styles
- Maintain character identity across all variations

### **4. Virtual Try-On Systems**
Foundation for virtual fitting rooms:
- User's avatar in base clothing
- Apply different outfit presets
- Preserve user's body proportions

---

## 📊 Preset Categories Summary

| Category | Count | Age Range | Examples |
|----------|-------|-----------|----------|
| Casual | 5 | All ages | Smart Casual, Weekend Relaxed, Urban Streetwear |
| Formal/Business | 5 | All ages | Business Professional, Executive Suit |
| Sport/Active | 3 | All ages | Athleisure, Sporty Active, Yoga Casual |
| Evening/Night | 3 | All ages | Evening Elegant, Night Out, Cocktail Ready |
| Fashion/Editorial | 4 | All ages | Minimalist Fashion, Avant-Garde |
| Mature/Casual | 4 | 50-75 | Coastal Grandma, Eclectic Grandpa |
| Mature/Elegant | 3 | 55-80 | Silver Sophistication, Elegant Mature |
| Mature/Active | 2 | 55-80 | Active Senior, Wellness Casual |
| Mature/Evening | 1 | 65-80 | Mature Evening Elegant |

---

## 🔄 Update History

- **v2.3.0** (2024-12-28): Qwen Image Edit 2509 support, optimized for dressing minimal-clothing models
- **v2.2.0** (2024-12-23): Added 10 mature/senior presets (50-80 years)
- **v2.1.0** (2024-12-20): Linear architecture, removed Variation Enhancer step
- **v2.0.0** (2024-12-15): Initial release with 20 presets

---

## 📝 License

MIT License - See [LICENSE](LICENSE) file for details.

---

## 🙏 Credits

**Created by:** YUTRO Casting Studio  
**Version:** 2.3.0  
**Contact:** [Your contact info]

---

## 🐛 Troubleshooting

### **Issue: Presets not loading**
**Solution:** Ensure `presets/wardrobe_presets_v2.json` exists in the node folder.

### **Issue: Identity not preserved**
**Solution:** 
- Use **preservation_strength: "Maximum"**
- Use **target_model: "Qwen Image Edit 2509"**
- Ensure input image is high quality and well-lit

### **Issue: Outfit doesn't match style**
**Solution:** 
- Try adding specific details in "additional_notes"
- Switch to "LLM_Enrich" mode for more creative control
- Verify the preset description matches your expectation

### **Issue: Qwen model not available**
**Solution:** 
- Ensure you have Qwen Image Edit 2509 node installed
- Fall back to "Nano Banana Pro" or "Generic" if Qwen unavailable

---

## 🚀 Roadmap

- [ ] Support for custom preset creation via UI
- [ ] Preset preview images
- [ ] Batch processing for multiple models
- [ ] Advanced color palette controls
- [ ] Integration with additional image editing models
- [ ] Preset tagging and search system

---

**🎬 Ready to transform your casting models? Install YUTRO Casting Studio v2.3 and start dressing!**
