#!/usr/bin/env python3
"""
validate_spec_registry.py - Structural drift guard for TCP/AI spec registry.
Uses standard library only.
"""

import json
import sys
import argparse
from pathlib import Path

def validate_spec(spec_path):
    print(f"Checking spec registry: {spec_path}")
    
    try:
        with open(spec_path, 'r', encoding='utf-8') as f:
            spec = json.load(f)
    except Exception as e:
        print(f"Error: Failed to parse JSON: {e}")
        return False

    errors = []

    # 1. Required top-level keys
    required_keys = ["version", "markers", "categories", "corpus_schema", "syntax_notes"]
    for key in required_keys:
        if key not in spec:
            errors.append(f"Missing top-level key: '{key}'")

    if errors:
        for err in errors:
            print(f"  [ERROR] {err}")
        return False

    # 2. Type validation
    if not isinstance(spec["version"], str):
        errors.append("Key 'version' must be a string.")
    
    if not isinstance(spec["markers"], dict) or not spec["markers"]:
        errors.append("Key 'markers' must be a non-empty object.")
    
    if not isinstance(spec["categories"], dict) or not spec["categories"]:
        errors.append("Key 'categories' must be a non-empty object.")
    
    if not isinstance(spec["corpus_schema"], dict):
        errors.append("Key 'corpus_schema' must be an object.")
    else:
        req_fields = spec["corpus_schema"].get("required_fields")
        if not isinstance(req_fields, list) or not req_fields:
            errors.append("Key 'corpus_schema.required_fields' must be a non-empty array.")
        
        opt_fields = spec["corpus_schema"].get("optional_fields")
        if opt_fields is not None and not isinstance(opt_fields, list):
            errors.append("Key 'corpus_schema.optional_fields' must be an array.")

    # 3. Marker validation
    valid_marker_types = {"modality", "response_shape", "register"}
    if isinstance(spec.get("markers"), dict):
        for marker, info in spec["markers"].items():
            if not isinstance(info, dict):
                errors.append(f"Marker '{marker}' info must be an object.")
                continue
            
            m_type = info.get("type")
            if m_type not in valid_marker_types:
                errors.append(f"Marker '{marker}' has invalid type: '{m_type}'. Expected one of {valid_marker_types}")
            
            if not info.get("meaning"):
                errors.append(f"Marker '{marker}' is missing a 'meaning' string.")

    # 4. Category validation
    if isinstance(spec.get("categories"), dict):
        for cat, info in spec["categories"].items():
            if not isinstance(info, dict):
                errors.append(f"Category '{cat}' info must be an object.")
                continue
            
            if not info.get("description"):
                errors.append(f"Category '{cat}' is missing a 'description' string.")

    # 5. Syntax notes validation
    if isinstance(spec.get("syntax_notes"), dict):
        if "parentheses" not in spec["syntax_notes"]:
            errors.append("Missing 'syntax_notes.parentheses' entry.")

    if errors:
        print(f"Validation failed with {len(errors)} errors:")
        for err in errors:
            print(f"  [ERROR] {err}")
        return False

    print("PASS: Spec registry structure is valid.")
    return True

def main():
    parser = argparse.ArgumentParser(description="Validate TCP/AI spec registry structure.")
    parser.add_index = True # Placeholder for future expansion
    parser.add_argument("--spec", type=str, default="spec/tcpai-v0.3.json", help="Path to spec JSON.")
    args = parser.parse_args()

    success = validate_spec(args.spec)
    if not success:
        sys.exit(1)
    sys.exit(0)

if __name__ == "__main__":
    main()
