"""Convert saved HTML pages to clean markdown files."""
import os
import re
import html2text
from bs4 import BeautifulSoup

def html_to_md(html_path):
    with open(html_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    soup = BeautifulSoup(content, 'html.parser')

    # Remove scripts, styles, nav, header, footer, cookie banners
    for tag in soup.find_all(['script', 'style', 'nav', 'header', 'footer',
                               'noscript', 'iframe', 'svg']):
        tag.decompose()
    for tag in soup.find_all(id=re.compile(r'onetrust|cookie|banner|nav|toolbar|toc-bar', re.I)):
        tag.decompose()
    for tag in soup.find_all(class_=re.compile(r'cookie|banner|nav|toolbar|toc-bar|sidebar|header|footer|logo|breadcrumb', re.I)):
        tag.decompose()

    # Find main content
    main = (soup.find('section', class_=re.compile(r'chapter|content|main', re.I)) or
            soup.find('div', class_=re.compile(r'chapter|content|main', re.I)) or
            soup.find('article') or
            soup.find('main') or
            soup.find('body'))

    if not main:
        main = soup

    h = html2text.HTML2Text()
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_tables = False
    h.body_width = 0
    h.unicode_snob = True

    md = h.handle(str(main))

    # Clean up excessive blank lines
    md = re.sub(r'\n{3,}', '\n\n', md)
    return md.strip()


def convert_book(html_dir, md_dir):
    os.makedirs(md_dir, exist_ok=True)
    html_files = sorted(f for f in os.listdir(html_dir)
                        if f.endswith('.html') and not f.endswith('_files'))
    converted = []
    for fname in html_files:
        html_path = os.path.join(html_dir, fname)
        # Derive md filename: strip trailing " _ Book Title" suffix
        md_name = re.sub(r'\s+_\s+.+$', '', fname[:-5]) + '.md'
        md_path = os.path.join(md_dir, md_name)
        print(f'  {fname} -> {md_name}')
        md = html_to_md(html_path)
        with open(md_path, 'w', encoding='utf-8') as f:
            f.write(md)
        converted.append(md_name)
    return converted


BASE = 'c:/Users/aidraworker/ws/todd/prompt-vault/pages/aws'

books = [
    'Security and Microservice Architecture on AWS',
    'AWS Cookbook',
]

for book in books:
    print(f'\n=== {book} ===')
    html_dir = os.path.join(BASE, book, 'html')
    md_dir = os.path.join(BASE, book, 'md')
    convert_book(html_dir, md_dir)

print('\nDone.')
