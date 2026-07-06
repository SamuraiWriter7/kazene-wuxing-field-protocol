# Yajirobe Regulation Layer

## Kazene Wuxing Field Protocol v0.4

The Yajirobe Regulation Layer introduces oscillation control for decentralized AI agent collectives.

Version 0.1 gave agents signals.

Version 0.2 gave agents local pressure sensing.

Version 0.3 allowed local formations to change shape.

Version 0.4 introduces restorative regulation.

The central question is:

> Can a collective remain adaptive without becoming structurally nervous?

The objective is not to eliminate oscillation.

The objective is to allow movement while preventing uncontrolled transition chatter, permanent over-concentration, permanent fragmentation, and repeated overreaction.

---

## 1. Dynamic Balance, Not Static Equilibrium

The Kazene Wuxing Field does not seek a permanently fixed midpoint.

A healthy collective may move toward Yin or Yang according to local conditions.

Temporary Yang-oriented states may support:

* concentration,
* synchronization,
* synthesis,
* crisis response,
* coordinated verification.

Temporary Yin-oriented states may support:

* dispersion,
* independent exploration,
* cooling,
* local execution,
* diversity restoration.

Neither direction is inherently correct.

The regulatory problem begins when a temporary state becomes excessive, unstable, or permanent.

The Yajirobe model therefore defines:

* a preferred oscillation band,
* soft excursion limits,
* hard excursions,
* recovery force,
* temporal transition constraints.

---

## 2. Preferred Band and Excursion

The oscillation axis is represented from `-1.0` to `1.0`.

```text
-1.0                    0.0                    +1.0
Deep Yin          Oscillatory Center          Deep Yang
```

A regulation policy may define:

```text
Soft Limit     Preferred Band       Soft Limit
    │                │                   │
    ▼                ▼                   ▼

-0.75       -0.30 ─── 0 ─── +0.30       +0.75
```

Three excursion states are recognized:

### Within Preferred Band

The current oscillation remains inside the preferred operating region.

### Soft Excursion

The collective is outside the preferred region but remains inside its soft limits.

A Soft Excursion does not necessarily require immediate correction.

### Hard Excursion

The collective has moved beyond a soft limit.

A stronger recovery response may be required.

The protocol does not require immediate return to zero.

Recovery may be gradual.

---

## 3. Hysteresis

Hysteresis prevents a regulation mode from repeatedly activating and deactivating around a single threshold.

Example:

```text
Entry threshold:
0.75

Release threshold:
0.45
```

A pressure state may activate regulation at `0.75`, but regulation continues until the pressure falls below `0.45`.

This prevents:

```text
Activate
Deactivate
Activate
Deactivate
```

from occurring because of small fluctuations near one threshold.

The collective should respond to meaningful change, not every tremor.

---

## 4. Cooldown

Cooldown introduces a temporary observation period after a formation transition.

Example:

```text
CLUSTER
   ↓
SCATTER
   ↓
Cooldown
   ↓
Observe
   ↓
Re-evaluate
```

Cooldown does not mean that the collective becomes blind or inactive.

Agents may continue:

* observing,
* emitting Beacons,
* recording Trace,
* sensing pressure,
* performing bounded local tasks.

The restriction applies to repeated topology change.

---

## 5. Minimum Dwell Time

A new formation should normally remain active long enough for its effects to become observable.

Without minimum dwell time, a collective may interpret the transient effects of a transition as evidence that the transition failed.

Example:

```text
SCATTER begins
       ↓
Immediate temporary coordination drop
       ↓
Premature interpretation:
"SCATTER failed"
       ↓
Immediate CLUSTER restoration
```

Minimum dwell time reduces this risk.

The field must be allowed to experience a state before evaluating it.

---

## 6. Pressure Decay

Pressure observations should not remain equally influential forever.

A pressure signal may decay over time.

Possible models include:

* none,
* linear,
* exponential.

Pressure decay supports a broader Kazene principle:

> The field should remember, but it should not remain trapped in old weather.

A high-pressure observation from the past may still matter, but its influence should normally decline unless renewed by new observations.

---

## 7. Transition Rate Limiting

A collective may define a maximum number of formation transitions inside a time window.

Example:

```text
Window:
900 seconds

Maximum transitions:
3
```

When the limit is reached, additional transitions may be:

* suppressed,
* delayed,
* escalated for review,
* overridden only under emergency conditions.

This protects the collective from structural thrashing.

---

## 8. Recovery Force

Recovery Force represents the strength of the tendency to return from excessive excursions.

It is not a command to move directly toward zero.

A collective may recover gradually.

Example:

```text
-0.92
   ↓
-0.78
   ↓
-0.61
   ↓
-0.43
   ↓
Preferred region
```

Recovery should preserve adaptation.

The Yajirobe does not freeze the collective.

It prevents the collective from falling.

---

## 9. Emergency Override

Normal oscillation regulation may be bypassed when emergency conditions require immediate response.

An emergency override must remain explicit.

It should include:

* active state,
* reason,
* expiration time,
* Human Gate requirement where appropriate.

Emergency override must not become a hidden method for creating permanent command authority.

Exceptional control must remain exceptional.

---

## 10. Regulation Decisions

The initial regulation actions are:

### hold

Maintain the current formation and continue observation.

### allow_transition

Permit the proposed transition under current policy.

### suppress_transition

Temporarily prevent a new transition.

### force_recovery

Initiate a bounded recovery response after excessive excursion.

### emergency_override

Permit exceptional action under declared emergency conditions.

These actions regulate movement.

They do not replace the Formation Transition Layer.

v0.3 defines how a group changes shape.

v0.4 decides whether the timing and amplitude of that change remain structurally healthy.

---

## 11. The Yajirobe Principle

The Yajirobe principle can be expressed simply:

> A stable collective is not a motionless collective.

It moves.

It leans.

It reacts.

It returns.

The important property is not perfect stillness.

It is the preservation of recoverable movement.

---

## 12. The v0.4 Boundary

Version 0.4 introduces oscillation regulation but does not yet complete the broader field-memory and Civilization OS integration.

The following remain for later work:

* full Field Trace propagation,
* cross-cluster Trace inheritance,
* Pranayama Bridge integration,
* Multi-Wing coordination bridge,
* Royalty OS value flow,
* Civilization OS interoperability.

Those connections belong to v0.5.

v0.3 allowed the school to move.

v0.4 teaches it to sway without falling.
