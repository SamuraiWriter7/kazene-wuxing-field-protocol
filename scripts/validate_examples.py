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
