"""
YUTRO Wardrobe Preset Node v2.1 - Linear Architecture
Professional wardrobe prompt generator for AI casting models.

Architecture:
- Direct Mode: YUTRO → NANO (complete prompt)
- LLM_Enrich Mode: YUTRO → LLM → NANO (instruction for LLM enrichment)

Author: YUTRO Casting Studio
Version: 2.1.0
License: MIT
"""

import json
import os
from pathlib import Path


class YUTROWardrobePreset:
    """
    Professional wardrobe preset node for casting model workflows.
    
    Features:
    - 20 professional outfit presets across 5 categories
    - 4-level body preservation system (Flexible → Maximum)
    - 2 generation modes:
      * Direct: Complete prompt for image models
      * LLM_Enrich: Instruction for LLM to enrich
    - Multi-model optimization (Nano Banana Pro, Seedream 4.5, Generic)
    - Gender fit adjustment
    """
    
    def __init__(self):
        """Initialize and load presets from JSON."""
        self.presets = self._load_presets()
    
    def _load_presets(self):
        """Load wardrobe presets from JSON file."""
        try:
            preset_path = Path(__file__).parent.parent / "presets" / "wardrobe_presets_v2.json"
            
            if not preset_path.exists():
                print(f"⚠️ Preset file not found: {preset_path}")
                return self._get_fallback_presets()
            
            with open(preset_path, 'r', encoding='utf-8') as f:
                presets = json.load(f)
            
            print(f"✅ Loaded {len(presets)} wardrobe presets")
            return presets
        
        except Exception as e:
            print(f"❌ Error loading presets: {e}")
            return self._get_fallback_presets()
    
    def _get_fallback_presets(self):
        """Fallback presets if JSON fails to load."""
        return {
            "Smart Casual": {
                "name": "Smart Casual",
                "outfit": "white dress shirt, navy chinos, brown loafers",
                "style": "smart casual",
                "vibe": "professional yet relaxed",
                "category": "Casual"
            }
        }
    
    @classmethod
    def INPUT_TYPES(cls):
        """Define node inputs."""
        # Load preset names for dropdown
        temp_instance = cls()
        preset_names = sorted(temp_instance.presets.keys())
        
        return {
            "required": {
                "preset_name": (
                    preset_names,
                    {
                        "default": preset_names[0] if preset_names else "Smart Casual",
                        "tooltip": "Select a professional outfit preset from 20 curated styles"
                    }
                ),
                "preservation_strength": (
                    ["Flexible", "Moderate", "Strong", "Maximum"],
                    {
                        "default": "Strong",
                        "tooltip": (
                            "Body/face preservation level:\n"
                            "• Flexible: Similar proportions (creative freedom)\n"
                            "• Moderate: Exact proportions (balanced)\n"
                            "• Strong: CRITICAL preservation (RECOMMENDED for casting)\n"
                            "• Maximum: LOCKED identity (maximum accuracy)"
                        )
                    }
                ),
                "variation_mode": (
                    ["Direct", "LLM_Enrich"],
                    {
                        "default": "Direct",
                        "tooltip": (
                            "Generation mode:\n"
                            "• Direct: Generates complete prompt ready for image model (no LLM needed)\n"
                            "• LLM_Enrich: Generates instruction for LLM to create enriched prompt (connect LLM node)"
                        )
                    }
                ),
                "target_model": (
                    ["Nano Banana Pro", "Seedream 4.5", "Generic"],
                    {
                        "default": "Nano Banana Pro",
                        "tooltip": (
                            "Target image generation model:\n"
                            "• Nano Banana Pro: Optimized for direct instruction format\n"
                            "• Seedream 4.5: Optimized for transformation format\n"
                            "• Generic: Universal format for any model"
                        )
                    }
                ),
                "gender_fit": (
                    ["Auto", "Male", "Female", "Unisex"],
                    {
                        "default": "Auto",
                        "tooltip": "Adjust outfit description for specific gender fit (Auto detects from preset)"
                    }
                ),
            },
            "optional": {
                "additional_notes": (
                    "STRING",
                    {
                        "default": "",
                        "multiline": True,
                        "placeholder": "Example: 'add leather belt', 'oversized fit', 'pastel colors', 'Nike brand'",
                        "tooltip": "Add custom details: accessories, fit adjustments, colors, brands, specific items"
                    }
                ),
            }
        }
    
    RETURN_TYPES = ("STRING",)
    RETURN_NAMES = ("prompt",)
    FUNCTION = "generate_prompt"
    CATEGORY = "YUTRO/Casting"
    
    OUTPUT_NODE = False
    
    def generate_prompt(
        self,
        preset_name,
        preservation_strength,
        variation_mode,
        target_model,
        gender_fit,
        additional_notes=""
    ):
        """
        Generate wardrobe prompt based on mode.
        
        Args:
            preset_name: Selected preset name
            preservation_strength: Body preservation level
            variation_mode: "Direct" or "LLM_Enrich"
            target_model: Target image model
            gender_fit: Gender adjustment
            additional_notes: Custom notes
        
        Returns:
            tuple: (prompt_string,)
        """
        
        # 1. Load preset data
        preset_data = self.presets.get(preset_name)
        if not preset_data:
            error_msg = f"❌ Preset '{preset_name}' not found"
            print(error_msg)
            return (error_msg,)
        
        # 2. Generate prompt based on mode
        if variation_mode == "Direct":
            prompt = self._build_direct_prompt(
                preset_data=preset_data,
                preservation=preservation_strength,
                target_model=target_model,
                gender_fit=gender_fit,
                additional_notes=additional_notes
            )
            print(f"✅ Direct prompt generated for: {preset_name}")
        
        elif variation_mode == "LLM_Enrich":
            prompt = self._build_llm_instruction(
                preset_data=preset_data,
                preservation=preservation_strength,
                target_model=target_model,
                gender_fit=gender_fit,
                additional_notes=additional_notes
            )
            print(f"✅ LLM instruction generated for: {preset_name}")
        
        else:
            error_msg = f"❌ Unknown variation_mode: {variation_mode}"
            print(error_msg)
            return (error_msg,)
        
        return (prompt,)
    
    def _build_direct_prompt(
        self,
        preset_data,
        preservation,
        target_model,
        gender_fit,
        additional_notes
    ):
        """
        Build complete prompt ready for image model (Direct mode).
        
        Returns:
            str: Complete optimized prompt
        """
        
        outfit = preset_data["outfit"]
        style = preset_data["style"]
        vibe = preset_data["vibe"]
        
        # Adjust for gender if specified
        if gender_fit != "Auto":
            outfit = self._adjust_gender(outfit, gender_fit)
        
        # Build base prompt optimized for target model
        if target_model == "Nano Banana Pro":
            base = f"Dress this person in {outfit}, {style} style, {vibe} vibe"
        
        elif target_model == "Seedream 4.5":
            base = f"Transform this person's outfit to: {outfit}, {style} style, {vibe} vibe. Maintain original pose and setting"
        
        else:  # Generic
            base = f"Change outfit to: {outfit}, {style} style, {vibe} vibe"
        
        # Add additional notes if provided
        if additional_notes.strip():
            base += f", {additional_notes.strip()}"
        
        # Add preservation instruction
        preservation_text = self._get_preservation_text(preservation)
        final_prompt = f"{base}. {preservation_text}"
        
        return final_prompt
    
    def _build_llm_instruction(
        self,
        preset_data,
        preservation,
        target_model,
        gender_fit,
        additional_notes
    ):
        """
        Build instruction for LLM to generate enriched prompt (LLM_Enrich mode).
        
        Returns:
            str: Detailed instruction for LLM
        """
        
        base_category = preset_data["name"]
        base_outfit = preset_data["outfit"]
        style = preset_data["style"]
        vibe = preset_data["vibe"]
        category = preset_data.get("category", "General")
        occasions = preset_data.get("occasions", [])
        
        preservation_text = self._get_preservation_text(preservation)
        
        # Build comprehensive instruction for LLM
        instruction = f"""You are a professional fashion stylist creating detailed outfit prompts for AI image generation in casting photoshoots.

TASK: Generate a creative and detailed outfit prompt for the style category "{base_category}".

BASE REFERENCE (use as inspiration, NOT exact copy):
- Category: {base_category} ({category})
- Base outfit: {base_outfit}
- Style: {style}
- Vibe: {vibe}
- Typical occasions: {', '.join(occasions) if occasions else 'versatile'}

REQUIREMENTS:
1. Create a CREATIVE VARIATION of this outfit (do NOT copy the base outfit exactly)
2. Vary: colors, textures, fabrics, materials, accessories, brands, specific details
3. MUST maintain the "{style}" style and "{vibe}" vibe
4. Gender fit: {gender_fit}
5. Target image generation model: {target_model}

OUTFIT DESCRIPTION MUST INCLUDE:
- Top garment (specific color, fabric type, texture, design details, fit)
- Bottom garment (specific color, material, cut, style details)
- Footwear (style, color, material, brand if relevant)
- Accessories (watch, belt, jewelry, bags, hats - be specific)
- Fabric details (cotton, wool, linen, leather, etc.)
- Style details (buttons, stitching, fit type, brand references)

OUTPUT FORMAT:
Generate a complete prompt ready for {target_model} following this EXACT structure:
"{self._get_model_prefix(target_model)}[detailed outfit description], {style} style, {vibe} vibe. {preservation_text}"

CRITICAL RULES:
- Output ONLY the final prompt text (no explanations, no markdown, no preamble)
- Start directly with "{self._get_model_prefix(target_model)}"
- Be highly specific with colors, materials, and details
- Ensure coherent color palette and style consistency
- Make it sound natural and professional

{f"ADDITIONAL USER NOTES TO INTEGRATE: {additional_notes.strip()}" if additional_notes.strip() else ""}

Generate the prompt now:"""

        return instruction
    
    def _get_model_prefix(self, target_model):
        """Get the appropriate prefix for each target model."""
        if target_model == "Nano Banana Pro":
            return "Dress this person in "
        elif target_model == "Seedream 4.5":
            return "Transform this person's outfit to: "
        else:
            return "Change outfit to: "
    
    def _get_preservation_text(self, preservation_level):
        """
        Get preservation instruction text based on level.
        
        Args:
            preservation_level: "Flexible", "Moderate", "Strong", or "Maximum"
        
        Returns:
            str: Preservation instruction
        """
        
        preservation_map = {
            "Flexible": "Keep similar body proportions and facial features",
            
            "Moderate": "Keep exact body proportions and facial features",
            
            "Strong": (
                "PRESERVE: exact body shape, muscle definition, body proportions, "
                "facial features, skin tone. This is a casting model showcase - "
                "identity accuracy is CRITICAL"
            ),
            
            "Maximum": (
                "CRITICAL PRESERVATION MODE: LOCKED identity. "
                "Preserve ALL physical characteristics: "
                "exact body shape, muscle mass, fat distribution, bone structure, "
                "body proportions, facial features (eyes, nose, mouth, jawline), "
                "skin tone and texture, body hair patterns. "
                "ONLY change the clothing. Everything else MUST remain IDENTICAL"
            )
        }
        
        return preservation_map.get(preservation_level, preservation_map["Strong"])
    
    def _adjust_gender(self, outfit, gender_fit):
        """
        Adjust outfit description for specific gender fit.
        
        Args:
            outfit: Original outfit description
            gender_fit: "Male", "Female", or "Unisex"
        
        Returns:
            str: Adjusted outfit description
        """
        
        # Simple gender-neutral adjustment
        # In production, this could be more sophisticated
        
        if gender_fit == "Unisex":
            # Ensure neutral terminology
            outfit = outfit.replace("dress shirt", "button-up shirt")
        
        # For Male/Female, keep as is for now
        # Future enhancement: more specific adjustments
        
        return outfit


# Node registration
NODE_CLASS_MAPPINGS = {
    "YUTROWardrobePreset": YUTROWardrobePreset
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "YUTROWardrobePreset": "YUTRO Wardrobe Preset 👔"
}
