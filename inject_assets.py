import os
import re

base_dir = r"E:\websites\freepercentage"

for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith('.html'):
            filepath = os.path.join(root, file)
            rel_path = os.path.relpath(filepath, base_dir)
            depth = 0 if rel_path == file else rel_path.count(os.sep)
            prefix = './' if depth == 0 else '../' * depth
            
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add favicon
            if 'rel="icon"' not in content:
                content = content.replace('</head>', f'  <link rel="icon" type="image/png" href="{prefix}assets/favicon.png">\n</head>')
            
            # Replace logo HTML
            logo_img = f'<img src="{prefix}assets/logo.png" alt="FreePercentage.com Logo" style="height: 42px; width: auto;" />'
            
            # This regex will match the inner HTML of the logo tag from the template
            # <a href="..." class="logo"> ... </a>
            
            content = re.sub(r'(<a[^>]*?class="logo"[^>]*>)\s*<span class="logo-icon">%</span>\s*<span class="logo-text">FreePercentage<span class="logo-dot">\.com</span></span>\s*(</a>)', r'\1\n        ' + logo_img + r'\n      \2', content, flags=re.DOTALL)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

print("Injected logo and favicon.")