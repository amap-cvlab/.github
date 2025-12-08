# coding=utf-8
"""
Generate profile README files (Markdown) and Website (HTML).
Reads from content.json (papers) and static.json (static text).
Links external style.css and script.js.
"""

import json
import os
import re
from urllib.parse import quote

# --- 全局配置 ---
DEFAULT_STARS = True  # 默认是否显示 GitHub Stars


# ----------------------------
# 1. 辅助函数：Markdown 转 HTML
# ----------------------------
def md_to_html(text):
    if not text:
        return ""
    # Bold
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.*?)\*", r"<em>\1</em>", text)
    # Link
    text = re.sub(r"\[(.*?)\]\((.*?)\)", r'<a href="\2" target="_blank">\1</a>', text)
    # Newlines
    text = text.replace("\n", "<br>")
    return text


def qs(s, safe="") -> str:
    out = quote(s, safe=safe)
    return out.replace("-", "%20")


# ----------------------------
# 2. Badge 类定义 (用于 Markdown)
# ----------------------------
class Badge(object):
    def __init__(self, id, label, badge_url, url):
        self.id, self.label, self.badge_url, self.url = id, label, badge_url, url

    def to_markdown(self) -> str:
        return f"[![{self.label}]({self.badge_url})]({self.url})"


class Project(Badge):
    def __init__(self, id, url):
        super().__init__(
            id,
            "Project",
            f"https://img.shields.io/badge/🌐%20%20Project-{qs(id)}-blue.svg",
            url,
        )


class ArXiv(Badge):
    def __init__(self, id):
        super().__init__(
            id,
            "arXiv",
            f"https://img.shields.io/badge/Arxiv-{id}-b31b1b.svg?logo=arXiv",
            f"https://arxiv.org/abs/{id}",
        )


class Publish(Badge):
    def __init__(self, id, url, publisher="conference"):
        prefix = "🏛  Conference"
        if publisher.lower() == "journal":
            prefix = "📗  Journal"
        elif publisher.lower() == "report":
            prefix = "📖  Report"
        super().__init__(
            id,
            "Conference",
            f"https://img.shields.io/badge/{qs(prefix)}-{qs(id)}-green.svg",
            url,
        )


class GitHub(Badge):
    def __init__(self, repo, id="Code", stars=None, not_finished=False):
        label = "GitHub"
        if not_finished:
            id = "Code (Comming Soon)"
        self.stars = stars if stars is not None else DEFAULT_STARS
        self.stars = self.stars and not not_finished
        super().__init__(
            id,
            label,
            f"https://img.shields.io/badge/{qs(id)}-{label}-181717.svg?logo=GitHub",
            f"https://github.com/{repo}",
        )
        self.repo = repo

    def to_markdown(self) -> str:
        base = super().to_markdown()
        return base + (
            f"\n![GitHub Stars](https://img.shields.io/github/stars/{self.repo})"
            if self.stars
            else ""
        )


class HuggingFace(Badge):
    def __init__(self, repo, id="HuggingFace", model=False, space=False, dataset=False):
        super().__init__(id, "HuggingFace", None, None)
        self.repo, self.model, self.space, self.dataset = repo, model, space, dataset

    def to_markdown(self) -> str:
        items = []
        if self.model:
            items.append(
                f"[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/{self.repo})"
            )
        if self.space:
            items.append(
                f"[![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-FFD21E.svg)](https://huggingface.co/spaces/{self.repo})"
            )
        if self.dataset:
            items.append(
                f"[![HuggingFace Dataset](https://img.shields.io/badge/🤗-HuggingFace%20Dataset-FFD21E.svg)](https://huggingface.co/datasets/{self.repo})"
            )
        return "\n".join(items) if items else ""


class ModelScope(Badge):
    def __init__(self, repo, id="ModelScope", model=True, studio=False, dataset=False):
        super().__init__(id, "ModelScope", None, None)
        self.repo, self.model, self.studio, self.dataset = repo, model, studio, dataset

    def to_markdown(self) -> str:
        items = []
        if self.model:
            items.append(
                f"[![ModelScope](https://img.shields.io/badge/👾-ModelScope-604DF4.svg)](https://modelscope.cn/models/{self.repo})"
            )
        if self.studio:
            items.append(
                f"[![ModelScope Studio](https://img.shields.io/badge/👾-ModelScope%20Studio-604DF4.svg.svg)](https://modelscope.cn/studios/{self.repo})"
            )
        if self.dataset:
            items.append(
                f"[![ModelScope Dataset](https://img.shields.io/badge/👾-ModelScope%20Dataset-604DF4.svg.svg)](https://modelscope.cn/datasets/{self.repo})"
            )
        return "\n".join(items) if items else ""


def create_badge(badge_type: str, **kwargs) -> Badge:
    badge_type = badge_type.lower()
    mapping = {
        "project": Project,
        "arxiv": ArXiv,
        "publish": Publish,
        "github": GitHub,
        "huggingface": HuggingFace,
        "modelscope": ModelScope,
    }
    return mapping[badge_type](**kwargs) if badge_type in mapping else None


# ----------------------------
# 3. HTML Badge 生成器
# ----------------------------
def create_html_badge(badge_type, data):
    url, icon, label = "", "", ""
    badge_type = badge_type.lower()

    if badge_type == "project":
        url, label, icon = data.get("url", "#"), "Project", "fas fa-globe"
    elif badge_type == "arxiv":
        url, label, icon = (
            f"https://arxiv.org/abs/{data.get('id', '')}",
            "arXiv",
            "fas fa-file-pdf",
        )
    elif badge_type == "publish":
        url, label, icon = (
            data.get("url", "#"),
            data.get("id", "Conference"),
            "fas fa-landmark",
        )
    elif badge_type == "huggingface":
        url, label, icon = (
            f"https://huggingface.co/{data.get('repo', '')}",
            "HuggingFace",
            "fas fa-face-smile",
        )
    elif badge_type == "modelscope":
        url, label, icon = (
            f"https://modelscope.cn/models/{data.get('repo', '')}",
            "ModelScope",
            "fas fa-cube",
        )

    # --- GitHub 特殊处理 ---
    elif badge_type == "github":
        repo = data.get("repo", "")
        url = f"https://github.com/{repo}"
        label = "Code"
        not_finished = data.get("not_finished", False)
        if not_finished:
            label = "Coming Soon"
        show_stars = data.get("stars", DEFAULT_STARS)
        data_attr = (
            f'data-github-repo="{repo}"' if (show_stars and not not_finished) else ""
        )

        html = (
            f'<a href="{url}" target="_blank" class="badge badge-github" {data_attr}>'
        )
        html += f'<i class="fab fa-github"></i> {label}'
        if show_stars and not not_finished:
            html += f'<span class="star-suffix" style="display:none"> (<span class="star-count"></span> <i class="fas fa-star"></i>)</span>'
        html += "</a>"
        return html

    else:
        return ""

    return f'<a href="{url}" target="_blank" class="badge badge-{badge_type}"><i class="{icon}"></i> {label}</a>'


# ----------------------------
# 4. 生成器逻辑
# ----------------------------
def generate_markdown(static_data, content_data, locale, output_file):
    lines = []
    suffix = "_zh" if locale == "zh" else ""
    s = static_data

    lines.append(f"# {s['hero']['title']}\n")
    link_md = "README_zh.md" if locale == "en" else "README.md"
    label_md = "中文阅读" if locale == "en" else "For English"
    lines.append(f"[{label_md}]({link_md})\n")

    lines.append(f"# 👋 {s['nav']['home']}\n")
    lines.append(f"{s['hero']['desc']}\n")
    lines.append(f"{s['hero']['intro']}\n")
    for d in s["hero"]["domains"]:
        lines.append(f"- {d}")
    lines.append(f"\n{s['hero']['outro']}\n")
    lines.append("---\n")
    lines.append(f"{s['welcome']}\n")

    lines.append(f"# 🔈 {s['news']['title']}\n")
    for item in s["news"]["items"]:
        lines.append(f"- {item}")
    lines.append("\n")

    lines.append(f"# 🔧 {s['tech']['title']}\n")
    badge_order = ["project", "publish", "arxiv", "github", "huggingface", "modelscope"]

    for topic in content_data:
        t_title = topic.get(f"title{suffix}")
        t_intro = topic.get(f"intro{suffix}")
        if not t_title:
            continue

        lines.append(f"## {topic['icon']} {t_title}\n")
        lines.append(f"{t_intro}\n<br><br>\n")

        for paper in topic.get("papers", []):
            if not paper.get("title"):
                continue
            lines.append(f"### {paper['title']}\n")
            for b_type in badge_order:
                if b_type in paper:
                    badge_obj = create_badge(b_type, **paper[b_type])
                    if badge_obj:
                        lines.append(badge_obj.to_markdown())
            p_intro = paper.get(f"intro{suffix}", "")
            lines.append(f"\n{p_intro}\n<br><br>\n")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"✅ Generated Markdown: {output_file}")


def generate_html(static_data, content_data, locale, output_file):
    suffix = "_zh" if locale == "zh" else ""
    s = static_data

    template = """<!DOCTYPE html>
<html lang="{lang}">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{hero_title}</title>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <link rel="stylesheet" href="style.css">
</head>
<body>
    <nav>
        <div class="logo-area">
            <img src="profile/assets/amap-cvlab.png" alt="Logo">
            <span>{hero_title}</span>
        </div>
        <div class="nav-links">
            <a href="#about">{nav_home}</a>
            <a href="#news">{nav_news}</a>
            <a href="#tech">{nav_tech}</a>
            <a href="{lang_link}" class="lang-btn">{lang_label}</a>
        </div>
    </nav>

    <section class="hero" id="about">
        <h1>{hero_title}</h1>
        <div class="hero-content">
            <p>{hero_desc}</p>
            <p>{hero_intro}</p>
            <ul>{hero_domains}</ul>
            <p>{hero_outro}</p>
        </div>
    </section>

    <div class="container">
        <section id="news" style="margin-bottom: 4rem;">
            <h2 class="section-title">{news_title}</h2>
            <ul class="news-list">{news_html}</ul>
        </section>

        <section id="tech">
            <h2 class="section-title">{tech_title}</h2>
            {papers_html}
        </section>
    </div>

    <footer><p>{footer}</p></footer>
    <script src="script.js"></script>
</body>
</html>"""

    # 1. Process Static Content
    hero_desc = md_to_html(s["hero"]["desc"])
    hero_intro = md_to_html(s["hero"]["intro"])
    hero_outro = md_to_html(s["hero"]["outro"]).replace("\n", "<br>")
    domain_html = "".join([f"<li>{md_to_html(d)}</li>" for d in s["hero"]["domains"]])
    news_html = "".join([f"<li>{md_to_html(item)}</li>" for item in s["news"]["items"]])

    # 2. Process Papers
    papers_html = ""
    badge_order = ["project", "publish", "arxiv", "github", "huggingface", "modelscope"]

    for topic in content_data:
        t_title = topic.get(f"title{suffix}")
        t_intro = topic.get(f"intro{suffix}")
        if not t_title:
            continue

        # --- 修复：对板块介绍 t_intro 进行 Markdown 转 HTML 处理 ---
        t_intro_html = md_to_html(t_intro)

        papers_html += f"""
        <div class="domain-block">
            <div class="domain-header">
                <div class="domain-icon">{topic.get("icon", "")}</div>
                <div class="domain-title">{t_title}</div>
            </div>
            <div class="domain-intro">{t_intro_html}</div>
            <div class="papers-grid">
        """

        for paper in topic.get("papers", []):
            if not paper.get("title"):
                continue

            p_title = paper.get("title")

            # --- 修复：对论文介绍 p_desc 进行 Markdown 转 HTML 处理 ---
            p_desc_raw = paper.get(f"intro{suffix}", "")
            p_desc_html = md_to_html(p_desc_raw)

            badges_html = ""
            for b_type in badge_order:
                if b_type in paper:
                    badges_html += create_html_badge(b_type, paper[b_type])

            papers_html += f"""
                <div class="paper-card">
                    <div class="paper-title">{p_title}</div>
                    <div class="paper-desc">{p_desc_html}</div>
                    <div class="badge-container">{badges_html}</div>
                </div>
            """
        papers_html += "</div></div>"

    final_html = template.format(
        lang=locale,
        hero_title=s["hero"]["title"],
        nav_home=s["nav"]["home"],
        nav_news=s["nav"]["news"],
        nav_tech=s["nav"]["tech"],
        lang_link=s["nav"]["lang_link"],
        lang_label=s["nav"]["lang_label"],
        hero_desc=hero_desc,
        hero_intro=hero_intro,
        hero_domains=domain_html,
        hero_outro=hero_outro,
        news_title=s["news"]["title"],
        news_html=news_html,
        tech_title=s["tech"]["title"],
        papers_html=papers_html,
        footer=s["footer"],
    )

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(final_html)
    print(f"✅ Generated HTML: {output_file}")


if __name__ == "__main__":
    base_dir = "code" if os.path.exists("code") else "."

    def load_json(filename):
        path = os.path.join(base_dir, filename)
        if not os.path.exists(path):
            path = filename
        if os.path.exists(path):
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        return None

    content_data = load_json("content.json")
    static_data = load_json("static.json")

    if content_data and static_data:
        generate_markdown(static_data["en"], content_data, "en", "README.md")
        generate_html(static_data["en"], content_data, "en", "index.html")
        generate_markdown(static_data["zh"], content_data, "zh", "README_zh.md")
        generate_html(static_data["zh"], content_data, "zh", "index.zh.html")
        print("🎉 All files generated successfully!")
    else:
        print("❌ Error: Missing json files")
