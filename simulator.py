###This is original Baldur's Gate character probability simulator.
from power_builds import *

# Generate minimum stat character by forcing minimal rolls
def get_minimum_legal_character(*classes):
    roll_class = None
    for cls in create_character(*classes).__class__.mro():
        if 'roll' in cls.__dict__:
            roll_class = cls
            break

    if roll_class is None:
        raise AttributeError("No class defines `roll()`")

    original_roll = roll_class.roll
    try:
        roll_class.roll = lambda self: 3
        return create_character(*classes)
    finally:
        roll_class.roll = original_roll

# Point pool calculation
def compute_point_pool(character, min_character):
    return sum(
        getattr(character, attr) - getattr(min_character, attr)
        for attr in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    )

def points_needed_for_build(power_build, min_character):
    return sum(
        max(0, power_build[attr] - getattr(min_character, attr))
        for attr in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
        if attr in power_build
    )

# Simulate rerolls and success rate
def simulate_power_build(power_build, classes, attempts=1000):
    min_char = get_minimum_legal_character(*classes)
    required_points = points_needed_for_build(power_build, min_char)

    print("\n=== Minimum legal character ===")
    min_char.display()
    print(f"Points needed to meet build: {required_points}\n")

    is_warrior = any(issubclass(cls, WARRIOR_CLASSES) for cls in classes)
    exceptional_required = power_build.get("exceptional_strength", None)

    success_count = 0

    for _ in range(attempts):
        rolled_char = create_character(*classes)

        # Check exceptional strength if required
        if is_warrior and exceptional_required is not None:
            actual_suffix = getattr(rolled_char, "exceptional_strength", 0)
            if actual_suffix is None or actual_suffix < exceptional_required:
                continue  # Fail immediately, re-roll

        # Check point pool
        pool = compute_point_pool(rolled_char, min_char)
        if pool >= required_points:
            success_count += 1

    print(f"Simulation result: {success_count}/{attempts} builds succeeded.")
    print(f"Success rate: {success_count / attempts * 100:.2f}%\n")

# Define which classes are Warriors (they may use exceptional strength)
WARRIOR_CLASSES = (Fighter, Paladin, Ranger)

#Validate your build
def validate_power_build(power_build, classes):
    warrior_classes = {Fighter, Ranger, Paladin}
    is_warrior = any(cls in warrior_classes for cls in classes)
    strength = power_build.get("strength")
    suffix = power_build.get("exceptional_strength")
    
    required_stats = ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']
    missing = [stat for stat in required_stats if stat not in power_build]
    if missing:
        raise ValueError(f"Power build is missing attributes: {', '.join(missing)}.")

    #Warrior-specific validations
    if is_warrior:
        if strength == 18 and suffix is None:
            raise ValueError("Warrior build with strength 18 must specify an 'exceptional_strength' suffix.")
        if strength != 18 and suffix is not None:
            raise ValueError("Warrior build with strength < 18 should NOT specify an 'exceptional_strength' suffix.")
    else:
        if suffix is not None:
            raise ValueError("Non-Warrior build should not include 'exceptional_strength'.")

    #Minimum legal character for validation
    min_char = get_minimum_legal_character(*classes)

    #Stat-by-stat legality check
    for attr in ['strength', 'dexterity', 'constitution', 'intelligence', 'wisdom', 'charisma']:
        min_val = getattr(min_char, attr)
        build_val = power_build.get(attr, 0)
        if build_val < min_val:
            raise ValueError(f"Power build error: {attr.capitalize()}={build_val} is less than minimum legal value {min_val}.")

    print("Power build validation passed.")


# Menu to pick and simulate
if __name__ == "__main__":
    print("Available builds:")
    for i, name in enumerate(POWER_BUILDS.keys(), 1):
        print(f"{i}. {name}")

    try:
        choice = int(input("Select a build by number: ")) - 1
        build_name = list(POWER_BUILDS.keys())[choice]
        selected = POWER_BUILDS[build_name]

        # Run validation before simulation
        validate_power_build(selected["build"], selected["classes"])

        simulate_power_build(selected["build"], selected["classes"], attempts=100)

    except ValueError as ve:
        print(f"Validation Error: {ve}")
    except IndexError:
        print("Invalid selection number.")
    except Exception as e:
        print(f"Unexpected error: {e}")

