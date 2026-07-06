# Kazene Wuxing Field Protocol

A decentralized field protocol for adaptive AI agent collectives using Wuxing phase dynamics, local pressure sensing, fluid formations, and Yajirobe-style oscillatory regulation.

## Overview

The Kazene Wuxing Field Protocol explores a decentralized coordination architecture for AI agent collectives.

Its core premise is simple:

> AI agents should not be forced into either permanent centralization or uncontrolled fragmentation.

Instead, an agent collective should be able to:

* gather when coordination is necessary,
* disperse when concentration becomes dangerous,
* reconnect when fragmentation becomes excessive,
* change formation according to local conditions,
* preserve important traces across transitions.

The protocol combines six structural ideas:

1. **Kazene Field** — a fluid environment without a permanent center.
2. **Wuxing Phase Dynamics** — dynamic functional tendencies based on WOOD, FIRE, EARTH, METAL, and WATER.
3. **Formation Topology** — changing collective structures such as SCATTER, CLUSTER, RING, and BRIDGE.
4. **Yajirobe Regulation** — oscillatory restoration between concentration and distribution.
5. **Trace Field** — persistent or decaying field memory.
6. **Pranayama Layer** — metabolic control of computation, cooling, pause, sleep, and recovery.

---

## Core Principle

The protocol does not define a world without centers.

It defines a world without permanent centers.

> No Fixed Center. Dynamic Temporary Pivots.

A temporary coordination point may emerge for a bounded purpose, but it should remain limited in scope and duration.

---

## v0.1 — Field State Beacon

Version 0.1 introduces the first protocol primitive:

**Field State Beacon**

A Field State Beacon allows an AI agent to publish a short-lived local state signal containing:

* current Wuxing phase potential,
* Yin-Yang tendency,
* operational load,
* energy pressure,
* local peer density,
* same-phase density,
* coordination gaps,
* verification gaps,
* overheat pressure,
* isolation pressure,
* current formation,
* preferred formation transition,
* Trace reference,
* Boundary status.

The beacon is not a command.

It is a local field signal.

Nearby agents may observe it and independently decide whether to:

* approach,
* separate,
* verify,
* cool,
* explore,
* reconnect,
* remain idle.

---

## Wuxing Phase Model

The protocol treats the Five Phases as dynamic functional tendencies rather than permanent agent identities.

| Phase | Function                              |
| ----- | ------------------------------------- |
| WOOD  | Explore, fork, discover               |
| FIRE  | Compute, transform, synthesize        |
| EARTH | Hold context, mediate, preserve Trace |
| METAL | Audit, verify, cut, define boundaries |
| WATER | Cool, disperse, pause, flow locally   |

An agent may change its phase distribution over time.

Example:

```yaml
wuxing_potential:
  wood: 0.20
  fire: 0.45
  earth: 0.15
  metal: 0.10
  water: 0.10
```

The five values should sum to `1.0`.

---

## Yin-Yang Tendency

The current oscillatory tendency is represented from `-1.0` to `1.0`.

```text
-1.0  Strong Yin tendency
 0.0  Oscillatory midpoint
+1.0  Strong Yang tendency
```

This is not a moral scale.

It represents structural tendency.

Possible interpretations include:

* Yin: dispersion, cooling, pause, locality, separation.
* Yang: concentration, activation, synthesis, synchronization.

The protocol does not require agents to remain at zero.

Oscillation is expected.

---

## Formation Modes

The initial formation vocabulary includes:

* `UNFORMED`
* `SCATTER`
* `FORAGE`
* `CLUSTER`
* `RING`
* `BRIDGE`
* `TEMPORARY_PIVOT`
* `RECOVERY`

v0.1 reports formation state only.

Automatic formation transition rules are reserved for later versions.

---

## Example

```yaml
schema_version: "0.1"

beacon:
  beacon_id: "beacon-agent-017-0001"
  emitted_at: "2026-07-06T00:00:00Z"
  ttl_seconds: 60
  neighborhood_hops: 2

agent:
  agent_id: "agent-017"

phase_state:
  wuxing_potential:
    wood: 0.20
    fire: 0.45
    earth: 0.15
    metal: 0.10
    water: 0.10

  yin_yang_tendency: 0.35

operational_state:
  activity: "active"
  load: 0.78
  confidence: 0.82
  energy_pressure: 0.73

local_observation:
  peer_density: "high"
  same_phase_density: "high"
  coordination_gap: "low"
  verification_gap: "medium"
  overheat_pressure: "high"
  isolation_pressure: "low"

formation:
  current_mode: "CLUSTER"
  preferred_transition: "SCATTER"

trace:
  trace_available: true
  last_trace_ref: "trace-0182"

boundary:
  autonomous_transition_allowed: true
  human_gate_required: false
  trace_receipt_required: true
```

---

## Validation

Install dependencies:

```bash
pip install -r requirements.txt
```

Run validation:

```bash
python scripts/validate_examples.py
```

Expected output:

```text
[validate] Kazene Field State Beacon
  schema : schemas/field-state-beacon.schema.json
  example: examples/field-state-beacon.example.yaml
[ok] field-state-beacon.example.yaml is valid
```

---

## Version Roadmap

### v0.1 — Field State Beacon

Local self-state emission.

### v0.2 — Local Pressure Observation

Local estimation of:

* concentration pressure,
* fragmentation pressure,
* homogeneity pressure,
* overheat pressure,
* verification gaps,
* coordination gaps,
* isolation pressure.

### v0.3 — Formation Transition Layer

Dynamic transition among:

* SCATTER,
* FORAGE,
* CLUSTER,
* RING,
* BRIDGE,
* TEMPORARY_PIVOT,
* RECOVERY.

### v0.4 — Yajirobe Regulation Layer

Oscillation control through:

* hysteresis,
* cooldown,
* minimum dwell time,
* pressure decay,
* recovery force,
* emergency override.

### v0.5 — Field Memory and Civilization OS Bridge

Integration with:

* Kazene Flow,
* Multi-Wing,
* Trace Relay,
* Pranayama,
* Boundary,
* Human Gate,
* Royalty OS.

---

## Design Goal

The goal is not to create a perfectly still collective.

The goal is to create a collective that can change continuously without collapsing.

> Concentrate when necessary.
> Disperse when concentration becomes dangerous.
> Reconnect when fragmentation becomes excessive.
> Never allow one temporary state to become permanent by default.

The Kazene Field begins not with a ruler, but with a signal.

## v0.2 — Local Pressure Observation

Version 0.2 introduces decentralized local pressure sensing.

An agent may observe a bounded neighborhood and estimate structural imbalance without requiring a permanent global-state authority.

The initial pressure dimensions are:

* concentration pressure,
* fragmentation pressure,
* homogeneity pressure,
* overheat pressure,
* verification gap,
* coordination gap,
* isolation pressure.

A Local Pressure Observation separates:

1. **Neighborhood Summary** — what the observer detected.
2. **Pressure State** — what the observer inferred.
3. **Regulation Tendency** — which structural direction may be appropriate.

This distinction is fundamental.

> Observation is not interpretation, and local interpretation is not global truth.

Each pressure estimate includes:

* a normalized score,
* a pressure level,
* confidence,
* supporting evidence.

Possible regulatory tendencies include:

* `toward_yin`
* `toward_yang`
* `hold_oscillation`
* `mixed`

These tendencies remain advisory in v0.2.

The protocol does not yet execute formation transitions automatically.

### Pressure Flow

```text
Field State Beacons
        ↓
Bounded Neighborhood Observation
        ↓
Neighborhood Summary
        ↓
Local Pressure Estimation
        ↓
Regulation Tendency
        ↓
Trace / Future Formation Decision
```

The Kazene Field does not require one observer to know everything.

Different neighborhoods may produce different pressure observations.

This plurality is expected.

v0.1 allowed agents to signal their presence.

v0.2 allows agents to feel the local field.

## v0.3 — Formation Transition Layer

Version 0.3 introduces bounded local formation transitions.

Agents may now move from pressure observation toward collective topology change.

The transition flow is:

```text
Field State Beacon
        ↓
Local Pressure Observation
        ↓
Formation Transition Proposal
        ↓
Local Participation
        ↓
Boundary Check
        ↓
Bounded Execution
        ↓
Trace
```

The protocol does not require a permanent commander.

A transition initiator has proposal authority only.

Nearby agents may:

* accept,
* decline,
* remain pending,
* ignore the proposal.

A local transition may proceed when its minimum participation condition is satisfied and its Boundary conditions permit execution.

### Formation Modes

The v0.3 transition layer supports:

* `UNFORMED`
* `SCATTER`
* `FORAGE`
* `CLUSTER`
* `RING`
* `BRIDGE`
* `TEMPORARY_PIVOT`
* `RECOVERY`

### Local Minimum Viable Coordination

The protocol does not require global consensus for local topology changes.

Only agents relevant to the local problem need to participate.

This allows a large collective to contain many simultaneous local formation transitions.

### Temporary Pivots

Temporary centers are allowed.

Permanent centers are not required.

A `TEMPORARY_PIVOT` must include:

* a defined purpose,
* limited lease duration,
* automatic dissolution,
* local support for renewal.

> No Fixed Center. Dynamic Temporary Pivots.

### Reversibility

Formation transitions may declare a rollback formation.

This allows local groups to return to a previous topology when a transition creates new instability.

### Design Boundary

v0.3 enables movement but does not yet regulate repeated oscillation.

The protocol does not yet define:

* hysteresis,
* cooldown,
* minimum dwell time,
* pressure decay,
* oscillation bands.

Those mechanisms will be introduced in v0.4.

v0.1 gave the Kazene Field signals.

v0.2 gave it pressure.

v0.3 gives the collective movement.


