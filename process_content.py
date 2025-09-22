import re
import os
import sys

def create_css():
    css_content = '''/* AI洞察日报 - 防弹版 */

h1:first-of-type {
  display: none;
}

.content {
  max-width: none !important;
  overflow: visible !important;
  line-height: 1.7 !important;
  word-wrap: break-word;
  word-break: break-word;
}

:root {
  --primary-color: #ff9900;
  --primary-light: #ffaa33;
  --primary-dark: #e68800;
}

/* 分类标签样式 */
.content blockquote {
  background: linear-gradient(135deg, rgba(255, 153, 0, 0.1), rgba(255, 153, 0, 0.03));
  border: none;
  border-left: 4px solid var(--primary-color);
  border-radius: 8px;
  padding: 1rem 1.5rem;
  margin: 1.5rem 0;
  box-shadow: 0 2px 8px rgba(255, 153, 0, 0.1);
}

.content blockquote p {
  margin: 0 !important;
  color: var(--primary-color) !important;
  font-weight: 600 !important;
  font-size: 0.95rem !important;
}

.content blockquote code {
  background-color: rgba(255, 153, 0, 0.2) !important;
  color: var(--primary-dark) !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  font-weight: 600 !important;
  border: 1px solid rgba(255, 153, 0, 0.3) !important;
}

/* 新闻条目样式 */
.content ol li,
.content ul li {
  margin-bottom: 1.5rem !important;
  padding: 1.2rem !important;
  background: rgba(255, 153, 0, 0.02) !important;
  border-radius: 8px !important;
  border-left: 3px solid var(--primary-color) !important;
  transition: all 0.3s ease !important;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05) !important;
}

.content ol li:hover,
.content ul li:hover {
  background: rgba(255, 153, 0, 0.05) !important;
  transform: translateX(4px) !important;
  box-shadow: 0 4px 12px rgba(255, 153, 0, 0.15) !important;
}

/* 分类标题样式 */
.content h3 {
  color: var(--primary-color) !important;
  border-bottom: 2px solid rgba(255, 153, 0, 0.2);
  padding-bottom: 0.5rem;
  margin: 2rem 0 1rem 0 !important;
  font-weight: 700 !important;
}

/* 链接样式 */
.content a {
  color: var(--primary-color) !important;
  text-decoration: none !important;
  font-weight: 500 !important;
  transition: all 0.2s ease !important;
}

.content a:hover {
  color: var(--primary-dark) !important;
  text-decoration: underline !important;
}

/* 强调文本 */
.content strong {
  color: var(--primary-color) !important;
  font-weight: 700 !important;
}

/* 图片样式 */
.content img {
  margin: 1rem auto !important;
  border-radius: 8px !important;
  max-width: 100% !important;
  height: auto !important;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1) !important;
}

/* 代码样式 */
.content code {
  background-color: rgba(255, 153, 0, 0.1) !important;
  color: var(--primary-dark) !important;
  padding: 2px 6px !important;
  border-radius: 4px !important;
  font-size: 0.9em !important;
}

/* 深色模式样式 */
html.dark .content blockquote {
  background: linear-gradient(135deg, rgba(255, 153, 0, 0.15), rgba(255, 153, 0, 0.05)) !important;
  border-left-color: #ff9900 !important;
  box-shadow: 0 4px 16px rgba(255, 153, 0, 0.2) !important;
}

html.dark .content blockquote p {
  color: #ff9900 !important;
}

html.dark .content blockquote code {
  background-color: rgba(255, 153, 0, 0.25) !important;
  color: #ffaa33 !important;
  border-color: rgba(255, 153, 0, 0.4) !important;
}

html.dark .content ol li,
html.dark .content ul li {
  background: rgba(255, 153, 0, 0.08) !important;
  border-left-color: #ff9900 !important;
  color: #f0f0f0 !important;
  box-shadow: 0 2px 8px rgba(255, 153, 0, 0.1) !important;
}

html.dark .content ol li:hover,
html.dark .content ul li:hover {
  background: rgba(255, 153, 0, 0.15) !important;
  box-shadow: 0 6px 20px rgba(255, 153, 0, 0.25) !important;
}

html.dark .content h2,
html.dark .content h3,
html.dark .content h4 {
  color: #ff9900 !important;
  border-bottom-color: rgba(255, 153, 0, 0.3) !important;
}

html.dark .content a {
  color: #ff9900 !important;
}

html.dark .content a:hover {
  color: #ffaa33 !important;
}

html.dark .content strong {
  color: #ff9900 !important;
}

html.dark .content code {
  background-color: #2a2a2a !important;
  color: #ff9900 !important;
  border: 1px solid #444 !important;
}

html.dark .content img {
  box-shadow: 0 8px 32px rgba(255, 153, 0, 0.15) !important;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .content {
    padding: 1rem !important;
  }
  
  .content ol li,
  .content ul li {
    padding: 1rem !important;
  }
  
  .content blockquote {
    padding: 1rem !important;
  }
}
'''
    with open('assets/css/custom.css', 'w', encoding='utf-8') as f:
        f.write(css_content)
    print("✅ 防弹版CSS已创建")

def create_index_files():
    # 创建根目录首页
    root_index = '''---
title: AI洞察日报
---

# AI洞察日报

**精选AI新闻与深度分析** | 每日为您过滤信息噪音，提供最精选的AI资讯

[查看最新日报 →](/cn/)
'''
    with open('content/_index.md', 'w', encoding='utf-8') as f:
        f.write(root_index)
    
    # 创建cn目录主页
    cn_index = '''---
linkTitle: AI Daily
title: AI Daily-AI资讯日报
breadcrumbs: false
description: "个人每日整理的AI资讯站。我们为您过滤信息噪音，只提供最精选的AI新闻、最实用的AI工具与AI教程，助您高效获取人工智能领域的前沿动态"
cascade:
  type: docs
---

## AI资讯日报

>  `AI资讯` | `每日早读` | `全网数据聚合` | `前沿科学探索` | `行业自由发声` | `开源创新力量` | `AI与人类未来` | [访问网页版↗️](https://april8000.github.io/Hextra-AI-Insight-Daily/)

欢迎来到AI洞察日报！这里为您提供每日精选的AI资讯和深度分析。

## 🔥 最新动态

浏览左侧的日期导航查看最新的AI日报内容，每日更新，精彩不断！
'''
    with open('content/cn/_index.md', 'w', encoding='utf-8') as f:
        f.write(cn_index)
    print("✅ 防弹版索引文件已创建")

def process_daily_content(source_file_path, target_file):
    # 读取原始内容
    with open(source_file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 提取日期
    filename = os.path.basename(source_file_path)
    date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
    if not date_match:
        return False
    
    date_part = date_match.group(1)
    date_display = date_part.replace('-', '/')
    
    # 智能提取摘要内容
    lines = content.split('\n')
    summary_lines = []
    
    for line in lines:
        line = line.strip()
        if line and len(line) > 15:
            if (not line.startswith('#') and 
                not line.startswith('```') and 
                not line.startswith('---') and
                not re.match(r'^\d+\.', line) and 
                not line.startswith('- ') and 
                not line.startswith('* ') and
                not line.startswith('>')):
                summary_lines.append(line)
                if len(summary_lines) >= 3:
                    break
    
    if summary_lines:
        summary_content = '\n'.join(summary_lines[:3])
    else:
        summary_content = f"{date_display}的AI行业动态汇总，包含最新产品发布、技术突破、行业投资等重要资讯。"
    
    # 分类新闻内容
    product_news = []
    research_news = []
    industry_news = []
    opensource_news = []
    social_news = []
    
    current_item = ""
    for line in lines:
        if line.strip() and (re.match(r'^\d+\.', line) or line.startswith('- ') or line.startswith('* ')):
            if current_item and len(current_item.strip()) > 20:
                if re.search(r'产品|功能|更新|发布|工具|平台|API|服务|模型|应用', current_item, re.IGNORECASE):
                    product_news.append(current_item.strip())
                elif re.search(r'研究|论文|学术|科学|实验|算法|框架', current_item, re.IGNORECASE):
                    research_news.append(current_item.strip())
                elif re.search(r'投资|融资|IPO|商业|公司|估值|行业|市场|影响|展望', current_item, re.IGNORECASE):
                    industry_news.append(current_item.strip())
                elif re.search(r'开源|GitHub|代码|开发者|项目|库|仓库', current_item, re.IGNORECASE):
                    opensource_news.append(current_item.strip())
                elif re.search(r'社交|媒体|分享|讨论|用户|社区|推特|微博', current_item, re.IGNORECASE):
                    social_news.append(current_item.strip())
                else:
                    product_news.append(current_item.strip())
            current_item = line
        elif line.strip() and current_item:
            current_item += '\n' + line
    
    # 处理最后一个条目
    if current_item and len(current_item.strip()) > 20:
        if re.search(r'产品|功能|更新|发布|工具|平台|API|服务|模型|应用', current_item, re.IGNORECASE):
            product_news.append(current_item.strip())
        elif re.search(r'研究|论文|学术|科学|实验|算法|框架', current_item, re.IGNORECASE):
            research_news.append(current_item.strip())
        elif re.search(r'投资|融资|IPO|商业|公司|估值|行业|市场|影响|展望', current_item, re.IGNORECASE):
            industry_news.append(current_item.strip())
        elif re.search(r'开源|GitHub|代码|开发者|项目|库|仓库', current_item, re.IGNORECASE):
            opensource_news.append(current_item.strip())
        elif re.search(r'社交|媒体|分享|讨论|用户|社区|推特|微博', current_item, re.IGNORECASE):
            social_news.append(current_item.strip())
        else:
            product_news.append(current_item.strip())
    
    # 创建Front Matter
    front_matter = f"""---
linkTitle: {date_part[5:]}-日报
title: {date_part[5:]}-日报-AI资讯日报
weight: 1
breadcrumbs: false
comments: true
description: "个人每日整理的AI资讯站。我们为您过滤信息噪音，只提供最精选的AI新闻、最实用的AI工具与AI教程，助您高效获取人工智能领域的前沿动态"
---

"""
    
    # 创建内容主体
    content_body = f"""## AI资讯日报 {date_display}

>  `AI资讯` | `每日早读` | `全网数据聚合` | `前沿科学探索` | `行业自由发声` | `开源创新力量` | `AI与人类未来` | [访问网页版↗️](https://april8000.github.io/Hextra-AI-Insight-Daily/)



### **今日摘要**

```
{summary_content}
```


"""
    
    # 添加分类内容
    if product_news:
        content_body += "\n### 产品与功能更新\n"
        for i, news in enumerate(product_news[:5], 1):
            clean_news = re.sub(r'^\d+\.\s*', '', news)
            content_body += f"{i}.  {clean_news}\n"
    
    if research_news:
        content_body += "\n### 前沿研究\n"
        for i, news in enumerate(research_news[:3], 1):
            clean_news = re.sub(r'^\d+\.\s*', '', news)
            content_body += f"{i}.  {clean_news}\n"
    
    if industry_news:
        content_body += "\n### 行业展望与社会影响\n"
        for i, news in enumerate(industry_news[:3], 1):
            clean_news = re.sub(r'^\d+\.\s*', '', news)
            content_body += f"{i}.  {clean_news}\n"
    
    if opensource_news:
        content_body += "\n### 开源TOP项目\n"
        for i, news in enumerate(opensource_news[:4], 1):
            clean_news = re.sub(r'^\d+\.\s*', '', news)
            content_body += f"{i}.  {clean_news}\n"
    
    if social_news:
        content_body += "\n### 社媒分享\n"
        for i, news in enumerate(social_news[:5], 1):
            clean_news = re.sub(r'^\d+\.\s*', '', news)
            content_body += f"{i}.  {clean_news}\n"
    
    # 写入文件
    os.makedirs(os.path.dirname(target_file), exist_ok=True)
    with open(target_file, "w", encoding="utf-8") as f:
        f.write(front_matter + content_body)
    
    print(f"✅ 防弹版文件已创建: {target_file}")
    return True

def create_month_index(target_dir, year_month):
    month_index_file = os.path.join(target_dir, '_index.md')
    if not os.path.exists(month_index_file):
        month_index = f"""---
title: "{year_month} AI日报"
date: {year_month}-01T00:00:00+08:00
type: docs
sidebar:
  open: true
weight: 1
---

# {year_month} AI洞察日报

本月的AI行业动态和技术趋势汇总，精选重要资讯。
"""
        with open(month_index_file, 'w', encoding='utf-8') as f:
            f.write(month_index)
        print(f"✅ 月份索引已创建: {month_index_file}")

if __name__ == "__main__":
    create_css()
    create_index_files()
    
    # 处理日报文件
    import glob
    source_files = glob.glob("source-repo/daily/*.md")
    source_files.sort(reverse=True)
    
    for source_file_path in source_files[:20]:  # 最多处理20个文件
        filename = os.path.basename(source_file_path)
        date_match = re.search(r'(\d{4}-\d{2}-\d{2})', filename)
        if date_match:
            date_part = date_match.group(1)
            year_month = date_part[:7]
            
            target_dir = f"content/cn/{year_month}"
            target_file = os.path.join(target_dir, filename)
            
            if process_daily_content(source_file_path, target_file):
                create_month_index(target_dir, year_month)
    
    print("--- 防弹版设置完成 ---")
