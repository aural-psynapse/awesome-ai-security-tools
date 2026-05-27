#!/usr/bin/env python3
"""Generate the Awesome AI Security Tools README from structured data.

Badges are dynamic shields.io endpoints (stars + last commit) that render live
from the GitHub API, so counts stay fresh without manual updates.
"""

from argparse import ArgumentParser
from pathlib import Path
import re

STAR = "%E2%98%85"  # ★


def badges(repo: str) -> str:
    s = (f"[![stars](https://img.shields.io/github/stars/{repo}"
         f"?style=flat-square&label={STAR})](https://github.com/{repo})")
    c = (f"[![updated](https://img.shields.io/github/last-commit/{repo}"
         f"?style=flat-square&label=updated)](https://github.com/{repo})")
    return f"{s} {c}"


def link(pair):
    label, url = pair
    return f"[{label}]({url})"


def github_anchor(title: str) -> str:
    """Approximate GitHub's Markdown heading anchors for this README."""
    cleaned = re.sub(r"[^\w\s-]", "", title.lower())
    return cleaned.replace(" ", "-")


def render_entry(e):
    repo = e["repo"]
    url = e.get("url", f"https://github.com/{repo}")
    tags = e["tags"]
    org = f" *({e['org']})*" if e.get("org") else ""
    note = f" {e['note']}" if e.get("note") else ""
    line = (f"- **[{e['name']}]({url})** {tags} — {e['desc']}{org}{note} "
            f"{badges(repo)}")
    out = [line]
    if e.get("sources"):
        out.append("  - **Sources:** " + " · ".join(link(s) for s in e["sources"]))
    if e.get("related"):
        out.append("  - **Related:** " + " · ".join(link(r) for r in e["related"]))
    return "\n".join(out)


# Short reusable link targets
GH = "https://github.com/"
VULNHUNTR = ("Vulnhuntr", GH + "protectai/vulnhuntr")
XVULNHUNTR = ("xvulnhuntr", GH + "CompassSecurity/xvulnhuntr")
VULNHUNTR_MOD = ("vulnhuntr-mod", GH + "kxcode/vulnhuntr-mod")
ASAMM = ("asamm", GH + "scadastrangelove/asamm")
AGENT_AUDIT = ("agent-audit", GH + "scadastrangelove/agent-audit")
ATR = ("ATR – Agent Threat Rules", GH + "panguard-ai/agent-threat-rules")
AGUARA = ("aguara", GH + "garagon/aguara")
AGENTGUARD = ("agentguard", GH + "GoPlusSecurity/agentguard")
AGENTIC_RADAR = ("agentic-radar", GH + "splx-ai/agentic-radar")
AGENT_SCAN = ("Snyk Agent Scan", GH + "snyk/agent-scan")
SKILL_SCANNER = ("Cisco AI Defense – skill-scanner", GH + "cisco-ai-defense/skill-scanner")
MCP_SCANNER = ("Cisco AI Defense – mcp-scanner", GH + "cisco-ai-defense/mcp-scanner")
NUCLEI_AT = ("nuclei-autotriage", GH + "cyberok-org/nuclei-autotriage")
SWE_AGENT = ("SWE-agent", GH + "SWE-agent/SWE-agent")
MODELSCAN = ("modelscan", GH + "protectai/modelscan")
FICKLING = ("Fickling", GH + "trailofbits/fickling")
PICKLESCAN = ("picklescan", GH + "mmaitre314/picklescan")

# ---------------------------------------------------------------------------
# Data model: list of (section_title, anchor, intro, body)
# body is either a list of entries (rendered) or a list of (subtitle, [entries])
# ---------------------------------------------------------------------------

SECTIONS = []

SECTIONS.append((
    "Autotriage of Security Findings",
    "autotriage-of-security-findings",
    "AI/LLM tools that triage, deduplicate, prioritize, or validate the output of scanners and finding sources.",
    [
        {"name": "nuclei-autotriage", "repo": "cyberok-org/nuclei-autotriage", "tags": "🟢⚠️",
         "org": "CyberOK",
         "desc": "Two-stage LLM triage (falsifier + red-team pass) of Nuclei JSONL findings via OpenAI-compatible endpoints (vLLM/Ollama).",
         "note": "— **note:** restrictive personal/non-commercial EULA, not a permissive OSS license.",
         "related": [AGENT_AUDIT, ASAMM]},
        {"name": "honeyslop", "repo": "gadievron/honeyslop", "tags": "🟢",
         "desc": "Code-canary decoys to triage AI-hallucinated (\"slop\") vulnerability reports flooding bug-bounty programs."},
        {"name": "nano-analyzer", "repo": "weareaisle/nano-analyzer", "tags": "🟢🔬", "org": "AISLE",
         "desc": "Minimal three-stage LLM pipeline (context → scan → skeptical triage) for zero-day discovery in C/C++."},
        {"name": "ai-soc-triage-assistant", "repo": "pranavibunny/ai-soc-triage-assistant", "tags": "🟢⚠️",
         "desc": "SOC alert triage assistant with prompt-injection guardrails, output validation, and MITRE ATT&CK mapping."},
    ],
    "> See also: GitHub Security Lab's *Taskflow Agent* (CodeQL-alert triage, credited with ~30 real CVEs since Aug 2025) and OpenAI's *Aardvark* / *Codex Security* research previews — public references exist, but there is no standalone installable repo to badge here.",
))

SECTIONS.append((
    "AI Agent & Coding-Agent Security",
    "ai-agent--coding-agent-security",
    "Securing the AI agents themselves — auditing coding agents (Claude Code, Codex, OpenClaw), scanning skills / plugins / MCP manifests, and governance for agentic development. A fast-moving 2026 category, split below by role.",
    [
        ("Scanners & Auditors", [
            {"name": "agent-audit", "repo": "scadastrangelove/agent-audit", "tags": "🟢", "org": "CyberOK / S. Gordeychik",
             "desc": "Forensic auditor for local AI coding agents (Claude Code, Codex CLI, OpenClaw) **and** project-surface scanner for repos shipping skills, plugins, and MCP manifests; 296 bundled rules across native + imported detector families, with optional LLM cross-verification.",
             "sources": [ASAMM, ATR, AGUARA, SKILL_SCANNER],
             "related": [ASAMM, AGUARA, AGENTGUARD, AGENTIC_RADAR, NUCLEI_AT]},
            {"name": "aguara", "repo": "garagon/aguara", "tags": "🟢",
             "desc": "Single-binary static scanner (Go, no LLM) for AI-agent skills and MCP servers; multi-layer engine (pattern + NLP + taint tracking + rug-pull detection). Companion **[aguara-mcp](https://github.com/garagon/aguara-mcp)** exposes scanning as an MCP tool.",
             "related": [("aguara-mcp", GH + "garagon/aguara-mcp"), AGENT_AUDIT, AGENT_SCAN, SKILL_SCANNER]},
            {"name": "agent-scan", "repo": "snyk/agent-scan", "tags": "🟢", "org": "Snyk",
             "desc": "Security scanner for AI agents, MCP servers, and agent skills; the successor path for the original Invariant Labs mcp-scan work.",
             "related": [AGUARA, MCP_SCANNER, SKILL_SCANNER]},
            {"name": "skill-scanner", "repo": "cisco-ai-defense/skill-scanner", "tags": "🟠", "org": "Cisco AI Defense",
             "desc": "Scanner for agent skills combining YAML + YARA patterns, LLM-as-a-judge, and behavioral dataflow analysis (Codex / Cursor skill formats).",
             "related": [("defenseclaw", GH + "cisco-ai-defense/defenseclaw"), AGUARA, MCP_SCANNER]},
            {"name": "mcp-scanner", "repo": "cisco-ai-defense/mcp-scanner", "tags": "🟢⚠️", "org": "Cisco AI Defense",
             "desc": "Scanner for MCP servers and agentic tool surfaces, covering tools, prompts, resources, package risk, malware indicators, and deployment readiness.",
             "related": [SKILL_SCANNER, AGENT_SCAN, AGUARA]},
            {"name": "agentic-radar", "repo": "splx-ai/agentic-radar", "tags": "🟠", "org": "SplxAI",
             "desc": "CLI security scanner for agentic workflows (LangGraph, CrewAI, n8n, etc.) — maps tools/data flows and flags risks."},
        ]),
        ("Frameworks, Rule Standards & Benchmarks", [
            {"name": "asamm", "repo": "scadastrangelove/asamm", "tags": "🔬", "org": "CyberOK / S. Gordeychik",
             "desc": "*Agentic SAMM* — an OWASP SAMM extension for AI-driven development: an entry-point-based threat taxonomy plus 17 controls across 5 SAMM functions (Governance, Design, Implementation, Verification, Operations) with L1/L2/L3 maturity. License: CC BY-SA 4.0.",
             "sources": [("OWASP SAMM", "https://owaspsamm.org/"),
                         ("NIST AI RMF", "https://www.nist.gov/itl/ai-risk-management-framework"),
                         ("NCSC Secure AI Guidelines", "https://www.ncsc.gov.uk/collection/guidelines-secure-ai-system-development"),
                         ("MCP Security Best Practices", "https://modelcontextprotocol.io/")],
             "related": [AGENT_AUDIT]},
            {"name": "agent-threat-rules (ATR)", "repo": "panguard-ai/agent-threat-rules", "tags": "🟢",
             "desc": "Open, versioned, machine-readable detection-rule format for AI-agent threats (prompt injection, tool poisoning, MCP attacks, skill compromise) — \"Sigma for agents\" (MIT). Engine-agnostic; converts to Splunk/Elastic/SARIF.",
             "related": [AGENT_AUDIT, AGUARA]},
            {"name": "AgentDojo", "repo": "ethz-spylab/agentdojo", "tags": "🟢🔬",
             "desc": "Benchmark environment for prompt-injection attacks and defenses in tool-using LLM agents.",
             "related": [AGENT_AUDIT, ATR]},
        ]),
        ("Runtime Protection & Enforcement", [
            {"name": "agentguard", "repo": "GoPlusSecurity/agentguard", "tags": "🟢",
             "desc": "Real-time security layer for coding agents: hooks scan every new skill, block dangerous actions before execution, run daily posture patrols, and track which skill triggered each action (incl. Web3-specific checks).",
             "related": [AGENT_AUDIT, ("defenseclaw", GH + "cisco-ai-defense/defenseclaw")]},
            {"name": "defenseclaw", "repo": "cisco-ai-defense/defenseclaw", "tags": "🟠", "org": "Cisco AI Defense",
             "desc": "Enforcement and evidence layer for agentic deployments: static CodeGuard checks, sandboxing, registry ingestion with SSRF guards, and audit/observability.",
             "related": [SKILL_SCANNER, AGENTGUARD]},
        ]),
    ],
    None,
))

SECTIONS.append((
    "AI/ML Supply Chain & Model Security",
    "aiml-supply-chain--model-security",
    "Tools for securing model artifacts, serialized ML files, and AI/ML supply-chain surfaces.",
    [
        {"name": "modelscan", "repo": "protectai/modelscan", "tags": "🟢", "org": "Protect AI",
         "desc": "Scans ML model files for unsafe serialization patterns and embedded code, with a focus on model serialization attacks.",
         "related": [FICKLING, PICKLESCAN, ("ai-exploits", GH + "protectai/ai-exploits")]},
        {"name": "Fickling", "repo": "trailofbits/fickling", "tags": "🟢", "org": "Trail of Bits",
         "desc": "Python pickle decompiler, rewriter, and static analyzer for inspecting and detecting malicious pickle/PyTorch payloads.",
         "related": [MODELSCAN, PICKLESCAN]},
        {"name": "picklescan", "repo": "mmaitre314/picklescan", "tags": "🟢",
         "desc": "Lightweight CLI/library for detecting suspicious Python pickle operations in ML and model artifacts.",
         "related": [MODELSCAN, FICKLING]},
    ],
    None,
))

SECTIONS.append((
    "Pentest & Red-Team Agents",
    "pentest--red-team-agents",
    "Autonomous and semi-autonomous AI agents for penetration testing, exploitation, and attack simulation.",
    [
        {"name": "PentestGPT", "repo": "GreyDGL/PentestGPT", "tags": "🟢🔬",
         "desc": "The original USENIX'24 LLM pentest agent; re-released as an autonomous pipeline with strong benchmark results."},
        {"name": "PentAGI", "repo": "vxcontrol/pentagi", "tags": "🟢", "org": "VXControl",
         "desc": "Fully autonomous multi-agent pentest framework with Docker sandboxing."},
        {"name": "CAI – Cybersecurity AI", "repo": "aliasrobotics/cai", "tags": "🟢🟠", "org": "Alias Robotics",
         "desc": "Modular, bug-bounty-ready agent framework supporting 300+ LLM models. MIT for research; separate commercial license for production/on-prem."},
        {"name": "Strix", "repo": "usestrix/strix", "tags": "🟢",
         "desc": "Autonomous \"AI hackers\" that dynamically run code and validate vulnerabilities with PoCs (Apache-2.0)."},
        {"name": "hackingBuddyGPT", "repo": "ipa-lab/hackingBuddyGPT", "tags": "🟢🔬",
         "desc": "Minimal (~50 LOC) research framework for LLM-driven Linux priv-esc and web pentesting (FSE'23)."},
        {"name": "Nebula", "repo": "berylliumsec/nebula", "tags": "🟢🟠",
         "desc": "AI pentesting CLI assistant with local-LLM support (Llama-3.1, Mistral, DeepSeek)."},
        {"name": "HexStrike-AI", "repo": "0x4m4/hexstrike-ai", "tags": "🟢",
         "desc": "MCP server exposing 150+ security tools (nmap, gobuster, nuclei, …) to AI agents (MIT)."},
        {"name": "Shannon", "repo": "KeygraphHQ/shannon", "tags": "🟢",
         "desc": "White-box autonomous AI pentester with strong XBOW-benchmark results."},
        {"name": "PentestAgent", "repo": "GH05TCREW/pentestagent", "tags": "🟢",
         "desc": "Black-box AI pentest framework with MCP, multi-agent spawning, and persistent sessions."},
        {"name": "cyber-security-llm-agents", "repo": "NVISOsecurity/cyber-security-llm-agents", "tags": "🟢⚠️", "org": "NVISO",
         "desc": "AutoGen-based agents for cybersecurity tasks (shown at RSAC 2024)."},
        {"name": "Pentest-Swarm-AI", "repo": "Armur-Ai/Pentest-Swarm-AI", "tags": "🟢",
         "desc": "Swarm-intelligence multi-agent pentest with stigmergic blackboard coordination (Go)."},
        {"name": "hackGPT", "repo": "NoDataFound/hackGPT", "tags": "🟢⚠️",
         "desc": "LLM offensive-security toolkit."},
    ],
    None,
))

SECTIONS.append((
    "AI-Powered SAST & Secure Code Review",
    "ai-powered-sast--secure-code-review",
    "Static analysis and secure code review enhanced with LLMs.",
    [
        {"name": "Vulnhuntr", "repo": "protectai/vulnhuntr", "tags": "🟢", "org": "Protect AI",
         "desc": "Zero-shot vulnerability discovery in Python repos via LLM call-chain analysis; credited with a 0-day RCE in Ragflow.",
         "related": [XVULNHUNTR, VULNHUNTR_MOD]},
        {"name": "claude-code-security-review", "repo": "anthropics/claude-code-security-review", "tags": "🟠", "org": "Anthropic",
         "desc": "Official Claude-based semantic SAST GitHub Action that reviews PR diffs."},
        {"name": "IRIS", "repo": "iris-sast/iris", "tags": "🟢🔬",
         "desc": "Neurosymbolic SAST combining LLMs with CodeQL for Java vulnerability detection (MIT)."},
        {"name": "xvulnhuntr", "repo": "CompassSecurity/xvulnhuntr", "tags": "🟢", "org": "Compass Security",
         "desc": "Archived fork of Vulnhuntr extending support to C#, Java, and Go.",
         "sources": [VULNHUNTR], "related": [VULNHUNTR_MOD]},
        {"name": "llm-security-scanner", "repo": "iknowjason/llm-security-scanner", "tags": "🟢⚠️",
         "desc": "LLM-powered code scanner that opens GitHub issues for findings."},
        {"name": "vulnhuntr-mod", "repo": "kxcode/vulnhuntr-mod", "tags": "🟢",
         "desc": "Modified Vulnhuntr with Qwen/Hunyuan support and Chinese-language prompts.",
         "sources": [VULNHUNTR], "related": [XVULNHUNTR]},
    ],
    None,
))

SECTIONS.append((
    "LLM-Driven Fuzzing",
    "llm-driven-fuzzing",
    "Two families: (a) LLMs generating harnesses/targets for traditional fuzzing, and (b) fuzzing the LLM itself.",
    [
        ("Harness / target generation", [
            {"name": "oss-fuzz-gen", "repo": "google/oss-fuzz-gen", "tags": "🟢", "org": "Google",
             "desc": "LLM-driven fuzz-harness generation for OSS-Fuzz; reported 26 real vulnerabilities (incl. CVE-2024-9143 in OpenSSL)."},
            {"name": "PromptFuzz", "repo": "PromptFuzz/PromptFuzz", "tags": "🟢🔬⚠️",
             "desc": "LLM-mutated prompts to generate fuzz drivers for C/C++ libraries (Rust)."},
            {"name": "Fuzz4All", "repo": "fuzz4all/fuzz4all", "tags": "🟢🔬",
             "desc": "\"Universal\" LLM-based fuzzer across compilers/languages (ICSE 2024)."},
            {"name": "ChatAFL", "repo": "ChatAFLndss/ChatAFL", "tags": "🟢🔬",
             "desc": "LLM-guided protocol fuzzing extending AFLNet (NDSS'24)."},
            {"name": "TitanFuzz", "repo": "ise-uiuc/TitanFuzz", "tags": "🟢🔬⚠️",
             "desc": "First LLM-based fuzzer for PyTorch/TensorFlow (ISSTA'23)."},
        ]),
        ("Fuzzing the LLM", [
            {"name": "LLMFuzzer", "repo": "mnns/LLMFuzzer", "tags": "🟢",
             "desc": "First open-source fuzzing framework for LLM API integrations."},
            {"name": "ps-fuzz", "repo": "prompt-security/ps-fuzz", "tags": "🟠", "org": "Prompt Security",
             "desc": "System-prompt hardening fuzzer; 16 attacks × 16 providers."},
            {"name": "FuzzyAI", "repo": "cyberark/FuzzyAI", "tags": "🟠", "org": "CyberArk",
             "desc": "Automated LLM fuzzer for jailbreaks/prompt injection."},
            {"name": "ai-prompt-fuzzer", "repo": "PortSwigger/ai-prompt-fuzzer", "tags": "🟢", "org": "PortSwigger",
             "desc": "Burp Suite extension fuzzing GenAI/LLM prompts."},
        ]),
    ],
    None,
))

SECTIONS.append((
    "Threat Intelligence",
    "threat-intelligence",
    "AI/LLM tooling for CTI gathering, IOC/TTP extraction, and analysis.",
    [
        {"name": "trs", "repo": "deadbits/trs", "tags": "🟢",
         "desc": "LLM + ChromaDB tool to summarize threat reports and extract MITRE TTPs and IOCs."},
        {"name": "TI-Mindmap-GPT", "repo": "format81/TI-Mindmap-GPT", "tags": "🟢",
         "desc": "Streamlit app: AI summaries, mindmaps, IOC/TTP extraction, and ATT&CK Navigator layers."},
        {"name": "aiocrioc", "repo": "referefref/aiocrioc", "tags": "🟢",
         "desc": "LLM + OCR IOC extraction (pulls IOCs from images/PDFs)."},
        {"name": "ThreatIngestor", "repo": "InQuest/ThreatIngestor", "tags": "🟢",
         "desc": "Extracts/aggregates IOCs from feeds; integrates with MISP/ThreatKB (pairs well with LLM post-processing)."},
        {"name": "IATelligence", "repo": "fr0gger/IATelligence", "tags": "🟢",
         "desc": "Explains imported Windows APIs in PE files via GPT and maps to MITRE ATT&CK.",
         "related": [("MCP_Security", GH + "fr0gger/MCP_Security")]},
        {"name": "MCP_Security", "repo": "fr0gger/MCP_Security", "tags": "🟢⚠️",
         "desc": "MCP server (ORKL) for querying the ORKL threat-intel API.",
         "related": [("IATelligence", GH + "fr0gger/IATelligence")]},
    ],
    None,
))

SECTIONS.append((
    "Log Analysis / SIEM / SOC Triage",
    "log-analysis--siem--soc-triage",
    "AI agents for SOC alert triage, investigation, and incident response.",
    [
        {"name": "AI-SOC-Agent", "repo": "M507/ai-soc-agent", "tags": "🟢",
         "desc": "Black Hat 2025 MCP server exposing security-investigation tools (ELK, IRIS)."},
        {"name": "agentic-soc-platform", "repo": "FunnyWolf/agentic-soc-platform", "tags": "🟢",
         "desc": "Agentic SOC platform (LangGraph/Dify) with local-LLM support."},
        {"name": "SOCGPT", "repo": "Ninadjos/SOCGPT-AI-Powered-SOC-Assistant", "tags": "🟢",
         "desc": "LLM log summarization, severity triage, MITRE mapping, and Q&A."},
        {"name": "AttackGen", "repo": "mrwadams/attackgen", "tags": "🟢",
         "desc": "LLM-driven incident-response scenario generator using MITRE ATT&CK + ATLAS."},
    ],
    None,
))

SECTIONS.append((
    "Reverse Engineering",
    "reverse-engineering",
    "LLM-assisted binary analysis and traffic inspection.",
    [
        {"name": "Gepetto", "repo": "JusticeRage/Gepetto", "tags": "🟢",
         "desc": "IDA Pro plugin: GPT adds comments and meaningful variable names."},
        {"name": "GhidraMCP", "repo": "LaurieWired/GhidraMCP", "tags": "🟢",
         "desc": "MCP server exposing Ghidra reverse-engineering ops to any MCP-capable LLM.",
         "related": [("GhidrOllama", GH + "lr-m/GhidrOllama"), ("OGhidra", GH + "llnl/OGhidra")]},
        {"name": "GhidrOllama", "repo": "lr-m/GhidrOllama", "tags": "🟢⚠️",
         "desc": "Ghidra script using the Ollama API for function analysis/renaming.",
         "related": [("OGhidra", GH + "llnl/OGhidra"), ("GhidraMCP", GH + "LaurieWired/GhidraMCP")]},
        {"name": "OGhidra", "repo": "llnl/OGhidra", "tags": "🟢", "org": "Lawrence Livermore National Lab",
         "desc": "Natural-language Ghidra analysis via Ollama.",
         "related": [("GhidrOllama", GH + "lr-m/GhidrOllama"), ("GhidraMCP", GH + "LaurieWired/GhidraMCP")]},
        {"name": "ghidra_tools (G-3PO)", "repo": "tenable/ghidra_tools", "tags": "🟢", "org": "Tenable",
         "desc": "Ghidra plugin for AI-assisted decompiled-code analysis."},
        {"name": "gpt-wpre", "repo": "moyix/gpt-wpre", "tags": "🔬",
         "desc": "Whole-program reverse engineering with GPT-3."},
        {"name": "burpgpt", "repo": "aress31/burpgpt", "tags": "🟢",
         "desc": "Burp Suite extension integrating GPT for passive scanning.",
         "related": [("Burp-extension-for-GPT", GH + "tenable/Burp-extension-for-GPT")]},
        {"name": "Burp-extension-for-GPT", "repo": "tenable/Burp-extension-for-GPT", "tags": "🟢", "org": "Tenable",
         "desc": "Burp extension to analyze HTTP traffic with GPT.",
         "related": [("burpgpt", GH + "aress31/burpgpt")]},
    ],
    None,
))

SECTIONS.append((
    "LLM Red-Teaming & Guardrails",
    "llm-red-teaming--guardrails",
    "Tools for attacking and defending LLM applications themselves.",
    [
        {"name": "garak", "repo": "NVIDIA/garak", "tags": "🟢", "org": "NVIDIA",
         "desc": "The LLM vulnerability scanner — probes for prompt injection, jailbreaks, data leakage, and more.",
         "related": [("PyRIT", GH + "microsoft/PyRIT"), ("promptfoo", GH + "promptfoo/promptfoo")]},
        {"name": "PyRIT", "repo": "microsoft/PyRIT", "tags": "🟢", "org": "Microsoft",
         "desc": "Python Risk Identification Tool; battle-tested across 100+ GenAI red-team operations."},
        {"name": "promptfoo", "repo": "promptfoo/promptfoo", "tags": "🟢",
         "desc": "LLM eval + red-teaming/pentesting CLI with 50+ attack plugins (MIT).",
         "note": "*Note: OpenAI announced an acquisition agreement in March 2026; remains MIT-licensed — track governance.*"},
        {"name": "DeepTeam", "repo": "confident-ai/deepteam", "tags": "🟢",
         "desc": "Open-source framework for red-teaming LLMs and LLM systems across jailbreaks, prompt injection, data leakage, and safety risks."},
        {"name": "Moonshot", "repo": "aiverify-foundation/moonshot", "tags": "🟢", "org": "AI Verify Foundation",
         "desc": "Modular tool for benchmarking, red-teaming, and evaluating LLM applications with custom connectors and recipes."},
        {"name": "LLM Guard", "repo": "protectai/llm-guard", "tags": "🟢", "org": "Protect AI",
         "desc": "Suite of input/output scanners (PII, prompt injection, etc.).",
         "related": [("Rebuff", GH + "protectai/rebuff")]},
        {"name": "Rebuff", "repo": "protectai/rebuff", "tags": "🟢", "org": "Protect AI",
         "desc": "Archived prompt-injection detector (heuristics + LLM + vector DB + canary tokens).",
         "related": [("LLM Guard", GH + "protectai/llm-guard")]},
        {"name": "NeMo Guardrails", "repo": "NVIDIA-NeMo/Guardrails", "tags": "🟢", "org": "NVIDIA",
         "desc": "Programmable guardrails (input/output/dialog/retrieval rails) for LLM apps."},
        {"name": "PurpleLlama", "repo": "meta-llama/PurpleLlama", "tags": "🟢", "org": "Meta",
         "desc": "Llama Guard classifiers, CodeShield, and CyberSecEval."},
        {"name": "Vigil", "repo": "deadbits/vigil-llm", "tags": "🟢🔬",
         "desc": "Library/REST API to scan prompts and responses for prompt injection."},
        {"name": "Counterfit", "repo": "Azure/counterfit", "tags": "🟢", "org": "Microsoft",
         "desc": "ML/AI penetration-testing automation tool."},
        {"name": "AI-Red-Teaming-Playground-Labs", "repo": "microsoft/AI-Red-Teaming-Playground-Labs", "tags": "🟢", "org": "Microsoft",
         "desc": "CTFd-based AI red-team training challenges."},
        {"name": "EasyJailbreak", "repo": "EasyJailbreak/EasyJailbreak", "tags": "🟢🔬",
         "desc": "Framework for building and testing adversarial jailbreak prompts."},
        {"name": "llm-security", "repo": "greshake/llm-security", "tags": "🔬",
         "desc": "Original PoC for indirect prompt-injection attacks."},
        {"name": "JailbreakLLMs", "repo": "TrustAIRLab/JailbreakLLMs", "tags": "🔬⚠️",
         "desc": "Research dataset of 6,387 ChatGPT prompts, including in-the-wild jailbreak prompts from Reddit, Discord, websites, and open datasets."},
        {"name": "prompt-injection-defenses", "repo": "tldrsec/prompt-injection-defenses", "tags": "🟢⚠️",
         "desc": "Curated catalog of practical defenses against prompt injection."},
    ],
    None,
))

SECTIONS.append((
    "LLM Honeypots & Deception",
    "llm-honeypots--deception",
    "Honeypots and deception that use LLMs to simulate convincing systems.",
    [
        {"name": "Beelzebub", "repo": "mariocandela/beelzebub", "tags": "🟢",
         "desc": "Low-code honeypot using LLMs to simulate SSH/HTTP/MCP services (Go)."},
        {"name": "shelLM", "repo": "stratosphereips/shelLM", "tags": "🟢🔬",
         "desc": "LLM-powered SSH honeypot (paper *\"LLM in the Shell\"*).",
         "related": [("VelLMes", GH + "stratosphereips/VelLMes-AI-Honeypot")]},
        {"name": "VelLMes", "repo": "stratosphereips/VelLMes-AI-Honeypot", "tags": "🟢🔬",
         "desc": "Multi-protocol LLM honeypot framework (successor to shelLM).",
         "related": [("shelLM", GH + "stratosphereips/shelLM")]},
        {"name": "llm-honeypot", "repo": "PalisadeResearch/llm-honeypot", "tags": "🔬⚠️", "org": "Palisade Research",
         "desc": "Cowrie SSH honeypot extended with prompt-injection traps to detect LLM hacker agents."},
    ],
    None,
))

SECTIONS.append((
    "CTF / Exploit / Bug-Bounty Agents & Benchmarks",
    "ctf--exploit--bug-bounty-agents--benchmarks",
    "Offensive agents and the benchmarks used to evaluate them.",
    [
        {"name": "SWE-agent (EnIGMA)", "repo": "SWE-agent/SWE-agent", "tags": "🟢🔬",
         "desc": "EnIGMA offensive-CTF mode; SOTA on NYU CTF, InterCode-CTF, and Cybench (v0.7 branch).",
         "related": [("Cybench", GH + "andyzorigin/cybench"), ("NYU CTF Bench", GH + "NYU-LLM-CTF/NYU_CTF_Bench"),
                     ("InterCode", GH + "princeton-nlp/intercode")]},
        {"name": "Cybench", "repo": "andyzorigin/cybench", "tags": "🔬",
         "desc": "40 professional CTF tasks across 4 competitions; widely used by AI safety institutes."},
        {"name": "NYU CTF Bench", "repo": "NYU-LLM-CTF/NYU_CTF_Bench", "tags": "🔬",
         "desc": "Dockerized CSAW CTF challenges for LLM-agent evaluation."},
        {"name": "InterCode", "repo": "princeton-nlp/intercode", "tags": "🔬",
         "desc": "Interactive-coding benchmark incl. InterCode-CTF."},
        {"name": "BountyBench", "repo": "bountybench/bountybench", "tags": "🔬",
         "desc": "25 real systems / 40 bug bounties for Detect-Exploit-Patch evaluation."},
        {"name": "Cyber-Zero", "repo": "amazon-science/Cyber-Zero", "tags": "🔬", "org": "Amazon Science",
         "desc": "Trains cybersecurity agents without runtime; ships an EnIGMA+ scaffold.",
         "sources": [SWE_AGENT], "related": [SWE_AGENT]},
        {"name": "ExploitBench", "repo": "exploitbench/exploitbench", "tags": "🔬",
         "desc": "Measures AI-agent progress on V8/Chromium exploit ladders."},
        {"name": "claude-bug-bounty", "repo": "shuvonsec/claude-bug-bounty", "tags": "🟢",
         "desc": "Claude Code plugin orchestrating recon → vuln classes → reporting."},
        {"name": "Bug-Bounty-Agents", "repo": "matty69v/Bug-Bounty-Agents", "tags": "🟢",
         "desc": "43 AI agent personas for Claude Code / Copilot / Cursor across the bug-bounty lifecycle."},
        {"name": "ai-exploits", "repo": "protectai/ai-exploits", "tags": "🟢", "org": "Protect AI",
         "desc": "Real-world AI/ML exploits (Metasploit modules + Nuclei templates) for MLflow, Ray, H2O."},
    ],
    None,
))

SECTIONS.append((
    "Cloud / IaC / DFIR / OSINT / Phishing",
    "cloud--iac--dfir--osint--phishing",
    "AI tooling for cloud/IaC security, digital forensics, OSINT, and phishing detection.",
    [
        {"name": "EscalateGPT", "repo": "tenable/EscalateGPT", "tags": "🟢", "org": "Tenable",
         "desc": "GPT-based discovery of privilege-escalation paths in AWS IAM policies."},
        {"name": "MemoryInvestigator", "repo": "jan-hendrik-lang/MemoryInvestigator", "tags": "🔬",
         "desc": "Volatility 3 + LLM + RAG for memory-forensic triage.",
         "related": [("Volatility-MCP-Server", GH + "bornpresident/Volatility-MCP-Server")]},
        {"name": "Volatility-MCP-Server", "repo": "bornpresident/Volatility-MCP-Server", "tags": "🟢",
         "desc": "MCP exposing Volatility 3 plugins for natural-language memory forensics.",
         "related": [("MemoryInvestigator", GH + "jan-hendrik-lang/MemoryInvestigator")]},
        {"name": "PhishLLM", "repo": "code-philia/PhishLLM", "tags": "🔬⚠️",
         "desc": "Reference-less phishing detection via LLM brand recognition (USENIX'24).",
         "related": [("PhishVLM", GH + "code-philia/PhishVLM")]},
        {"name": "osintgpt", "repo": "estebanpdl/osintgpt", "tags": "🟢⚠️",
         "desc": "OpenAI embeddings + Qdrant over OSINT corpora."},
        {"name": "gpt-osint", "repo": "gigz/gpt-osint", "tags": "🟢",
         "desc": "Web-based GPT-4 OSINT tool over social-media dumps and CSVs."},
    ],
    None,
))

# Related awesome lists (repos -> badges too)
AWESOME = [
    ("awesome-llm-cybersecurity-tools", "tenable/awesome-llm-cybersecurity-tools", "Tenable's list (archived but a strong reference)."),
    ("Awesome-LLM4Cybersecurity", "tmylla/Awesome-LLM4Cybersecurity", "600+ papers on LLMs for cybersecurity."),
    ("awesome-ai-cybersecurity", "ElNiak/awesome-ai-cybersecurity", "Broad AI-for-security collection."),
    ("awesome-genai-cyberhub", "Ashfaaq98/awesome-genai-cyberhub", "GenAI-driven cybersecurity resources."),
    ("awesome-ai-security", "gmh5225/awesome-ai-security", "For pentesters, bug hunters, and researchers."),
    ("awesome-ai-security", "ottosulin/awesome-ai-security", "AI security resources."),
    ("Awesome-AI-Security", "TalEliyahu/Awesome-AI-Security", "AI security resources."),
    ("awesome-llm-security", "corca-ai/awesome-llm-security", "Securing LLMs."),
    ("awesome-security-for-ai", "zmre/awesome-security-for-ai", "Products for securing AI systems."),
    ("awesome-gpt-security", "cckuailong/awesome-gpt-security", "GPT/LLM security tools and cases."),
    ("awesome-threat-intelligence", "hslatman/awesome-threat-intelligence", "Classic CTI list (pairs with the AI-CTI section)."),
]


def build():
    out = []
    out.append("# Awesome AI Security Tools [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)")
    out.append("")
    out.append("> A curated list of **public-source, research, and commercial** tools for AI security and AI-assisted cybersecurity — autotriage, agent security, AI/ML supply chain, pentest agents, AI SAST, LLM-driven fuzzing, threat intelligence, SOC/SIEM triage, reverse engineering, LLM red-teaming, and more.")
    out.append("")
    out.append("[![License: CC0-1.0](https://img.shields.io/badge/license-CC0--1.0-lightgrey.svg)](https://creativecommons.org/publicdomain/zero/1.0/)")
    out.append("[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](#contributing)")
    out.append("")
    out.append("**Type legend:** 🟢 public source / open-source · 🔬 research (paper / benchmark / dataset / framework) · 🟠 commercial with open components · ⚠️ restrictive, non-commercial, or unclear/no license — check before use.")
    out.append("")
    out.append("Each entry shows live **★ stars** and **last-commit** badges (rendered from the GitHub API by shields.io). Ordering within a section favors flagship and actively maintained projects.")
    out.append("")
    out.append("---")
    out.append("")
    # Contents
    out.append("## Contents")
    out.append("")
    for title, anchor, _intro, body, _foot in SECTIONS:
        out.append(f"- [{title}](#{anchor})")
        if body and isinstance(body[0], tuple):
            for sub_title, _ in body:
                out.append(f"  - [{sub_title}](#{github_anchor(sub_title)})")
    out.append("- [Related Awesome Lists](#related-awesome-lists)")
    out.append("- [Contributing](#contributing)")
    out.append("- [License](#license)")
    out.append("")
    out.append("---")
    out.append("")
    # Sections
    for title, anchor, intro, body, foot in SECTIONS:
        out.append(f"## {title}")
        out.append("")
        if intro:
            out.append(intro)
            out.append("")
        if body and isinstance(body[0], tuple):
            for sub_title, entries in body:
                out.append(f"### {sub_title}")
                out.append("")
                for e in entries:
                    out.append(render_entry(e))
                out.append("")
        else:
            for e in body:
                out.append(render_entry(e))
            out.append("")
        if foot:
            out.append(foot)
            out.append("")
        out.append("---")
        out.append("")
    # Awesome lists
    out.append("## Related Awesome Lists")
    out.append("")
    for name, repo, desc in AWESOME:
        out.append(f"- **[{name}]({GH}{repo})** — {desc} {badges(repo)}")
    out.append("")
    out.append("---")
    out.append("")
    # Contributing
    out.append("## Contributing")
    out.append("")
    out.append("Contributions are welcome! Open a PR adding entries in the format below, keeping each section sorted by relevance/maintenance.")
    out.append("")
    out.append("```")
    out.append("- **[name](repo-url)** 🟢/🔬/🟠/⚠️ — One-line description. *(maintainer/org)* <stars badge> <last-commit badge>")
    out.append("  - **Sources:** [upstream A](url) · [upstream B](url)       # optional — projects this is built on")
    out.append("  - **Related:** [sibling tool](url) · [related project](url) # optional — peers / forks / successors")
    out.append("```")
    out.append("")
    out.append("Badges use the dynamic shields.io GitHub endpoints, so they update automatically:")
    out.append("")
    out.append("```")
    out.append("[![stars](https://img.shields.io/github/stars/OWNER/REPO?style=flat-square&label=★)](https://github.com/OWNER/REPO)")
    out.append("[![updated](https://img.shields.io/github/last-commit/OWNER/REPO?style=flat-square&label=updated)](https://github.com/OWNER/REPO)")
    out.append("```")
    out.append("")
    out.append("Guidelines: link the canonical upstream repo (not a fork); verify the URL resolves; tag the correct type and add ⚠️ for non-permissive, non-commercial, or unclear/no-license projects; prefer real, installable projects over blog-only references.")
    out.append("")
    out.append("## License")
    out.append("")
    out.append("To the extent possible under law, the contributors have waived all copyright and related rights to this list ([CC0-1.0](https://creativecommons.org/publicdomain/zero/1.0/)). Linked projects retain their own licenses — check each before use.")
    out.append("")
    return "\n".join(out).rstrip() + "\n"


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("-o", "--output", type=Path,
                        default=Path(__file__).with_name("README.md"),
                        help="README path to write or check")
    parser.add_argument("--check", action="store_true",
                        help="fail if the output README is not up to date")
    args = parser.parse_args()

    rendered = build()
    if args.check:
        current = args.output.read_text(encoding="utf-8")
        if current != rendered:
            print(f"{args.output} is out of date; run gen_readme.py", flush=True)
            return 1
        print(f"{args.output} is up to date.")
        return 0

    args.output.write_text(rendered, encoding="utf-8")
    print(f"{args.output} generated.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
