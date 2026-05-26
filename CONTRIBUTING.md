# Contributing to TokenSense

Thank you for considering contributing to TokenSense. This project exists because of people like you — developers who believe good infrastructure should be open, sustainable, and built together.

Every contribution matters, whether it's fixing a typo, writing a test, or building a new feature. You don't need to be an expert. You need to be curious and willing to learn.

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [Who Can Contribute](#who-can-contribute)
- [How to Get Started](#how-to-get-started)
- [Setting Up Locally](#setting-up-locally)
- [Finding Something to Work On](#finding-something-to-work-on)
- [Making a Pull Request](#making-a-pull-request)
- [Commit Message Format](#commit-message-format)
- [Code Style](#code-style)
- [Testing](#testing)
- [Review Timeline](#review-timeline)
- [Recognition](#recognition)

---

## Code of Conduct

This project is a respectful, inclusive space. We do not tolerate harassment, discrimination, or gatekeeping of any kind. Be kind. Be patient. Assume good intent.

If you experience or witness unacceptable behavior, email: **gssoc@girlscript.org**

---

## Who Can Contribute

Everyone. Seriously.

- First-time open source contributors
- Students participating in GSSoC 2026
- Developers new to Python or AI/ML
- Experienced engineers who want to give back
- Technical writers who want to improve documentation
- Anyone who believes in sustainable AI systems

---

## How to Get Started

1. **Star the repo** so you can find it easily later
2. **Read the README** to understand what TokenSense does
3. **Browse open issues** and find one labeled `good-first-issue`
4. **Comment on the issue** saying you'd like to work on it
5. **Wait for assignment** — we will assign it to you within 24 hours
6. **Fork, code, and open a PR**

Do not start coding before being assigned. This keeps the project organized and avoids duplicate work.

---

## Setting Up Locally

```bash
# 1. Fork the repo on GitHub, then clone your fork
git clone https://github.com/YOUR_USERNAME/tokensense
cd tokensense

# 2. Create a virtual environment
python -m venv venv
source venv/bin/activate        # on Windows: venv\Scripts\activate

# 3. Install in development mode
pip install -e ".[dev]"

# 4. Run tests to confirm everything works
pytest

# 5. Create a branch for your work
git checkout -b feat/your-feature-name
```

---

## Finding Something to Work On

Browse issues at: https://github.com/ShivamRaut1610/tokensense/issues

Labels explained:

| Label | Meaning |
|---|---|
| `good-first-issue` | Small, well-defined task, perfect for first-time contributors |
| `bug` | Something is broken |
| `enhancement` | New feature or improvement |
| `documentation` | Docs, README, comments |
| `testing` | Writing or improving tests |
| `help wanted` | Anyone can pick this up |

If you have an idea not listed, open an issue and describe it before writing any code.

---

## Making a Pull Request

```bash
# Make sure your branch is up to date with main
git fetch upstream
git rebase upstream/main

# Push your branch
git push origin feat/your-feature-name
```

Then open a Pull Request on GitHub with:

- A clear title describing what you did
- A short description of the change and why
- Reference to the issue it closes (e.g. `Closes #12`)

Example PR title:
```
feat: add token counter for Anthropic Claude API
```

**PR checklist before submitting:**
- [ ] Code works and does what the issue describes
- [ ] Tests written and passing
- [ ] No unused imports or commented-out code
- [ ] Follows the code style below

---

## Commit Message Format

We follow **conventional commits**:

```
type: short description in lowercase

Optional longer explanation here.
```

Types:
| Type | Use for |
|---|---|
| `feat` | New feature |
| `fix` | Bug fix |
| `docs` | Documentation only |
| `test` | Adding or fixing tests |
| `refactor` | Code change that is not a fix or feature |
| `chore` | Maintenance, config, tooling |

Examples:
```
feat: add tiktoken-based counter for OpenAI models
fix: handle empty string input in chunker
docs: update contributing guide with setup steps
test: add edge case tests for pricing estimator
```

---

## Code Style

- Python 3.8+ compatible code only
- Follow PEP 8 — use `black` for auto-formatting
- Type hints encouraged on all public functions
- Docstrings required on all public functions and classes
- No hardcoded API keys or credentials ever

Format your code before pushing:
```bash
pip install black
black tokensense/
```

---

## Testing

All new code must include tests. We use `pytest`.

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=tokensense
```

- Aim for at least 80% coverage on new code
- Tests live in the `tests/` folder
- Name test files `test_<module>.py`
- Name test functions `test_<what_it_does>()`

---

## Review Timeline

- **Issue assignment**: within 24 hours of your comment
- **PR review**: within 48 hours of submission
- **Feedback**: constructive, specific, and respectful always
- **Merge**: once tests pass and review is approved

If you haven't heard back in 48 hours, comment on the PR to follow up.

---

## Recognition

Every contributor matters here.

- Every merged PR gets a **public shoutout** on GitHub Discussions
- Every contributor is added to **CONTRIBUTORS.md**
- GSSoC contributors receive official GSSoC recognition and points
- Top contributors will be highlighted in the project README

---

## Questions?

Open a GitHub Discussion or reach out on Discord.

We are here to help you succeed, not judge your skill level.

**TokenSense is built for developers who think in systems, not just scripts. Welcome to the team.**
