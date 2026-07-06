# Changelog

All notable changes to the Kazene Wuxing Field Protocol will be documented in this file.

The project is currently in an experimental pre-release stage.

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
