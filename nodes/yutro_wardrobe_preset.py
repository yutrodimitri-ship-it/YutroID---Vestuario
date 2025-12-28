"""
YUTRO Wardrobe Preset Node v2.3 - Linear Architecture with Qwen Support
Professional wardrobe prompt generator for AI casting models.

Architecture:
- Direct Mode: YUTRO → Image Model (complete prompt)
- LLM_Enrich Mode: YUTRO → LLM → Image Model (instruction for LLM enrichment)

NEW in v2.3:
- Qwen Image Edit 2509 support optimized for dressing models in minimal clothing
- Enhanced preservation system for "dress-the-mannequin" workflow

Author: YUTRO Casting Studio
Version: 2.3.0
License: MIT
"""

import json
import os
from pathlib import Path


class YUTROWardrobePreset:
    """
    Professional wardrobe preset node for casting model workflows.
    
    Features:
    - 30 professional outfit presets across 8 categories (20 general + 10 mature)
    - 4-level body preservation system (Flexible → Maximum)
    - 2 generation modes:
      * Direct: Complete prompt for image models
      * LLM_Enrich: Instruction for LLM to enrich
    - Multi-model optimization:
      * Nano Banana Pro: Direct instruction format
      * Seedream 4.5: Transformation format
      * Qwen Image Edit 2509: Optimized for dressing minimal-clothing models
      * Generic: Universal format
    - Gender fit adjustment
    
    Primary Use Case:
    Take a model/character in minimal clothing (underwear) and dress them
    in professional outfits while preserving 100% of their facial features
    and body proportions.
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
                        "tooltip": "Select a professional outfit preset from 30 curated styles (20 general + 10 mature)"
                    }
                ),
                "preservation_strength": (
                    ["Flexible", "Moderate", "Strong", "Maximum"],
                    {
                        "default": "Maximum",
                        "tooltip": (
                            "Body/face preservation level:\n"
                            "• Flexible: Similar proportions (creative freedom)\n"
                            "• Moderate: Exact proportions (balanced)\n"
                            "• Strong: CRITICAL preservation (recommended for casting)\n"
                            "• Maximum: LOCKED identity (use this for dressing models in minimal clothing)"
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
                    ["Nano Banana Pro", "Seedream 4.5", "Qwen Image Edit 2509", "Generic"],
                    {
                        "default": "Qwen Image Edit 2509",
                        "tooltip": (
                            "Target image generation model:\n"
                            "• Nano Banana Pro: Optimized for direct instruction format\n"
                            "• Seedream 4.5: Optimized for transformation format\n"
                            "• Qwen Image Edit 2509: BEST for adding clothing to minimal-dress models (preserves face/body)\n"
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
            print(f"✅ Direct prompt generated for: {preset_name} ({target_model})")
        
        elif variation_mode == "LLM_Enrich":
            prompt = self._build_llm_instruction(
                preset_data=preset_data,
                preservation=preservation_strength,
                target_model=target_model,
                gender_fit=gender_fit,
                additional_notes=additional_notes
            )
            print(f"✅ LLM instruction generated for: {preset_name} ({target_model})")
        
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
        
        elif target_model == "Qwen Image Edit 2509":
            # Optimized for dressing models in minimal clothing (underwear)
            base = f"Add these clothes to this person: {outfit}. Style: {style}, Vibe: {vibe}. The person is currently in minimal clothing. Dress them while keeping their face, body shape, proportions, pose and background completely unchanged"
        
        else:  # Generic
            base = f"Change outfit to: {outfit}, {style} style, {vibe} vibe"
        
        # Add additional notes if provided
        if additional_notes.strip():
            base += f", {additional_notes.strip()}"
        
        # Add preservation instruction (model-specific)
        preservation_text = self._get_preservation_text(preservation, target_model)
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
        
        preservation_text = self._get_preservation_text(preservation, target_model)
        
        # Build comprehensive instruction for LLM
        instruction = f"""You are a professional fashion stylist creating detailed outfit prompts for AI image generation in casting photoshoots.

CONTEXT: The input image shows a model/character in minimal clothing (underwear). Your task is to generate a prompt that will DRESS this person in a complete outfit.

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

CRITICAL RULES FOR CASTING MODELS:
- The input image has a person in MINIMAL CLOTHING (underwear/undergarments)
- Your prompt will ADD CLOTHING to this base model
- PRESERVATION is CRITICAL: face, body proportions, pose must stay identical
- Think of this as "dressing a mannequin" - only clothes change
- Output ONLY the final prompt text (no explanations, no markdown, no preamble)
- Start directly with "{self._get_model_prefix(target_model)}"
- Be highly specific with colors, materials, and details
- Ensure coherent color palette and style consistency

{f"ADDITIONAL USER NOTES TO INTEGRATE: {additional_notes.strip()}" if additional_notes.strip() else ""}

Generate the prompt now:"""

        return instruction
    
    def _get_model_prefix(self, target_model):
        """Get the appropriate prefix for each target model."""
        if target_model == "Nano Banana Pro":
            return "Dress this person in "
        elif target_model == "Seedream 4.5":
            return "Transform this person's outfit to: "
        elif target_model == "Qwen Image Edit 2509":
            return "Add these clothes to this person: "
        else:
            return "Change outfit to: "
    
    def _get_preservation_text(self, preservation_level, target_model="Generic"):
        """
        Get preservation instruction text based on level and target model.
        
        Args:
            preservation_level: "Flexible", "Moderate", "Strong", or "Maximum"
            target_model: Target image generation model
        
        Returns:
            str: Preservation instruction optimized for model
        """
        
        # Qwen Image Edit 2509: Optimized for dressing models in minimal clothing
        if target_model == "Qwen Image Edit 2509":
            preservation_map = {
                "Flexible": "Preserve overall facial features and body proportions while adding outfit",
                
                "Moderate": "Preserve face and body shape exactly. Only add the clothing",
                
                "Strong": (
                    "PRESERVE IDENTITY: Face (eyes, nose, mouth, expression), "
                    "body proportions (height, build, muscle tone), pose, skin tone. "
                    "ONLY add the outfit items. This is like dressing a mannequin - "
                    "the base person stays identical"
                ),
                
                "Maximum": (
                    "CRITICAL CASTING MODE: The model is in minimal clothing (underwear). "
                    "Your task is to ADD ONLY the specified outfit. "
                    "LOCK ALL BASE FEATURES: facial features (every detail), "
                    "body shape (proportions, muscle definition, posture), "
                    "skin characteristics, background, lighting, camera angle. "
                    "Think: same person, just dressed. Zero changes except clothing"
                )
            }
        
        # Other models: Standard preservation system
        else:
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
