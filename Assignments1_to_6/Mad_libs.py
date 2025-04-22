print("\n=== Simple Mad Libs ===")
noun = input("Enter a noun: ")
adj = input("Enter an adjective: ")
verb = input("Enter a past tense verb: ")
animal = input("Enter an animal: ")

story = (
    f"\nOne {adj} day, a {noun} decided to {verb} "
    f"with a {animal}. They became best friends and "
    "lived happily ever after. The end!\n"
)

print(story)