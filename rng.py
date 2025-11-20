import random

def get_comment(percent: int) -> str:
    """Return a comment based on the percentage."""
    if percent == 0:
        return "No homo detected at all."
    elif percent <= 20:
        return "Straight mode: mostly active."
    elif percent <= 40:
        return "A little bit sus, but still chill."
    elif percent <= 60:
        return "Bisexual energy detected."
    elif percent <= 80:
        return "Rainbow aura: pretty strong."
    elif percent < 100:
        return "Full LGBT vibes, proud moment."
    else:  
        return "Certified rainbow overlord."

def main():
    print("=== HOW GAY ARE YOU? (RNG EDITION) ===")
    print("Type 'exit' to close the program.\n")

    while True:
        name = input("Enter your name / friend's name: ").strip()

        if not name:
            print("Name can't be empty. Try again.\n")
            continue

        if name.lower() == "exit":
            print("\nThanks for playing. Goodbye.")
            break

        percent = random.randint(0, 100)
        comment = get_comment(percent)

        print(f"\n{name} is {percent}% gay.")
        print(f"Note: {comment}\n")


if __name__ == "__main__":
    main()
