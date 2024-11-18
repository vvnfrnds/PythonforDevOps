environments = ["dev","stage","prod"]

def deploy_env(env):
    print(f"deploy to the {env} server")

for env in environments:
    deploy_env(env)