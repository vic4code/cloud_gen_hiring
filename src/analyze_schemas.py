import json
import os
from typing import Dict, Any, List
from collections import defaultdict
from pathlib import Path

def analyze_schema(data: Any, path: str = "") -> Dict[str, Any]:
    """Recursively analyze schema structure"""
    if isinstance(data, dict):
        return {
            "type": "object",
            "properties": {
                k: analyze_schema(v, f"{path}.{k}" if path else k)
                for k, v in data.items()
            }
        }
    elif isinstance(data, list):
        if data:
            # For arrays, collect all possible item schemas
            item_schemas = [analyze_schema(item, path) for item in data]
            # If all items have the same schema, use that
            if len(set(str(s) for s in item_schemas)) == 1:
                return {
                    "type": "array",
                    "items": item_schemas[0]
                }
            # Otherwise, include all possible schemas
            return {
                "type": "array",
                "items": {
                    "oneOf": item_schemas
                }
            }
        return {"type": "array", "items": {"type": "any"}}
    else:
        return {
            "type": type(data).__name__,
            "example": str(data)
        }

def get_all_sample_files(resume_type: str) -> List[str]:
    """Get all sample files for a given resume type"""
    resume_dir = Path("data/resume")
    return [str(f) for f in resume_dir.glob(f"{resume_type}_sample*.json")]

def main():
    # Define resume types and their sample files
    resume_types = {
        "ds": get_all_sample_files("ds"),
        "mle": get_all_sample_files("mle"),
        "pm": get_all_sample_files("pm")
    }
    
    schemas = {}
    for resume_type, file_paths in resume_types.items():
        schemas[resume_type] = {
            "samples": [],
            "common_schema": None
        }
        
        # Analyze each sample file
        for file_path in file_paths:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                sample_schema = analyze_schema(data)
                schemas[resume_type]["samples"].append({
                    "file": os.path.basename(file_path),
                    "schema": sample_schema
                })
        
        # Generate common schema by merging all sample schemas
        if schemas[resume_type]["samples"]:
            schemas[resume_type]["common_schema"] = merge_schemas(
                [s["schema"] for s in schemas[resume_type]["samples"]]
            )
    
    # Create output directory
    output_dir = Path("data/schemas")
    output_dir.mkdir(exist_ok=True)
    
    # Save complete schema file
    with open(output_dir / "resume_schemas.json", 'w', encoding='utf-8') as f:
        json.dump(schemas, f, ensure_ascii=False, indent=2)
    
    # Generate Markdown documentation
    with open(output_dir / "resume_schemas.md", 'w', encoding='utf-8') as f:
        f.write("# Resume Schema Documentation\n\n")
        
        for resume_type, schema_data in schemas.items():
            f.write(f"## {resume_type.upper()} Resume Schemas\n\n")
            
            # Write common schema
            f.write("### Common Schema\n\n")
            f.write("This schema represents the common structure across all samples:\n\n")
            f.write("```json\n")
            f.write(json.dumps(schema_data["common_schema"], ensure_ascii=False, indent=2))
            f.write("\n```\n\n")
            
            # Write individual sample schemas
            f.write("### Sample-specific Schemas\n\n")
            for sample in schema_data["samples"]:
                f.write(f"#### {sample['file']}\n\n")
                f.write("```json\n")
                f.write(json.dumps(sample["schema"], ensure_ascii=False, indent=2))
                f.write("\n```\n\n")
            
            # Add field descriptions
            f.write("### Field Descriptions\n\n")
            f.write("| Field Path | Type | Description |\n")
            f.write("|------------|------|-------------|\n")
            
            def add_field_descriptions(schema: Dict, path: str = ""):
                if not isinstance(schema, dict):
                    return
                if "oneOf" in schema:
                    for sub_schema in schema["oneOf"]:
                        add_field_descriptions(sub_schema, path)
                    return
                if schema.get("type") == "object":
                    for field, field_schema in schema["properties"].items():
                        new_path = f"{path}.{field}" if path else field
                        add_field_descriptions(field_schema, new_path)
                elif schema.get("type") == "array":
                    add_field_descriptions(schema.get("items", {}), path + "[]")
                else:
                    f.write(f"| {path} | {schema.get('type', 'unknown')} | {schema.get('example', '')} |\n")
            
            add_field_descriptions(schema_data["common_schema"])
            f.write("\n")

def merge_schemas(schemas: List[Dict]) -> Dict:
    """Merge multiple schemas into a common schema"""
    if not schemas:
        return {}
    
    if len(schemas) == 1:
        return schemas[0]
    
    # For objects, merge properties
    if all(s["type"] == "object" for s in schemas):
        all_properties = set()
        for schema in schemas:
            all_properties.update(schema["properties"].keys())
        
        merged_properties = {}
        for prop in all_properties:
            prop_schemas = [
                s["properties"][prop]
                for s in schemas
                if prop in s["properties"]
            ]
            if prop_schemas:
                merged_properties[prop] = merge_schemas(prop_schemas)
        
        return {
            "type": "object",
            "properties": merged_properties
        }
    
    # For arrays, merge item schemas
    if all(s["type"] == "array" for s in schemas):
        item_schemas = []
        for schema in schemas:
            if "items" in schema:
                if isinstance(schema["items"], dict) and "oneOf" in schema["items"]:
                    item_schemas.extend(schema["items"]["oneOf"])
                else:
                    item_schemas.append(schema["items"])
        
        if item_schemas:
            return {
                "type": "array",
                "items": merge_schemas(item_schemas)
            }
        return {"type": "array", "items": {"type": "any"}}
    
    # For other types, include all possible types
    return {
        "oneOf": schemas
    }

if __name__ == "__main__":
    main() 