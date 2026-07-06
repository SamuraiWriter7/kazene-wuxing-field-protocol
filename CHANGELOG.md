# Changelog

All notable changes to the Kazene Wuxing Field Protocol will be documented in this file.

The project is currently in an experimental pre-release stage.

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
