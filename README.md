<div align="center">

```
████████╗ ██████╗ ██╗  ██╗███████╗███╗   ██╗███████╗███████╗███╗   ██╗███████╗███████╗
╚══██╔══╝██╔═══██╗██║ ██╔╝██╔════╝████╗  ██║██╔════╝██╔════╝████╗  ██║██╔════╝██╔════╝
   ██║   ██║   ██║█████╔╝ █████╗  ██╔██╗ ██║███████╗█████╗  ██╔██╗ ██║███████╗█████╗  
   ██║   ██║   ██║██╔═██╗ ██╔══╝  ██║╚██╗██║╚════██║██╔══╝  ██║╚██╗██║╚════██║██╔══╝  
   ██║   ╚██████╔╝██║  ██╗███████╗██║ ╚████║███████║███████╗██║ ╚████║███████║███████╗
   ╚═╝    ╚═════╝ ╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝╚═╝  ╚═══╝╚══════╝╚══════╝
```

**Know your tokens. Build sustainably. Waste nothing.**

[![PyPI version](https://img.shields.io/pypi/v/tokensense?color=0F6E56&label=pypi)](https://pypi.org/project/tokensense)
[![License: MIT](https://img.shields.io/badge/license-MIT-185FA5.svg)](LICENSE)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-3B6D11.svg)](https://python.org)
[![GSSoC 2026](https://img.shields.io/badge/GSSoC-2026-854F0B.svg)](https://gssoc.girlscript.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-534AB7.svg)](CONTRIBUTING.md)
[![Open Source](https://img.shields.io/badge/open-source-D85A30.svg)](https://github.com/ShivamRaut1610/tokensense)

</div>

---

## The Problem Nobody Talks About

Every time you send a prompt to an AI system, you're spending tokens.

Most tools hide this from you. You don't see how many tokens your prompt consumes, how close you are to the context window limit, how much it's costing you, or whether your prompt could do the same job with half the tokens.

This is not just a developer problem. It's a systems problem.

Bloated prompts mean higher API costs. Wasted context windows mean agents that forget things. Inefficient tokenization means AI systems that don't scale. And at the scale of millions of API calls per day, across thousands of teams, it adds up — in money, in energy, in compute.

**TokenSense exists to change that.**

---

## What TokenSense Does

TokenSense is an open source Python library and web dashboard that makes you tokenization-aware — whether you're a developer building agents or an everyday user interacting with AI tools.

It gives you visibility into what was hidden, control over what was automatic, and the tools to build AI systems that are efficient, sustainable, and built to last.

```python
from tokensense import TokenSense

ts = TokenSense(provider="anthropic")
result = ts.analyze("Your prompt here")

print(result.token_count)       # 47
print(result.estimated_cost)    # $0.00014
print(result.context_usage)     # 0.2% of 200k window
print(result.suggestions)       # ["Remove redundant preamble", "Chunk into 2 reusable parts"]
```

---

## Core Features

### Token Counting
Real-time token counting across all major LLM providers. Know exactly what you're spending before you send.

```python
ts = TokenSense(provider="openai", model="gpt-4o")
count = ts.count("Summarize this document for me.")
# → 7 tokens
```

### Prompt Chunking
Break long prompts into reusable, memory-efficient pieces. Stop sending the same context over and over.

```python
chunks = ts.chunk(long_document, max_tokens=1000)
# → [Chunk(tokens=998), Chunk(tokens=743), Chunk(tokens=512)]
```

### Context Window Management
Never silently overflow a context window again. Get warnings before it happens.

```python
ts.check_context(messages, model="claude-sonnet-4-6")
# → ContextStatus(used=45230, limit=200000, remaining=154770, warning=False)
```

### Cost Estimation
Understand the real cost of every prompt across providers before you send it.

```python
ts.estimate_cost(prompt, provider="anthropic", model="claude-sonnet-4-6")
# → CostEstimate(input_cost=0.00014, output_est=0.00042, total_est=0.00056)
```

### Memory Optimization
Smarter memory for long-running agents. Compress, summarize, and reuse context intelligently.

```python
ts.optimize_memory(conversation_history, strategy="rolling_summary")
# → MemoryResult(original_tokens=12400, optimized_tokens=3100, savings=75%)
```

### Prompt Optimization Suggestions
Actionable suggestions to reduce tokens without losing meaning.

```python
ts.suggest(prompt)
# → ["Remove filler preamble (saves ~12 tokens)",
#    "This can be split into 2 reusable chunks",
#    "Redundant instruction detected on line 3"]
```

---

## Supported Providers

| Provider | Token Counting | Cost Estimation | Context Management |
|---|---|---|---|
| Anthropic (Claude) | ✅ | ✅ | ✅ |
| OpenAI (GPT) | ✅ | ✅ | ✅ |
| Google (Gemini) | ✅ | ✅ | ✅ |
| Mistral | ✅ | ✅ | 🔜 |
| Ollama (local) | ✅ | N/A | ✅ |
| Cohere | 🔜 | 🔜 | 🔜 |

---

## Installation

```bash
pip install tokensense
```

Or install from source:

```bash
git clone https://github.com/ShivamRaut1610/tokensense
cd tokensense
pip install -e .
```

---

## Project Structure

```
tokensense/
├── tokensense/
│   ├── __init__.py
│   ├── core.py               # main TokenSense class
│   ├── counters/
│   │   ├── anthropic.py      # Anthropic tokenizer
│   │   ├── openai.py         # tiktoken-based counter
│   │   ├── gemini.py         # Gemini tokenizer
│   │   └── ollama.py         # local model counter
│   ├── chunker.py            # prompt chunking logic
│   ├── memory.py             # memory optimization
│   ├── context.py            # context window management
│   └── pricing.py            # cost estimation config
├── dashboard/                # web dashboard (phase 2)
│   └── app.py
├── tests/
│   ├── test_counters.py
│   ├── test_chunker.py
│   └── test_pricing.py
├── docs/
│   ├── CONTRIBUTING.md
│   └── ROADMAP.md
├── setup.py
├── pyproject.toml
└── README.md
```

---

## Roadmap

- [x] Repo setup and project structure
- [ ] Token counter — Anthropic
- [ ] Token counter — OpenAI
- [ ] Token counter — Gemini
- [ ] Prompt chunker with sentence-boundary preservation
- [ ] Cost estimator across providers
- [ ] Context window manager with overflow warnings
- [ ] Memory optimizer for long-running agents
- [ ] Prompt optimization suggestions
- [ ] PyPI publish
- [ ] GitHub Actions CI pipeline
- [ ] Web dashboard (Phase 2)
- [ ] VS Code extension (Phase 3)

---

## Philosophy

TokenSense is not built for speed. It is built to last.

We believe that sustainable AI systems are better AI systems. Systems that use tokens efficiently cost less, perform better, and place less load on the infrastructure that runs them. When millions of developers build more efficient agents, the cumulative effect matters — for businesses, for teams, and for the planet.

This project is open source because good infrastructure belongs to everyone. Every contribution, however small, makes the AI ecosystem a little more sustainable.

---

## Contributing

TokenSense is an active GSSoC 2026 project and welcomes contributors of all backgrounds and experience levels.

**Good first issues are labeled and ready.** You don't need to know everything. You need to be curious, read the issue description, and open a pull request.

```bash
# Fork the repo, then:
git clone https://github.com/YOUR_USERNAME/tokensense
cd tokensense
pip install -e ".[dev]"
pytest
```

Please read [CONTRIBUTING.md](CONTRIBUTING.md) before raising your first PR. It covers code style, commit messages, testing requirements, and review timelines.

Every merged PR receives a public shoutout. Every contributor is listed in [CONTRIBUTORS.md](CONTRIBUTORS.md).

---

## Built With Intention

| Value | What it means here |
|---|---|
| Sustainable | Built for longevity, not hype |
| Open | MIT licensed, built in public |
| Grounded | Solves a real problem, not a demo |
| Inclusive | Welcomes first-time contributors |
| Provider-agnostic | Works with any LLM, not just one |

---

## License

MIT — free to use, modify, and distribute

---

<div align="center">

**TokenSense is built for developers who think in systems, not just scripts.**

[⭐ Star this repo](https://github.com/ShivamRaut1610/tokensense) · [🐛 Report a bug](https://github.com/ShivamRaut1610/tokensense/issues) · [💡 Request a feature](https://github.com/ShivamRaut1610/tokensense/issues) · [🤝 Contribute](CONTRIBUTING.md)

</div>
