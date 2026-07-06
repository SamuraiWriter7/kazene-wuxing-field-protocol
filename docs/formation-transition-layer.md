# Formation Transition Layer

## Kazene Wuxing Field Protocol v0.3

The Formation Transition Layer introduces bounded topology change for decentralized AI agent collectives.

Version 0.1 allowed agents to emit state.

Version 0.2 allowed agents to estimate local pressure.

Version 0.3 allows local groups to change formation.

The central question of this release is:

> Can an AI agent collective change shape without requiring a permanent central commander?

The Kazene approach answers this through local proposal, voluntary participation, bounded execution, reversible transition, and Trace continuity.

---

## 1. A Proposal Is Not a Command

Any compatible agent may propose a local formation transition when supported by local pressure observations.

However, the proposer does not automatically gain authority over participating agents.

The initiator is defined as:

`proposal_only`

This distinction is fundamental.

The proposal may be:

* accepted,
* declined,
* ignored,
* delayed,
* allowed to expire.

The Kazene Field permits coordination without converting every coordination event into hierarchy.

---

## 2. Formation Transition Flow

A typical transition follows this sequence:

```text
Local Pressure Observation
        ↓
Formation Proposal
        ↓
Local Participation Decision
        ↓
Quorum Check
        ↓
Boundary Check
        ↓
Bounded Execution
        ↓
Trace Emission
        ↓
Completion or Rollback
```

Not all transitions must reach completion.

Possible lifecycle states are:

* proposed,
* negotiating,
* approved,
* executing,
* completed,
* aborted,
* expired.

Failure to form is a valid result.

---

## 3. Local Minimum Viable Coordination

v0.3 does not require global consensus.

A formation transition should involve only the agents necessary for the local problem.

For example:

```text
Total collective:
1,000 agents

Relevant neighborhood:
8 agents

Minimum participants:
3 agents

Accepted:
4 agents

Result:
Local formation transition may proceed.
```

This principle is called:

**Local Minimum Viable Coordination**

It prevents decentralized systems from replacing central control with permanent collective voting overhead.

---

## 4. Formation Vocabulary

### SCATTER

Used for:

* exploration,
* independent verification,
* provider diversification,
* load spreading,
* overheat reduction.

### FORAGE

Used for:

* parallel information gathering,
* hypothesis exploration,
* lightweight synthesis.

### CLUSTER

Used for:

* temporary concentrated problem solving,
* synthesis,
* cooperative inference.

### RING

Used for:

* mutual verification,
* circular review,
* non-central deliberation.

### BRIDGE

Used for:

* reconnecting fragmented groups,
* restoring Trace continuity,
* context exchange.

### TEMPORARY_PIVOT

Used for:

* bounded coordination,
* emergency response,
* short-lived synthesis.

A Temporary Pivot must include:

* purpose,
* lease,
* bounded authority,
* automatic dissolution,
* local support for renewal.

### RECOVERY

Used for:

* post-failure reconstruction,
* route discovery,
* Trace recovery,
* collective re-entry.

---

## 5. Temporary Centers Are Allowed

The protocol does not prohibit temporary centers.

It prohibits silent permanence.

A Temporary Pivot is therefore valid only when it is:

* purpose-bound,
* scope-limited,
* time-limited,
* Trace-producing,
* automatically dissolvable.

A pivot may coordinate.

It must not become permanent merely because other agents forgot to remove it.

> The center may emerge with the task and disappear with the task.

---

## 6. Reversibility

Formation transitions should be reversible whenever possible.

A transition record therefore includes:

* source formation,
* target formation,
* rollback formation,
* execution status,
* completion time.

For example:

```text
CLUSTER
   ↓
SCATTER
   ↓
unexpected coordination failure
   ↓
rollback
   ↓
CLUSTER
```

Later versions may introduce more complex recovery paths.

v0.3 begins with explicit rollback awareness.

---

## 7. Pressure-Based Transition

A transition proposal should reference one or more Local Pressure Observation records.

Possible transition patterns include:

```text
High Concentration
+
High Homogeneity
→ SCATTER
```

```text
High Fragmentation
+
High Isolation
→ BRIDGE
```

```text
High Coordination Gap
+
Urgent Shared Task
→ TEMPORARY_PIVOT
```

```text
Post-Failure Trace Loss
→ RECOVERY
```

These mappings are not mandatory global laws.

Different implementations may adopt different local policies.

The protocol standardizes the record of the transition, not a single universal optimization algorithm.

---

## 8. Boundary Before Movement

A formation transition may be structurally appropriate but operationally unsafe.

Therefore, transition execution remains subject to:

* safety checks,
* risk level,
* autonomy permission,
* Human Gate requirements.

A formation proposal must not override a stronger safety boundary.

Field pressure suggests movement.

Boundary determines whether movement is permitted.

---

## 9. Trace Continuity

A formation transition must produce a Trace.

The Trace should preserve:

* source pressure observations,
* transition proposal,
* participation result,
* target formation,
* execution outcome,
* rollback information,
* unresolved local needs.

Without Trace continuity, a moving collective may become structurally forgetful.

Kazene aims for movement without amnesia.

---

## 10. The v0.3 Boundary

Version 0.3 introduces formation transition records and bounded local execution.

It does not yet define:

* oscillation hysteresis,
* minimum dwell time,
* cooldown periods,
* pressure decay,
* repeated transition suppression,
* adaptive equilibrium bands.

Those belong to v0.4.

v0.3 allows the school to change shape.

v0.4 will prevent it from changing shape too nervously.
