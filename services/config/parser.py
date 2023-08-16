import copy
import config


def parse():
    repo_configs = copy.deepcopy(config.CONFIG)
    for repo_config in repo_configs.keys():
        repo_configs[repo_config] = [f"get_{item}" for item in repo_configs[repo_config]]

    return repo_configs
