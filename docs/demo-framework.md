# Sawn: demo video framework (v2, rebuilt against the mentor's five notes)

Everything below is written against `app/sawn-platform.html` and
`app/rag-simulator.html`; every click exists in those files.

## The mentor's five notes, and where each is answered

| # | Note | Where it is answered |
|---|---|---|
| 1 | Clearly show the setup, with clear voice-over | Scene 0 opens the video with both windows on screen and a voice-over naming each |
| 2 | English subtitles | `docs/demo-subtitles.srt` carries the full voice-over, timed to the scenes; burn it in |
| 3 | Scenarios explained in sequence | Scenes 1–8 are numbered on screen with a spoken "Scenario N" line before each |
| 4 | Expected output explained before actual output | Every scene is written as **Expect → Do → Confirm**: say what will happen, do it, point at it |
| 5 | Finish with impact and mapping to policy documents | Scene 9 closes on an impact card and the policy mapping card, read aloud |

The habit that satisfies note 4 everywhere: **never click while silent, and never
click before saying what the click will produce.**

---

## Recording setup (what the viewer sees first)

Two browser windows, opened before recording, arranged left to right:

1. `sawn-platform.html` — the platform, signed out, on the login screen
2. `rag-simulator.html` — the simulator, untouched

1920×1080, browser zoom 100%, bookmarks bar hidden, notifications off. Record
the whole screen, not one window, so the cuts between windows are visible and
honest. Open window 1 fresh just before recording: the gap register, counters
and audit trail accumulate as you click, and scene 9 depends on that.

---

## Scene 0 · Setup · 0:00–0:25

**Say (over the two tiled windows):**
"This is everything Sawn is: two files, no server, no installation, no API
key. On the left, the platform, one HTML file with all three roles inside it.
On the right, the retrieval simulator that carries our evaluation set.
Everything you are about to see runs from these files exactly as they are in
the repository."

**Do:** slow mouse circle over each window as it is named. Then maximise
window 1.

---

## Scene 1 · The problem · 0:25–1:10

**Expect (say first):** "Scenario one, the problem. I will sign in as the Al
Baha education department and sort the queue the way the Kingdom sorts it
today, by the date on the form. Watch the last row: you should see a chained
emergency exit at the very bottom, because it was filed five hours ago."

**Do:** sign in as Education department → Triage queue → click **By date filed**.

**Confirm (point):** "There it is. Emergency exit chained shut, position
fourteen of fourteen, thirteen older requests ahead of it. That is first come
first served, and it is the whole problem."

---

## Scene 2 · The rule · 1:10–1:45

**Expect:** "Scenario two, the rule that replaces the date. I will open
governance. You should see eight published weights that sum to one hundred,
and an escalation rule underneath saying a structural or electrical score of
eight or more is Critical whatever the number."

**Do:** Governance and fairness → scroll to "Who may change the weights?".

**Confirm:** "Eight weights, fifty-two per cent on physical safety, and the
escalation rule, exactly as published in the report. The weights are public
on purpose; the anomaly model handles the gaming risk, and we will come back
to that."

---

## Scene 3 · Triage · 1:45–2:35

**Expect:** "Scenario three, the same queue under the rule. I will click 'By
risk'. The chained exit should jump from fourteen to the top three with an
arrow showing how far it moved, turn Critical, and start a twenty-four hour
clock."

**Do:** Triage queue → click **By risk**.

**Confirm:** "Position three, up eleven places, Critical, mandatory
escalation, twenty-three hours and change on the clock." Open the row.
"And here is what makes it defensible: the eight indicator bars, the score,
and one generated explanation sentence. No rank leaves the system without
one."

---

## Scene 4 · The knowledge base · 2:35–3:25

**Expect:** "Scenario four, where the authority comes from. In this same
record you should see the governing instrument retrieved for this fault: the
fire code, SBC 801, with its issuing authority and a link. Then I will ask
the knowledge base a question, and the answer should carry its source."

**Do:** point at the instruments block in the record → Instruments and gaps →
press **Exit inspection**.

**Confirm:** read the answer aloud, then: "SBC 801, Saudi Building Code
National Committee, with the link. The system did not write a rule; it
retrieved one."

---

## Scene 5 · The gap · 3:25–4:05

**Expect:** "Scenario five, the part most systems hide. I will ask a question
that no published instrument answers: who is liable when an official
overrides the ranking. The correct behaviour is a refusal, and the question
should drop into the gap register on the right."

**Do:** press **Override liability**.

**Confirm:** "No published instrument answers this, and the question is now
in the register." Point at the register: "Seven regression questions, one per
policy gap in our report, are already here because the platform asks them
every time it loads, plus a deadline gap for every open request. These gaps
are an output of running the system, not an opinion in a document."

---

## Scene 6 · Who holds it · 4:05–4:45

**Expect:** "Scenario six, accountability. I will sign in as the school
principal and open a handled request. You should see a complete chain of
custody: the company, the engineer, handover notes, and two electronic
signatures with fingerprints."

**Do:** sign out → sign in as School principal → My school requests → open
the handled fire alarm request → scroll the custody block slowly.

**Confirm:** read it: "The company and its commercial registration, the
authorised signatory, the supervising engineer with his council number, the
dates in and out, the handover notes saying what was left undone, and two
signature fingerprints computed over the declaration itself. A later edit
breaks them. This request could not have closed without them."

---

## Scene 7 · The retrieval, measured · 4:45–5:30

**Expect:** "Scenario seven, proof, in the second window. I will run a
question through the pipeline stage by stage; you should see the metrics
strip report ninety-five per cent first-hit accuracy, seven of seven gaps
refused, and one honest failure. Then I will lower the coverage floor and
the miscitation count should rise, which is why the threshold sits at 0.40."

**Do:** switch to window 2 → press **who must inspect a blocked fire exit**
→ let the four stages run → drag the coverage floor from 0.40 to 0.20.

**Confirm:** "Both floors passed and SBC 801 came back. And there: at 0.20,
miscitations climb from one to two. The threshold is an argument you can
drag, not a claim."

---

## Scene 8 · The sandbox · 5:30–6:10

**Expect:** "Scenario eight, changing the policy safely. Back in the
platform, in governance, I will raise the People-affected weight from ten to
twenty-two in the Y.3181 sandbox and run a counterfactual. You should see
which requests would move, the small-versus-large school gap widen from zero
to two, and a note that nothing has been applied."

**Do:** window 1 → Governance and fairness → sandbox panel → drag People
affected to 22 → **Run counterfactual**.

**Confirm:** "Three requests would move, the fairness gap opens from zero to
two, and the last line: nothing has been applied. A weight change reaches
production only as a versioned committee decision with this table attached.
That is the ITU sandbox recommendation, working."

---

## Scene 9 · Close: impact and the policy documents · 6:10–6:50

**Do:** Audit trail tab; the sandbox run is the top entry, hash-chained.
Then hold on the screen and say the close over it.

**Say — impact:**
"What this changes: twenty-four thousand and seventy-five public schools
ranked on one comparable scale instead of thirteen regional habits; a
chained fire exit waits hours, not weeks; every rank carries its regulation
and one explanation sentence a school can read; and no repair closes without
a named company, a named engineer and a signature. The AI decides the order;
a named official signs the action."

**Say — mapping to the policy documents:**
"And what it stands on: the pipeline is ITU-T Y.3172 with Y.3173 and Y.3174;
the sandbox you just watched is Y.3181; the corpus is twenty-three published
Saudi and international instruments, from the Saudi Building Code and Civil
Defence requirements to the Personal Data Protection Law, the NCA controls,
the Electronic Transactions Law and four ISO standards; and the seven gaps
the system found are drafted as inputs to national policy and to ITU Study
Group 13. Sawn. Which school cannot wait."

---

## Subtitles

The full voice-over above is provided, timed, as
`docs/demo-subtitles.srt`. Load it into the editor, nudge each
block to match your actual takes, then **burn the subtitles in** rather than
shipping a separate file. Keep each line under 42 characters where you edit.

## Recording notes

- One scene per take is fine; cut on the window switches.
- Speak slowly; the reviewers are non-native English speakers.
- Never narrate the interface ("here you can see a dashboard"); narrate the
  decision ("this school moved above thirteen older requests, and here is
  the rule that says it should").
- Total target 6:45, hard limit 7:00. If a scene runs long, shorten scene 2,
  never scenes 5, 7 or 9.
- Do not reload window 1 mid-recording; the register and audit trail are the
  evidence scene 9 stands on.

## Pre-submission checklist

- [ ] Video opens on the three-window setup with the setup voice-over (note 1)
- [ ] English subtitles burned in from the .srt (note 2)
- [ ] Every scenario announced by number, in order 1→8 (note 3)
- [ ] Every scene follows Expect → Do → Confirm (note 4)
- [ ] Closes on impact + policy document mapping, spoken, ≤ 7:00 (note 5)
- [ ] Report header fields completed; team name matches registration (Crescent)
- [ ] Repo public, Pages links replaced with the real account, no keys
- [ ] Submitted before 31 August, 23:59 KSA
