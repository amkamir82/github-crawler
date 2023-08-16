import importlib
from services.config import parser
import json


def run():
    result = []
    repo_owner = "telegramdesktop"
    repo_name = "tdesktop"
    ok = {"repo_owner": repo_owner, "repo_name": repo_name}

    config = parser.parse()
    for module_name in config:
        for function in config[module_name]:
            module = importlib.import_module(f"GitHub.retriever.{module_name}")
            function_to_call = getattr(module, function)
            data = function_to_call({"repo_owner": repo_owner, "repo_name": repo_name})
            # print(data)
            if module_name not in ok.keys():
                ok[module_name] = {}
            ok[module_name][function[4::]] = data
        result.append(ok)
        with open("file.json", "w") as file:
            aha = json.dumps(result)
            file.write(aha)


if __name__ == "__main__":
    run()
