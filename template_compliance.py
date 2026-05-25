"""template_compliance.py — Verify project files match template structure.

Checks that all mandatory project files exist and follow the template
structure defined in prompts/templates/. Does NOT check content quality —
only structural compliance.
"""
import os
import re
from pathlib import Path

PROJECT_ROOT = Path.cwd()
TEMPLATE_DIR = Path(r'G:\My Drive\prompts\templates')

REQUIRED_FILES = {
    'PROJECT-CHARTER.md': ['Scope', 'Success Criteria', 'Constraints', 'Dependencies', 'Deliverables'],
    'SPRINT-BACKLOG.md': ['Sprint Goal', 'Active Tasks', 'Blocked', 'Sprint Health'],
    'PRODUCT-BACKLOG.md': ['Priority Legend', 'Backlog', 'Completed'],
    'CHANGELOG.md': ['Added', 'Changed', 'Removed', 'Fixed'],
    'RISK-REGISTER.md': ['Active Risks', 'Pre-Populated Known Risks'],
    'DEFINITION-OF-DONE.md': ['CODE TASK', 'DOCUMENT TASK', 'PUBLICATION TASK', 'ANALYSIS TASK'],
    'README.md': ['Dependencies', 'Architecture', 'Usage', 'Key Files'],
}

OPTIONAL_FILES = {
    'docs/adr/README.md': ['ADR Index'],
    '.gitignore': ['__pycache__'],
}

def check_file(filepath, required_sections):
    """Check if a file exists and contains required sections."""
    full_path = PROJECT_ROOT / filepath
    
    if not full_path.exists():
        return False, f'MISSING: {filepath}'
    
    try:
        with open(full_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return False, f'UNREADABLE: {filepath}'
    
    missing_sections = []
    for section in required_sections:
        if section.lower() not in content.lower():
            missing_sections.append(section)
    
    if missing_sections:
        return False, f'MISSING SECTIONS in {filepath}: {", ".join(missing_sections)}'
    
    return True, f'OK: {filepath}'


def check_all():
    """Run full compliance check."""
    print('# Template Compliance Report')
    print(f'**Project:** {PROJECT_ROOT.name}')
    print(f'**Path:** {PROJECT_ROOT}')
    print()

    all_pass = True
    results = []

    # Check required files
    print('## Required Files')
    for filepath, sections in REQUIRED_FILES.items():
        passed, msg = check_file(filepath, sections)
        results.append((passed, msg))
        icon = '[OK]' if passed else '[FAIL]'
        print(f'- {icon} {msg}')
        if not passed:
            all_pass = False

    # Check optional files
    print()
    print('## Optional Files')
    for filepath, sections in OPTIONAL_FILES.items():
        passed, msg = check_file(filepath, sections)
        results.append((passed, msg))
        icon = '[OK]' if passed else '[MISSING]'
        print(f'- {icon} {msg}')

    # Summary
    print()
    passed_count = sum(1 for p, _ in results if p)
    total_count = len(results)
    print(f'## Summary: {passed_count}/{total_count} checks passed')
    
    if all_pass:
        print('**All required checks passed.** Template compliance verified.')
    else:
        print('**Compliance failures detected.** See [FAIL] items above.')
        print()
        print('To fix: fill the corresponding template from `prompts/templates/`.')

    return all_pass


if __name__ == '__main__':
    ok = check_all()
    exit(0 if ok else 1)
