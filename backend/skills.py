import re
from typing import Iterable, Optional, Set


COMMON_SKILLS = {
    "python",
    "java",
    "javascript",
    "typescript",
    "es6",
    "dom",
    "c",
    "c++",
    "c#",
    "go",
    "rust",
    "ruby",
    "php",
    "sql",
    "postgresql",
    "mysql",
    "mongodb",
    "redis",
    "graphql",
    "rest api",
    "rest apis",
    "rest",
    "node.js",
    "react",
    "next.js",
    "vue",
    "vue.js",
    "nuxt",
    "svelte",
    "angular",
    "html",
    "html5",
    "css",
    "css3",
    "sass",
    "scss",
    "less",
    "tailwind",
    "bootstrap",
    "material ui",
    "chakra ui",
    "styled components",
    "redux",
    "redux toolkit",
    "zustand",
    "mobx",
    "react query",
    "tanstack query",
    "storybook",
    "jest",
    "cypress",
    "playwright",
    "vitest",
    "testing library",
    "vite",
    "webpack",
    "babel",
    "eslint",
    "prettier",
    "figma",
    "responsive design",
    "accessibility",
    "a11y",
    "seo",
    "performance",
    "performance optimization",
    "pwa",
    "firebase",
    "supabase",
    "vercel",
    "netlify",
    "github",
    "gitlab",
    "npm",
    "yarn",
    "pnpm",
    "docker",
    "kubernetes",
    "aws",
    "gcp",
    "azure",
    "linux",
    "git",
    "ci/cd",
    "terraform",
    "spark",
    "hadoop",
    "airflow",
    "fastapi",
    "django",
    "flask",
    "pandas",
    "numpy",
    "scikit-learn",
    "machine learning",
    "tensorflow",
    "pytorch",
    "keras",
    "data analysis",
    "data engineering",
    "data science",
    "statistics",
    "linear algebra",
    "probability",
    "deep learning",
    "neural networks",
    "nlp",
    "computer vision",
    "jupyter",
    "anaconda",
    "product management",
    "project management",
    "agile",
    "scrum",
    "ui/ux",
}

SKILL_SYNONYMS = {
    "javascript": {"js"},
    "typescript": {"ts"},
    "node.js": {"node", "nodejs"},
    "next.js": {"nextjs"},
    "c++": {"cpp"},
    "c#": {"csharp"},
    "postgresql": {"postgres", "postgre"},
    "ci/cd": {"cicd", "ci cd"},
    "machine learning": {"ml"},
    "ui/ux": {"ux", "ui"},
    "material ui": {"mui"},
    "styled components": {"styled-components"},
    "react query": {"tanstack query"},
    "rest api": {"rest apis", "restful api", "restful"},
    "responsive design": {"responsive"},
    "tensorflow": {"tf"},
    "pytorch": {"torch"},
    "scikit-learn": {"sklearn"},
    "natural language processing": {"nlp"},
    "neural networks": {"nn", "neural net"},
    "deep learning": {"dl"},
    "linear algebra": {"linalg"},
    "computer vision": {"cv"},
    "jupyter": {"jupyter notebook"},
}

ROLE_KEYWORDS = {
    "frontend": {"frontend", "front-end", "front end", "ui", "web"},
    "backend": {"backend", "back-end", "back end", "api", "server"},
    "fullstack": {"fullstack", "full stack"},
    "data": {"data engineer", "data scientist", "ml", "machine learning", "analytics"},
    "devops": {"devops", "sre", "platform", "infrastructure"},
}

ROLE_SKILLS = {
    "frontend": {
        "html",
        "html5",
        "css",
        "css3",
        "javascript",
        "typescript",
        "react",
        "next.js",
        "vue",
        "angular",
        "responsive design",
        "accessibility",
        "rest api",
        "rest apis",
        "jest",
        "cypress",
        "testing library",
        "webpack",
        "vite",
        "git",
        "github",
        "tailwind",
        "bootstrap",
        "figma",
    },
    "backend": {
        "python",
        "java",
        "node.js",
        "rest api",
        "rest apis",
        "graphql",
        "sql",
        "postgresql",
        "mysql",
        "mongodb",
        "redis",
        "docker",
        "kubernetes",
        "aws",
        "gcp",
        "azure",
    },
    "fullstack": {
        "javascript",
        "typescript",
        "react",
        "node.js",
        "rest api",
        "sql",
        "postgresql",
        "docker",
        "git",
    },
    "data": {
        "python",
        "sql",
        "pandas",
        "numpy",
        "scikit-learn",
        "machine learning",
        "data analysis",
        "data engineering",
        "data science",
        "tensorflow",
        "pytorch",
        "keras",
        "deep learning",
        "neural networks",
        "statistics",
        "linear algebra",
        "probability",
        "nlp",
        "computer vision",
        "jupyter",
        "anaconda",
    },
    "devops": {
        "docker",
        "kubernetes",
        "ci/cd",
        "terraform",
        "aws",
        "gcp",
        "azure",
        "linux",
    },
}


def detect_role(job_text: str) -> str:
    lowered = job_text.lower()

    # Check SPECIFIC roles FIRST (ML, DevOps) before GENERIC ones (Frontend, Backend)
    # This prevents "UI" in a ML job from being detected as frontend
    if any(term in lowered for term in ROLE_KEYWORDS["data"]):
        return "data"
    if any(term in lowered for term in ROLE_KEYWORDS["devops"]):
        return "devops"

    # Then check generic roles
    frontend = any(term in lowered for term in ROLE_KEYWORDS["frontend"])
    backend = any(term in lowered for term in ROLE_KEYWORDS["backend"])

    if frontend and backend:
        return "fullstack"
    if any(term in lowered for term in ROLE_KEYWORDS["fullstack"]):
        return "fullstack"
    if frontend:
        return "frontend"
    if backend:
        return "backend"

    return "general"


def role_skill_set(job_text: str) -> Set[str]:
    role = detect_role(job_text)
    return ROLE_SKILLS.get(role, set())


def role_suggestions(job_text: str) -> list[str]:
    role = detect_role(job_text)
    if role == "frontend":
        return [
            "Add a dedicated Skills section with React, JavaScript, HTML, CSS, and REST APIs.",
            "Include 2–3 project bullets that mention responsive UI and performance improvements.",
            "Mirror job keywords like TypeScript, accessibility, and testing (Jest/Cypress).",
        ]
    if role == "backend":
        return [
            "Highlight APIs you built (REST/GraphQL) and the data stores used.",
            "Quantify performance or reliability improvements (latency, uptime).",
            "List backend stack explicitly (language, framework, database, cloud).",
        ]
    if role == "fullstack":
        return [
            "Show both frontend and backend contributions in each project.",
            "List end‑to‑end features with APIs, database, and UI.",
            "Add a tech stack line per project (React, Node.js, SQL, etc.).",
        ]
    if role == "data":
        return [
            "List data tools (SQL, Python, pandas) and ML libraries if relevant.",
            "Quantify impact: accuracy, time saved, or scale of data processed.",
            "Highlight pipelines, models, or dashboards you built.",
        ]
    if role == "devops":
        return [
            "List infrastructure tools (Docker, Kubernetes, CI/CD, cloud).",
            "Quantify uptime, deployment frequency, or cost savings.",
            "Mention monitoring/alerting and automation work.",
        ]
    return [
        "Add a Skills section with exact job keywords.",
        "Quantify impact in 2–3 bullets (%, time saved, scale).",
        "Mirror 3–5 phrases from the job description.",
    ]


def _has_term(text: str, term: str) -> bool:
    pattern = r"(?<!\w)" + re.escape(term) + r"(?!\w)"
    return re.search(pattern, text) is not None


def _normalize(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def extract_known_skills(
    text: str, allowed_skills: Optional[Iterable[str]] = None
) -> set[str]:
    lowered = text.lower()
    normalized = _normalize(text)
    found = set()
    skill_set = set(allowed_skills) if allowed_skills else COMMON_SKILLS

    for skill in skill_set:
        if _has_term(lowered, skill) or _has_term(normalized, _normalize(skill)):
            found.add(skill)

    for canonical, aliases in SKILL_SYNONYMS.items():
        if canonical not in skill_set:
            continue
        for alias in aliases:
            if _has_term(lowered, alias) or _has_term(normalized, _normalize(alias)):
                found.add(canonical)

    return found
