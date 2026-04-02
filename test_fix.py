import os
import re

base_dir = r"E:\websites\freepercentage"

# Missing tools and proper titles
missing_tools = {
    "discount-calculator": "Discount Calculator",
    "percentage-increase-decrease": "Percentage Increase/Decrease",
    "percentage-difference": "Percentage Difference",
    "reverse-percentage": "Reverse Percentage Calculator",
    "percentage-of-percentage": "Percentage of a Percentage",
    "salary-increment": "Salary Increment Calculator"
}

missing_pages = {
    "about": "About Us",
    "contact": "Contact Us",
    "disclaimer": "Disclaimer",
    "terms-of-service": "Terms of Service"
}

# 1. Read base templates
gst_path = os.path.join(base_dir, 'tools', 'gst-calculator', 'index.html')
with open(gst_path, 'r', encoding='utf-8') as f:
    tool_template = f.read()

privacy_path = os.path.join(base_dir, 'privacy-policy', 'index.html')
with open(privacy_path, 'r', encoding='utf-8') as f:
    page_template = f.read()

# Helper to fix links inside HTML according to depth
def fix_links(html_content, depth):
    if depth == 0:
        prefix = './'
    else:
        prefix = '../' * depth
    
    # Replace href="/ with href="prefix
    html_content = re.sub(r'href="/(?!/)', f'href="{prefix}', html_content)
    # Replace src="/ with src="prefix
    html_content = re.sub(r'src="/(?!/)', f'src="{prefix}', html_content)
    return html_content

# We only want to keep the headers, replace the body content with a generic message for generated pages
def generate_tool_html(key, title):
    html = tool_template
    # Replace title tags
    html = re.sub(r'<title>.*?</title>', f'<title>{title} — Free Online Calculator | FreePercentage.com</title>', html, flags=re.DOTALL)
    # Replace the h1 in the hero
    html = re.sub(r'<div class="container">\s*<h1>.*?</h1>', f'<div class="container">\\n                <h1>{title}</h1>', html, count=1, flags=re.DOTALL)
    html = re.sub(r'<section id="calculator" class="calculator-card">.*?</section>', f'<section id="calculator" class="calculator-card">\\n                    <h2>{title}</h2>\\n                    <p>Basic tool structure goes here. Under development.</p>\\n                </section>', html, count=1, flags=re.DOTALL)
    html = fix_links(html, 2)
    return html

def generate_page_html(key, title):
    html = page_template
    html = re.sub(r'<title>.*?</title>', f'<title>{title} | FreePercentage.com</title>', html, flags=re.DOTALL)
    # Replace the hero text
    html = re.sub(r'<div class="container hero-content">\s*<h1>.*?</h1>', f'<div class="container hero-content">\\n                <h1>{title}</h1>', html, count=1, flags=re.DOTALL)
    # Replace main text content
    html = re.sub(r'<div class="content-box">.*?</div>', f'<div class="content-box">\\n                <h2>{title} Information</h2>\\n                <p>This is the {title} page. Content goes here.</p>\\n            </div>', html, count=1, flags=re.DOTALL)
    html = fix_links(html, 1)
    return html

# Generate missing tools
for key, title in missing_tools.items():
    folder = os.path.join(base_dir, 'tools', key)
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, 'index.html')
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generate_tool_html(key, title))

# Generate missing pages
for key, title in missing_pages.items():
    folder = os.path.join(base_dir, key)
    os.makedirs(folder, exist_ok=True)
    file_path = os.path.join(folder, 'index.html')
    if not os.path.exists(file_path):
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(generate_page_html(key, title))

# Finally, update ALL html files in the directory to fix the / -> relative path issue
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            # Find depth 
            rel_path = os.path.relpath(filepath, base_dir)
            
            depth = 0 if rel_path == file else rel_path.count(os.sep)
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Since some files might already be updated by generation or not, we carefully replace
            # Check if it has href="/ (excluding // which is external)
            if 'href="/' in content or 'src="/' in content:
                content = fix_links(content, depth)
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)

print("Done generating pages and fixing links.")
