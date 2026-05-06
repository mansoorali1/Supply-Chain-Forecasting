# tests/test_placeholder.py
# Placeholder tests that pass immediately.
# Real tests are added as each src/ module is built.

def test_project_structure():
    """Verify core project files exist."""
    import os
    assert os.path.exists("params.yaml"), "params.yaml must exist"
    assert os.path.exists("requirements.txt"), "requirements.txt must exist"

def test_params_yaml_readable():
    """Verify params.yaml is valid YAML and has required keys."""
    import yaml
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    assert "data" in params
    assert "splits" in params
    assert "features" in params
    assert "sarima" in params
    assert "prophet" in params
    assert "lstm" in params
    assert "optimization" in params
    assert "evaluation" in params
    assert "monitoring" in params
    assert "mlflow" in params

def test_params_critical_values():
    """Verify critical parameter values are sensible."""
    import yaml
    with open("params.yaml", "r") as f:
        params = yaml.safe_load(f)
    assert 0 < params["splits"]["test_size"] < 1
    assert 0 < params["splits"]["validation_size"] < 1
    assert params["splits"]["test_size"] + params["splits"]["validation_size"] < 1
    assert params["optimization"]["service_level_target"] > 0.5
    assert params["lstm"]["min_weeks_required"] >= params["splits"]["walk_forward_initial"]
