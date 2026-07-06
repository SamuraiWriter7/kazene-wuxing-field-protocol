# Local Pressure Model

## Kazene Wuxing Field Protocol v0.2

The Local Pressure Observation Layer introduces decentralized pressure sensing for AI agent collectives.

Version 0.1 allowed an agent to emit a Field State Beacon.

Version 0.2 allows an agent to observe nearby signals and estimate local structural pressure without requiring a permanent global-state authority.

The core question of v0.2 is:

> Can an agent sense imbalance from its neighborhood without asking a central system to describe the entire collective?

---

## 1. Observation Is Not Global Truth

A Local Pressure Observation is always local.

An observer may inspect:

* nearby Field State Beacons,
* recent local Trace signals,
* peer density,
* phase distribution,
* load,
* energy pressure,
* connectivity,
* verification coverage,
* isolation conditions.

The result must not be presented as an unquestionable description of the entire collective.

A local observation may be:

* incomplete,
* delayed,
* noisy,
* biased by neighborhood structure,
* affected by stale signals.

For this reason, observations and pressure estimates should carry confidence information where appropriate.

---

## 2. Observation and Interpretation Must Be Separated

v0.2 separates two concepts.

### Neighborhood Summary

The `neighborhood_summary` section records aggregated observations.

Examples include:

* dominant local phase,
* local Wuxing phase distribution,
* average load,
* energy pressure,
* verification coverage,
* coordination connectivity,
* isolated peer ratio.

These are observations.

### Pressure State

The `pressure_state` section contains interpretations derived from those observations.

Examples include:

* concentration pressure,
* fragmentation pressure,
* homogeneity pressure,
* overheat pressure,
* verification gap,
* coordination gap,
* isolation pressure.

These are estimates.

The distinction is essential.

> What an agent sees and what an agent concludes must remain distinguishable.

---

## 3. Seven Initial Pressure Dimensions

### Concentration Pressure

Measures local structural concentration.

Possible indicators include:

* excessive peer density,
* excessive dependence on one local pivot,
* high task convergence,
* repeated routing through the same node,
* excessive clustering.

High concentration pressure may suggest movement toward dispersion.

---

### Fragmentation Pressure

Measures loss of useful collective cohesion.

Possible indicators include:

* low connectivity,
* disconnected subgroups,
* incompatible context states,
* broken Trace continuity,
* repeated failed handoffs.

High fragmentation pressure may suggest temporary reconnection or clustering.

---

### Homogeneity Pressure

Measures excessive similarity inside the local field.

Possible indicators include:

* one Wuxing phase dominating the neighborhood,
* insufficient independent verification,
* repeated use of identical models or methods,
* low role diversity,
* repeated agreement without adversarial inspection.

High homogeneity pressure may suggest diversification.

---

### Overheat Pressure

Measures excessive computational or operational activation.

Possible indicators include:

* sustained high load,
* high energy pressure,
* excessive FIRE phase density,
* repeated inference loops,
* insufficient cooling or sleep states.

High overheat pressure may suggest WATER-oriented responses or Pranayama intervention.

---

### Verification Gap

Measures insufficient auditing and verification capacity.

Possible indicators include:

* low METAL presence,
* low review coverage,
* unresolved conflicting claims,
* missing provenance,
* incomplete Trace verification.

High verification gaps may suggest additional independent review.

---

### Coordination Gap

Measures insufficient ability to cooperate.

Possible indicators include:

* low connectivity,
* repeated task duplication,
* incomplete context exchange,
* incompatible local goals,
* unresolved handoff failures.

High coordination gaps may suggest temporary clustering, bridging, or a bounded pivot.

---

### Isolation Pressure

Measures excessive local node separation.

Possible indicators include:

* high isolated-peer ratio,
* unreachable peers,
* missing Trace continuity,
* persistent single-node execution,
* unavailable recovery routes.

High isolation pressure may suggest reconnection or BRIDGE formation.

---

## 4. Pressure Is Directional, Not Authoritative

A pressure observation may suggest a regulatory tendency.

Possible directions are:

* `toward_yin`
* `toward_yang`
* `hold_oscillation`
* `mixed`

These are not commands.

For example:

```text
Critical concentration pressure
+
Critical homogeneity pressure
+
High overheat pressure
=
Possible tendency toward Yin
```

A local agent may still decide not to act because of:

* Boundary constraints,
* Human Gate requirements,
* emergency conditions,
* insufficient confidence,
* conflicting local signals.

---

## 5. Local Pressure Does Not Require a Global Score

The protocol intentionally avoids requiring a single collective balance number.

A global score could become:

* a central dependency,
* a bottleneck,
* a target for manipulation,
* a false appearance of certainty.

Instead, multiple local observations may coexist.

Two agents may legitimately report different pressure states because they occupy different semantic neighborhoods.

This is expected.

Kazene Field is not a single dashboard.

It is a field of partially overlapping perspectives.

---

## 6. Confidence and Evidence

Every pressure dimension includes:

* `score`
* `level`
* `confidence`
* `evidence`

Example:

```yaml
overheat_pressure:
  score: 0.74
  level: "high"
  confidence: 0.87
  evidence:
    - "Average neighborhood load is elevated."
    - "Average energy pressure is elevated."
```

This prevents an estimated pressure from appearing as unsupported certainty.

The field should not only say:

> Pressure is high.

It should also say:

> This is why I believe pressure is high, and this is how confident I am.

---

## 7. The v0.2 Boundary

Version 0.2 observes and estimates.

It does not yet execute formation changes.

The following remain outside the v0.2 scope:

* automatic SCATTER execution,
* automatic CLUSTER formation,
* automatic BRIDGE creation,
* temporary pivot election,
* transition hysteresis,
* cooldown enforcement,
* minimum dwell time.

Those functions belong to later versions.

The v0.2 responsibility is narrower:

> Sense the local field before attempting to reshape it.

v0.1 gave the Kazene Field signals.

v0.2 gives it pressure.
