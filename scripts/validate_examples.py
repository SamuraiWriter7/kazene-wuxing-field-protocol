from __future__ import annotations

import json
import math
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator
from jsonschema.exceptions import SchemaError


ROOT = Path(__file__).resolve().parents[1]

SCHEMA_PATH = (
    ROOT / "schemas" / "field-state-beacon.schema.json"
)

EXAMPLE_PATH = (
    ROOT / "examples" / "field-state-beacon.example.yaml"
)

WUXING_KEYS = (
    "wood",
    "fire",
    "earth",
    "metal",
    "water",
)

WUXING_SUM_TOLERANCE = 1e-6


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = json.load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a JSON object.")

    return data


def load_yaml(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        data = yaml.safe_load(file)

    if not isinstance(data, dict):
        raise ValueError(f"{path} must contain a YAML mapping.")

    return data


def validate_wuxing_sum(instance: dict[str, Any]) -> list[str]:
    errors: list[str] = []

    try:
        potentials = instance["phase_state"]["wuxing_potential"]
        total = sum(float(potentials[key]) for key in WUXING_KEYS)
    except (KeyError, TypeError, ValueError) as exc:
        return [f"Unable to calculate Wuxing potential sum: {exc}"]

    if not math.isclose(
        total,
        1.0,
        rel_tol=0.0,
        abs_tol=WUXING_SUM_TOLERANCE,
    ):
        errors.append(
            "phase_state.wuxing_potential must sum to 1.0 "
            f"(actual: {total:.12f})"
        )

    return errors


def format_path(error_path: Any) -> str:
    parts = [str(part) for part in error_path]
    return ".".join(parts) if parts else "<root>"


def main() -> int:
    print("[validate] Kazene Field State Beacon")
    print(f"  schema : {SCHEMA_PATH.relative_to(ROOT)}")
    print(f"  example: {EXAMPLE_PATH.relative_to(ROOT)}")

    try:
        schema = load_json(SCHEMA_PATH)
        instance = load_yaml(EXAMPLE_PATH)

        Draft202012Validator.check_schema(schema)

    except (
        FileNotFoundError,
        ValueError,
        json.JSONDecodeError,
        yaml.YAMLError,
        SchemaError,
    ) as exc:
        print(f"[fatal] {exc}", file=sys.stderr)
        return 1

    validator = Draft202012Validator(
        schema,
        format_checker=Draft202012Validator.FORMAT_CHECKER,
    )

    schema_errors = sorted(
        validator.iter_errors(instance),
        key=lambda error: list(error.absolute_path),
    )

    custom_errors = validate_wuxing_sum(instance)

    has_errors = False

    for error in schema_errors:
        has_errors = True
        path = format_path(error.absolute_path)
        print(
            f"Error: {path}: {error.message}",
            file=sys.stderr,
        )

    for message in custom_errors:
        has_errors = True
        print(
            f"Error: {message}",
            file=sys.stderr,
        )

    if has_errors:
        return 1

    print(
        "[ok] field-state-beacon.example.yaml is valid"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
