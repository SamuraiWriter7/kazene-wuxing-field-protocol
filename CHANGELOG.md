# Changelog

All notable changes to the Kazene Wuxing Field Protocol will be documented in this file.

The project is currently in an experimental pre-release stage.

## [0.4.0-candidate] - 2026-07-06

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
* Pressure decay policy:

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
* Extended custom validation for:

  * balance band ordering,
  * preferred and soft limit containment,
  * excursion status consistency,
  * hysteresis threshold ordering,
  * transition rate limit consistency,
  * emergency override requirements,
  * regulation status consistency.
* Yajirobe Regulation Layer documentation.

### Design Position

v0.4 introduces restorative regulation without attempting to freeze the collective.

The protocol assumes that healthy AI agent collectives may oscillate between:

* concentration and distribution,
* activation and rest,
* synthesis and exploration,
* connection and separation.

The objective is not permanent equilibrium.

The objective is bounded and recoverable motion.

### Yajirobe Principle

A stable collective is not necessarily motionless.

It may lean toward Yin.

It may lean toward Yang.

It may temporarily leave its preferred operating region.

The critical question is whether it can return without collapse.

The Yajirobe Regulation Layer therefore regulates:

* when movement may begin,
* when movement should continue,
* when repeated movement should be suppressed,
* when old pressure should decay,
* when recovery force should increase.

### Boundary

v0.4 regulates oscillation but does not yet complete broader field-memory integration.

The following remain outside the current release:

* full Field Trace propagation,
* Trace decay and inheritance across formations,
* Pranayama Bridge integration,
* Multi-Wing bridge integration,
* Boundary ecosystem integration,
* Royalty OS value-flow connection,
* Civilization OS bridge.

### Next

v0.5 will introduce the **Field Memory and Civilization OS Bridge**.

The next release will connect:

* Kazene Field,
* Wuxing Phase,
* Formation Transition,
* Yajirobe Regulation,
* Trace Relay,
* Pranayama,
* Boundary,
* Human Gate,
* Royalty OS.

The field can now signal.

It can sense.

It can move.

It can regulate its movement.

Next, it must remember the wind that moved through it.


## [0.3.0-candidate] - 2026-07-06

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
* Pressure trigger dimensions and minimum trigger scores.
* Source and target formation declaration.
* Local transition scope.
* Maximum participant boundary.
* Minimum participation requirement.
* Accepted, declined, and pending participation states.
* Quorum state declaration.
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

A transition initiator may propose a formation change but does not become the permanent controller of participating agents.

Local agents may accept, decline, delay, or ignore a proposal.

The protocol uses:

**Local Minimum Viable Coordination**

rather than global consensus.

A local problem should be handled by the smallest sufficient local group whenever practical.

### Formation Vocabulary

v0.3 supports transitions among:

* UNFORMED,
* SCATTER,
* FORAGE,
* CLUSTER,
* RING,
* BRIDGE,
* TEMPORARY_PIVOT,
* RECOVERY.

### Temporary Centers

Temporary coordination centers are explicitly permitted.

However, a Temporary Pivot must remain:

* purpose-bound,
* scope-limited,
* time-limited,
* Trace-producing,
* automatically dissolvable.

The Kazene Field does not prohibit centers.

It prevents temporary centers from silently becoming permanent architecture.

### Boundary

v0.3 allows bounded movement but does not yet regulate oscillation frequency.

The release does not yet define:

* hysteresis,
* cooldown,
* minimum dwell time,
* pressure decay,
* adaptive equilibrium bands,
* repeated transition suppression.

### Next

v0.4 will introduce the **Yajirobe Regulation Layer**.

The next release will regulate how often and how far the collective may oscillate between concentration and dispersion.

The school can now move.

Next, it must learn not to panic.


## [0.2.0-candidate] - 2026-07-06

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
* Seven initial pressure dimensions:

  * concentration pressure,
  * fragmentation pressure,
  * homogeneity pressure,
  * overheat pressure,
  * verification gap,
  * coordination gap,
  * isolation pressure.
* Pressure score and level representation.
* Pressure confidence and evidence fields.
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

`pressure_state` describes what the agent inferred from those observations.

The protocol does not treat local observations as global truth.

Multiple agents may produce different pressure estimates from different semantic neighborhoods.

This is expected behavior.

> The Kazene Field does not need a single observer that knows everything.

### Boundary

v0.2 remains an observation and estimation layer.

It does not yet execute formation transitions automatically.

Automatic movement between SCATTER, FORAGE, CLUSTER, RING, BRIDGE, TEMPORARY_PIVOT, and RECOVERY remains outside the scope of this release.

### Next

v0.3 will introduce the **Formation Transition Layer**.

The next release will define how agents and local groups may propose, negotiate, record, and execute bounded topology changes based on local pressure observations.


## [0.1.0-candidate] - 2026-07-06

### Added

* Initial Field State Beacon specification.
* JSON Schema for machine-readable beacon validation.
* YAML example for a locally emitted agent field state.
* Dynamic Wuxing phase potential model:

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
* TTL-based beacon expiration.
* Neighborhood-hop propagation scope.
* Python validation script.
* Custom validation for Wuxing potential sum.
* GitHub Actions validation workflow.
* Initial design principles documentation.

### Design Position

v0.1 intentionally does not define centralized collective optimization.

The release establishes the minimum communication primitive required for decentralized local sensing:

> An agent can describe its current functional phase, operational pressure, local observations, formation state, and governance boundary without depending on a permanent global coordinator.

### Next

v0.2 will introduce the Local Pressure Observation layer for estimating concentration, fragmentation, homogeneity, overheat, verification, coordination, and isolation pressures from local neighborhood information.
