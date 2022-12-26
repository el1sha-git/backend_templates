from pathlib import Path


def parse_envs_to_dict(path_to_env: Path) -> dict:
    """Parse .env file to dict"""
    with open(path_to_env, "r") as f:
        envs = f.read().splitlines()
    envs = [env.split("=") for env in envs]
    envs = {env[0]: env[1] for env in envs}
    return envs
