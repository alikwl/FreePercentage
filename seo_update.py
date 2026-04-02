import os
import re
from datetime import datetime

base_dir = r"E:\websites\freepercentage"

# URL List for Sitemap
urls = [
    ('/', 1.0, 'daily'),
    ('/tools/marks-percentage/', 0.9, 'weekly'),
    ('/tools/final-grade/', 0.9, 'weekly'),
    ('/tools/decimal-to-percent/', 0.9, 'weekly'),
    ('/tools/profit-margin/', 0.9, 'weekly'),
    ('/tools/gst-calculator/', 0.9, 'weekly'),
    ('/tools/discount-calculator/', 0.9, 'weekly'),
    ('/tools/percentage-increase-decrease/', 0.9, 'weekly'),
    ('/tools/percentage-difference/', 0.9, 'weekly'),
    ('/tools/reverse-percentage/', 0.9, 'weekly'),
    ('/tools/percentage-of-percentage/', 0.9, 'weekly'),
    ('/tools/salary-increment/', 0.9, 'weekly'),
    ('/about/', 0.8, 'monthly'),
    ('/contact/', 0.8, 'monthly'),
    ('/disclaimer/', 0.7, 'monthly'),
    ('/privacy-policy/', 0.7, 'monthly'),
    ('/terms-of-service/', 0.7, 'monthly'),
]

# Write robots.txt
robots_content = """User-agent: *
Allow: /

# Sitemap
Sitemap: https://freepercentage.com/sitemap.xml
"""
with open(os.path.join(base_dir, 'robots.txt'), 'w', encoding='utf-8') as f:
    f.write(robots_content)

# Write sitemap.xml
today = datetime.utcnow().strftime('%Y-%m-%d')
sitemap_xml = ['<?xml version="1.0" encoding="UTF-8"?>']
sitemap_xml.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

for loc, priority, changefreq in urls:
    full_url = f"https://freepercentage.com{loc}"
    sitemap_xml.append('  <url>')
    sitemap_xml.append(f'    <loc>{full_url}</loc>')
    sitemap_xml.append(f'    <lastmod>{today}</lastmod>')
    sitemap_xml.append(f'    <changefreq>{changefreq}</changefreq>')
    sitemap_xml.append(f'    <priority>{priority}</priority>')
    sitemap_xml.append('  </url>')

sitemap_xml.append('</urlset>')
with open(os.path.join(base_dir, 'sitemap.xml'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(sitemap_xml))

# Content for legal pages
pages_data = {
    "about": {
        "title": "About Us",
        "description": "Learn more about FreePercentage.com, our mission to provide fast, accurate, and free percentage calculators for students, professionals, and businesses.",
        "content": """
        <section class="content-section" style="padding:60px 0;">
            <div class="container">
                <h1 style="margin-bottom:20px; font-size: 2.5rem;">About FreePercentage.com</h1>
                <p>Welcome to <strong>FreePercentage.com</strong>, your ultimate destination for everything related to percentages. We understand that calculating percentages, whether for academics, finance, retail shopping, or corporate growth, can sometimes be confusing or time-consuming. That's why we created a comprehensive suite of completely free online percentage calculators.</p>
                <h2 style="margin-top:40px; margin-bottom:15px;">Our Mission</h2>
                <p>Our mission is simple: to make percentage calculations accessible, accurate, and lightning-fast for everyone. We believe that critical mathematical tools should be heavily optimized, ad-unintrusive, and available without the hassle of downloading apps or signing up for accounts. <strong>Math should be free and accessible to all.</strong></p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">Why Choose Us?</h2>
                <ul style="line-height:1.8; margin-bottom:20px; padding-left: 20px;">
                    <li><strong>100% Free Forever:</strong> We will never ask you to pay for core calculator functionalities.</li>
                    <li><strong>No Registrations:</strong> Your privacy is important. Do your math and go. We don't need your data.</li>
                    <li><strong>Data Security:</strong> All calculations are executed completely on the client-side (inside your browser), which means your numbers never leave your device.</li>
                    <li><strong>Mobile Optimized:</strong> Use our calculators smoothly whether you are on a 4K desktop or a small smartphone.</li>
                </ul>

                <h2 style="margin-top:40px; margin-bottom:15px;">Who We Serve</h2>
                <p>We've crafted specialized calculators targeting different user bases:</p>
                <div style="background-color: #f7f9fc; padding: 20px; border-radius: 8px; margin-top:20px;">
                    <p>🎓 <strong>Students & Teachers:</strong> Grading calculators, final marks percentage, and decimal conversions.</p>
                    <p>💼 <strong>Business & Retail:</strong> Profit margin, GST, discounts, and custom tax estimators.</p>
                    <p>📈 <strong>Professionals & HR:</strong> Salary increments, absolute differences, and performance growth.</p>
                </div>
            </div>
        </section>
        """
    },
    "contact": {
        "title": "Contact Us",
        "description": "Get in touch with the FreePercentage.com team. Have a feature request, bug report, or general inquiry? Reach out to us today.",
        "content": """
        <section class="content-section" style="padding:60px 0;">
            <div class="container">
                <h1 style="margin-bottom:20px; font-size: 2.5rem;">Contact Us</h1>
                <p>We love hearing from our users! Whether you've found a bug, want to request a new type of calculator, or have advertising and partnership inquiries, feel free to reach out to the <strong>FreePercentage.com</strong> team.</p>
                
                <div style="display:flex; flex-wrap: wrap; gap: 40px; margin-top: 40px;">
                    <div style="flex:1; min-width:300px; background: #fdfdfd; padding: 30px; border-radius: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05);">
                        <h2 style="margin-bottom:20px;">Get In Touch</h2>
                        <p style="margin-bottom:15px;"><strong>Email:</strong> support@freepercentage.com</p>
                        <p style="margin-bottom:15px;"><strong>Response Time:</strong> We typically respond within 24-48 business hours.</p>
                        <p>If you are submitting a bug report, please include information about the device and browser you are using, alongside steps to reproduce the error.</p>
                    </div>

                    <div style="flex:1; min-width:300px;">
                        <h2>Frequently Asked Queries</h2>
                        <ul style="line-height:1.8; margin-bottom:20px; padding-left: 20px; margin-top:15px;">
                            <li><strong>Custom Calculators:</strong> Let us know if you need to embed a specialized calculator into your own app or business website! We are working on APIs.</li>
                            <li><strong>Advertising:</strong> Interested in ad placements? Email us with 'Partnership' in the subject line.</li>
                        </ul>
                    </div>
                </div>
            </div>
        </section>
        """
    },
    "disclaimer": {
        "title": "Disclaimer",
        "description": "Read the standard medical, legal, and financial disclaimer for FreePercentage.com. We provide calculation tools for estimating purposes, not professional advice.",
        "content": """
        <section class="content-section" style="padding:60px 0;">
            <div class="container">
                <h1 style="margin-bottom:20px; font-size: 2.5rem;">Disclaimer</h1>
                <p><em>Last Updated: April 2, 2026</em></p>
                <hr style="margin:20px 0; border: none; border-top: 1px solid #eaeaea;">
                <p>The information and tools provided by <strong>FreePercentage.com</strong> are for general informational and mathematical estimation purposes only. All information on the Site is provided in good faith, however, we make no representation or warranty of any kind, express or implied, regarding the accuracy, adequacy, validity, reliability, availability, or completeness of any information or mathematical outcome on the Site.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">Financial & Tax Advice Disclaimer</h2>
                <p>Calculators related to business, finance, taxation (such as the GST Calculator or Profit Margin Calculator), and salary metrics are intended as quick estimation tools. They <strong>do not</strong> constitute professional financial, tax, or legal advice. Tax codes and regulations change rapidly and vary by strict geographical boundaries. You should always consult with a licensed accountant, financial advisor, or legal attorney before making major financial decisions or filing mandatory tax documents.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">Error and Revisions</h2>
                <p>While we extensively test our Javascript formulas, edge cases or rounding errors can occur. FreePercentage.com, its owners, developers, and affiliates will not be held liable for any loss, damage, or financial discrepancy arising directly or indirectly from the use of our calculators.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">Fair Use and Copyright</h2>
                <p>Any brands, organizations, trademarks, or external links mentioned on the Site belong to their respective owners. We do not claim endorsement unless explicitly stated.</p>
            </div>
        </section>
        """
    },
    "privacy-policy": {
        "title": "Privacy Policy",
        "description": "The Privacy Policy for FreePercentage.com. Learn about how we handle cookies, analytics, and why we guarantee total privacy for your calculations.",
        "content": """
        <section class="content-section" style="padding:60px 0;">
            <div class="container">
                <h1 style="margin-bottom:20px; font-size: 2.5rem;">Privacy Policy</h1>
                <p><em>Effective Date: April 2, 2026</em></p>
                <hr style="margin:20px 0; border: none; border-top: 1px solid #eaeaea;">
                <p>At <strong>FreePercentage.com</strong>, accessible from https://freepercentage.com, one of our main priorities is the privacy of our visitors. This Privacy Policy document contains types of information that is collected and recorded by FreePercentage.com and how we use it.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">1. Client-Side Calculations</h2>
                <p>We are proud to inform you that <strong>100% of our calculator logic executes directly in your browser</strong> via client-side JavaScript. This means that the monetary values, grades, or personal business figures you type into our calculators are <strong>never</strong> transmitted to, processed by, or stored on our servers. Your mathematical input is completely private and secure.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">2. Log Files</h2>
                <p>FreePercentage.com follows a standard procedure of using log files. These files log visitors when they visit websites. The information collected by log files include internet protocol (IP) addresses, browser type, Internet Service Provider (ISP), date and time stamp, referring/exit pages, and possibly the number of clicks. These are not linked to any information that is personally identifiable.</p>
                
                <h2 style="margin-top:40px; margin-bottom:15px;">3. Cookies and Web Beacons</h2>
                <p>Like any other website, we use "cookies" to store information including visitors' preferences, and the pages on the website that the visitor accessed or visited. The information is used to optimize the users' experience by customizing our web page content based on visitors' browser type and/or other information. Third-party vendors, including Google, use cookies to serve ads based on a user's prior visits to your website or other websites.</p>

                <h2 style="margin-top:40px; margin-bottom:15px;">4. Third Party Privacy Policies</h2>
                <p>FreePercentage.com's Privacy Policy does not apply to other advertisers or websites. Thus, we are advising you to consult the respective Privacy Policies of these third-party ad servers (like Google AdSense) for more detailed information. It may include their practices and instructions about how to opt-out of certain options.</p>

                <h2 style="margin-top:40px; margin-bottom:15px;">5. Consent</h2>
                <p>By using our website, you hereby consent to our Privacy Policy and agree to its Terms and Conditions.</p>
            </div>
        </section>
        """
    },
    "terms-of-service": {
        "title": "Terms of Service",
        "description": "Terms of Service and user agreement for FreePercentage.com. Rules regarding fair usage, intellectual property, and limitations of liability.",
        "content": """
        <section class="content-section" style="padding:60px 0;">
            <div class="container">
                <h1 style="margin-bottom:20px; font-size: 2.5rem;">Terms of Service</h1>
                <p><em>Effective Date: April 2, 2026</em></p>
                <hr style="margin:20px 0; border: none; border-top: 1px solid #eaeaea;">
                <p>Welcome to <strong>FreePercentage.com</strong>!</p>
                <p>These terms and conditions outline the rules and regulations for the use of FreePercentage.com's Website. By accessing this website we assume you accept these terms and conditions. Do not continue to use FreePercentage.com if you do not agree to take all of the terms and conditions stated on this page.</p>

                <h2 style="margin-top:40px; margin-bottom:15px;">1. License to Use</h2>
                <p>Unless otherwise stated, FreePercentage.com and/or its licensors own the intellectual property rights for all material (algorithms, code, design, logos, and layout) on FreePercentage.com. All intellectual property rights are reserved. You may access this from FreePercentage.com for your own personal, non-commercial use subjected to restrictions set in these terms and conditions.</p>
                <p><strong>You must not:</strong></p>
                <ul style="line-height:1.8; margin-bottom:20px; padding-left: 20px;">
                    <li>Republish our CSS, HTML, JS, or calculator implementations on your own website.</li>
                    <li>Sell, rent or sub-license material from FreePercentage.com.</li>
                    <li>Reproduce, duplicate or copy material from FreePercentage.com.</li>
                    <li>Utilize automated crawlers to flood our calculation endpoints (not applicable currently as all compute is client-side, but standard DDoS terms remain in effect).</li>
                </ul>

                <h2 style="margin-top:40px; margin-bottom:15px;">2. Hyperlinking to our Content</h2>
                <p>Educational institutions, online communities, directories, and financial blogs are inherently permitted and encouraged to link to our home page or specific calculators. You do not need to ask for permission to link to us.</p>

                <h2 style="margin-top:40px; margin-bottom:15px;">3. iFrames</h2>
                <p>Without prior approval and written permission, you may not create frames around our Webpages that alter in any way the visual presentation or appearance of our Website.</p>

                <h2 style="margin-top:40px; margin-bottom:15px;">4. Removal of links from our website</h2>
                <p>If you find any link on our Website that is offensive for any reason, you are free to contact and inform us any moment. We will consider requests to remove links but we are not obligated to or so or to respond to you directly.</p>

                <p style="margin-top: 40px;"><em>Failure to adhere to these Terms of Use may result in IP bans or reporting to respective web hosts.</em></p>
            </div>
        </section>
        """
    }
}

# Use root index.html to extract header and footer template
index_path = os.path.join(base_dir, 'index.html')
with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

parts = index_content.split('<main>')
header_part = parts[0]
footer_part = parts[1].split('</main>')[1]

# Make sure we fix relative paths in the base header/footer templates since they are for directory depth = 1 it'll be ../
# Replace ./ with ../
header_part = header_part.replace('href="./', 'href="../').replace('src="./', 'src="../')
footer_part = footer_part.replace('href="./', 'href="../').replace('src="./', 'src="../')

# If the index.html had href="/FreePercentage/" or something differently, let's just make sure.
# Wait, my previous script made it ./ for depth 0. We've just replaced ./ with ../ which is perfectly correct for depth 1!

for key, data in pages_data.items():
    title = data['title']
    desc = data['description']
    inner_html = data['content']
    
    # Customize the header for this page
    page_header = header_part
    # Title
    page_header = re.sub(r'<title>.*?</title>', f'<title>{title} | Free Percentage Calculators</title>', page_header, flags=re.DOTALL)
    # Description
    page_header = re.sub(r'<meta\s+name="description"\s+content=".*?">', f'<meta name="description" content="{desc}">', page_header, flags=re.DOTALL|re.IGNORECASE)
    # canonical
    page_header = re.sub(r'<link\s+rel="canonical"\s+href=".*?">', f'<link rel="canonical" href="https://freepercentage.com/{key}/">', page_header, flags=re.DOTALL|re.IGNORECASE)
    # OG URL
    page_header = re.sub(r'<meta\s+property="og:url"\s+content=".*?">', f'<meta property="og:url" content="https://freepercentage.com/{key}/">', page_header, flags=re.DOTALL|re.IGNORECASE)
    # OG Title
    page_header = re.sub(r'<meta\s+property="og:title"\s+content=".*?">', f'<meta property="og:title" content="{title} | FreePercentage.com">', page_header, flags=re.DOTALL|re.IGNORECASE)
    
    # JSON-LD Schema
    schema = f'''
  <script type="application/ld+json">
    {{
      "@context": "https://schema.org",
      "@type": "WebPage",
      "name": "{title}",
      "description": "{desc}",
      "url": "https://freepercentage.com/{key}/",
      "publisher": {{
        "@type": "Organization",
        "name": "FreePercentage.com",
        "url": "https://freepercentage.com"
      }}
    }}
  </script>
'''
    # Replace existing JSON LD schema 
    page_header = re.sub(r'<script type="application/ld\+json">.*?</script>', schema, page_header, flags=re.DOTALL)

    full_page = page_header + '\n<main>\n' + inner_html + '\n</main>\n' + footer_part
    
    file_path = os.path.join(base_dir, key, 'index.html')
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(full_page)

print("SEO update completed.")