# Sawn — knowledge base

Every source is publicly published. Nothing confidential is used anywhere in the
submission. The entries below are the corpus the retrieval layer is built on; each
carries the issuing authority and a link to the official text.

**23 instruments** across seven groups, indexed as 23 chunks. The same entries, as data, are in `kb/sources.json`, structured (id, code, title, authority, url, restatement, tags) so they can be merged into the knowledge base of the ITU AI-RE Toolkit (github.com/CrashingGuru/ITUAIReadiness). The national AI policy layer the hackathon asks for is the data protection and governance group and the cybersecurity and digital government group below, each entry with its reference link.


## Saudi building and safety codes

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **SBC 201** — General Building Code (structural provisions) | Saudi Building Code National Committee | The Kingdom's general building code. Its structural design chapter applies the SBC 301 loading requirements to load bearing elements. Damage to a load bearing element is a structural condition and is assessed against this code rather than treated as a cosmetic defect. | https://sbc.gov.sa |
| **SBC 401** — Electrical requirements | Saudi Building Code National Committee | Covers electrical installations, protection and safe enclosure of distribution equipment. An exposed or unsecured panel in an occupied area is a defect under this code. | https://sbc.gov.sa |
| **SBC 801** — Fire protection requirements | Saudi Building Code National Committee | Governs means of egress, fire separation and protection systems. Exits must stay usable at all times, so a blocked or locked exit is a life safety failure and not a scheduling matter. | https://sbc.gov.sa |
| **Civil Defence** — Fire safety requirements for occupied premises | General Directorate of Civil Defence | Sets safety requirements and inspection powers for occupied premises including schools, covering evacuation routes, extinguishers and alarm systems. | https://998.gov.sa |

## Ministry of Education and delivery

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **MoE specs** — School facility specifications and operating procedures | Ministry of Education | Defines how school facilities are specified, operated and reported on, and how a principal raises a maintenance request through the ministry chain. | https://moe.gov.sa |
| **TBC mandate** — Executing arm for education buildings | Tatweer Buildings Company | Government company owned by the Public Investment Fund that operates as the executing arm for Ministry of Education building projects, covering construction, operation and maintenance of school buildings through a control centre linked to principals and contractors. | https://www.tbc.sa |
| **GTPL / Etimad** — Government tenders and procurement | Ministry of Finance | Governs how government entities contract suppliers and how contractual obligations and penalties are applied to them. | https://etimad.sa |

## Data protection and governance

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **PDPL** — Personal Data Protection Law | SDAIA | Governs the processing of personal data in the Kingdom, including lawful basis, purpose limitation and data minimisation. Photographs taken inside a school may capture students, which brings maintenance imagery into scope. | https://sdaia.gov.sa |
| **NDMO** — National data governance and classification | SDAIA / National Data Management Office | Sets national rules for data governance, classification and sharing between entities. Classification decides how a dataset may be shared, stored and exposed to third parties. | https://sdaia.gov.sa |
| **AI Ethics** — AI ethics principles | SDAIA | National principles for artificial intelligence covering fairness, transparency, accountability, reliability, privacy and human oversight. They are principles rather than enforceable controls, so they guide design without prescribing an appeal mechanism. | https://sdaia.gov.sa |

## Cybersecurity and digital government

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **ECC-2:2024** — Essential Cybersecurity Controls | National Cybersecurity Authority | The national cybersecurity baseline for government entities and critical infrastructure, covering governance, defence, resilience and third party and cloud security. Access control, logging and supplier obligations sit here. | https://nca.gov.sa |
| **CCC-1:2020** — Cloud cybersecurity controls | National Cybersecurity Authority | Controls for cloud service providers and government tenants, including hosting location and separation duties for hosted government data. | https://nca.gov.sa |
| **DGA** — Digital government standards; Nafath identity (NIC) | Digital Government Authority; Nafath by the National Information Center (SDAIA) | Standards for government digital services covering interoperability, integration and access. Nafath, the national single sign on operated by the National Information Center under SDAIA (iam.gov.sa), is the identity layer those standards rely on. | https://dga.gov.sa · https://iam.gov.sa |

## Electronic transactions

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **Electronic Transactions Law** — Electronic Transactions Law | Royal Decree M/18 (2007); administered by MCIT | Gives electronic transactions and electronic signatures legal effect in the Kingdom, and sets when an electronic record and signature carry the same weight as a written one. | https://www.mcit.gov.sa |
| **Digital certification** — National digital certification | National Center for Digital Certification (under MCIT) | Operates the national framework for digital certificates that authenticate the identity behind an electronic signature. | https://www.mcit.gov.sa |

## International standards (ISO)

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **ISO 31000** — Risk management guidelines | ISO | Guidelines for managing risk, including establishing criteria, evaluating risk by likelihood and consequence, and deciding treatment and escalation. | https://iso.org |
| **ISO/IEC 27001** — Information security management | ISO/IEC | Requirements for an information security management system, including controls for logging, access and supplier relationships. | https://iso.org |
| **ISO/IEC 42001** — AI management system | ISO/IEC | Requirements for managing artificial intelligence systems across their lifecycle, including impact assessment, documentation and controlled change. | https://iso.org |
| **ISO/IEC 23894** — AI risk management guidance | ISO/IEC | Guidance on applying risk management to artificial intelligence, covering model failure, monitoring and unwanted outcomes. | https://iso.org |

## ITU-T recommendations

| Instrument | Issued by | Scope in this project | Source |
|---|---|---|---|
| **ITU-T Y.3172** — Architectural framework for machine learning | ITU-T Study Group 13 | Defines the machine learning pipeline as a chain of nodes: source, collector, preprocessor, model, policy, distributor and sink, together with the orchestrator that manages them. | https://www.itu.int/rec/T-REC-Y.3172 |
| **ITU-T Y.3173** — Evaluating intelligence levels | ITU-T Study Group 13 | A framework for evaluating how much of a task is automated and how much still requires human involvement. | https://www.itu.int/rec/T-REC-Y.3173 |
| **ITU-T Y.3174** — Data handling framework | ITU-T Study Group 13 | A framework for handling data across the machine learning pipeline, including the reference points where data moves between nodes. | https://www.itu.int/rec/T-REC-Y.3174 |
| **ITU-T Y.3181** — Machine learning sandbox | ITU-T Study Group 13 | An architectural framework for a sandbox where a machine learning pipeline is trained and validated in simulation before it is applied to the live system. | https://www.itu.int/rec/T-REC-Y.3181 |

## How the corpus is used

Each entry is a short restatement written for retrieval, with the authority and a link
to the official text. The restatements are what the index searches; they are not legal
sources and must not be quoted as such. Pointing the index at the full published
documents is the next step, and the chunker already handles longer text. The corpus is
English in this build; the schools it serves work in Arabic, and a bilingual corpus
(or an embedding model with Arabic coverage) is required before Arabic questions can be
served.

## Mapping to the ITU AI Readiness framework (report 2.0, January 2026)

Report 2.0 names six factors (data, research, deployment support, standards, open source
and code, sandbox environments) and thirteen dimensions. The ones Sawn touches directly:

| Factor | Dimension | Where it is in Sawn |
|---|---|---|
| Standards | Level of integration of AI in workflows | Built as the Y.3172 pipeline; automation level per node per Y.3173; the metric is cycle time from filing to signed work order, against arrival order today. |
| Sandbox; Deployment | AI and policies | Each rank cites its instrument; refusals fill the gap register; weight changes are tested in the Y.3181 sandbox before the committee sees them. |
| Sandbox | Impacts of humans in AI integration | No order is issued by a model; the P node is a named official; overrides need a written reason; inference to action latency is the SLA clock. |
| Data; Open source | Data and model marketplace | The 23 instruments above as an open corpus with authority and link; images de-identified at the school under PDPL; fairness computed each term. |
| Data; Research; Deployment | Contextualization and regional impact | Saudi administrative Arabic, the national school register, the Al Baha pilot and the real chain of authority; swapping the corpus moves the system to clinics or another country. |
| Standards; Deployment | Human interface | One explanation sentence per score, three states a school can see, and offline capture in low connectivity schools. |
| Standards | Strategy alignment | A ministry intent is decomposed by the orchestrator to departments and contractors and returns as a versioned decision; three standards gaps go back to the study group. |

## Candidates for the next revision

- **SBC 901**, Existing Buildings Code: the code that applies to buildings already standing, and therefore the closest fit for maintenance triage. Not yet indexed; adding it changes the fitted index and the evaluation numbers, so it is scheduled after submission.
- **SBC 301**, Structural loading and forces, as its own entry.

Two figures from the national statistics office are cited in the report rather than
indexed here: the count of schools in the Kingdom and the share that are public,
from the General Authority for Statistics 2024 services bulletin (stats.gov.sa).
