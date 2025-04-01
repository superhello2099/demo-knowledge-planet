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
        <meta name="color-scheme" content="light dark">
        <title>{title}</title>
        <script src="https://cdn.tailwindcss.com"></script>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css">
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/github-markdown-css/5.5.0/github-markdown-light.min.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+SC:wght@300;400;500;700&display=swap');
            
            :root {{
                --primary-color: #4f46e5;
                --text-color: #1f2937;
                --bg-color: #ffffff;
                --bg-secondary: #f3f4f6;
                --border-color: #e5e7eb;
            }}

            :root[data-theme="dark"] {{
                --primary-color: #818cf8;
                --text-color: #e5e7eb;
                --bg-color: #111827;
                --bg-secondary: #1f2937;
                --border-color: #374151;
            }}

            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}

            body {{
                font-family: 'Noto Sans SC', sans-serif;
                color: var(--text-color);
                background-color: var(--bg-secondary);
                -webkit-font-smoothing: antialiased;
                transition: background-color 0.3s ease, color 0.3s ease;
            }}

            /* 优化的 Markdown 样式 */
            .markdown-body {{
                background-color: var(--bg-color);
                color: var(--text-color);
                box-sizing: border-box;
                min-width: 200px;
                max-width: 980px;
                margin: 0 auto;
                padding: 45px;
                line-height: 1.8;
                font-weight: 400;
                transition: background-color 0.3s ease, color 0.3s ease;
            }}

            .markdown-body h1 {{
                font-size: 2rem;
                font-weight: 700;
                margin: 2rem 0 1.5rem;
                color: var(--text-color);
                letter-spacing: -0.025em;
            }}

            .markdown-body h2 {{
                font-size: 1.5rem;
                font-weight: 600;
                margin: 1.75rem 0 1rem;
                color: var(--text-color);
            }}

            .markdown-body h3 {{
                font-size: 1.25rem;
                font-weight: 500;
                margin: 1.5rem 0 0.75rem;
                color: var(--text-color);
            }}

            .markdown-body p {{
                margin: 0 0 1.25rem;
                font-weight: 300;
                color: var(--text-color);
                line-height: 1.8;
                text-align: justify;
            }}

            .markdown-body strong {{
                font-weight: 500;
                color: var(--text-color);
            }}

            article {{
                background: var(--bg-color);
                margin: 1rem;
                border-radius: 0.75rem;
                overflow: hidden;
                box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
                transition: background-color 0.3s ease;
            }}

            .banner-image {{
                width: 100%;
                max-width: 800px;
                height: auto;
                margin: 0 auto 2rem auto;
                display: block;
                border-radius: 0.75rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
            }}

            .theme-toggle {{
                position: fixed;
                top: 1rem;
                right: 1rem;
                z-index: 1001;
                background: var(--bg-color);
                border: 1px solid var(--border-color);
                padding: 0.75rem 1rem;
                border-radius: 0.75rem;
                cursor: pointer;
                transition: all 0.3s ease;
                display: flex;
                align-items: center;
                gap: 0.75rem;
                font-size: 0.875rem;
                color: var(--text-color);
                box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
                backdrop-filter: blur(8px);
                -webkit-backdrop-filter: blur(8px);
            }}

            .theme-toggle i {{
                font-size: 1.125rem;
                transition: transform 0.3s ease;
            }}

            .theme-toggle:hover {{
                transform: translateY(-2px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
            }}

            .theme-toggle:hover i {{
                transform: rotate(15deg);
            }}

            .progress-bar {{
                position: fixed;
                top: 0;
                left: 0;
                width: 0%;
                height: 3px;
                background: var(--primary-color);
                z-index: 1000;
                transition: width 0.2s ease;
            }}

            .back-to-top {{
                position: fixed;
                bottom: 2rem;
                right: 2rem;
                background: var(--bg-color);
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
                color: var(--primary-color);
                border: 1px solid var(--border-color);
            }}

            .toc {{
                position: fixed;
                left: 2rem;
                top: 50%;
                transform: translateY(-50%);
                max-width: 250px;
                max-height: 80vh;
                overflow-y: auto;
                background: var(--bg-color);
                padding: 1.5rem;
                border-radius: 0.75rem;
                box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
                display: none;
                border: 1px solid var(--border-color);
                transition: background-color 0.3s ease;
            }}

            .toc a {{
                color: var(--text-color);
                text-decoration: none;
                transition: color 0.2s ease;
            }}

            .toc a:hover {{
                color: var(--primary-color);
            }}

            header {{
                background: var(--bg-color);
                border-bottom: 1px solid var(--border-color);
                transition: background-color 0.3s ease;
            }}

            header a {{
                color: var(--text-color);
                text-decoration: none;
                transition: color 0.2s ease;
            }}

            header a:hover {{
                color: var(--primary-color);
            }}

            footer {{
                background: var(--bg-color);
                color: var(--text-color);
                transition: background-color 0.3s ease;
            }}

            @media (min-width: 1400px) {{
                .toc {{
                    display: block;
                }}
            }}

            @media (max-width: 767px) {{
                .markdown-body {{
                    padding: 1.25rem;
                    font-size: 16px;
                }}

                .markdown-body p {{
                    font-weight: 300;
                    margin-bottom: 1rem;
                }}

                .markdown-body h1 {{
                    font-size: 1.75rem;
                }}

                .markdown-body h2 {{
                    font-size: 1.375rem;
                }}

                .markdown-body h3 {{
                    font-size: 1.25rem;
                }}

                article {{
                    margin: 0.5rem;
                }}

                .theme-toggle {{
                    top: 0.75rem;
                    right: 0.75rem;
                    padding: 0.5rem;
                }}

                .theme-toggle .theme-text {{
                    display: none;
                }}

                .theme-toggle i {{
                    font-size: 1.25rem;
                }}
            }}

            @media (min-width: 768px) {{
                .theme-toggle {{
                    opacity: 0.9;
                }}

                .theme-toggle:hover {{
                    opacity: 1;
                }}
            }}

            /* 代码块样式优化 */
            .markdown-body pre {{
                background-color: var(--bg-secondary) !important;
                border: 1px solid var(--border-color);
                border-radius: 0.5rem;
                padding: 1rem;
                margin: 1.5rem 0;
            }}

            .markdown-body code {{
                font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
                font-size: 0.9em;
                padding: 0.2em 0.4em;
                border-radius: 0.25rem;
                background-color: var(--bg-secondary);
                color: var(--primary-color);
            }}

            /* 引用块样式 */
            .markdown-body blockquote {{
                border-left: 4px solid var(--primary-color);
                margin: 1.5rem 0;
                padding: 0.5rem 1rem;
                color: var(--text-color);
                background-color: var(--bg-secondary);
                border-radius: 0 0.5rem 0.5rem 0;
            }}
        </style>
    </head>
    <body>
        <div class="progress-bar"></div>
        <button class="theme-toggle" onclick="toggleTheme()">
            <i class="fas fa-sun light-icon"></i>
            <i class="fas fa-moon dark-icon" style="display: none;"></i>
            <span class="theme-text">切换主题</span>
        </button>
        <header class="shadow-sm mb-8 sticky top-0 z-50">
            <div class="max-w-7xl mx-auto px-4 py-6">
                <nav class="flex items-center justify-between">
                    <a href="../../index.html" class="hover:text-primary flex items-center">
                        <i class="fas fa-arrow-left mr-2"></i>返回首页
                    </a>
                    <div class="text-sm breadcrumbs opacity-75">
                        <span>{category}</span>
                        <i class="fas fa-chevron-right mx-2"></i>
                        <span>{title}</span>
                    </div>
                </nav>
            </div>
        </header>
        <article class="markdown-body shadow-lg rounded-lg overflow-hidden relative">
            {banner_image}
            <div class="toc">
                <h3 class="text-lg font-medium mb-4">目录</h3>
                <div id="toc-content"></div>
            </div>
            {content}
        </article>
        <button class="back-to-top" onclick="window.scrollTo({{top: 0, behavior: 'smooth'}})">
            <i class="fas fa-arrow-up"></i>
        </button>
        <footer class="mt-12 py-6">
            <div class="max-w-7xl mx-auto px-4 text-center opacity-75">
                <p>© 2025 知识星球矩阵. All rights reserved.</p>
            </div>
        </footer>
        <script>
            // 主题切换
            function toggleTheme() {{
                const root = document.documentElement;
                const currentTheme = root.getAttribute('data-theme');
                const newTheme = currentTheme === 'dark' ? 'light' : 'dark';
                root.setAttribute('data-theme', newTheme);
                
                // 保存主题选择
                localStorage.setItem('theme', newTheme);
                
                // 更新图标
                const lightIcon = document.querySelector('.light-icon');
                const darkIcon = document.querySelector('.dark-icon');
                if (newTheme === 'dark') {{
                    lightIcon.style.display = 'none';
                    darkIcon.style.display = 'inline-block';
                }} else {{
                    lightIcon.style.display = 'inline-block';
                    darkIcon.style.display = 'none';
                }}
            }}

            // 初始化主题
            document.addEventListener('DOMContentLoaded', () => {{
                const savedTheme = localStorage.getItem('theme') || 'light';
                document.documentElement.setAttribute('data-theme', savedTheme);
                
                // 设置初始图标
                const lightIcon = document.querySelector('.light-icon');
                const darkIcon = document.querySelector('.dark-icon');
                if (savedTheme === 'dark') {{
                    lightIcon.style.display = 'none';
                    darkIcon.style.display = 'inline-block';
                }}
            }});

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
                            <a href="#${{id}}" class="hover:text-primary text-sm">
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
    course_titles = {
        'AI时代的老庄智慧研究所': '道法自然：AI时代的老庄智慧研究所',
        '区块链金融：从入门到精通': '区块链金融：从入门到精通',
        '德扑思维实验室': '德扑思维实验室：提升战略思考力'
    }

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
            original_title = os.path.basename(md_file).replace('.md', '')
            
            # Replace "开篇" with the course title for the first article
            if '开篇' in original_title:
                title = f'知识课程：{course_titles[folder]}'
            else:
                title = original_title
            
            # Only add banner image for opening articles
            banner_image = ''
            if '开篇' in original_title:
                banner_image = f'<img src="../images/{image_mapping[folder]}" alt="{title}" class="banner-image">'
            
            # Create HTML file with banner image
            category = folder
            html = html_template.format(
                title=title,
                content=html_content,
                banner_image=banner_image,
                category=category
            )
            
            # Save HTML file - replace "开篇" with "知识课程" in the filename
            output_filename = os.path.basename(md_file).replace('开篇', '知识课程').replace('.md', '.html')
            html_filename = os.path.join(articles_dir, output_filename)
            with open(html_filename, 'w', encoding='utf-8') as f:
                f.write(html)

if __name__ == '__main__':
    # Create articles directory
    os.makedirs('articles', exist_ok=True)
    convert_markdown_to_html() 