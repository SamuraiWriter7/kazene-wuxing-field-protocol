# Changelog

All notable changes to the Kazene Wuxing Field Protocol will be documented in this file.

The project is currently in an experimental pre-release stage.

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
