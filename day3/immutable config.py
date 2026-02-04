# Screen resolution stored as a tuple (immutable)
screen_res = (1920, 1080)

# Print current resolution
print("Current Resolution:", str(screen_res[0]) + "x" + str(screen_res[1]))


# -------------------------
# The Experiment (will cause error)
# Uncomment this line to test the TypeError
# screen_res[0] = 1280
# -------------------------


# The Fix
print("Tuples cannot be modified!")