import os
import markdown
import glob
import shutil

def convert_markdown_to_html():
    # Create images directory and copy images
    os.makedirs('articles/images', exist_ok=True)
    image_mapping = {
        'AI时代的老庄智慧研究所': '样图2.png',
        '区块链金融：从入门到精通': '样图3.png',
        '德扑思维实验室': '样图1.png'
    }
    
    # Copy images to articles directory
    for image in image_mapping.values():
        if os.path.exists(image):
            shutil.copy2(image, f'articles/images/{image}')

    # HTML template
    html_template = """
    <!DOCTYPE html>
    <html lang="zh">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.0/github-markdown.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@400;500;700&display=swap');
            body {{
                font-family: 'Noto Sans SC', sans-serif;
                color: #1f2937;
                background-color: #f8fafc;
            }}
            .markdown-body {{
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
                color: #1f2937;
                background-color: #ffffff;
            }}
            article {{
                background: #ffffff;
                margin: 1rem;
                border-radius: 0.5rem;
                overflow: hidden;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
            }}
            .banner-image {{
                width: 100%;
                max-width: 800px;
                height: auto;
                margin: 0 auto 2rem auto;
                display: block;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
            }}
            .progress-bar {{
                position: fixed;
                top: 0;
                left: 0;
                width: 0%;
                height: 3px;
                background: linear-gradient(to right, #4f46e5, #7c3aed);
                z-index: 1000;
                transition: width 0.2s ease;
            }}
            .back-to-top {{
                position: fixed;
                bottom: 2rem;
                right: 2rem;
                background: white;
                width: 3rem;
                height: 3rem;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                cursor: pointer;
                opacity: 0;
                transition: all 0.3s ease;
                color: #4f46e5;
            }}
            .back-to-top:hover {{
                transform: translateY(-3px);
                box-shadow: 0 6px 8px -1px rgba(0, 0, 0, 0.15);
            }}
            .toc {{
                position: fixed;
                left: 2rem;
                top: 50%;
                transform: translateY(-50%);
                max-width: 250px;
                max-height: 80vh;
                overflow-y: auto;
                background: white;
                padding: 1rem;
                border-radius: 0.5rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                display: none;
            }}
            @media (min-width: 1400px) {{
                .toc {{
                    display: block;
                }}
            }}
            @media (max-width: 767px) {{
                body {{
                    background-color: #ffffff;
                    padding-top: 0;
                    margin: 0;
                }}
                article {{
                    margin: 0;
                    border-radius: 0;
                    box-shadow: none;
                    padding: 0;
                }}
                .markdown-body {{
                    padding: 1rem;
                    margin: 0;
                    font-size: 16px;
                    line-height: 1.8;
                    color: #000000;
                    background: #ffffff;
                }}
                .markdown-body h1 {{
                    font-size: 1.5rem;
                    margin: 1.5rem 0 1rem;
                    font-weight: 700;
                    color: #000000;
                    line-height: 1.4;
                }}
                .markdown-body h2 {{
                    font-size: 1.25rem;
                    margin: 1.5rem 0 0.75rem;
                    font-weight: 600;
                    color: #000000;
                    line-height: 1.4;
                }}
                .markdown-body h3 {{
                    font-size: 1.125rem;
                    margin: 1.25rem 0 0.75rem;
                    font-weight: 600;
                    color: #000000;
                    line-height: 1.4;
                }}
                .markdown-body p {{
                    margin: 0 0 1rem;
                    opacity: 1;
                    color: #000000;
                    line-height: 1.8;
                }}
                .markdown-body ul,
                .markdown-body ol {{
                    margin: 0 0 1rem;
                    padding-left: 1.5rem;
                    color: #000000;
                }}
                .markdown-body li {{
                    margin-bottom: 0.5rem;
                }}
                .markdown-body strong {{
                    font-weight: 600;
                    color: #000000;
                }}
                header {{
                    margin: 0;
                    padding: 0;
                    position: sticky;
                    top: 0;
                    background: #ffffff;
                    z-index: 50;
                    border-bottom: 1px solid #f0f0f0;
                }}
                header .max-w-7xl {{
                    padding: 0;
                }}
                header a {{
                    display: flex;
                    align-items: center;
                    padding: 0.875rem 1rem;
                    font-size: 1rem;
                    color: #4f46e5;
                    background: #ffffff;
                    font-weight: 500;
                }}
                header a i {{
                    margin-right: 0.5rem;
                }}
                .banner-image {{
                    margin: 0;
                    width: 100%;
                    border-radius: 0;
                    max-height: 240px;
                    object-fit: cover;
                    box-shadow: none;
                }}
                .breadcrumbs {{
                    display: none;
                }}
                footer {{
                    margin-top: 2rem;
                    padding: 1rem;
                    border-top: 1px solid #f0f0f0;
                    text-align: center;
                    color: #666666;
                    font-size: 0.875rem;
                }}
                .back-to-top {{
                    bottom: 1.5rem;
                    right: 1.5rem;
                    width: 2.5rem;
                    height: 2.5rem;
                    background: rgba(255, 255, 255, 0.9);
                    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
                }}
            }}
        </style>
    </head>
    <body class="bg-gray-50">
        <div class="progress-bar"></div>
        <header class="bg-white shadow-sm mb-8 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-6">
                <nav class="flex items-center justify-between">
                    <a href="../../index.html" class="text-gray-600 hover:text-gray-900">
                        <i class="fas fa-arrow-left mr-2"></i>返回首页
                    </a>
                    <div class="text-sm breadcrumbs text-gray-500">
                        <span>{category}</span>
                        <i class="fas fa-chevron-right mx-2 text-gray-400"></i>
                        <span>{title}</span>
                    </div>
                </nav>
            </div>
        </header>
        <article class="markdown-body bg-white shadow-lg rounded-lg overflow-hidden relative">
            {banner_image}
            <div class="toc">
                <h3 class="text-lg font-bold mb-4">目录</h3>
                <div id="toc-content"></div>
            </div>
            {content}
        </article>
        <button class="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
            <i class="fas fa-arrow-up"></i>
        </button>
        <footer class="bg-white mt-12 py-6">
            <div class="max-w-7xl mx-auto px-4 text-center text-gray-600">
                <p>© 2025 知识星球矩阵. All rights reserved.</p>
            </div>
        </footer>
        <script>
            // 阅读进度条
            window.addEventListener('scroll', () => {{
                const winScroll = document.body.scrollTop || document.documentElement.scrollTop;
                const height = document.documentElement.scrollHeight - document.documentElement.clientHeight;
                const scrolled = (winScroll / height) * 100;
                document.querySelector('.progress-bar').style.width = scrolled + '%';
                
                // 返回顶部按钮
                const backToTop = document.querySelector('.back-to-top');
                if (winScroll > 300) {{
                    backToTop.style.opacity = '1';
                }} else {{
                    backToTop.style.opacity = '0';
                }}
            }});

            // 生成目录
            document.addEventListener('DOMContentLoaded', () => {{
                const article = document.querySelector('.markdown-body');
                const toc = document.querySelector('#toc-content');
                const headings = article.querySelectorAll('h1, h2, h3');
                const tocItems = [];

                headings.forEach((heading, index) => {{
                    const id = `heading-${{index}}`;
                    heading.id = id;
                    const level = parseInt(heading.tagName.charAt(1));
                    tocItems.push(`
                        <div class="pl-${{(level-1)*4}} py-1">
                            <a href="#${{id}}" class="text-gray-600 hover:text-gray-900 text-sm">
                                ${{heading.textContent}}
                            </a>
                        </div>
                    `);
                }});

                toc.innerHTML = tocItems.join('');
            }});
        </script>
    </body>
    </html>
    """

    # Convert all markdown files
    for folder in ['AI时代的老庄智慧研究所', '区块链金融：从入门到精通', '德扑思维实验室']:
        if not os.path.exists(folder):
            continue
            
        # Create articles directory if it doesn't exist
        articles_dir = os.path.join('articles', folder)
        os.makedirs(articles_dir, exist_ok=True)
        
        # Convert each markdown file
        for md_file in glob.glob(os.path.join(folder, '*.md')):
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
            
            # Convert markdown to HTML
            html_content = markdown.markdown(md_content, extensions=['extra', 'toc'])
            
            # Get title from filename
            title = os.path.basename(md_file).replace('.md', '')
            
            # Only add banner image for opening articles
            banner_image = ''
            if '开篇' in title:
                banner_image = f'<img src="../images/{image_mapping[folder]}" alt="{title}" class="banner-image">'
            
            # Create HTML file with banner image
            category = folder
            html = html_template.format(
                title=title,
                content=html_content,
                banner_image=banner_image,
                category=category
            )
            
            # Save HTML file
            html_filename = os.path.join(articles_dir, os.path.basename(md_file).replace('.md', '.html'))
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html)

if __name__ == '__main__':
    # Create articles directory
    os.makedirs('articles', exist_ok=True)
    convert_markdown_to_html() 