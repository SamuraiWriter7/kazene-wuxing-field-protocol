from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any, Callable

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[1]

WUXING_KEYS = (
    "wood",
    "fire",
    "earth",
    "metal",
    "water",
)

SUM_TOLERANCE = 1e-6


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a JSON object."
        )

    return data


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(
            f"{path} must contain a YAML mapping."
        )

    return data


def format_path(error_path: Any) -> str:
    parts = [
        str(part)
        for part in error_path
    ]

    return ".".join(parts) if parts else "<root>"


def validate_distribution_sum(
    distribution: dict[str, Any],
    path_name: str,
) -> list[str]:
    errors: list[str] = []

    try:
        total = sum(
            float(distribution[key])
            for key in WUXING_KEYS
        )
    except (
        KeyError,
        TypeError,
        ValueError,
    ) as exc:
        return [
            f"{path_name}: unable to calculate "
            f"Wuxing sum: {exc}"
        ]

    if not math.isclose(
        total,
        1.0,
        rel_tol=0.0,
        abs_tol=SUM_TOLERANCE,
    ):
        errors.append(
            f"{path_name} must sum to 1.0 "
            f"(actual: {total:.12f})"
        )

    return errors


def validate_field_state_beacon(
    instance: dict[str, Any],
) -> list[str]:
    try:
        distribution = (
            instance["phase_state"]
            ["wuxing_potential"]
        )
    except (
        KeyError,
        TypeError,
    ):
        return []

    return validate_distribution_sum(
        distribution,
        "phase_state.wuxing_potential",
    )


def expected_pressure_level(
    score: float,
) -> str:
    if score < 0.25:
        return "low"

    if score < 0.50:
        return "medium"

    if score < 0.75:
        return "high"

    return "critical"


def validate_pressure_levels(
    instance: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    pressure_state = instance.get(
        "pressure_state"
    )

    if not isinstance(
        pressure_state,
        dict,
    ):
        return errors

    for name, pressure in pressure_state.items():
        if not isinstance(
            pressure,
            dict,
        ):
            continue

        score = pressure.get("score")
        level = pressure.get("level")

        if not isinstance(
            score,
            (int, float),
        ):
            continue

        if not isinstance(
            level,
            str,
        ):
            continue

        expected = expected_pressure_level(
            float(score)
        )

        if level != expected:
            errors.append(
                f"pressure_state.{name}.level "
                f"must be '{expected}' "
                f"for score {score}, "
                f"but got '{level}'"
            )

    return errors


def validate_local_pressure_observation(
    instance: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    try:
        distribution = (
            instance["neighborhood_summary"]
            ["phase_distribution"]
        )
    except (
        KeyError,
        TypeError,
    ):
        distribution = None

    if isinstance(
        distribution,
        dict,
    ):
        errors.extend(
            validate_distribution_sum(
                distribution,
                (
                    "neighborhood_summary."
                    "phase_distribution"
                ),
            )
        )

    errors.extend(
        validate_pressure_levels(
            instance
        )
    )

    return errors


def validate_formation_transition(
    instance: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    formation_change = instance.get(
        "formation_change",
        {},
    )

    current_mode = formation_change.get(
        "current_mode"
    )

    target_mode = formation_change.get(
        "target_mode"
    )

    if (
        current_mode is not None
        and target_mode is not None
        and current_mode == target_mode
    ):
        errors.append(
            "formation_change.current_mode and "
            "formation_change.target_mode "
            "must be different"
        )

    participation = instance.get(
        "participation",
        {},
    )

    accepted = participation.get(
        "accepted_agent_ids",
        [],
    )

    declined = participation.get(
        "declined_agent_ids",
        [],
    )

    pending = participation.get(
        "pending_agent_ids",
        [],
    )

    minimum = participation.get(
        "minimum_participants"
    )

    quorum_met = participation.get(
        "quorum_met"
    )

    if isinstance(
        minimum,
        int,
    ):
        expected_quorum = (
            len(accepted) >= minimum
        )

        if quorum_met != expected_quorum:
            errors.append(
                "participation.quorum_met "
                "does not match accepted participant count"
            )

    scope = instance.get(
        "scope",
        {},
    )

    maximum = scope.get(
        "maximum_participants"
    )

    unique_participants = set(
        accepted
        + declined
        + pending
    )

    if (
        isinstance(maximum, int)
        and len(unique_participants) > maximum
    ):
        errors.append(
            "total participant population exceeds "
            "scope.maximum_participants"
        )

    pressure_basis = instance.get(
        "pressure_basis",
        {},
    )

    triggers = pressure_basis.get(
        "trigger_dimensions",
        [],
    )

    for index, trigger in enumerate(triggers):
        if not isinstance(
            trigger,
            dict,
        ):
            continue

        score = trigger.get("score")
        minimum_trigger_score = trigger.get(
            "minimum_trigger_score"
        )

        if (
            isinstance(
                score,
                (int, float),
            )
            and isinstance(
                minimum_trigger_score,
                (int, float),
            )
            and score < minimum_trigger_score
        ):
            errors.append(
                "pressure_basis.trigger_dimensions"
                f".{index}.score "
                "is below minimum_trigger_score"
            )

    transition = instance.get(
        "transition",
        {},
    )

    execution = instance.get(
        "execution",
        {},
    )

    status = transition.get("status")
    completed_at = execution.get(
        "completed_at"
    )

    if (
        status == "completed"
        and completed_at is None
    ):
        errors.append(
            "execution.completed_at is required "
            "when transition.status is completed"
        )

    if (
        target_mode == "TEMPORARY_PIVOT"
        and "temporary_pivot" not in instance
    ):
        errors.append(
            "temporary_pivot is required when "
            "target_mode is TEMPORARY_PIVOT"
        )

    return errors


ValidationFunction = Callable[
    [dict[str, Any]],
    list[str],
]

def validate_yajirobe_regulation(
    instance: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    oscillation_state = instance.get(
        "oscillation_state",
        {},
    )

    balance_band = oscillation_state.get(
        "balance_band",
        {},
    )

    preferred_min = balance_band.get(
        "preferred_min"
    )

    preferred_max = balance_band.get(
        "preferred_max"
    )

    soft_limit_min = balance_band.get(
        "soft_limit_min"
    )

    soft_limit_max = balance_band.get(
        "soft_limit_max"
    )

    values = (
        preferred_min,
        preferred_max,
        soft_limit_min,
        soft_limit_max,
    )

    if all(
        isinstance(value, (int, float))
        for value in values
    ):
        if preferred_min > preferred_max:
            errors.append(
                "oscillation_state.balance_band."
                "preferred_min must not exceed "
                "preferred_max"
            )

        if soft_limit_min > soft_limit_max:
            errors.append(
                "oscillation_state.balance_band."
                "soft_limit_min must not exceed "
                "soft_limit_max"
            )

        if soft_limit_min > preferred_min:
            errors.append(
                "soft_limit_min must be less than or "
                "equal to preferred_min"
            )

        if preferred_max > soft_limit_max:
            errors.append(
                "preferred_max must be less than or "
                "equal to soft_limit_max"
            )

    axis_position = oscillation_state.get(
        "axis_position"
    )

    excursion_status = oscillation_state.get(
        "excursion_status"
    )

    if (
        isinstance(axis_position, (int, float))
        and all(
            isinstance(value, (int, float))
            for value in values
        )
    ):
        if (
            preferred_min
            <= axis_position
            <= preferred_max
        ):
            expected_excursion = (
                "within_preferred_band"
            )

        elif (
            soft_limit_min
            <= axis_position
            <= soft_limit_max
        ):
            expected_excursion = (
                "soft_excursion"
            )

        else:
            expected_excursion = (
                "hard_excursion"
            )

        if excursion_status != expected_excursion:
            errors.append(
                "oscillation_state.excursion_status "
                f"must be '{expected_excursion}' "
                f"for axis_position {axis_position}"
            )

    policy = instance.get(
        "regulation_policy",
        {},
    )

    hysteresis = policy.get(
        "hysteresis",
        {},
    )

    entry_score = hysteresis.get(
        "entry_score"
    )

    release_score = hysteresis.get(
        "release_score"
    )

    if (
        isinstance(entry_score, (int, float))
        and isinstance(
            release_score,
            (int, float),
        )
        and release_score >= entry_score
    ):
        errors.append(
            "regulation_policy.hysteresis."
            "release_score must be lower than "
            "entry_score"
        )

    formation_history = instance.get(
        "formation_history",
        {},
    )

    recent_transition_count = (
        formation_history.get(
            "recent_transition_count"
        )
    )

    transition_rate_limit = policy.get(
        "transition_rate_limit",
        {},
    )

    maximum_transitions = (
        transition_rate_limit.get(
            "maximum_transitions"
        )
    )

    decision = instance.get(
        "regulation_decision",
        {},
    )

    action = decision.get("action")

    if (
        isinstance(
            recent_transition_count,
            int,
        )
        and isinstance(
            maximum_transitions,
            int,
        )
        and recent_transition_count
        >= maximum_transitions
        and action == "allow_transition"
    ):
        errors.append(
            "regulation_decision.action cannot be "
            "'allow_transition' when the transition "
            "rate limit has been reached"
        )

    emergency_override = instance.get(
        "emergency_override",
        {},
    )

    override_active = emergency_override.get(
        "active"
    )

    override_reason = emergency_override.get(
        "reason"
    )

    override_expires_at = (
        emergency_override.get(
            "expires_at"
        )
    )

    if override_active is True:
        if not override_reason:
            errors.append(
                "emergency_override.reason is required "
                "when emergency override is active"
            )

        if not override_expires_at:
            errors.append(
                "emergency_override.expires_at is "
                "required when emergency override "
                "is active"
            )

    regulation = instance.get(
        "regulation",
        {},
    )

    regulation_status = regulation.get(
        "status"
    )

    if (
        regulation_status == "emergency_override"
        and override_active is not True
    ):
        errors.append(
            "emergency_override.active must be true "
            "when regulation.status is "
            "'emergency_override'"
        )

    if (
        action == "emergency_override"
        and override_active is not True
    ):
        errors.append(
            "emergency_override.active must be true "
            "when regulation_decision.action is "
            "'emergency_override'"
        )

    return errors

BRIDGE_INTENTS: dict[str, set[str]] = {
    "TRACE_RELAY": {
        "preserve_trace",
        "relay_trace",
        "merge_lineage",
    },
    "PRANAYAMA": {
        "cool_compute",
        "pause_cycle",
        "compress_memory",
        "resume_cycle",
    },
    "MULTI_WING": {
        "dispatch_wing",
        "request_analysis",
        "request_verification",
        "request_bridge",
    },
    "BOUNDARY": {
        "boundary_review",
        "enforce_boundary",
    },
    "HUMAN_GATE": {
        "request_human_review",
    },
    "ROYALTY_OS": {
        "register_value_event",
        "allocate_value",
    },
}


def validate_field_memory_bridge(
    instance: dict[str, Any],
) -> list[str]:
    errors: list[str] = []

    try:
        distribution = (
            instance["wuxing_residue"]
            ["phase_distribution"]
        )
    except (KeyError, TypeError):
        distribution = None

    if isinstance(distribution, dict):
        errors.extend(
            validate_distribution_sum(
                distribution,
                "wuxing_residue.phase_distribution",
            )
        )

    source_context = instance.get(
        "source_context",
        {},
    )

    source_ref_count = 0

    if isinstance(source_context, dict):
        for refs in source_context.values():
            if isinstance(refs, list):
                source_ref_count += len(refs)

    if source_ref_count == 0:
        errors.append(
            "source_context must contain at least "
            "one source reference"
        )

    propagation = instance.get(
        "propagation",
        {},
    )

    mode = propagation.get("mode")
    radius_hops = propagation.get(
        "radius_hops"
    )
    relay_required = propagation.get(
        "relay_required"
    )

    if mode == "none":
        if radius_hops != 0:
            errors.append(
                "propagation.radius_hops must be 0 "
                "when propagation.mode is 'none'"
            )

        if relay_required is True:
            errors.append(
                "propagation.relay_required must be "
                "false when propagation.mode is 'none'"
            )

    bridge_routes = instance.get(
        "bridge_routes",
        [],
    )

    seen_targets: set[str] = set()

    for index, route in enumerate(bridge_routes):
        if not isinstance(route, dict):
            continue

        target = route.get("target")
        intent = route.get("intent")

        if isinstance(target, str):
            if target in seen_targets:
                errors.append(
                    f"bridge_routes.{index}.target "
                    f"duplicates target '{target}'"
                )

            seen_targets.add(target)

        allowed_intents = BRIDGE_INTENTS.get(
            target,
            set(),
        )

        if (
            isinstance(intent, str)
            and allowed_intents
            and intent not in allowed_intents
        ):
            errors.append(
                f"bridge_routes.{index}.intent "
                f"'{intent}' is not valid for "
                f"target '{target}'"
            )

    governance = instance.get(
        "governance",
        {},
    )

    human_gate_required = governance.get(
        "human_gate_required"
    )

    if (
        human_gate_required is True
        and "HUMAN_GATE" not in seen_targets
    ):
        errors.append(
            "a HUMAN_GATE bridge route is required "
            "when governance.human_gate_required "
            "is true"
        )

    value_flow = instance.get(
        "value_flow",
        {},
    )

    generated_value = value_flow.get(
        "generated_value"
    )

    value_event_ref = value_flow.get(
        "value_event_ref"
    )

    royalty_hook_required = value_flow.get(
        "royalty_hook_required"
    )

    if generated_value is False:
        if value_event_ref is not None:
            errors.append(
                "value_flow.value_event_ref must be "
                "null when generated_value is false"
            )

        if royalty_hook_required is True:
            errors.append(
                "value_flow.royalty_hook_required "
                "cannot be true when generated_value "
                "is false"
            )

    if royalty_hook_required is True:
        if "ROYALTY_OS" not in seen_targets:
            errors.append(
                "a ROYALTY_OS bridge route is required "
                "when royalty_hook_required is true"
            )

        if value_event_ref is None:
            errors.append(
                "value_flow.value_event_ref is required "
                "when royalty_hook_required is true"
            )

    lineage = instance.get(
        "lineage",
        {},
    )

    mutation_type = lineage.get(
        "mutation_type"
    )

    parent_trace_refs = lineage.get(
        "parent_trace_refs",
        [],
    )

    if (
        mutation_type == "origin"
        and len(parent_trace_refs) > 0
    ):
        errors.append(
            "lineage.parent_trace_refs must be empty "
            "when mutation_type is 'origin'"
        )

    if (
        mutation_type != "origin"
        and len(parent_trace_refs) == 0
    ):
        errors.append(
            "lineage.parent_trace_refs must contain "
            "at least one reference for non-origin "
            "mutation types"
        )

    return errors

VALIDATION_TARGETS: list[
    tuple[
        str,
        Path,
        Path,
        ValidationFunction,
    ]
] = [
    (
        "Kazene Field State Beacon",
        ROOT
        / "schemas"
        / "field-state-beacon.schema.json",
        ROOT
        / "examples"
        / "field-state-beacon.example.yaml",
        validate_field_state_beacon,
    ),
    (
        "Kazene Local Pressure Observation",
        ROOT
        / "schemas"
        / "local-pressure-observation.schema.json",
        ROOT
        / "examples"
        / "local-pressure-observation.example.yaml",
        validate_local_pressure_observation,
    ),
    (
        "Kazene Formation Transition Record",
        ROOT
        / "schemas"
        / "formation-transition-record.schema.json",
        ROOT
        / "examples"
        / "formation-transition-record.example.yaml",
        validate_formation_transition,
    ),
    (
    "Kazene Yajirobe Regulation Record",
    ROOT
    / "schemas"
    / "yajirobe-regulation-record.schema.json",
    ROOT
    / "examples"
    / "yajirobe-regulation-record.example.yaml",
    validate_yajirobe_regulation,
),
    (
    "Kazene Field Memory Bridge Record",
    ROOT
    / "schemas"
    / "field-memory-bridge-record.schema.json",
    ROOT
    / "examples"
    / "field-memory-bridge-record.example.yaml",
    validate_field_memory_bridge,
),
]


def validate_target(
    title: str,
    schema_path: Path,
    example_path: Path,
    custom_validator: ValidationFunction,
) -> bool:
    print(f"[validate] {title}")
    print(
        f"  schema : "
        f"{schema_path.relative_to(ROOT)}"
    )
    print(
        f"  example: "
        f"{example_path.relative_to(ROOT)}"
    )

    schema = load_json(schema_path)
    instance = load_yaml(example_path)

    Draft202012Validator.check_schema(
        schema
    )

    validator = Draft202012Validator(
        schema,
        format_checker=(
            Draft202012Validator.FORMAT_CHECKER
        ),
    )

    schema_errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: list(
            error.absolute_path
        ),
    )

    custom_errors = custom_validator(
        instance
    )

    has_errors = False

    for error in schema_errors:
        has_errors = True

        print(
            f"Error: "
            f"{format_path(error.absolute_path)}: "
            f"{error.message}",
            file=sys.stderr,
        )

    for message in custom_errors:
        has_errors = True

        print(
            f"Error: {message}",
            file=sys.stderr,
        )

    if has_errors:
        return False

    print(
        f"[ok] {example_path.name} is valid"
    )

    return True


def main() -> int:
    try:
        all_valid = True

        for (
            title,
            schema_path,
            example_path,
            custom_validator,
        ) in VALIDATION_TARGETS:
            valid = validate_target(
                title,
                schema_path,
                example_path,
                custom_validator,
            )

            if not valid:
                all_valid = False

    except (
        FileNotFoundError,
        ValueError,
        json.JSONDecodeError,
        yaml.YAMLError,
        SchemaError,
    ) as exc:
        print(
            f"[fatal] {exc}",
            file=sys.stderr,
        )

        return 1

    return 0 if all_valid else 1


if __name__ == "__main__":
    raise SystemExit(main())
