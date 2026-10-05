# ============================================
# ASSOCIATIVE MEMORY NETWORK
# Auto-Associative + Hetero-Associative
# ============================================

# --------------------------------------------
# TRAINING DATA
# --------------------------------------------

# Auto-associative memory
# Input and output are the same

auto_memory = [
    "APPLE",
    "BANANA",
    "ORANGE",
    "PYTHON",
    "COLLEGE",
    "STUDENT",
    "MACHINE",
    "NETWORK",
    "ENGINEERING",
    "COMPUTER"
]


# Hetero-associative memory
# Input and output are different

hetero_memory = {
    "APPLE": "FRUIT",
    "BANANA": "FRUIT",
    "ORANGE": "FRUIT",
    "DOG": "ANIMAL",
    "CAT": "ANIMAL",
    "LION": "ANIMAL",
    "CAR": "VEHICLE",
    "BUS": "VEHICLE",
    "TRAIN": "VEHICLE",
    "PYTHON": "PROGRAMMING LANGUAGE",
    "JAVA": "PROGRAMMING LANGUAGE"
}


# --------------------------------------------
# FUNCTION TO CONVERT WORD INTO NUMBERS
# --------------------------------------------

def word_to_vector(word):

    word = word.upper()

    vector = []

    for character in word:

        # Convert A-Z into numbers 1-26
        value = ord(character) - ord('A') + 1

        vector.append(value)

    return vector


# --------------------------------------------
# FUNCTION TO CALCULATE SIMILARITY
# --------------------------------------------

def calculate_similarity(input_word, stored_word):

    input_word = input_word.upper()
    stored_word = stored_word.upper()

    # Find the maximum length
    max_length = max(len(input_word), len(stored_word))

    matches = 0

    # Compare characters at the same position
    for i in range(min(len(input_word), len(stored_word))):

        if input_word[i] == stored_word[i]:
            matches += 1

    # Convert matches into percentage
    similarity = (matches / max_length) * 100

    return similarity


# --------------------------------------------
# AUTO-ASSOCIATIVE MEMORY
# --------------------------------------------

def auto_associative(input_word):

    best_word = None
    best_similarity = 0

    for stored_word in auto_memory:

        similarity = calculate_similarity(
            input_word,
            stored_word
        )

        if similarity > best_similarity:

            best_similarity = similarity
            best_word = stored_word

    return best_word, best_similarity


# --------------------------------------------
# HETERO-ASSOCIATIVE MEMORY
# --------------------------------------------

def hetero_associative(input_word):

    best_word = None
    best_similarity = 0

    for stored_word in hetero_memory:

        similarity = calculate_similarity(
            input_word,
            stored_word
        )

        if similarity > best_similarity:

            best_similarity = similarity
            best_word = stored_word

    if best_word is not None:

        associated_output = hetero_memory[best_word]

        return best_word, associated_output, best_similarity

    return None, None, 0


# --------------------------------------------
# MAIN PROGRAM
# --------------------------------------------

while True:

    print("\n======================================")
    print("     ASSOCIATIVE MEMORY NETWORK")
    print("======================================")

    print("1. Auto-Associative Memory")
    print("2. Hetero-Associative Memory")
    print("3. Exit")

    choice = input("\nEnter your choice: ")

    # ----------------------------------------
    # AUTO-ASSOCIATIVE
    # ----------------------------------------

    if choice == "1":

        print("\n--- AUTO-ASSOCIATIVE MEMORY ---")

        print("\nStored Patterns:")

        for word in auto_memory:
            print(word)

        user_input = input(
            "\nEnter a word or noisy word: "
        )

        user_input = user_input.upper()

        result, similarity = auto_associative(
            user_input
        )

        print("\nInput Pattern   :", user_input)

        print("Recalled Pattern:", result)

        print("Similarity      :", round(similarity, 2), "%")

        if similarity >= 50:

            print("\nMemory successfully recalled!")

        else:

            print("\nPattern not recognized clearly.")


    # ----------------------------------------
    # HETERO-ASSOCIATIVE
    # ----------------------------------------

    elif choice == "2":

        print("\n--- HETERO-ASSOCIATIVE MEMORY ---")

        print("\nStored Associations:")

        for word, category in hetero_memory.items():

            print(word, "→", category)

        user_input = input(
            "\nEnter a word: "
        )

        user_input = user_input.upper()

        result, output, similarity = hetero_associative(
            user_input
        )

        print("\nInput Pattern     :", user_input)

        print("Matched Pattern   :", result)

        print("Associated Output :", output)

        print("Similarity        :", round(similarity, 2), "%")


    # ----------------------------------------
    # EXIT
    # ----------------------------------------

    elif choice == "3":

        print("\nProgram terminated.")

        break

    else:

        print("\nInvalid choice. Please enter 1, 2 or 3.")