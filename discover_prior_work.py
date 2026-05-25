"""discover_prior_work.py — Automated Archive/Release/CPL Discovery

Scans the project ecosystem for prior work relevant to a new project.
Called at project initialization per DEFAULT.md §0.1.4.

Usage: python discover_prior_work.py "<project-name>" "<keyword1> <keyword2> ..."
Output: Prior Work Report to stdout (markdown format)
"""
import os
import sys
import re
from pathlib import Path

# Root paths
ARCHIVE_ROOT = Path(r'G:\My Drive\Archive\projects')
RELEASES_ROOT = Path(r'G:\My Drive\Obsidian\releases')
CPL_PATH = Path(r'G:\My Drive\projects\_shared\CROSS-PROJECT-LEARNINGS.md')

def search_archive(keywords, project_name):
    """Search Archive for projects matching keywords."""
    results = []
    if not ARCHIVE_ROOT.exists():
        return results

    for root, dirs, files in os.walk(ARCHIVE_ROOT):
        # Skip deep nesting beyond reasonable depth
        if root.count(os.sep) - str(ARCHIVE_ROOT).count(os.sep) > 5:
            continue

        # Check if this directory looks like a project (has README.md)
        if 'README.md' in files:
            dir_name = os.path.basename(root)
            # Search directory name and README for keywords
            readme_path = os.path.join(root, 'README.md')
            try:
                with open(readme_path, 'r', encoding='utf-8', errors='ignore') as f:
                    readme_content = f.read(2000)  # First 2000 chars
            except:
                readme_content = ''

            score = 0
            search_text = (dir_name + ' ' + readme_content).lower()
            for kw in keywords:
                if kw.lower() in search_text:
                    score += 1

            if score > 0:
                # Check for LEARNINGS.md
                learnings_path = os.path.join(root, 'LEARNINGS.md')
                has_learnings = os.path.exists(learnings_path)

                results.append({
                    'path': str(Path(root).relative_to(ARCHIVE_ROOT.parent.parent)),
                    'name': dir_name,
                    'score': score,
                    'has_learnings': has_learnings,
                    'readme_excerpt': readme_content[:300].strip()
                })

    # Sort by score descending
    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:10]  # Top 10


def search_releases(keywords):
    """Search releases for matching publications."""
    results = []
    if not RELEASES_ROOT.exists():
        return results

    for root, dirs, files in os.walk(RELEASES_ROOT):
        for file in files:
            if file.endswith('.md'):
                filepath = os.path.join(root, file)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(3000)
                except:
                    continue

                score = 0
                search_text = (file + ' ' + content).lower()
                for kw in keywords:
                    if kw.lower() in search_text:
                        score += 1

                if score > 0:
                    # Extract YAML frontmatter if present
                    title = file.replace('.md', '')
                    doi = ''
                    author = ''
                    if content.startswith('---'):
                        fm_end = content.find('---', 3)
                        if fm_end > 0:
                            fm = content[3:fm_end]
                            for line in fm.split('\n'):
                                if line.startswith('title:'):
                                    title = line.replace('title:', '').strip().strip('"').strip("'")
                                if line.startswith('DOI:') or line.startswith('doi:'):
                                    doi = line.split(':', 1)[1].strip()
                                if line.startswith('author:'):
                                    author = line.replace('author:', '').strip()

                    results.append({
                        'file': file,
                        'path': str(Path(filepath).relative_to(RELEASES_ROOT)),
                        'title': title,
                        'doi': doi,
                        'author': author,
                        'score': score
                    })

    results.sort(key=lambda x: x['score'], reverse=True)
    return results[:10]


def search_cpl(keywords):
    """Search CPL for applicable lessons from matching projects."""
    results = []
    if not CPL_PATH.exists():
        return results

    try:
        with open(CPL_PATH, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return results

    # Parse CPL by lesson blocks
    lessons = re.split(r'\n### L\d+:', content)
    
    for i, block in enumerate(lessons):
        if i == 0:  # Skip preamble
            continue
        
        lesson_num = i  # L1 corresponds to lessons[1]
        
        # Extract source project
        source_match = re.search(r'\*\*Source:\*\*\s*(.+?)(?:\n|$)', block)
        source = source_match.group(1).strip() if source_match else 'Unknown'
        
        # Check if any keywords match the lesson content
        score = 0
        search_text = (source + ' ' + block[:500]).lower()
        for kw in keywords:
            if kw.lower() in search_text:
                score += 1
        
        if score > 0:
            # Extract the lesson title (first line after header)
            lines = block.strip().split('\n')
            title = lines[0].strip() if lines else ''
            
            # Extract cross-project flag
            cp_match = re.search(r'\*\*Cross-Project:\*\*\s*(YES|NO|POTENTIALLY)', block)
            cross_project = cp_match.group(1) if cp_match else 'NO'
            
            results.append({
                'lesson': f'L{lesson_num}',
                'source': source,
                'title': title[:100],
                'cross_project': cross_project,
                'score': score
            })
    
    results.sort(key=lambda x: x['score'], reverse=True)
    return [r for r in results if r['cross_project'] == 'YES'][:15]


def generate_report(keywords, project_name):
    """Generate a comprehensive Prior Work Report."""
    print('# Prior Work Discovery Report')
    print(f'**Project:** {project_name}')
    print(f'**Keywords:** {", ".join(keywords)}')
    print(f'**Generated:** {__import__("datetime").datetime.now().isoformat()}')
    print()

    # Archive search
    print('## 1. Archive Projects (Prior Work)')
    print()
    archive_results = search_archive(keywords, project_name)
    if archive_results:
        for i, r in enumerate(archive_results, 1):
            print(f'### {i}. {r["name"]} (score: {r["score"]})')
            print(f'**Path:** `{r["path"]}`')
            print(f'**Has LEARNINGS.md:** {"Yes" if r["has_learnings"] else "No"}')
            if r['readme_excerpt']:
                print(f'**Excerpt:** {r["readme_excerpt"][:200]}...')
            print()
    else:
        print('**No matching Archive projects found.**')
        print('Search locations:')
        print(f'- `{ARCHIVE_ROOT}`')
        print()

    # Release search
    print('## 2. Published Releases (Prior Publications)')
    print()
    release_results = search_releases(keywords)
    if release_results:
        for i, r in enumerate(release_results, 1):
            print(f'### {i}. {r["title"]} (score: {r["score"]})')
            print(f'**File:** `{r["file"]}`')
            if r['doi']:
                print(f'**DOI:** {r["doi"]}')
            if r['author']:
                print(f'**Author:** {r["author"]}')
            print()
    else:
        print('**No matching releases found.**')
        print(f'Search location: `{RELEASES_ROOT}`')
        print()

    # CPL cross-reference
    print('## 3. Cross-Project Lessons (Applicable CPL)')
    print()
    cpl_results = search_cpl(keywords)
    if cpl_results:
        for i, r in enumerate(cpl_results, 1):
            print(f'### {i}. {r["lesson"]}: {r["title"]}')
            print(f'**Source Project:** {r["source"]}')
            print(f'**Cross-Project:** {r["cross_project"]}')
            print(f'**Recommendation:** Review this lesson before starting. Add to RISK-REGISTER.md if applicable.')
            print()
    else:
        print('**No matching CPL lessons found.**')
        print()

    # Summary
    print('## 4. Recommendations')
    print()
    if archive_results:
        print(f'- Review {len(archive_results)} Archive projects for reusable code, methods, and documented failure patterns')
        for r in archive_results:
            if r['has_learnings']:
                print(f'  - Read LEARNINGS.md in `{r["name"]}` for applicable lessons')
    if release_results:
        print(f'- Cite {len(release_results)} prior publications to avoid reinventing wheels (F20)')
    if cpl_results:
        print(f'- Apply {len(cpl_results)} CPL lessons to prevent known failure patterns')
    if not archive_results and not release_results:
        print('- **WARNING: No prior work found.** Document search patterns and exclusion criteria per §0.1.4 gate.')
        print(f'- Search keywords used: {keywords}')
        print(f'- Directories searched: Archive/{ARCHIVE_ROOT.name}/, {RELEASES_ROOT}')
        print('- This may indicate: (a) genuinely novel territory, or (b) insufficient search coverage.')
        print('- **False negatives are worse than no search (CPL L2).**')

    print()
    print('---')
    print('*Generated by discover_prior_work.py — part of the Project Init Protocol (§0.1.4)*')


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python discover_prior_work.py "<project-name>" "<keyword1> <keyword2> ..."')
        print('Example: python discover_prior_work.py "Quantum Computing" "quantum qubit gate error correction"')
        sys.exit(1)

    project_name = sys.argv[1]
    keywords = sys.argv[2:]
    generate_report(keywords, project_name)
