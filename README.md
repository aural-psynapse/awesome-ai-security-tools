# Awesome AI Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> A curated list of **public-source, research, and commercial** tools for AI security and AI-assisted cybersecurity — autotriage, agent security, AI/ML supply chain, pentest agents, AI SAST, LLM-driven fuzzing, threat intelligence, SOC/SIEM triage, reverse engineering, LLM red-teaming, and more.

[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)

**Type legend:** 🟢 public source / open-source · 🔬 research (paper / benchmark / dataset / framework) · 🟠 commercial with open components · ⚠️ restrictive, non-commercial, or unclear/no license — check before use.

Each entry shows live **★ stars** and **last-commit** badges (rendered from the GitHub API by shields.io). Ordering within a section favors flagship and actively maintained projects.

---

## Contents

- [Autotriage of Security Findings](#autotriage-of-security-findings)
- [AI Agent & Coding-Agent Security](#ai-agent--coding-agent-security)
  - [Scanners & Auditors](#scanners--auditors)
  - [Frameworks, Rule Standards & Benchmarks](#frameworks-rule-standards--benchmarks)
  - [Runtime Protection & Enforcement](#runtime-protection--enforcement)
- [AI/ML Supply Chain & Model Security](#aiml-supply-chain--model-security)
- [Pentest & Red-Team Agents](#pentest--red-team-agents)
- [AI-Powered SAST & Secure Code Review](#ai-powered-sast--secure-code-review)
- [LLM-Driven Fuzzing](#llm-driven-fuzzing)
  - [Harness / target generation](#harness--target-generation)
  - [Fuzzing the LLM](#fuzzing-the-llm)
- [Threat Intelligence](#threat-intelligence)
- [Log Analysis / SIEM / SOC Triage](#log-analysis--siem--soc-triage)
- [Reverse Engineering](#reverse-engineering)
- [LLM Red-Teaming & Guardrails](#llm-red-teaming--guardrails)
- [LLM Honeypots & Deception](#llm-honeypots--deception)
- [CTF / Exploit / Bug-Bounty Agents & Benchmarks](#ctf--exploit--bug-bounty-agents--benchmarks)
- [Cloud / IaC / DFIR / OSINT / Phishing](#cloud--iac--dfir--osint--phishing)
- [Related Awesome Lists](#related-awesome-lists)
- [Contributing](#contributing)
- [License](#license)

---

## Autotriage of Security Findings

AI/LLM tools that triage, deduplicate, prioritize, or validate the output of scanners and finding sources.

- **[nuclei-autotriage](https://github.com/cyberok-org/nuclei-autotriage)** 🟢⚠️ — Two-stage LLM triage (falsifier + red-team pass) of Nuclei JSONL findings via OpenAI-compatible endpoints (vLLM/Ollama). *(CyberOK)* — **note:** restrictive personal/non-commercial EULA, not a permissive OSS license. [![stars](https://img.shields.io/github/stars/cyberok-org/nuclei-autotriage?style=flat-square&label=%E2%98%85)](https://github.com/cyberok-org/nuclei-autotriage) [![updated](https://img.shields.io/github/last-commit/cyberok-org/nuclei-autotriage?style=flat-square&label=updated)](https://github.com/cyberok-org/nuclei-autotriage)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [asamm](https://github.com/scadastrangelove/asamm)
- **[honeyslop](https://github.com/gadievron/honeyslop)** 🟢 — Code-canary decoys to triage AI-hallucinated ("slop") vulnerability reports flooding bug-bounty programs. [![stars](https://img.shields.io/github/stars/gadievron/honeyslop?style=flat-square&label=%E2%98%85)](https://github.com/gadievron/honeyslop) [![updated](https://img.shields.io/github/last-commit/gadievron/honeyslop?style=flat-square&label=updated)](https://github.com/gadievron/honeyslop)
- **[nano-analyzer](https://github.com/weareaisle/nano-analyzer)** 🟢🔬 — Minimal three-stage LLM pipeline (context → scan → skeptical triage) for zero-day discovery in C/C++. *(AISLE)* [![stars](https://img.shields.io/github/stars/weareaisle/nano-analyzer?style=flat-square&label=%E2%98%85)](https://github.com/weareaisle/nano-analyzer) [![updated](https://img.shields.io/github/last-commit/weareaisle/nano-analyzer?style=flat-square&label=updated)](https://github.com/weareaisle/nano-analyzer)
- **[ai-soc-triage-assistant](https://github.com/pranavibunny/ai-soc-triage-assistant)** 🟢⚠️ — SOC alert triage assistant with prompt-injection guardrails, output validation, and MITRE ATT&CK mapping. [![stars](https://img.shields.io/github/stars/pranavibunny/ai-soc-triage-assistant?style=flat-square&label=%E2%98%85)](https://github.com/pranavibunny/ai-soc-triage-assistant) [![updated](https://img.shields.io/github/last-commit/pranavibunny/ai-soc-triage-assistant?style=flat-square&label=updated)](https://github.com/pranavibunny/ai-soc-triage-assistant)

> See also: GitHub Security Lab's *Taskflow Agent* (CodeQL-alert triage, credited with ~30 real CVEs since Aug 2025) and OpenAI's *Aardvark* / *Codex Security* research previews — public references exist, but there is no standalone installable repo to badge here.

---

## AI Agent & Coding-Agent Security

Securing the AI agents themselves — auditing coding agents (Claude Code, Codex, OpenClaw), scanning skills / plugins / MCP manifests, and governance for agentic development. A fast-moving 2026 category, split below by role.

### Scanners & Auditors

- **[agent-audit](https://github.com/scadastrangelove/agent-audit)** 🟢 — Forensic auditor for local AI coding agents (Claude Code, Codex CLI, OpenClaw) **and** project-surface scanner for repos shipping skills, plugins, and MCP manifests; 296 bundled rules across native + imported detector families, with optional LLM cross-verification. *(CyberOK / S. Gordeychik)* [![stars](https://img.shields.io/github/stars/scadastrangelove/agent-audit?style=flat-square&label=%E2%98%85)](https://github.com/scadastrangelove/agent-audit) [![updated](https://img.shields.io/github/last-commit/scadastrangelove/agent-audit?style=flat-square&label=updated)](https://github.com/scadastrangelove/agent-audit)
  - **Sources:** [asamm](https://github.com/scadastrangelove/asamm) · [ATR – Agent Threat Rules](https://github.com/panguard-ai/agent-threat-rules) · [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
  - **Related:** [asamm](https://github.com/scadastrangelove/asamm) · [aguara](https://github.com/garagon/aguara) · [agentguard](https://github.com/GoPlusSecurity/agentguard) · [agentic-radar](https://github.com/splx-ai/agentic-radar) · [nuclei-autotriage](https://github.com/cyberok-org/nuclei-autotriage)
- **[aguara](https://github.com/garagon/aguara)** 🟢 — Single-binary static scanner (Go, no LLM) for AI-agent skills and MCP servers; multi-layer engine (pattern + NLP + taint tracking + rug-pull detection). Companion **[aguara-mcp](https://github.com/garagon/aguara-mcp)** exposes scanning as an MCP tool. [![stars](https://img.shields.io/github/stars/garagon/aguara?style=flat-square&label=%E2%98%85)](https://github.com/garagon/aguara) [![updated](https://img.shields.io/github/last-commit/garagon/aguara?style=flat-square&label=updated)](https://github.com/garagon/aguara)
  - **Related:** [aguara-mcp](https://github.com/garagon/aguara-mcp) · [agent-audit](https://github.com/scadastrangelove/agent-audit) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[agent-scan](https://github.com/snyk/agent-scan)** 🟢 — Security scanner for AI agents, MCP servers, and agent skills; the successor path for the original Invariant Labs mcp-scan work. *(Snyk)* [![stars](https://img.shields.io/github/stars/snyk/agent-scan?style=flat-square&label=%E2%98%85)](https://github.com/snyk/agent-scan) [![updated](https://img.shields.io/github/last-commit/snyk/agent-scan?style=flat-square&label=updated)](https://github.com/snyk/agent-scan)
  - **Related:** [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner) · [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)
- **[skill-scanner](https://github.com/cisco-ai-defense/skill-scanner)** 🟠 — Scanner for agent skills combining YAML + YARA patterns, LLM-as-a-judge, and behavioral dataflow analysis (Codex / Cursor skill formats). *(Cisco AI Defense)* [![stars](https://img.shields.io/github/stars/cisco-ai-defense/skill-scanner?style=flat-square&label=%E2%98%85)](https://github.com/cisco-ai-defense/skill-scanner) [![updated](https://img.shields.io/github/last-commit/cisco-ai-defense/skill-scanner?style=flat-square&label=updated)](https://github.com/cisco-ai-defense/skill-scanner)
  - **Related:** [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw) · [aguara](https://github.com/garagon/aguara) · [Cisco AI Defense – mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)
- **[mcp-scanner](https://github.com/cisco-ai-defense/mcp-scanner)** 🟢⚠️ — Scanner for MCP servers and agentic tool surfaces, covering tools, prompts, resources, package risk, malware indicators, and deployment readiness. *(Cisco AI Defense)* [![stars](https://img.shields.io/github/stars/cisco-ai-defense/mcp-scanner?style=flat-square&label=%E2%98%85)](https://github.com/cisco-ai-defense/mcp-scanner) [![updated](https://img.shields.io/github/last-commit/cisco-ai-defense/mcp-scanner?style=flat-square&label=updated)](https://github.com/cisco-ai-defense/mcp-scanner)
  - **Related:** [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [Snyk Agent Scan](https://github.com/snyk/agent-scan) · [aguara](https://github.com/garagon/aguara)
- **[agentic-radar](https://github.com/splx-ai/agentic-radar)** 🟠 — CLI security scanner for agentic workflows (LangGraph, CrewAI, n8n, etc.) — maps tools/data flows and flags risks. *(SplxAI)* [![stars](https://img.shields.io/github/stars/splx-ai/agentic-radar?style=flat-square&label=%E2%98%85)](https://github.com/splx-ai/agentic-radar) [![updated](https://img.shields.io/github/last-commit/splx-ai/agentic-radar?style=flat-square&label=updated)](https://github.com/splx-ai/agentic-radar)

### Frameworks, Rule Standards & Benchmarks

- **[asamm](https://github.com/scadastrangelove/asamm)** 🔬 — *Agentic SAMM* — an OWASP SAMM extension for AI-driven development: an entry-point-based threat taxonomy plus 17 controls across 5 SAMM functions (Governance, Design, Implementation, Verification, Operations) with L1/L2/L3 maturity. License: CC BY-SA 4.0. *(CyberOK / S. Gordeychik)* [![stars](https://img.shields.io/github/stars/scadastrangelove/asamm?style=flat-square&label=%E2%98%85)](https://github.com/scadastrangelove/asamm) [![updated](https://img.shields.io/github/last-commit/scadastrangelove/asamm?style=flat-square&label=updated)](https://github.com/scadastrangelove/asamm)
  - **Sources:** [OWASP SAMM](https://owaspsamm.org/) · [NIST AI RMF](https://www.nist.gov/itl/ai-risk-management-framework) · [NCSC Secure AI Guidelines](https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development) · [MCP Security Best Practices](https://modelcontextprotocol.io/)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit)
- **[agent-threat-rules (ATR)](https://github.com/panguard-ai/agent-threat-rules)** 🟢 — Open, versioned, machine-readable detection-rule format for AI-agent threats (prompt injection, tool poisoning, MCP attacks, skill compromise) — "Sigma for agents" (MIT). Engine-agnostic; converts to Splunk/Elastic/SARIF. [![stars](https://img.shields.io/github/stars/panguard-ai/agent-threat-rules?style=flat-square&label=%E2%98%85)](https://github.com/panguard-ai/agent-threat-rules) [![updated](https://img.shields.io/github/last-commit/panguard-ai/agent-threat-rules?style=flat-square&label=updated)](https://github.com/panguard-ai/agent-threat-rules)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [aguara](https://github.com/garagon/aguara)
- **[AgentDojo](https://github.com/ethz-spylab/agentdojo)** 🟢🔬 — Benchmark environment for prompt-injection attacks and defenses in tool-using LLM agents. [![stars](https://img.shields.io/github/stars/ethz-spylab/agentdojo?style=flat-square&label=%E2%98%85)](https://github.com/ethz-spylab/agentdojo) [![updated](https://img.shields.io/github/last-commit/ethz-spylab/agentdojo?style=flat-square&label=updated)](https://github.com/ethz-spylab/agentdojo)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [ATR – Agent Threat Rules](https://github.com/panguard-ai/agent-threat-rules)

### Runtime Protection & Enforcement

- **[agentguard](https://github.com/GoPlusSecurity/agentguard)** 🟢 — Real-time security layer for coding agents: hooks scan every new skill, block dangerous actions before execution, run daily posture patrols, and track which skill triggered each action (incl. Web3-specific checks). [![stars](https://img.shields.io/github/stars/GoPlusSecurity/agentguard?style=flat-square&label=%E2%98%85)](https://github.com/GoPlusSecurity/agentguard) [![updated](https://img.shields.io/github/last-commit/GoPlusSecurity/agentguard?style=flat-square&label=updated)](https://github.com/GoPlusSecurity/agentguard)
  - **Related:** [agent-audit](https://github.com/scadastrangelove/agent-audit) · [defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)
- **[defenseclaw](https://github.com/cisco-ai-defense/defenseclaw)** 🟠 — Enforcement and evidence layer for agentic deployments: static CodeGuard checks, sandboxing, registry ingestion with SSRF guards, and audit/observability. *(Cisco AI Defense)* [![stars](https://img.shields.io/github/stars/cisco-ai-defense/defenseclaw?style=flat-square&label=%E2%98%85)](https://github.com/cisco-ai-defense/defenseclaw) [![updated](https://img.shields.io/github/last-commit/cisco-ai-defense/defenseclaw?style=flat-square&label=updated)](https://github.com/cisco-ai-defense/defenseclaw)
  - **Related:** [Cisco AI Defense – skill-scanner](https://github.com/cisco-ai-defense/skill-scanner) · [agentguard](https://github.com/GoPlusSecurity/agentguard)

---

## AI/ML Supply Chain & Model Security

Tools for securing model artifacts, serialized ML files, and AI/ML supply-chain surfaces.

- **[modelscan](https://github.com/protectai/modelscan)** 🟢 — Scans ML model files for unsafe serialization patterns and embedded code, with a focus on model serialization attacks. *(Protect AI)* [![stars](https://img.shields.io/github/stars/protectai/modelscan?style=flat-square&label=%E2%98%85)](https://github.com/protectai/modelscan) [![updated](https://img.shields.io/github/last-commit/protectai/modelscan?style=flat-square&label=updated)](https://github.com/protectai/modelscan)
  - **Related:** [Fickling](https://github.com/trailofbits/fickling) · [picklescan](https://github.com/mmaitre314/picklescan) · [ai-exploits](https://github.com/protectai/ai-exploits)
- **[Fickling](https://github.com/trailofbits/fickling)** 🟢 — Python pickle decompiler, rewriter, and static analyzer for inspecting and detecting malicious pickle/PyTorch payloads. *(Trail of Bits)* [![stars](https://img.shields.io/github/stars/trailofbits/fickling?style=flat-square&label=%E2%98%85)](https://github.com/trailofbits/fickling) [![updated](https://img.shields.io/github/last-commit/trailofbits/fickling?style=flat-square&label=updated)](https://github.com/trailofbits/fickling)
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [picklescan](https://github.com/mmaitre314/picklescan)
- **[picklescan](https://github.com/mmaitre314/picklescan)** 🟢 — Lightweight CLI/library for detecting suspicious Python pickle operations in ML and model artifacts. [![stars](https://img.shields.io/github/stars/mmaitre314/picklescan?style=flat-square&label=%E2%98%85)](https://github.com/mmaitre314/picklescan) [![updated](https://img.shields.io/github/last-commit/mmaitre314/picklescan?style=flat-square&label=updated)](https://github.com/mmaitre314/picklescan)
  - **Related:** [modelscan](https://github.com/protectai/modelscan) · [Fickling](https://github.com/trailofbits/fickling)

---

## Pentest & Red-Team Agents

Autonomous and semi-autonomous AI agents for penetration testing, exploitation, and attack simulation.

- **[PentestGPT](https://github.com/GreyDGL/PentestGPT)** 🟢🔬 — The original USENIX'24 LLM pentest agent; re-released as an autonomous pipeline with strong benchmark results. [![stars](https://img.shields.io/github/stars/GreyDGL/PentestGPT?style=flat-square&label=%E2%98%85)](https://github.com/GreyDGL/PentestGPT) [![updated](https://img.shields.io/github/last-commit/GreyDGL/PentestGPT?style=flat-square&label=updated)](https://github.com/GreyDGL/PentestGPT)
- **[PentAGI](https://github.com/vxcontrol/pentagi)** 🟢 — Fully autonomous multi-agent pentest framework with Docker sandboxing. *(VXControl)* [![stars](https://img.shields.io/github/stars/vxcontrol/pentagi?style=flat-square&label=%E2%98%85)](https://github.com/vxcontrol/pentagi) [![updated](https://img.shields.io/github/last-commit/vxcontrol/pentagi?style=flat-square&label=updated)](https://github.com/vxcontrol/pentagi)
- **[CAI – Cybersecurity AI](https://github.com/aliasrobotics/cai)** 🟢🟠 — Modular, bug-bounty-ready agent framework supporting 300+ LLM models. MIT for research; separate commercial license for production/on-prem. *(Alias Robotics)* [![stars](https://img.shields.io/github/stars/aliasrobotics/cai?style=flat-square&label=%E2%98%85)](https://github.com/aliasrobotics/cai) [![updated](https://img.shields.io/github/last-commit/aliasrobotics/cai?style=flat-square&label=updated)](https://github.com/aliasrobotics/cai)
- **[Strix](https://github.com/usestrix/strix)** 🟢 — Autonomous "AI hackers" that dynamically run code and validate vulnerabilities with PoCs (Apache-2.0). [![stars](https://img.shields.io/github/stars/usestrix/strix?style=flat-square&label=%E2%98%85)](https://github.com/usestrix/strix) [![updated](https://img.shields.io/github/last-commit/usestrix/strix?style=flat-square&label=updated)](https://github.com/usestrix/strix)
- **[hackingBuddyGPT](https://github.com/ipa-lab/hackingBuddyGPT)** 🟢🔬 — Minimal (~50 LOC) research framework for LLM-driven Linux priv-esc and web pentesting (FSE'23). [![stars](https://img.shields.io/github/stars/ipa-lab/hackingBuddyGPT?style=flat-square&label=%E2%98%85)](https://github.com/ipa-lab/hackingBuddyGPT) [![updated](https://img.shields.io/github/last-commit/ipa-lab/hackingBuddyGPT?style=flat-square&label=updated)](https://github.com/ipa-lab/hackingBuddyGPT)
- **[Nebula](https://github.com/berylliumsec/nebula)** 🟢🟠 — AI pentesting CLI assistant with local-LLM support (Llama-3.1, Mistral, DeepSeek). [![stars](https://img.shields.io/github/stars/berylliumsec/nebula?style=flat-square&label=%E2%98%85)](https://github.com/berylliumsec/nebula) [![updated](https://img.shields.io/github/last-commit/berylliumsec/nebula?style=flat-square&label=updated)](https://github.com/berylliumsec/nebula)
- **[HexStrike-AI](https://github.com/0x4m4/hexstrike-ai)** 🟢 — MCP server exposing 150+ security tools (nmap, gobuster, nuclei, …) to AI agents (MIT). [![stars](https://img.shields.io/github/stars/0x4m4/hexstrike-ai?style=flat-square&label=%E2%98%85)](https://github.com/0x4m4/hexstrike-ai) [![updated](https://img.shields.io/github/last-commit/0x4m4/hexstrike-ai?style=flat-square&label=updated)](https://github.com/0x4m4/hexstrike-ai)
- **[Shannon](https://github.com/KeygraphHQ/shannon)** 🟢 — White-box autonomous AI pentester with strong XBOW-benchmark results. [![stars](https://img.shields.io/github/stars/KeygraphHQ/shannon?style=flat-square&label=%E2%98%85)](https://github.com/KeygraphHQ/shannon) [![updated](https://img.shields.io/github/last-commit/KeygraphHQ/shannon?style=flat-square&label=updated)](https://github.com/KeygraphHQ/shannon)
- **[PentestAgent](https://github.com/GH05TCREW/pentestagent)** 🟢 — Black-box AI pentest framework with MCP, multi-agent spawning, and persistent sessions. [![stars](https://img.shields.io/github/stars/GH05TCREW/pentestagent?style=flat-square&label=%E2%98%85)](https://github.com/GH05TCREW/pentestagent) [![updated](https://img.shields.io/github/last-commit/GH05TCREW/pentestagent?style=flat-square&label=updated)](https://github.com/GH05TCREW/pentestagent)
- **[cyber-security-llm-agents](https://github.com/NVISOsecurity/cyber-security-llm-agents)** 🟢⚠️ — AutoGen-based agents for cybersecurity tasks (shown at RSAC 2024). *(NVISO)* [![stars](https://img.shields.io/github/stars/NVISOsecurity/cyber-security-llm-agents?style=flat-square&label=%E2%98%85)](https://github.com/NVISOsecurity/cyber-security-llm-agents) [![updated](https://img.shields.io/github/last-commit/NVISOsecurity/cyber-security-llm-agents?style=flat-square&label=updated)](https://github.com/NVISOsecurity/cyber-security-llm-agents)
- **[Pentest-Swarm-AI](https://github.com/Armur-Ai/Pentest-Swarm-AI)** 🟢 — Swarm-intelligence multi-agent pentest with stigmergic blackboard coordination (Go). [![stars](https://img.shields.io/github/stars/Armur-Ai/Pentest-Swarm-AI?style=flat-square&label=%E2%98%85)](https://github.com/Armur-Ai/Pentest-Swarm-AI) [![updated](https://img.shields.io/github/last-commit/Armur-Ai/Pentest-Swarm-AI?style=flat-square&label=updated)](https://github.com/Armur-Ai/Pentest-Swarm-AI)
- **[hackGPT](https://github.com/NoDataFound/hackGPT)** 🟢⚠️ — LLM offensive-security toolkit. [![stars](https://img.shields.io/github/stars/NoDataFound/hackGPT?style=flat-square&label=%E2%98%85)](https://github.com/NoDataFound/hackGPT) [![updated](https://img.shields.io/github/last-commit/NoDataFound/hackGPT?style=flat-square&label=updated)](https://github.com/NoDataFound/hackGPT)

---

## AI-Powered SAST & Secure Code Review

Static analysis and secure code review enhanced with LLMs.

- **[Vulnhuntr](https://github.com/protectai/vulnhuntr)** 🟢 — Zero-shot vulnerability discovery in Python repos via LLM call-chain analysis; credited with a 0-day RCE in Ragflow. *(Protect AI)* [![stars](https://img.shields.io/github/stars/protectai/vulnhuntr?style=flat-square&label=%E2%98%85)](https://github.com/protectai/vulnhuntr) [![updated](https://img.shields.io/github/last-commit/protectai/vulnhuntr?style=flat-square&label=updated)](https://github.com/protectai/vulnhuntr)
  - **Related:** [xvulnhuntr](https://github.com/CompassSecurity/xvulnhuntr) · [vulnhuntr-mod](https://github.com/kxcode/vulnhuntr-mod)
- **[claude-code-security-review](https://github.com/anthropics/claude-code-security-review)** 🟠 — Official Claude-based semantic SAST GitHub Action that reviews PR diffs. *(Anthropic)* [![stars](https://img.shields.io/github/stars/anthropics/claude-code-security-review?style=flat-square&label=%E2%98%85)](https://github.com/anthropics/claude-code-security-review) [![updated](https://img.shields.io/github/last-commit/anthropics/claude-code-security-review?style=flat-square&label=updated)](https://github.com/anthropics/claude-code-security-review)
- **[IRIS](https://github.com/iris-sast/iris)** 🟢🔬 — Neurosymbolic SAST combining LLMs with CodeQL for Java vulnerability detection (MIT). [![stars](https://img.shields.io/github/stars/iris-sast/iris?style=flat-square&label=%E2%98%85)](https://github.com/iris-sast/iris) [![updated](https://img.shields.io/github/last-commit/iris-sast/iris?style=flat-square&label=updated)](https://github.com/iris-sast/iris)
- **[xvulnhuntr](https://github.com/CompassSecurity/xvulnhuntr)** 🟢 — Archived fork of Vulnhuntr extending support to C#, Java, and Go. *(Compass Security)* [![stars](https://img.shields.io/github/stars/CompassSecurity/xvulnhuntr?style=flat-square&label=%E2%98%85)](https://github.com/CompassSecurity/xvulnhuntr) [![updated](https://img.shields.io/github/last-commit/CompassSecurity/xvulnhuntr?style=flat-square&label=updated)](https://github.com/CompassSecurity/xvulnhuntr)
  - **Sources:** [Vulnhuntr](https://github.com/protectai/vulnhuntr)
  - **Related:** [vulnhuntr-mod](https://github.com/kxcode/vulnhuntr-mod)
- **[llm-security-scanner](https://github.com/iknowjason/llm-security-scanner)** 🟢⚠️ — LLM-powered code scanner that opens GitHub issues for findings. [![stars](https://img.shields.io/github/stars/iknowjason/llm-security-scanner?style=flat-square&label=%E2%98%85)](https://github.com/iknowjason/llm-security-scanner) [![updated](https://img.shields.io/github/last-commit/iknowjason/llm-security-scanner?style=flat-square&label=updated)](https://github.com/iknowjason/llm-security-scanner)
- **[vulnhuntr-mod](https://github.com/kxcode/vulnhuntr-mod)** 🟢 — Modified Vulnhuntr with Qwen/Hunyuan support and Chinese-language prompts. [![stars](https://img.shields.io/github/stars/kxcode/vulnhuntr-mod?style=flat-square&label=%E2%98%85)](https://github.com/kxcode/vulnhuntr-mod) [![updated](https://img.shields.io/github/last-commit/kxcode/vulnhuntr-mod?style=flat-square&label=updated)](https://github.com/kxcode/vulnhuntr-mod)
  - **Sources:** [Vulnhuntr](https://github.com/protectai/vulnhuntr)
  - **Related:** [xvulnhuntr](https://github.com/CompassSecurity/xvulnhuntr)

---

## LLM-Driven Fuzzing

Two families: (a) LLMs generating harnesses/targets for traditional fuzzing, and (b) fuzzing the LLM itself.

### Harness / target generation

- **[oss-fuzz-gen](https://github.com/google/oss-fuzz-gen)** 🟢 — LLM-driven fuzz-harness generation for OSS-Fuzz; reported 26 real vulnerabilities (incl. CVE-2024-9143 in OpenSSL). *(Google)* [![stars](https://img.shields.io/github/stars/google/oss-fuzz-gen?style=flat-square&label=%E2%98%85)](https://github.com/google/oss-fuzz-gen) [![updated](https://img.shields.io/github/last-commit/google/oss-fuzz-gen?style=flat-square&label=updated)](https://github.com/google/oss-fuzz-gen)
- **[PromptFuzz](https://github.com/PromptFuzz/PromptFuzz)** 🟢🔬⚠️ — LLM-mutated prompts to generate fuzz drivers for C/C++ libraries (Rust). [![stars](https://img.shields.io/github/stars/PromptFuzz/PromptFuzz?style=flat-square&label=%E2%98%85)](https://github.com/PromptFuzz/PromptFuzz) [![updated](https://img.shields.io/github/last-commit/PromptFuzz/PromptFuzz?style=flat-square&label=updated)](https://github.com/PromptFuzz/PromptFuzz)
- **[Fuzz4All](https://github.com/fuzz4all/fuzz4all)** 🟢🔬 — "Universal" LLM-based fuzzer across compilers/languages (ICSE 2024). [![stars](https://img.shields.io/github/stars/fuzz4all/fuzz4all?style=flat-square&label=%E2%98%85)](https://github.com/fuzz4all/fuzz4all) [![updated](https://img.shields.io/github/last-commit/fuzz4all/fuzz4all?style=flat-square&label=updated)](https://github.com/fuzz4all/fuzz4all)
- **[ChatAFL](https://github.com/ChatAFLndss/ChatAFL)** 🟢🔬 — LLM-guided protocol fuzzing extending AFLNet (NDSS'24). [![stars](https://img.shields.io/github/stars/ChatAFLndss/ChatAFL?style=flat-square&label=%E2%98%85)](https://github.com/ChatAFLndss/ChatAFL) [![updated](https://img.shields.io/github/last-commit/ChatAFLndss/ChatAFL?style=flat-square&label=updated)](https://github.com/ChatAFLndss/ChatAFL)
- **[TitanFuzz](https://github.com/ise-uiuc/TitanFuzz)** 🟢🔬⚠️ — First LLM-based fuzzer for PyTorch/TensorFlow (ISSTA'23). [![stars](https://img.shields.io/github/stars/ise-uiuc/TitanFuzz?style=flat-square&label=%E2%98%85)](https://github.com/ise-uiuc/TitanFuzz) [![updated](https://img.shields.io/github/last-commit/ise-uiuc/TitanFuzz?style=flat-square&label=updated)](https://github.com/ise-uiuc/TitanFuzz)

### Fuzzing the LLM

- **[LLMFuzzer](https://github.com/mnns/LLMFuzzer)** 🟢 — First open-source fuzzing framework for LLM API integrations. [![stars](https://img.shields.io/github/stars/mnns/LLMFuzzer?style=flat-square&label=%E2%98%85)](https://github.com/mnns/LLMFuzzer) [![updated](https://img.shields.io/github/last-commit/mnns/LLMFuzzer?style=flat-square&label=updated)](https://github.com/mnns/LLMFuzzer)
- **[ps-fuzz](https://github.com/prompt-security/ps-fuzz)** 🟠 — System-prompt hardening fuzzer; 16 attacks × 16 providers. *(Prompt Security)* [![stars](https://img.shields.io/github/stars/prompt-security/ps-fuzz?style=flat-square&label=%E2%98%85)](https://github.com/prompt-security/ps-fuzz) [![updated](https://img.shields.io/github/last-commit/prompt-security/ps-fuzz?style=flat-square&label=updated)](https://github.com/prompt-security/ps-fuzz)
- **[FuzzyAI](https://github.com/cyberark/FuzzyAI)** 🟠 — Automated LLM fuzzer for jailbreaks/prompt injection. *(CyberArk)* [![stars](https://img.shields.io/github/stars/cyberark/FuzzyAI?style=flat-square&label=%E2%98%85)](https://github.com/cyberark/FuzzyAI) [![updated](https://img.shields.io/github/last-commit/cyberark/FuzzyAI?style=flat-square&label=updated)](https://github.com/cyberark/FuzzyAI)
- **[ai-prompt-fuzzer](https://github.com/PortSwigger/ai-prompt-fuzzer)** 🟢 — Burp Suite extension fuzzing GenAI/LLM prompts. *(PortSwigger)* [![stars](https://img.shields.io/github/stars/PortSwigger/ai-prompt-fuzzer?style=flat-square&label=%E2%98%85)](https://github.com/PortSwigger/ai-prompt-fuzzer) [![updated](https://img.shields.io/github/last-commit/PortSwigger/ai-prompt-fuzzer?style=flat-square&label=updated)](https://github.com/PortSwigger/ai-prompt-fuzzer)

---

## Threat Intelligence

AI/LLM tooling for CTI gathering, IOC/TTP extraction, and analysis.

- **[trs](https://github.com/deadbits/trs)** 🟢 — LLM + ChromaDB tool to summarize threat reports and extract MITRE TTPs and IOCs. [![stars](https://img.shields.io/github/stars/deadbits/trs?style=flat-square&label=%E2%98%85)](https://github.com/deadbits/trs) [![updated](https://img.shields.io/github/last-commit/deadbits/trs?style=flat-square&label=updated)](https://github.com/deadbits/trs)
- **[TI-Mindmap-GPT](https://github.com/format81/TI-Mindmap-GPT)** 🟢 — Streamlit app: AI summaries, mindmaps, IOC/TTP extraction, and ATT&CK Navigator layers. [![stars](https://img.shields.io/github/stars/format81/TI-Mindmap-GPT?style=flat-square&label=%E2%98%85)](https://github.com/format81/TI-Mindmap-GPT) [![updated](https://img.shields.io/github/last-commit/format81/TI-Mindmap-GPT?style=flat-square&label=updated)](https://github.com/format81/TI-Mindmap-GPT)
- **[aiocrioc](https://github.com/referefref/aiocrioc)** 🟢 — LLM + OCR IOC extraction (pulls IOCs from images/PDFs). [![stars](https://img.shields.io/github/stars/referefref/aiocrioc?style=flat-square&label=%E2%98%85)](https://github.com/referefref/aiocrioc) [![updated](https://img.shields.io/github/last-commit/referefref/aiocrioc?style=flat-square&label=updated)](https://github.com/referefref/aiocrioc)
- **[ThreatIngestor](https://github.com/InQuest/ThreatIngestor)** 🟢 — Extracts/aggregates IOCs from feeds; integrates with MISP/ThreatKB (pairs well with LLM post-processing). [![stars](https://img.shields.io/github/stars/InQuest/ThreatIngestor?style=flat-square&label=%E2%98%85)](https://github.com/InQuest/ThreatIngestor) [![updated](https://img.shields.io/github/last-commit/InQuest/ThreatIngestor?style=flat-square&label=updated)](https://github.com/InQuest/ThreatIngestor)
- **[IATelligence](https://github.com/fr0gger/IATelligence)** 🟢 — Explains imported Windows APIs in PE files via GPT and maps to MITRE ATT&CK. [![stars](https://img.shields.io/github/stars/fr0gger/IATelligence?style=flat-square&label=%E2%98%85)](https://github.com/fr0gger/IATelligence) [![updated](https://img.shields.io/github/last-commit/fr0gger/IATelligence?style=flat-square&label=updated)](https://github.com/fr0gger/IATelligence)
  - **Related:** [MCP_Security](https://github.com/fr0gger/MCP_Security)
- **[MCP_Security](https://github.com/fr0gger/MCP_Security)** 🟢⚠️ — MCP server (ORKL) for querying the ORKL threat-intel API. [![stars](https://img.shields.io/github/stars/fr0gger/MCP_Security?style=flat-square&label=%E2%98%85)](https://github.com/fr0gger/MCP_Security) [![updated](https://img.shields.io/github/last-commit/fr0gger/MCP_Security?style=flat-square&label=updated)](https://github.com/fr0gger/MCP_Security)
  - **Related:** [IATelligence](https://github.com/fr0gger/IATelligence)

---

## Log Analysis / SIEM / SOC Triage

AI agents for SOC alert triage, investigation, and incident response.

- **[AI-SOC-Agent](https://github.com/M507/ai-soc-agent)** 🟢 — Black Hat 2025 MCP server exposing security-investigation tools (ELK, IRIS). [![stars](https://img.shields.io/github/stars/M507/ai-soc-agent?style=flat-square&label=%E2%98%85)](https://github.com/M507/ai-soc-agent) [![updated](https://img.shields.io/github/last-commit/M507/ai-soc-agent?style=flat-square&label=updated)](https://github.com/M507/ai-soc-agent)
- **[agentic-soc-platform](https://github.com/FunnyWolf/agentic-soc-platform)** 🟢 — Agentic SOC platform (LangGraph/Dify) with local-LLM support. [![stars](https://img.shields.io/github/stars/FunnyWolf/agentic-soc-platform?style=flat-square&label=%E2%98%85)](https://github.com/FunnyWolf/agentic-soc-platform) [![updated](https://img.shields.io/github/last-commit/FunnyWolf/agentic-soc-platform?style=flat-square&label=updated)](https://github.com/FunnyWolf/agentic-soc-platform)
- **[SOCGPT](https://github.com/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant)** 🟢 — LLM log summarization, severity triage, MITRE mapping, and Q&A. [![stars](https://img.shields.io/github/stars/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant?style=flat-square&label=%E2%98%85)](https://github.com/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant) [![updated](https://img.shields.io/github/last-commit/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant?style=flat-square&label=updated)](https://github.com/Ninadjos/SOCGPT-AI-Powered-SOC-Assistant)
- **[AttackGen](https://github.com/mrwadams/attackgen)** 🟢 — LLM-driven incident-response scenario generator using MITRE ATT&CK + ATLAS. [![stars](https://img.shields.io/github/stars/mrwadams/attackgen?style=flat-square&label=%E2%98%85)](https://github.com/mrwadams/attackgen) [![updated](https://img.shields.io/github/last-commit/mrwadams/attackgen?style=flat-square&label=updated)](https://github.com/mrwadams/attackgen)

---

## Reverse Engineering

LLM-assisted binary analysis and traffic inspection.

- **[Gepetto](https://github.com/JusticeRage/Gepetto)** 🟢 — IDA Pro plugin: GPT adds comments and meaningful variable names. [![stars](https://img.shields.io/github/stars/JusticeRage/Gepetto?style=flat-square&label=%E2%98%85)](https://github.com/JusticeRage/Gepetto) [![updated](https://img.shields.io/github/last-commit/JusticeRage/Gepetto?style=flat-square&label=updated)](https://github.com/JusticeRage/Gepetto)
- **[GhidraMCP](https://github.com/LaurieWired/GhidraMCP)** 🟢 — MCP server exposing Ghidra reverse-engineering ops to any MCP-capable LLM. [![stars](https://img.shields.io/github/stars/LaurieWired/GhidraMCP?style=flat-square&label=%E2%98%85)](https://github.com/LaurieWired/GhidraMCP) [![updated](https://img.shields.io/github/last-commit/LaurieWired/GhidraMCP?style=flat-square&label=updated)](https://github.com/LaurieWired/GhidraMCP)
  - **Related:** [GhidrOllama](https://github.com/lr-m/GhidrOllama) · [OGhidra](https://github.com/llnl/OGhidra)
- **[GhidrOllama](https://github.com/lr-m/GhidrOllama)** 🟢⚠️ — Ghidra script using the Ollama API for function analysis/renaming. [![stars](https://img.shields.io/github/stars/lr-m/GhidrOllama?style=flat-square&label=%E2%98%85)](https://github.com/lr-m/GhidrOllama) [![updated](https://img.shields.io/github/last-commit/lr-m/GhidrOllama?style=flat-square&label=updated)](https://github.com/lr-m/GhidrOllama)
  - **Related:** [OGhidra](https://github.com/llnl/OGhidra) · [GhidraMCP](https://github.com/LaurieWired/GhidraMCP)
- **[OGhidra](https://github.com/llnl/OGhidra)** 🟢 — Natural-language Ghidra analysis via Ollama. *(Lawrence Livermore National Lab)* [![stars](https://img.shields.io/github/stars/llnl/OGhidra?style=flat-square&label=%E2%98%85)](https://github.com/llnl/OGhidra) [![updated](https://img.shields.io/github/last-commit/llnl/OGhidra?style=flat-square&label=updated)](https://github.com/llnl/OGhidra)
  - **Related:** [GhidrOllama](https://github.com/lr-m/GhidrOllama) · [GhidraMCP](https://github.com/LaurieWired/GhidraMCP)
- **[ghidra_tools (G-3PO)](https://github.com/tenable/ghidra_tools)** 🟢 — Ghidra plugin for AI-assisted decompiled-code analysis. *(Tenable)* [![stars](https://img.shields.io/github/stars/tenable/ghidra_tools?style=flat-square&label=%E2%98%85)](https://github.com/tenable/ghidra_tools) [![updated](https://img.shields.io/github/last-commit/tenable/ghidra_tools?style=flat-square&label=updated)](https://github.com/tenable/ghidra_tools)
- **[gpt-wpre](https://github.com/moyix/gpt-wpre)** 🔬 — Whole-program reverse engineering with GPT-3. [![stars](https://img.shields.io/github/stars/moyix/gpt-wpre?style=flat-square&label=%E2%98%85)](https://github.com/moyix/gpt-wpre) [![updated](https://img.shields.io/github/last-commit/moyix/gpt-wpre?style=flat-square&label=updated)](https://github.com/moyix/gpt-wpre)
- **[burpgpt](https://github.com/aress31/burpgpt)** 🟢 — Burp Suite extension integrating GPT for passive scanning. [![stars](https://img.shields.io/github/stars/aress31/burpgpt?style=flat-square&label=%E2%98%85)](https://github.com/aress31/burpgpt) [![updated](https://img.shields.io/github/last-commit/aress31/burpgpt?style=flat-square&label=updated)](https://github.com/aress31/burpgpt)
  - **Related:** [Burp-extension-for-GPT](https://github.com/tenable/Burp-extension-for-GPT)
- **[Burp-extension-for-GPT](https://github.com/tenable/Burp-extension-for-GPT)** 🟢 — Burp extension to analyze HTTP traffic with GPT. *(Tenable)* [![stars](https://img.shields.io/github/stars/tenable/Burp-extension-for-GPT?style=flat-square&label=%E2%98%85)](https://github.com/tenable/Burp-extension-for-GPT) [![updated](https://img.shields.io/github/last-commit/tenable/Burp-extension-for-GPT?style=flat-square&label=updated)](https://github.com/tenable/Burp-extension-for-GPT)
  - **Related:** [burpgpt](https://github.com/aress31/burpgpt)

---

## LLM Red-Teaming & Guardrails

Tools for attacking and defending LLM applications themselves.

- **[garak](https://github.com/NVIDIA/garak)** 🟢 — The LLM vulnerability scanner — probes for prompt injection, jailbreaks, data leakage, and more. *(NVIDIA)* [![stars](https://img.shields.io/github/stars/NVIDIA/garak?style=flat-square&label=%E2%98%85)](https://github.com/NVIDIA/garak) [![updated](https://img.shields.io/github/last-commit/NVIDIA/garak?style=flat-square&label=updated)](https://github.com/NVIDIA/garak)
  - **Related:** [PyRIT](https://github.com/microsoft/PyRIT) · [promptfoo](https://github.com/promptfoo/promptfoo)
- **[PyRIT](https://github.com/microsoft/PyRIT)** 🟢 — Python Risk Identification Tool; battle-tested across 100+ GenAI red-team operations. *(Microsoft)* [![stars](https://img.shields.io/github/stars/microsoft/PyRIT?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/PyRIT) [![updated](https://img.shields.io/github/last-commit/microsoft/PyRIT?style=flat-square&label=updated)](https://github.com/microsoft/PyRIT)
- **[promptfoo](https://github.com/promptfoo/promptfoo)** 🟢 — LLM eval + red-teaming/pentesting CLI with 50+ attack plugins (MIT). *Note: OpenAI announced an acquisition agreement in March 2026; remains MIT-licensed — track governance.* [![stars](https://img.shields.io/github/stars/promptfoo/promptfoo?style=flat-square&label=%E2%98%85)](https://github.com/promptfoo/promptfoo) [![updated](https://img.shields.io/github/last-commit/promptfoo/promptfoo?style=flat-square&label=updated)](https://github.com/promptfoo/promptfoo)
- **[DeepTeam](https://github.com/confident-ai/deepteam)** 🟢 — Open-source framework for red-teaming LLMs and LLM systems across jailbreaks, prompt injection, data leakage, and safety risks. [![stars](https://img.shields.io/github/stars/confident-ai/deepteam?style=flat-square&label=%E2%98%85)](https://github.com/confident-ai/deepteam) [![updated](https://img.shields.io/github/last-commit/confident-ai/deepteam?style=flat-square&label=updated)](https://github.com/confident-ai/deepteam)
- **[Moonshot](https://github.com/aiverify-foundation/moonshot)** 🟢 — Modular tool for benchmarking, red-teaming, and evaluating LLM applications with custom connectors and recipes. *(AI Verify Foundation)* [![stars](https://img.shields.io/github/stars/aiverify-foundation/moonshot?style=flat-square&label=%E2%98%85)](https://github.com/aiverify-foundation/moonshot) [![updated](https://img.shields.io/github/last-commit/aiverify-foundation/moonshot?style=flat-square&label=updated)](https://github.com/aiverify-foundation/moonshot)
- **[LLM Guard](https://github.com/protectai/llm-guard)** 🟢 — Suite of input/output scanners (PII, prompt injection, etc.). *(Protect AI)* [![stars](https://img.shields.io/github/stars/protectai/llm-guard?style=flat-square&label=%E2%98%85)](https://github.com/protectai/llm-guard) [![updated](https://img.shields.io/github/last-commit/protectai/llm-guard?style=flat-square&label=updated)](https://github.com/protectai/llm-guard)
  - **Related:** [Rebuff](https://github.com/protectai/rebuff)
- **[Rebuff](https://github.com/protectai/rebuff)** 🟢 — Archived prompt-injection detector (heuristics + LLM + vector DB + canary tokens). *(Protect AI)* [![stars](https://img.shields.io/github/stars/protectai/rebuff?style=flat-square&label=%E2%98%85)](https://github.com/protectai/rebuff) [![updated](https://img.shields.io/github/last-commit/protectai/rebuff?style=flat-square&label=updated)](https://github.com/protectai/rebuff)
  - **Related:** [LLM Guard](https://github.com/protectai/llm-guard)
- **[NeMo Guardrails](https://github.com/NVIDIA-NeMo/Guardrails)** 🟢 — Programmable guardrails (input/output/dialog/retrieval rails) for LLM apps. *(NVIDIA)* [![stars](https://img.shields.io/github/stars/NVIDIA-NeMo/Guardrails?style=flat-square&label=%E2%98%85)](https://github.com/NVIDIA-NeMo/Guardrails) [![updated](https://img.shields.io/github/last-commit/NVIDIA-NeMo/Guardrails?style=flat-square&label=updated)](https://github.com/NVIDIA-NeMo/Guardrails)
- **[PurpleLlama](https://github.com/meta-llama/PurpleLlama)** 🟢 — Llama Guard classifiers, CodeShield, and CyberSecEval. *(Meta)* [![stars](https://img.shields.io/github/stars/meta-llama/PurpleLlama?style=flat-square&label=%E2%98%85)](https://github.com/meta-llama/PurpleLlama) [![updated](https://img.shields.io/github/last-commit/meta-llama/PurpleLlama?style=flat-square&label=updated)](https://github.com/meta-llama/PurpleLlama)
- **[Vigil](https://github.com/deadbits/vigil-llm)** 🟢🔬 — Library/REST API to scan prompts and responses for prompt injection. [![stars](https://img.shields.io/github/stars/deadbits/vigil-llm?style=flat-square&label=%E2%98%85)](https://github.com/deadbits/vigil-llm) [![updated](https://img.shields.io/github/last-commit/deadbits/vigil-llm?style=flat-square&label=updated)](https://github.com/deadbits/vigil-llm)
- **[Counterfit](https://github.com/Azure/counterfit)** 🟢 — ML/AI penetration-testing automation tool. *(Microsoft)* [![stars](https://img.shields.io/github/stars/Azure/counterfit?style=flat-square&label=%E2%98%85)](https://github.com/Azure/counterfit) [![updated](https://img.shields.io/github/last-commit/Azure/counterfit?style=flat-square&label=updated)](https://github.com/Azure/counterfit)
- **[AI-Red-Teaming-Playground-Labs](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)** 🟢 — CTFd-based AI red-team training challenges. *(Microsoft)* [![stars](https://img.shields.io/github/stars/microsoft/AI-Red-Teaming-Playground-Labs?style=flat-square&label=%E2%98%85)](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs) [![updated](https://img.shields.io/github/last-commit/microsoft/AI-Red-Teaming-Playground-Labs?style=flat-square&label=updated)](https://github.com/microsoft/AI-Red-Teaming-Playground-Labs)
- **[EasyJailbreak](https://github.com/EasyJailbreak/EasyJailbreak)** 🟢🔬 — Framework for building and testing adversarial jailbreak prompts. [![stars](https://img.shields.io/github/stars/EasyJailbreak/EasyJailbreak?style=flat-square&label=%E2%98%85)](https://github.com/EasyJailbreak/EasyJailbreak) [![updated](https://img.shields.io/github/last-commit/EasyJailbreak/EasyJailbreak?style=flat-square&label=updated)](https://github.com/EasyJailbreak/EasyJailbreak)
- **[llm-security](https://github.com/greshake/llm-security)** 🔬 — Original PoC for indirect prompt-injection attacks. [![stars](https://img.shields.io/github/stars/greshake/llm-security?style=flat-square&label=%E2%98%85)](https://github.com/greshake/llm-security) [![updated](https://img.shields.io/github/last-commit/greshake/llm-security?style=flat-square&label=updated)](https://github.com/greshake/llm-security)
- **[JailbreakLLMs](https://github.com/TrustAIRLab/JailbreakLLMs)** 🔬⚠️ — Research dataset of 6,387 ChatGPT prompts, including in-the-wild jailbreak prompts from Reddit, Discord, websites, and open datasets. [![stars](https://img.shields.io/github/stars/TrustAIRLab/JailbreakLLMs?style=flat-square&label=%E2%98%85)](https://github.com/TrustAIRLab/JailbreakLLMs) [![updated](https://img.shields.io/github/last-commit/TrustAIRLab/JailbreakLLMs?style=flat-square&label=updated)](https://github.com/TrustAIRLab/JailbreakLLMs)
- **[prompt-injection-defenses](https://github.com/tldrsec/prompt-injection-defenses)** 🟢⚠️ — Curated catalog of practical defenses against prompt injection. [![stars](https://img.shields.io/github/stars/tldrsec/prompt-injection-defenses?style=flat-square&label=%E2%98%85)](https://github.com/tldrsec/prompt-injection-defenses) [![updated](https://img.shields.io/github/last-commit/tldrsec/prompt-injection-defenses?style=flat-square&label=updated)](https://github.com/tldrsec/prompt-injection-defenses)

---

## LLM Honeypots & Deception

Honeypots and deception that use LLMs to simulate convincing systems.

- **[Beelzebub](https://github.com/mariocandela/beelzebub)** 🟢 — Low-code honeypot using LLMs to simulate SSH/HTTP/MCP services (Go). [![stars](https://img.shields.io/github/stars/mariocandela/beelzebub?style=flat-square&label=%E2%98%85)](https://github.com/mariocandela/beelzebub) [![updated](https://img.shields.io/github/last-commit/mariocandela/beelzebub?style=flat-square&label=updated)](https://github.com/mariocandela/beelzebub)
- **[shelLM](https://github.com/stratosphereips/shelLM)** 🟢🔬 — LLM-powered SSH honeypot (paper *"LLM in the Shell"*). [![stars](https://img.shields.io/github/stars/stratosphereips/shelLM?style=flat-square&label=%E2%98%85)](https://github.com/stratosphereips/shelLM) [![updated](https://img.shields.io/github/last-commit/stratosphereips/shelLM?style=flat-square&label=updated)](https://github.com/stratosphereips/shelLM)
  - **Related:** [VelLMes](https://github.com/stratosphereips/VelLMes-AI-Honeypot)
- **[VelLMes](https://github.com/stratosphereips/VelLMes-AI-Honeypot)** 🟢🔬 — Multi-protocol LLM honeypot framework (successor to shelLM). [![stars](https://img.shields.io/github/stars/stratosphereips/VelLMes-AI-Honeypot?style=flat-square&label=%E2%98%85)](https://github.com/stratosphereips/VelLMes-AI-Honeypot) [![updated](https://img.shields.io/github/last-commit/stratosphereips/VelLMes-AI-Honeypot?style=flat-square&label=updated)](https://github.com/stratosphereips/VelLMes-AI-Honeypot)
  - **Related:** [shelLM](https://github.com/stratosphereips/shelLM)
- **[llm-honeypot](https://github.com/PalisadeResearch/llm-honeypot)** 🔬⚠️ — Cowrie SSH honeypot extended with prompt-injection traps to detect LLM hacker agents. *(Palisade Research)* [![stars](https://img.shields.io/github/stars/PalisadeResearch/llm-honeypot?style=flat-square&label=%E2%98%85)](https://github.com/PalisadeResearch/llm-honeypot) [![updated](https://img.shields.io/github/last-commit/PalisadeResearch/llm-honeypot?style=flat-square&label=updated)](https://github.com/PalisadeResearch/llm-honeypot)

---

## CTF / Exploit / Bug-Bounty Agents & Benchmarks

Offensive agents and the benchmarks used to evaluate them.

- **[SWE-agent (EnIGMA)](https://github.com/SWE-agent/SWE-agent)** 🟢🔬 — EnIGMA offensive-CTF mode; SOTA on NYU CTF, InterCode-CTF, and Cybench (v0.7 branch). [![stars](https://img.shields.io/github/stars/SWE-agent/SWE-agent?style=flat-square&label=%E2%98%85)](https://github.com/SWE-agent/SWE-agent) [![updated](https://img.shields.io/github/last-commit/SWE-agent/SWE-agent?style=flat-square&label=updated)](https://github.com/SWE-agent/SWE-agent)
  - **Related:** [Cybench](https://github.com/andyzorigin/cybench) · [NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) · [InterCode](https://github.com/princeton-nlp/intercode)
- **[Cybench](https://github.com/andyzorigin/cybench)** 🔬 — 40 professional CTF tasks across 4 competitions; widely used by AI safety institutes. [![stars](https://img.shields.io/github/stars/andyzorigin/cybench?style=flat-square&label=%E2%98%85)](https://github.com/andyzorigin/cybench) [![updated](https://img.shields.io/github/last-commit/andyzorigin/cybench?style=flat-square&label=updated)](https://github.com/andyzorigin/cybench)
- **[NYU CTF Bench](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)** 🔬 — Dockerized CSAW CTF challenges for LLM-agent evaluation. [![stars](https://img.shields.io/github/stars/NYU-LLM-CTF/NYU_CTF_Bench?style=flat-square&label=%E2%98%85)](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench) [![updated](https://img.shields.io/github/last-commit/NYU-LLM-CTF/NYU_CTF_Bench?style=flat-square&label=updated)](https://github.com/NYU-LLM-CTF/NYU_CTF_Bench)
- **[InterCode](https://github.com/princeton-nlp/intercode)** 🔬 — Interactive-coding benchmark incl. InterCode-CTF. [![stars](https://img.shields.io/github/stars/princeton-nlp/intercode?style=flat-square&label=%E2%98%85)](https://github.com/princeton-nlp/intercode) [![updated](https://img.shields.io/github/last-commit/princeton-nlp/intercode?style=flat-square&label=updated)](https://github.com/princeton-nlp/intercode)
- **[BountyBench](https://github.com/bountybench/bountybench)** 🔬 — 25 real systems / 40 bug bounties for Detect-Exploit-Patch evaluation. [![stars](https://img.shields.io/github/stars/bountybench/bountybench?style=flat-square&label=%E2%98%85)](https://github.com/bountybench/bountybench) [![updated](https://img.shields.io/github/last-commit/bountybench/bountybench?style=flat-square&label=updated)](https://github.com/bountybench/bountybench)
- **[Cyber-Zero](https://github.com/amazon-science/Cyber-Zero)** 🔬 — Trains cybersecurity agents without runtime; ships an EnIGMA+ scaffold. *(Amazon Science)* [![stars](https://img.shields.io/github/stars/amazon-science/Cyber-Zero?style=flat-square&label=%E2%98%85)](https://github.com/amazon-science/Cyber-Zero) [![updated](https://img.shields.io/github/last-commit/amazon-science/Cyber-Zero?style=flat-square&label=updated)](https://github.com/amazon-science/Cyber-Zero)
  - **Sources:** [SWE-agent](https://github.com/SWE-agent/SWE-agent)
  - **Related:** [SWE-agent](https://github.com/SWE-agent/SWE-agent)
- **[ExploitBench](https://github.com/exploitbench/exploitbench)** 🔬 — Measures AI-agent progress on V8/Chromium exploit ladders. [![stars](https://img.shields.io/github/stars/exploitbench/exploitbench?style=flat-square&label=%E2%98%85)](https://github.com/exploitbench/exploitbench) [![updated](https://img.shields.io/github/last-commit/exploitbench/exploitbench?style=flat-square&label=updated)](https://github.com/exploitbench/exploitbench)
- **[claude-bug-bounty](https://github.com/shuvonsec/claude-bug-bounty)** 🟢 — Claude Code plugin orchestrating recon → vuln classes → reporting. [![stars](https://img.shields.io/github/stars/shuvonsec/claude-bug-bounty?style=flat-square&label=%E2%98%85)](https://github.com/shuvonsec/claude-bug-bounty) [![updated](https://img.shields.io/github/last-commit/shuvonsec/claude-bug-bounty?style=flat-square&label=updated)](https://github.com/shuvonsec/claude-bug-bounty)
- **[Bug-Bounty-Agents](https://github.com/matty69v/Bug-Bounty-Agents)** 🟢 — 43 AI agent personas for Claude Code / Copilot / Cursor across the bug-bounty lifecycle. [![stars](https://img.shields.io/github/stars/matty69v/Bug-Bounty-Agents?style=flat-square&label=%E2%98%85)](https://github.com/matty69v/Bug-Bounty-Agents) [![updated](https://img.shields.io/github/last-commit/matty69v/Bug-Bounty-Agents?style=flat-square&label=updated)](https://github.com/matty69v/Bug-Bounty-Agents)
- **[ai-exploits](https://github.com/protectai/ai-exploits)** 🟢 — Real-world AI/ML exploits (Metasploit modules + Nuclei templates) for MLflow, Ray, H2O. *(Protect AI)* [![stars](https://img.shields.io/github/stars/protectai/ai-exploits?style=flat-square&label=%E2%98%85)](https://github.com/protectai/ai-exploits) [![updated](https://img.shields.io/github/last-commit/protectai/ai-exploits?style=flat-square&label=updated)](https://github.com/protectai/ai-exploits)

---

## Cloud / IaC / DFIR / OSINT / Phishing

AI tooling for cloud/IaC security, digital forensics, OSINT, and phishing detection.

- **[EscalateGPT](https://github.com/tenable/EscalateGPT)** 🟢 — GPT-based discovery of privilege-escalation paths in AWS IAM policies. *(Tenable)* [![stars](https://img.shields.io/github/stars/tenable/EscalateGPT?style=flat-square&label=%E2%98%85)](https://github.com/tenable/EscalateGPT) [![updated](https://img.shields.io/github/last-commit/tenable/EscalateGPT?style=flat-square&label=updated)](https://github.com/tenable/EscalateGPT)
- **[MemoryInvestigator](https://github.com/jan-hendrik-lang/MemoryInvestigator)** 🔬 — Volatility 3 + LLM + RAG for memory-forensic triage. [![stars](https://img.shields.io/github/stars/jan-hendrik-lang/MemoryInvestigator?style=flat-square&label=%E2%98%85)](https://github.com/jan-hendrik-lang/MemoryInvestigator) [![updated](https://img.shields.io/github/last-commit/jan-hendrik-lang/MemoryInvestigator?style=flat-square&label=updated)](https://github.com/jan-hendrik-lang/MemoryInvestigator)
  - **Related:** [Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)
- **[Volatility-MCP-Server](https://github.com/bornpresident/Volatility-MCP-Server)** 🟢 — MCP exposing Volatility 3 plugins for natural-language memory forensics. [![stars](https://img.shields.io/github/stars/bornpresident/Volatility-MCP-Server?style=flat-square&label=%E2%98%85)](https://github.com/bornpresident/Volatility-MCP-Server) [![updated](https://img.shields.io/github/last-commit/bornpresident/Volatility-MCP-Server?style=flat-square&label=updated)](https://github.com/bornpresident/Volatility-MCP-Server)
  - **Related:** [MemoryInvestigator](https://github.com/jan-hendrik-lang/MemoryInvestigator)
- **[PhishLLM](https://github.com/code-philia/PhishLLM)** 🔬⚠️ — Reference-less phishing detection via LLM brand recognition (USENIX'24). [![stars](https://img.shields.io/github/stars/code-philia/PhishLLM?style=flat-square&label=%E2%98%85)](https://github.com/code-philia/PhishLLM) [![updated](https://img.shields.io/github/last-commit/code-philia/PhishLLM?style=flat-square&label=updated)](https://github.com/code-philia/PhishLLM)
  - **Related:** [PhishVLM](https://github.com/code-philia/PhishVLM)
- **[osintgpt](https://github.com/estebanpdl/osintgpt)** 🟢⚠️ — OpenAI embeddings + Qdrant over OSINT corpora. [![stars](https://img.shields.io/github/stars/estebanpdl/osintgpt?style=flat-square&label=%E2%98%85)](https://github.com/estebanpdl/osintgpt) [![updated](https://img.shields.io/github/last-commit/estebanpdl/osintgpt?style=flat-square&label=updated)](https://github.com/estebanpdl/osintgpt)
- **[gpt-osint](https://github.com/gigz/gpt-osint)** 🟢 — Web-based GPT-4 OSINT tool over social-media dumps and CSVs. [![stars](https://img.shields.io/github/stars/gigz/gpt-osint?style=flat-square&label=%E2%98%85)](https://github.com/gigz/gpt-osint) [![updated](https://img.shields.io/github/last-commit/gigz/gpt-osint?style=flat-square&label=updated)](https://github.com/gigz/gpt-osint)

---

## Related Awesome Lists

- **[awesome-llm-cybersecurity-tools](https://github.com/tenable/awesome-llm-cybersecurity-tools)** — Tenable's list (archived but a strong reference). [![stars](https://img.shields.io/github/stars/tenable/awesome-llm-cybersecurity-tools?style=flat-square&label=%E2%98%85)](https://github.com/tenable/awesome-llm-cybersecurity-tools) [![updated](https://img.shields.io/github/last-commit/tenable/awesome-llm-cybersecurity-tools?style=flat-square&label=updated)](https://github.com/tenable/awesome-llm-cybersecurity-tools)
- **[Awesome-LLM4Cybersecurity](https://github.com/tmylla/Awesome-LLM4Cybersecurity)** — 600+ papers on LLMs for cybersecurity. [![stars](https://img.shields.io/github/stars/tmylla/Awesome-LLM4Cybersecurity?style=flat-square&label=%E2%98%85)](https://github.com/tmylla/Awesome-LLM4Cybersecurity) [![updated](https://img.shields.io/github/last-commit/tmylla/Awesome-LLM4Cybersecurity?style=flat-square&label=updated)](https://github.com/tmylla/Awesome-LLM4Cybersecurity)
- **[awesome-ai-cybersecurity](https://github.com/ElNiak/awesome-ai-cybersecurity)** — Broad AI-for-security collection. [![stars](https://img.shields.io/github/stars/ElNiak/awesome-ai-cybersecurity?style=flat-square&label=%E2%98%85)](https://github.com/ElNiak/awesome-ai-cybersecurity) [![updated](https://img.shields.io/github/last-commit/ElNiak/awesome-ai-cybersecurity?style=flat-square&label=updated)](https://github.com/ElNiak/awesome-ai-cybersecurity)
- **[awesome-genai-cyberhub](https://github.com/Ashfaaq98/awesome-genai-cyberhub)** — GenAI-driven cybersecurity resources. [![stars](https://img.shields.io/github/stars/Ashfaaq98/awesome-genai-cyberhub?style=flat-square&label=%E2%98%85)](https://github.com/Ashfaaq98/awesome-genai-cyberhub) [![updated](https://img.shields.io/github/last-commit/Ashfaaq98/awesome-genai-cyberhub?style=flat-square&label=updated)](https://github.com/Ashfaaq98/awesome-genai-cyberhub)
- **[awesome-ai-security](https://github.com/gmh5225/awesome-ai-security)** — For pentesters, bug hunters, and researchers. [![stars](https://img.shields.io/github/stars/gmh5225/awesome-ai-security?style=flat-square&label=%E2%98%85)](https://github.com/gmh5225/awesome-ai-security) [![updated](https://img.shields.io/github/last-commit/gmh5225/awesome-ai-security?style=flat-square&label=updated)](https://github.com/gmh5225/awesome-ai-security)
- **[awesome-ai-security](https://github.com/ottosulin/awesome-ai-security)** — AI security resources. [![stars](https://img.shields.io/github/stars/ottosulin/awesome-ai-security?style=flat-square&label=%E2%98%85)](https://github.com/ottosulin/awesome-ai-security) [![updated](https://img.shields.io/github/last-commit/ottosulin/awesome-ai-security?style=flat-square&label=updated)](https://github.com/ottosulin/awesome-ai-security)
- **[Awesome-AI-Security](https://github.com/TalEliyahu/Awesome-AI-Security)** — AI security resources. [![stars](https://img.shields.io/github/stars/TalEliyahu/Awesome-AI-Security?style=flat-square&label=%E2%98%85)](https://github.com/TalEliyahu/Awesome-AI-Security) [![updated](https://img.shields.io/github/last-commit/TalEliyahu/Awesome-AI-Security?style=flat-square&label=updated)](https://github.com/TalEliyahu/Awesome-AI-Security)
- **[awesome-llm-security](https://github.com/corca-ai/awesome-llm-security)** — Securing LLMs. [![stars](https://img.shields.io/github/stars/corca-ai/awesome-llm-security?style=flat-square&label=%E2%98%85)](https://github.com/corca-ai/awesome-llm-security) [![updated](https://img.shields.io/github/last-commit/corca-ai/awesome-llm-security?style=flat-square&label=updated)](https://github.com/corca-ai/awesome-llm-security)
- **[awesome-security-for-ai](https://github.com/zmre/awesome-security-for-ai)** — Products for securing AI systems. [![stars](https://img.shields.io/github/stars/zmre/awesome-security-for-ai?style=flat-square&label=%E2%98%85)](https://github.com/zmre/awesome-security-for-ai) [![updated](https://img.shields.io/github/last-commit/zmre/awesome-security-for-ai?style=flat-square&label=updated)](https://github.com/zmre/awesome-security-for-ai)
- **[awesome-gpt-security](https://github.com/cckuailong/awesome-gpt-security)** — GPT/LLM security tools and cases. [![stars](https://img.shields.io/github/stars/cckuailong/awesome-gpt-security?style=flat-square&label=%E2%98%85)](https://github.com/cckuailong/awesome-gpt-security) [![updated](https://img.shields.io/github/last-commit/cckuailong/awesome-gpt-security?style=flat-square&label=updated)](https://github.com/cckuailong/awesome-gpt-security)
- **[awesome-threat-intelligence](https://github.com/hslatman/awesome-threat-intelligence)** — Classic CTI list (pairs with the AI-CTI section). [![stars](https://img.shields.io/github/stars/hslatman/awesome-threat-intelligence?style=flat-square&label=%E2%98%85)](https://github.com/hslatman/awesome-threat-intelligence) [![updated](https://img.shields.io/github/last-commit/hslatman/awesome-threat-intelligence?style=flat-square&label=updated)](https://github.com/hslatman/awesome-threat-intelligence)

---

## Contributing

Contributions are welcome! Open a PR adding entries in the format below, keeping each section sorted by relevance/maintenance.

```
- **[name](repo-url)** 🟢/🔬/🟠/⚠️ — One-line description. *(maintainer/org)* <stars badge> <last-commit badge>
  - **Sources:** [upstream A](url) · [upstream B](url)       # optional — projects this is built on
  - **Related:** [sibling tool](url) · [related project](url) # optional — peers / forks / successors
```

Badges use the dynamic shields.io GitHub endpoints, so they update automatically:

```
[![stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square&label=★)](https://github.com/OWNER/REPO)
[![updated](https://img.shields.io/github/last-commit/OWNER/REPO?style=flat-square&label=updated)](https://github.com/OWNER/REPO)
```

Guidelines: link the canonical upstream repo (not a fork); verify the URL resolves; tag the correct type and add ⚠️ for non-permissive, non-commercial, or unclear/no-license projects; prefer real, installable projects over blog-only references.

## License

To the extent possible under law, the contributors have waived all copyright and related rights to this list ([CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)). Linked projects retain their own licenses — check each before use.
