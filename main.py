from simulator import simulate_power_build, validate_power_build
from power_builds import POWER_BUILDS

def main():
    print("Available builds:")
    for i, name in enumerate(POWER_BUILDS.keys(), 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Select a build by number: ")) - 1
        build_name = list(POWER_BUILDS.keys())[choice]
        selected = POWER_BUILDS[build_name]

        validate_power_build(selected["build"], selected["classes"])
        simulate_power_build(selected["build"], selected["classes"], attempts=1000)

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
