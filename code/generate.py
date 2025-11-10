# coding=utf-8
"""
Generate profile README files.

Author: Frank Jiang
E-mail: frank.jf@alibaba-inc.com
Date: 10/31 03:17:35
"""

from urllib.parse import quote
import json


def qs(s, safe="") -> str:
    out = quote(s, safe=safe)
    return out.replace("-", "%20")


class Badge(object):
    """Badge class to generate markdown badge strings."""

    def __init__(self, id, label, badge_url, url):
        self.id = id
        self.label = label
        self.badge_url = badge_url
        self.url = url

    def to_markdown(self) -> str:
        """Generate markdown string for the badge."""
        return f"[![{self.label}]({self.badge_url})]({self.url})"


class Project(Badge):
    """Project badge class."""

    def __init__(self, id, url):
        label = "Project"
        badge_url = f"https://img.shields.io/badge/🌐%20%20Project-{qs(id)}-blue.svg"
        super().__init__(id, label, badge_url, url)


class ArXiv(Badge):
    """ArXiv badge class."""

    def __init__(self, id):
        label = "arXiv"
        badge_url = f"https://img.shields.io/badge/Arxiv-{id}-b31b1b.svg?logo=arXiv"
        url = f"https://arxiv.org/abs/{id}"
        super().__init__(id, label, badge_url, url)


class Publish(Badge):
    """Publish badge class."""

    def __init__(self, id, url, publisher="conference"):
        label = "Conference"
        prefix = "🏛  Conference"
        if publisher.lower() == "journal":
            prefix = "📗  Journal"
        elif publisher.lower() == "report":
            prefix = "📖  Report"
        else:
            raise ValueError("Publisher must be 'conference', 'journal', or 'report'.")
        badge_url = f"https://img.shields.io/badge/{prefix}-{id}-green.svg"
        super().__init__(id, label, badge_url, url)


class GitHub(Badge):
    """GitHub badge class."""

    def __init__(self, repo, id="Code", stars: bool = True, not_finished: bool = False):
        label = "GitHub"
        if not_finished:
            id = "Code (Comming Soon)"
        badge_url = (
            f"https://img.shields.io/badge/{qs(id)}-{label}-181717.svg?logo=GitHub"
        )
        url = f"https://github.com/{repo}"
        super().__init__(repo, label, badge_url, url)
        self.repo = repo
        self.stars = stars

        if not_finished:
            id = "Code (Comming Soon)"
            self.stars = False

    def to_markdown(self) -> str:
        return super().to_markdown() + (
            f"\n![GitHub Stars](https://img.shields.io/github/stars/{self.repo})"
            if self.stars
            else ""
        )


class HuggingFace(Badge):
    """HuggingFace badge class."""

    def __init__(
        self,
        repo,
        id="HuggingFace",
        model: bool = False,
        space: bool = False,
        dataset: bool = False,
    ):
        super().__init__(id, "HuggingFace", None, None)

        self.repo = repo
        self.model = model
        self.space = space
        self.dataset = dataset
        assert (
            model or space or dataset
        ), "At least one of model, space, or dataset must be True."

    def to_markdown(self) -> str:

        selected_items = []
        if self.model:
            selected_items.append(
                f"[![HuggingFace Model](https://img.shields.io/badge/🤗-HuggingFace-FFD21E.svg)](https://huggingface.co/{self.repo})"
            )
        if self.space:
            selected_items.append(
                f"[![HuggingFace Space](https://img.shields.io/badge/🤗-HuggingFace%20Space-FFD21E.svg)](https://huggingface.co/spaces/{self.repo})"
            )
        if self.dataset:
            selected_items.append(
                f"[![HuggingFace Dataset](https://img.shields.io/badge/🤗-HuggingFace%20Dataset-FFD21E.svg)](https://huggingface.co/datasets/{self.repo})"
            )
        return "\n".join(selected_items) if selected_items else ""


class ModelScope(Badge):
    """ModelScope badge class."""

    def __init__(
        self,
        repo,
        id="ModelScope",
        model: bool = True,
        studio: bool = False,
        dataset: bool = False,
    ):

        super().__init__(id, "ModelScope", None, None)

        self.prefix = "👾"
        self.repo = repo
        self.model = model
        self.studio = studio
        self.dataset = dataset
        assert (
            model or studio or dataset
        ), "At least one of model, studio, or dataset must be True."

    def to_markdown(self) -> str:

        selected_items = []

        if self.model:
            selected_items.append(
                f"[![ModelScope](https://img.shields.io/badge/{self.prefix}-ModelScope-604DF4.svg)](https://modelscope.cn/models/{self.repo})"
            )
        if self.studio:
            selected_items.append(
                f"[![ModelScope Studio](https://img.shields.io/badge/{self.prefix}-ModelScope%20Studio-604DF4.svg.svg)](https://modelscope.cn/studios/{self.repo})"
            )
        if self.dataset:
            selected_items.append(
                f"[![ModelScope Dataset](https://img.shields.io/badge/{self.prefix}-ModelScope%20Dataset-604DF4.svg.svg)](https://modelscope.cn/datasets/{self.repo})"
            )
        return "\n".join(selected_items) if selected_items else ""


def create_badge(badge_type: str, **kwargs) -> Badge:
    """Factory method to create badge instances based on badge type."""
    badge_type = badge_type.lower()
    if badge_type == "project":
        return Project(**kwargs)
    elif badge_type == "arxiv":
        return ArXiv(**kwargs)
    elif badge_type == "publish":
        return Publish(**kwargs)
    elif badge_type == "github":
        return GitHub(**kwargs)
    elif badge_type == "huggingface":
        return HuggingFace(**kwargs)
    elif badge_type == "modelscope":
        return ModelScope(**kwargs)
    else:
        raise ValueError(f"Unsupported badge type: {badge_type}")


def create_readme(
    topics: list, template_file: str, output_file: str, locale: None
) -> str:
    """Create README content from papers list."""

    lines = []
    suffix = "_zh" if locale == "zh" else ""
    orders = ["project", "arxiv", "github", "huggingface", "modelscope"]

    for topic in topics:
        if not topic.get("icon") or not topic.get(f"title{suffix}"):
            continue
        lines.extend(
            [
                f'## {topic["icon"]} {topic[f"title{suffix}"]}\n',
                f'{topic[f"intro{suffix}"]}\n<br><br>\n',
            ]
        )

        if papers := topic.get("papers", []):
            for paper in papers:
                lines.append(f'### {paper["title"]}\n')
                lines.extend(
                    create_badge(badge, **paper[badge]).to_markdown()
                    for badge in orders
                    if badge in paper
                )
                lines.append(f'\n{paper[f"intro{suffix}"]}\n<br><br>\n')
        else:
            lines.append("Comming soon...\n")

    with open(template_file, "r", encoding="utf-8") as f:
        template = f.read()
    template = template.replace("<!-- Auto-generated Papers -->", "\n".join(lines))
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(template)


if __name__ == "__main__":

    with open("code/content.json", "r", encoding="utf-8") as f:
        topics = json.load(f)

    create_readme(
        topics,
        template_file="code/README.md",
        output_file="profile//README.md",
        locale=None,
    )
    create_readme(
        topics,
        template_file="code/README_zh.md",
        output_file="profile/README_zh.md",
        locale="zh",
    )
    print("Done.")
