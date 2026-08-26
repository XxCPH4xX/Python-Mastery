import json
import sys

def validate_strings_notebook():
    # Read the Booleans notebook for reference
    with open('H:/Python-Mastery/01_Python_Basics/06_Booleans/notes.ipynb', 'r', encoding='utf-8') as f:
        booleans_nb = json.load(f)

    # Read the Strings notebook
    with open('H:/Python-Mastery/01_Python_Basics/05_Strings/notes.ipynb', 'r', encoding='utf-8') as f:
        strings_nb = json.load(f)

    print("=== VALIDATION RESULTS ===")
    print(f"Booleans notebook cell count: {len(booleans_nb['cells'])}")
    print(f"Strings notebook cell count: {len(strings_nb['cells'])}")
    print()

    # Check metadata
    print("=== METADATA COMPARISON ===")
    booleans_meta = booleans_nb.get('metadata', {})
    strings_meta = strings_nb.get('metadata', {})

    print("Booleans metadata:")
    print(json.dumps(booleans_meta, indent=2))
    print("\nStrings metadata:")
    print(json.dumps(strings_meta, indent=2))
    print()

    # Check specific metadata fields
    kernelspec_match = booleans_meta.get('kernelspec') == strings_meta.get('kernelspec')
    language_info_match = booleans_meta.get('language_info') == strings_meta.get('language_info')
    nbformat_match = booleans_nb.get('nbformat') == strings_nb.get('nbformat')
    nbformat_minor_match = booleans_nb.get('nbformat_minor') == strings_nb.get('nbformat_minor')

    print("=== SPECIFIC CHECKS ===")
    print(f"Kernelspec match: {kernelspec_match}")
    print(f"Language info match: {language_info_match}")
    print(f"Nbformat match: {nbformat_match}")
    print(f"Nbformat minor match: {nbformat_minor_match}")
    print()

    if not kernelspec_match:
        print("Kernelspec differences:")
        print(f"  Booleans: {booleans_meta.get('kernelspec')}")
        print(f"  Strings:  {strings_meta.get('kernelspec')}")

    if not language_info_match:
        print("Language info differences:")
        print(f"  Booleans: {booleans_meta.get('language_info')}")
        print(f"  Strings:  {strings_meta.get('language_info')}")

    print()
    print("=== CELL COUNT CHECK ===")
    target_min = 120
    actual_count = len(strings_nb['cells'])
    print(f"Target minimum cells: {target_min}")
    print(f"Actual cell count: {actual_count}")
    print(f"Meets requirement: {actual_count >= target_min}")

    if actual_count < target_min:
        needed = target_min - actual_count
        print(f"Need {needed} more cells to reach {target_min}")

    print()
    print("=== OVERALL VALIDATION ===")
    metadata_ok = kernelspec_match and language_info_match
    format_ok = nbformat_match and nbformat_minor_match
    count_ok = actual_count >= target_min

    print(f"Metadata correct: {metadata_ok}")
    print(f"Format correct: {format_ok}")
    print(f"Cell count sufficient: {count_ok}")
    print(f"Overall validation: {metadata_ok and format_ok and count_ok}")

    return metadata_ok and format_ok and count_ok

if __name__ == "__main__":
    success = validate_strings_notebook()
    sys.exit(0 if success else 1)