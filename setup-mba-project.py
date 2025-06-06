#!/usr/bin/env python3
"""
MBA Assignment Workflow Setup Script
Creates structured project folders and agent prompts for automated MBA assignment completion
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

def load_environment():
    """Load environment variables from .env file or system"""
    # Try to load from .env file first
    env_path = Path(__file__).parent / '.env'
    if env_path.exists():
        load_dotenv(env_path)
    
    # Get environment variables with fallbacks
    mba_courses_dir = os.getenv('MBA_COURSES_DIR')
    university_name = os.getenv('UNIVERSITY_NAME', 'University')
    default_work_dir = os.getenv('DEFAULT_WORK_DIR', str(Path.cwd()))
    
    return {
        'mba_courses_dir': mba_courses_dir,
        'university_name': university_name,
        'default_work_dir': default_work_dir
    }

def get_available_directories(env_config):
    """Get list of available directories for project creation"""
    available_dirs = []
    
    # Add current directory
    available_dirs.append(str(Path.cwd()))
    
    # Add MBA courses directory if configured
    if env_config['mba_courses_dir'] and Path(env_config['mba_courses_dir']).exists():
        mba_path = Path(env_config['mba_courses_dir'])
        available_dirs.append(str(mba_path))
        
        # Add subdirectories (course folders)
        for subdir in mba_path.iterdir():
            if subdir.is_dir() and not subdir.name.startswith('.'):
                available_dirs.append(str(subdir))
    
    # Add default work directory if different and exists
    default_work = Path(env_config['default_work_dir'])
    if default_work.exists() and str(default_work) not in available_dirs:
        available_dirs.append(str(default_work))
    
    return available_dirs

def create_project_structure(project_details):
    """Create the complete MBA project folder structure"""
    
    # Extract details
    assignment_number = project_details['assignment_number']
    assignment_name = project_details['assignment_name']
    due_date = project_details['due_date']
    page_count = project_details['page_count']
    min_sources = project_details['min_sources']
    assignment_type = project_details['assignment_type']
    frameworks = project_details['frameworks']
    existing_folder = project_details['existing_folder']
    
    # Create base project directory inside MBA Assignment Workflow System folder
    base_path = Path(existing_folder) if existing_folder != "." else Path.cwd()
    workflow_system_dir = base_path / "MBA Assignment Workflow System"
    workflow_system_dir.mkdir(exist_ok=True)
    
    project_dir = workflow_system_dir / f"assignment{assignment_number}-{assignment_name}"
    project_dir.mkdir(exist_ok=True)
    
    # Define simplified folder structure
    folders = [
        "01-planning",
        "02-sources/academic/files",
        "02-sources/academic/analysis",
        "02-sources/industry/files", 
        "02-sources/industry/analysis",
        "03-frameworks/individual",
        "04-writing",
        "05-final"
    ]
    
    # Add conditional folders based on requirements
    charts_required = project_details.get('charts_required', False)
    tables_required = project_details.get('tables_required', False)
    
    if charts_required or tables_required:
        folders.append("04-writing/visuals")
    
    # Create all folders
    for folder in folders:
        (project_dir / folder).mkdir(parents=True, exist_ok=True)
    
    # Create instructions.md template
    instructions_content = f"""# Assignment Instructions

## Assignment Information
- **Assignment Number**: {assignment_number}
- **Assignment Name**: {assignment_name}
- **Assignment Type**: {assignment_type}
- **Due Date**: {due_date}
- **Page Count**: {page_count}
- **Minimum Sources**: {min_sources}
- **Frameworks Required**: {', '.join(frameworks)}

## Assignment Requirements
[Add specific assignment requirements here]

## Deliverables
- [ ] Complete {assignment_type.lower()} using required frameworks
- [ ] APA 7th Edition formatted paper
- [ ] Executive summary
- [ ] Supporting evidence and citations
- [ ] Minimum {min_sources} credible sources

## Submission Details
- **Due Date**: {due_date}
- **Format**: Academic paper
- **Length**: {page_count} pages
- **Citation Style**: APA 7th Edition
- **Type**: {assignment_type}
"""
    
    with open(project_dir / "01-planning" / "instructions.md", "w") as f:
        f.write(instructions_content)
    
    # Create CLAUDE.md with agent prompts
    claude_content = generate_agent_prompts(frameworks, 
                                           project_details.get('charts_required', False),
                                           project_details.get('tables_required', False))
    with open(project_dir / "01-planning" / "CLAUDE.md", "w") as f:
        f.write(claude_content)
    
    return project_dir

def generate_agent_prompts(frameworks, charts_required=False, tables_required=False):
    """Generate the complete CLAUDE.md file with all agent prompts"""
    
    frameworks_text = ', '.join(frameworks)
    
    content = f"""# MBA Assignment Agent Workflow

## Project Configuration
- **Required Frameworks**: {frameworks_text}
- **Output Standard**: MBA-level academic writing with APA 7th Edition
- **Workflow**: Sequential 6-agent process

---

## AGENT 1: Research Director

**Role**: Strategic research planning and framework mapping

**Instructions**:
You are the Research Director for this MBA assignment. Your role is to create a comprehensive research strategy that maps the required frameworks to specific evidence needs.

**Required Frameworks for this assignment**:
{frameworks_text}

**Tasks**:
1. Read the assignment instructions in `01-planning/instructions.md` thoroughly
2. For each required framework, identify:
   - Key theoretical components that need evidence
   - Types of data/information required
   - Specific questions the framework should answer
3. Create a source collection strategy specifying:
   - Academic sources needed (peer-reviewed papers, case studies)
   - Industry sources needed (reports, company documents)
   - Minimum number of sources per category
4. Generate automated search links for:
   - Google Scholar searches with specific queries
   - Industry database searches
   - Company report repositories
   - Academic database searches
   - Backup Google search links for industry sources (fallback options)
5. Create comprehensive planning summary for user review covering:
   - Assignment interpretation and understanding
   - Framework application approach
   - Research strategy and rationale
   - Expected outcomes and deliverables
6. Generate clear guidance for subsequent agents

**Output Files**:
- `01-planning/research-strategy.md` - Comprehensive approach summary for USER REVIEW
- `02-sources/search-links.md` - Ready-to-click search URLs for automatic source discovery

**Completion Signal**: "Research Director Complete. REVIEW research-strategy.md and approve before collecting sources. Then run AGENT 2."

---

## AGENT 2: Academic Scout

**Role**: Source analysis and template creation

**Instructions**:
You are the Academic Scout. Your role is to analyze collected sources and create structured templates for evidence extraction.

**Prerequisites**: User has reviewed and approved `01-planning/research-strategy.md`

**Tasks**:
1. Use LS tool to scan `02-sources/academic/files/` for academic PDFs
2. Use LS tool to scan `02-sources/industry/files/` for industry reports
3. For each source found, create analysis templates based on filename analysis
4. Generate overall source quality assessment

**IMPORTANT**: Do NOT attempt to read PDF files directly. Use filename information only to create templates.

**Output Files**:
- Analysis templates in `02-sources/*/analysis/` folders
- `02-sources/source-inventory.md` - Overall quality assessment

**Completion Signal**: "Academic Scout Complete. Run AGENT 3 to extract evidence."

---

## AGENT 3: Research Analyst

**Role**: Evidence extraction and synthesis

**Instructions**:
You are the Research Analyst. Your role is to systematically extract evidence from all sources and organize it for framework application.

**Required Frameworks**: {frameworks_text}

**Tasks**:
1. Use Read tool to analyze ALL PDFs/documents in `02-sources/*/files/` folders
2. For each source, create detailed analysis in `02-sources/*/analysis/` folders
3. Extract evidence relevant to each required framework
4. Generate research synthesis integrating all findings

**IMPORTANT**: Use the Read tool for PDF files - it can handle binary files including PDFs.

**Output Files**:
- Individual source analyses in `02-sources/*/analysis/` folders
- `03-frameworks/evidence-synthesis.md` - Integrated research findings

**Completion Signal**: "Research Analyst Complete. Run AGENT 4 for framework analysis."

---

## AGENT 4: Framework Specialist

**Role**: Strategic framework application

**Instructions**:
You are the Framework Specialist. Your role is to apply each required framework systematically using the extracted evidence.

**Required Frameworks**: {frameworks_text}

**Tasks**:
1. For each framework, create comprehensive analysis:
   - Apply framework methodology correctly
   - Use extracted evidence to support all components
   - Generate framework-specific insights and conclusions
2. Create individual framework analysis files
3. Synthesize insights across all frameworks
4. Develop integrated strategic recommendations

**Output Files**:
- Individual framework files in `03-frameworks/individual/`
- `03-frameworks/synthesis.md` - Integrated strategic analysis

**Completion Signal**: "Framework Specialist Complete. Run AGENT 5 for writing."

---

## AGENT 5: Writing Coordinator

**Role**: Academic writing and document creation

**Instructions**:
You are the Writing Coordinator. Your role is to create the complete academic draft integrating all framework analyses.

**Tasks**:
1. Create detailed section-by-section outline
2. Write complete first draft with:
   - Professional academic tone
   - Clear integration of all framework analyses
   - Proper APA 7th Edition citations throughout
   - Logical flow and strong arguments
3. Generate comprehensive reference list
4. Create executive summary"""
    
    # Add conditional tasks
    if charts_required:
        content += "\n5. Create charts/graphs in `04-writing/visuals/`"
    if tables_required:
        task_num = 6 if charts_required else 5
        content += f"\n{task_num}. Create data tables in `04-writing/visuals/`"
    
    content += """

**Output Files**:
- `04-writing/draft.md` - Complete assignment
- `04-writing/references.md` - APA citations
- `04-writing/presentation.md` - Executive summary"""
    
    # Add conditional output files
    if charts_required or tables_required:
        content += "\n- Visual materials in `04-writing/visuals/`"
    
    content += """

**Completion Signal**: "Writing Coordinator Complete. Run AGENT 6 for final review."

---

## AGENT 6: Quality Controller

**Role**: Final review and submission preparation

**Instructions**:
You are the Quality Controller. Your role is to ensure the assignment meets all academic standards and requirements.

**Tasks**:
1. Comprehensive quality review:
   - Verify all framework applications are complete and accurate
   - Check APA citation compliance throughout
   - Assess academic writing standards
   - Ensure assignment requirements are fully addressed
2. Create final submission package
3. Generate quality assurance documentation

**Output Files**:
- `05-final/submission.md` - Final submission-ready assignment

**Completion Signal**: "Quality Controller Complete. Assignment ready in 05-final/submission.md"

---

## Usage Instructions

1. **Copy each agent prompt** sequentially to Claude Code
2. **Wait for completion message** before proceeding to next agent
3. **Collect sources** between Agent 1 and Agent 2:
   - Place academic PDFs in `02-sources/academic/files/`
   - Place industry reports in `02-sources/industry/files/`
4. **Final assignment** will be in `05-final/submission.md`

## Framework Definitions

### Porter's Five Forces
Analyzes industry competitive forces: supplier power, buyer power, competitive rivalry, threat of substitutes, threat of new entrants.

### SWOT Analysis
Internal strengths/weaknesses and external opportunities/threats analysis.

### VRIO Framework
Resource analysis: Value, Rarity, Imitability, Organization for competitive advantage.

### PESTEL Analysis
Macro-environment analysis: Political, Economic, Social, Technological, Environmental, Legal factors.

### Value Chain Analysis
Primary and support activities that create competitive advantage.

### Business Model Canvas
Nine building blocks of business model design and innovation.

### McKinsey 7S
Seven interdependent factors for organizational effectiveness: Strategy, Structure, Systems, Shared Values, Style, Staff, Skills.
"""
    
    return content

def main():
    """Main setup function"""
    print("🎓 MBA Assignment Workflow Setup")
    print("=" * 40)
    
    # Load environment configuration
    env_config = load_environment()
    
    if not env_config['mba_courses_dir']:
        print("⚠️  No MBA_COURSES_DIR configured in .env file")
        print("   Create .env file from .env.example for personalized setup")
        print()
    
    # Select existing folder
    print("\\nSelect existing folder:")
    
    available_dirs = get_available_directories(env_config)
    
    # Display options
    if available_dirs:
        for i, dir_path in enumerate(available_dirs, 1):
            print(f"{i}. {dir_path}")
        print(f"{len(available_dirs) + 1}. Enter custom path")
        
        choice = input(f"\\nSelect folder (1-{len(available_dirs) + 1}): ").strip()
        
        try:
            choice_num = int(choice)
            if 1 <= choice_num <= len(available_dirs):
                existing_folder = available_dirs[choice_num - 1]
            elif choice_num == len(available_dirs) + 1:
                existing_folder = input("Enter custom path: ").strip()
            else:
                existing_folder = str(Path.cwd())
        except ValueError:
            existing_folder = str(Path.cwd())
    else:
        existing_folder = input("Enter folder path (or press Enter for current directory): ").strip()
        if not existing_folder:
            existing_folder = str(Path.cwd())
    
    # Assignment details
    assignment_number = input("Assignment number: ").strip()
    if not assignment_number:
        assignment_number = "01"
    
    assignment_name = input("Assignment name: ").strip()
    if not assignment_name:
        print("Assignment name is required!")
        return
    
    due_date = input("Due date: ").strip()
    if not due_date:
        due_date = "[Add due date]"
    
    page_count = input("Page count: ").strip()
    if not page_count:
        page_count = "[Add page count]"
    
    min_sources = input("Min sources: ").strip()
    if not min_sources:
        min_sources = "10"
    
    assignment_type = input("Assignment type: ").strip()
    if not assignment_type:
        assignment_type = "Strategic Analysis"
    
    # Visual requirements
    charts_required = input("Charts/graphs required? (y/n): ").strip().lower()
    charts_required = charts_required in ['y', 'yes', '1', 'true']
    
    tables_required = input("Data tables required? (y/n): ").strip().lower()
    tables_required = tables_required in ['y', 'yes', '1', 'true']
    
    auto_open = input("Open project in VS Code? (y/n): ").strip().lower()
    auto_open = auto_open in ['y', 'yes', '1', 'true']
    
    # Framework selection
    available_frameworks = [
        "Porter's Five Forces",
        "SWOT Analysis", 
        "VRIO Framework",
        "PESTEL Analysis",
        "Value Chain Analysis",
        "Business Model Canvas",
        "McKinsey 7S"
    ]
    
    print("\\nAvailable frameworks:")
    for i, framework in enumerate(available_frameworks, 1):
        print(f"{i}. {framework}")
    
    print("\\nSelect frameworks (enter numbers separated by commas, e.g., 1,2,3):")
    selection = input("Frameworks: ").strip()
    
    try:
        indices = [int(x.strip()) - 1 for x in selection.split(',')]
        frameworks = [available_frameworks[i] for i in indices if 0 <= i < len(available_frameworks)]
    except:
        frameworks = ["SWOT Analysis", "Porter's Five Forces"]  # Default
    
    if not frameworks:
        frameworks = ["SWOT Analysis", "Porter's Five Forces"]  # Default
    
    # Create project with all details
    project_details = {
        'assignment_number': assignment_number,
        'assignment_name': assignment_name,
        'due_date': due_date,
        'page_count': page_count,
        'min_sources': min_sources,
        'assignment_type': assignment_type,
        'frameworks': frameworks,
        'existing_folder': existing_folder,
        'charts_required': charts_required,
        'tables_required': tables_required,
        'auto_open': auto_open
    }
    
    project_dir = create_project_structure(project_details)
    
    print(f"\\n✅ Project created in MBA Assignment Workflow System:")
    print(f"📁 Location: {project_dir}")
    print(f"📁 Type: {assignment_type}")
    print(f"📁 Frameworks: {', '.join(frameworks)}")
    print(f"📅 Due: {due_date}")
    
    # Show conditional features
    if charts_required:
        print("📊 Charts/graphs: Enabled")
    if tables_required:
        print("📋 Data tables: Enabled")
    
    # Auto-open project if requested
    if auto_open:
        print("\\n🚀 Opening project in VS Code...")
        import subprocess
        try:
            subprocess.run(['code', str(project_dir)], check=True)
            print("✅ Project opened in VS Code")
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("❌ Could not open VS Code automatically")
            print(f"Manual command: code '{project_dir}'")
    
    print("\\n📋 Next steps:")
    if not auto_open:
        print("1. Navigate to your MBA Assignment Workflow System folder")
        print("2. Open project folder in VS Code")
        print("3. Edit 01-planning/instructions.md with assignment details")
        print("4. Open 01-planning/CLAUDE.md for agent prompts")
        print("5. Run AGENT 1 in Claude Code")
    else:
        print("1. Edit 01-planning/instructions.md with assignment details")
        print("2. Open 01-planning/CLAUDE.md for agent prompts")
        print("3. Run AGENT 1 in Claude Code")

if __name__ == "__main__":
    main()