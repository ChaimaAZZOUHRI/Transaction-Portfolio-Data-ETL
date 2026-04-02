import subprocess
import sys
from pathlib import Path


def run_step(script_name: str, description: str) -> None:
    print(f"\n=== Running: {description} ===")
    result = subprocess.run([sys.executable, script_name], check=False)
    if result.returncode != 0:
        raise SystemExit(f"Step failed: {script_name} (exit code {result.returncode})")


def main() -> None:
    project_dir = Path(__file__).resolve().parent
    scripts = [
        ("step1_exploration.py", "Step 1 - Exploration"),
        ("step2_cleaning.py", "Step 2 - Cleaning"),
        ("step3_features_export.py", "Step 3 - Feature engineering"),
        ("step4_export.py", "Step 4 - Final export"),
    ]

    for script_name, description in scripts:
        script_path = project_dir / script_name
        if not script_path.exists():
            raise FileNotFoundError(f"Missing script: {script_path}")
        run_step(str(script_path), description)

    print("\n=== Pipeline completed successfully ===")


if __name__ == "__main__":
    main()
