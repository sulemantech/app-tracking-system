# job_parser/job_parser.py
import re

def parse_job_description(job_description_path):
    """Extracts key skills and requirements from a job description."""
    with open(job_description_path, 'r') as file:
        job_description = file.read()
    
    # Example: Extract skills and requirements using regex
    # This example assumes skills are listed in a 'Skills:' section
    skills = re.findall(r'Skills:\s*(.*)', job_description, re.IGNORECASE)
    
    # If skills are in a list format, split them
    if skills:
        skills = skills[0].split(',')
    
    return {
        'description': job_description,
        'skills': [skill.strip() for skill in skills]
    }
