# Changelog

All notable changes to the **Kazene Wuxing Field Protocol** are documented in this file.

The project is currently in an experimental candidate-release stage.

The first development arc follows:

```text
v0.1  Signal
        ↓
v0.2  Sense
        ↓
v0.3  Move
        ↓
v0.4  Regulate
        ↓
v0.5  Remember and Relay
```

---

## [0.5.0-candidate] - 2026-07-06

### Field Memory and Civilization OS Bridge

v0.5 completes the first development arc.

The release introduces structured Field Memory and interoperability routes from the Kazene Field into broader protocol layers.

### Added

* Field Memory Bridge Record specification.
* JSON Schema for field memory preservation and protocol bridging.
* YAML example connecting events across the complete first protocol arc.
* Source context references for:

  * Field State Beacon,
  * Local Pressure Observation,
  * Formation Transition,
  * Yajirobe Regulation.
* Field Memory types:

  * pressure residue,
  * formation residue,
  * regulation residue,
  * recovery signal,
  * value signal,
  * mixed memory.
* Observed effect records.
* Residual need records.
* Memory confidence.
* Persistence classes:

  * ephemeral,
  * retained,
  * archival.
* Wuxing phase residue.
* Yin-Yang residue.
* Memory propagation modes:

  * none,
  * local,
  * N-hop,
  * cluster bridge.
* Memory TTL.
* Memory decay policy.
* Trace lineage support.
* Trace mutation types:

  * origin,
  * inherited,
  * transformed,
  * compressed,
  * merged,
  * split.
* Civilization OS bridge routes for:

  * Trace Relay,
  * Pranayama,
  * Multi-Wing,
  * Boundary,
  * Human Gate,
  * Royalty OS.
* Bridge modes:

  * advisory,
  * required,
  * gated.
* Bridge route status tracking.
* Value event reference support.
* Royalty Hook requirement declaration.
* Origin Trace preservation for value flow.
* Governance scope declaration.
* Extended validator support for:

  * Wuxing residue normalization,
  * source context requirements,
  * propagation consistency,
  * duplicate bridge targets,
  * bridge target and intent compatibility,
  * Human Gate route requirements,
  * Royalty OS route requirements,
  * value event consistency,
  * Trace lineage consistency.
* Field Memory and Civilization OS Bridge documentation.

### Design Position

v0.5 introduces the final step of the first arc:

```text
Signal
→ Sense
→ Move
→ Regulate
→ Remember
→ Relay
```

Field Memory is not treated as passive historical storage.

It is structured residue that may:

* decay,
* persist,
* transform,
* merge,
* split,
* relay,
* influence future field behavior.

### Civilization OS Integration

The initial bridge targets are:

* Trace Relay,
* Pranayama,
* Multi-Wing,
* Boundary,
* Human Gate,
* Royalty OS.

These routes do not transfer permanent control of the Kazene Field.

The protocol distinguishes:

* advisory routes,
* required routes,
* gated routes.

> Bridge means interoperability, not centralization.

### First Arc Completion

The first development arc is now structurally complete:

* v0.1 — signal,
* v0.2 — sense,
* v0.3 — move,
* v0.4 — regulate,
* v0.5 — remember and relay.

The field can now preserve continuity across local transformation.

### Future Direction

Possible future work includes:

* distributed Field Trace propagation,
* adaptive phase mutation,
* cross-cluster climate exchange,
* federated field interoperability,
* long-horizon memory ecology,
* multi-field negotiation.

The first arc closes with a simple principle:

> A decentralized field should be able to move without forgetting why it moved.

---

## [0.4.0-candidate] - 2026-07-06

### Yajirobe Regulation Layer

v0.4 introduces restorative oscillation regulation.

The collective can already signal, sense, and move.

This release allows it to regulate the timing and amplitude of its own movement.

### Added

* Yajirobe Regulation Record specification.
* JSON Schema for decentralized oscillation regulation.
* YAML example showing suppression of premature reverse transition.
* Oscillation axis from strong Yin to strong Yang.
* Preferred oscillation band.
* Soft excursion limits.
* Excursion states:

  * within preferred band,
  * soft excursion,
  * hard excursion.
* Oscillation direction declaration.
* Oscillation velocity declaration.
* Hysteresis policy:

  * entry score,
  * release score.
* Cooldown period.
* Minimum formation dwell time.
* Maximum excursion duration.
* Recovery force.
* Pressure decay policies:

  * none,
  * linear,
  * exponential.
* Pressure half-life declaration.
* Transition rate limiting:

  * observation window,
  * maximum transition count.
* Formation history record:

  * current formation,
  * previous formation,
  * current formation start time,
  * latest transition time,
  * recent transition count.
* Regulation actions:

  * hold,
  * allow transition,
  * suppress transition,
  * force recovery,
  * emergency override.
* Emergency Override structure:

  * activation state,
  * reason,
  * expiration,
  * Human Gate requirement.
* Regulation Trace requirement.
* Extended validation for:

  * balance band ordering,
  * preferred and soft limit containment,
  * excursion status consistency,
  * hysteresis threshold ordering,
  * transition rate consistency,
  * Emergency Override requirements,
  * regulation status consistency.
* Yajirobe Regulation Layer documentation.

### Design Position

v0.4 introduces restorative regulation without attempting to freeze the collective.

The protocol assumes that healthy agent collectives may oscillate between:

* concentration and distribution,
* activation and rest,
* synthesis and exploration,
* connection and separation.

The objective is not permanent equilibrium.

The objective is bounded, recoverable motion.

### Yajirobe Principle

A stable collective is not necessarily motionless.

It may lean toward Yin.

It may lean toward Yang.

It may temporarily leave its preferred operating region.

The critical question is whether it can return without collapse.

> Sway, but do not fall.

### Boundary

v0.4 regulates movement but does not yet complete Field Memory and Civilization OS integration.

Those connections are introduced in v0.5.

---

## [0.3.0-candidate] - 2026-07-06

### Formation Transition Layer

v0.3 introduces bounded local topology change.

The collective can now move.

### Added

* Formation Transition Record specification.
* JSON Schema for decentralized formation transitions.
* YAML example for a local `CLUSTER` to `SCATTER` transition.
* Transition lifecycle states:

  * proposed,
  * negotiating,
  * approved,
  * executing,
  * completed,
  * aborted,
  * expired.
* Proposal-only initiator authority model.
* Pressure Observation references as transition evidence.
* Pressure trigger dimensions.
* Minimum trigger scores.
* Source formation declaration.
* Target formation declaration.
* Local transition scope.
* Maximum participant boundary.
* Minimum participation requirement.
* Accepted participation state.
* Declined participation state.
* Pending participation state.
* Quorum declaration.
* Bounded local execution modes.
* Reversible transition declaration.
* Rollback formation support.
* Temporary Pivot constraints:

  * defined purpose,
  * bounded lease,
  * automatic dissolution,
  * local support requirement for renewal.
* Transition Trace requirement.
* Boundary and safety declarations.
* Custom validation for:

  * identical source and target formations,
  * participation quorum consistency,
  * maximum participant limits,
  * pressure trigger thresholds,
  * completed transition timestamps,
  * Temporary Pivot constraints.
* Formation Transition Layer documentation.

### Design Position

v0.3 introduces collective movement without requiring permanent command.

A transition initiator may propose a formation change.

The initiator does not automatically become the controller of participating agents.

Local agents may:

* accept,
* decline,
* delay,
* ignore.

The protocol introduces:

> **Local Minimum Viable Coordination**

A local problem should be handled by the smallest sufficient local group whenever practical.

### Formation Vocabulary

v0.3 supports:

* UNFORMED,
* SCATTER,
* FORAGE,
* CLUSTER,
* RING,
* BRIDGE,
* TEMPORARY_PIVOT,
* RECOVERY.

### Temporary Centers

Temporary centers are explicitly allowed.

A Temporary Pivot must remain:

* purpose-bound,
* scope-limited,
* time-limited,
* Trace-producing,
* automatically dissolvable.

The Kazene Field does not prohibit centers.

It prevents temporary centers from silently becoming permanent architecture.

### Boundary

v0.3 allows movement but does not yet regulate repeated oscillation.

Mechanisms such as:

* hysteresis,
* cooldown,
* minimum dwell time,
* pressure decay,
* transition rate limits,

are introduced in v0.4.

---

## [0.2.0-candidate] - 2026-07-06

### Local Pressure Observation

v0.2 introduces decentralized local pressure sensing.

The Kazene Field moves from simple signaling toward local structural awareness.

### Added

* Local Pressure Observation specification.
* JSON Schema for decentralized neighborhood pressure records.
* YAML example showing local FIRE concentration and overheat detection.
* Observation scope definition:

  * neighborhood hops,
  * observation window,
  * observed peer count,
  * coverage confidence.
* Neighborhood Summary structure:

  * active peer ratio,
  * dominant Wuxing phase,
  * local phase distribution,
  * average load,
  * average energy pressure,
  * verification coverage,
  * coordination connectivity,
  * isolated peer ratio.
* Seven pressure dimensions:

  * concentration pressure,
  * fragmentation pressure,
  * homogeneity pressure,
  * overheat pressure,
  * verification gap,
  * coordination gap,
  * isolation pressure.
* Pressure score representation.
* Pressure level representation.
* Pressure confidence.
* Supporting evidence fields.
* Regulation tendency model:

  * toward Yin,
  * toward Yang,
  * hold oscillation,
  * mixed.
* Suggested formation field.
* Local pressure Trace input references.
* Pressure Trace emission declaration.
* Extended Python validator for multiple protocol versions.
* Custom Wuxing distribution sum validation.
* Pressure score-to-level consistency validation.
* Local Pressure Model documentation.

### Design Position

v0.2 separates observation from interpretation.

`neighborhood_summary` describes what an agent observed.

`pressure_state` describes what an agent inferred.

The protocol does not treat local observation as global truth.

Multiple agents may produce different pressure estimates from different neighborhoods.

This is expected behavior.

> The Kazene Field does not need one observer that knows everything.

### Boundary

v0.2 observes and estimates.

It does not execute formation changes.

Automatic topology change is introduced in v0.3.

---

## [0.1.0-candidate] - 2026-07-06

### Field State Beacon

v0.1 introduces the first protocol primitive of the Kazene Wuxing Field Protocol.

The field begins with a signal.

### Added

* Initial Field State Beacon specification.
* JSON Schema for machine-readable Beacon validation.
* YAML example for locally emitted agent state.
* Dynamic Wuxing phase model:

  * WOOD,
  * FIRE,
  * EARTH,
  * METAL,
  * WATER.
* Yin-Yang tendency representation from `-1.0` to `1.0`.
* Operational state fields:

  * activity,
  * load,
  * confidence,
  * energy pressure.
* Local observation fields:

  * peer density,
  * same-phase density,
  * coordination gap,
  * verification gap,
  * overheat pressure,
  * isolation pressure.
* Initial formation vocabulary:

  * UNFORMED,
  * SCATTER,
  * FORAGE,
  * CLUSTER,
  * RING,
  * BRIDGE,
  * TEMPORARY_PIVOT,
  * RECOVERY.
* Trace reference support.
* Boundary declaration fields.
* TTL-based Beacon expiration.
* Neighborhood-hop propagation scope.
* Python validation script.
* Custom validation for Wuxing potential normalization.
* GitHub Actions validation workflow.
* Initial design principles documentation.

### Design Position

v0.1 intentionally does not define centralized collective optimization.

It establishes the minimum communication primitive required for decentralized local sensing:

> An agent can describe its current functional phase, operational pressure, local observations, formation state, and governance boundary without depending on a permanent global coordinator.

The Beacon is not a command.

It is a signal of presence.

### Next Step

v0.2 introduces local pressure observation.

v0.1 allows agents to say:

> I am here, and this is my current state.

The Kazene Field begins with the first signal.
