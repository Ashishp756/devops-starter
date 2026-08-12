# DevOps Starter Project

A tiny static website used to practice a real **GitHub Actions CI/CD pipeline**:

- 🔍 `pr-checks.yml` — runs tests automatically on every Pull Request
- 🚀 `deploy.yml` — automatically deploys the site to **GitHub Pages** every time code is merged into `main`

## Project structure
```
.
├── index.html              # the website
├── assets/style.css        # styling
├── tests/test_site.py      # sanity tests run by CI
├── requirements.txt        # test dependencies
└── .github/workflows/
    ├── pr-checks.yml       # CI: runs on every PR
    └── deploy.yml          # CD: runs on merge to main
```

See the full walkthrough in the chat / project instructions for step-by-step setup.
