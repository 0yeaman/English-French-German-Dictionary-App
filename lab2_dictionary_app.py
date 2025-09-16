# AML 2504 - Lab 2: InterBase Dictionary App
# Author: Amandeep Singh

# English → French → German dictionary
english_to_french = {
    "hello": "bonjour",
    "apple": "pomme",
    "car": "voiture",
    "cat": "chat",
    "black": "noir",
    "dog": "chien",
    "white": "blanc",
    "red": "rouge"
}

french_to_german = {
    "bonjour": "hallo",
    "pomme": "apfel",
    "voiture": "auto",
    "chat": "katze",
    "noir": "schwarz",
    "chien": "hund",
    "blanc": "weiß",
    "rouge": "rot"
}

# Function for PART I
def english_to_german():
    word = input("Enter an English word: ").lower()
    french_word = english_to_french.get(word)
    if french_word:
        german_word = french_to_german.get(french_word)
        if german_word:
            print(f"\n🔸 French: {french_word}")
            print(f"🔸 German: {german_word}\n")
        else:
            print("⚠️ No German translation found.")
    else:
        print("⚠️ Word not found in English-French dictionary.")

# Function for PART II
def rule_based_sentence():
    print("Enter a 2-word phrase (like 'black cat' or 'white car'):")
    phrase = input("→ ").lower().strip()
    words = phrase.split()
    
    if len(words) == 2:
        adj, noun = words[0], words[1]
        french_noun = english_to_french.get(noun)
        french_adj = english_to_french.get(adj)
        if french_noun and french_adj:
            print(f"\n🔸 French: {french_noun} {french_adj} (noun-adjective order)\n")
        else:
            print("⚠️ Word(s) not found in dictionary.")
    else:
        print("⚠️ Please enter exactly two words (adj + noun).")

# Function for PART III explanation
def explain_models():
    print("\n📘 Encoder-Decoder & Attention Explanation:\n")
    print("🔹 Encoder: Processes input sentence and converts it to a context vector.")
    print("   Example: 'I am eating' → [0.3, 0.6, -0.2,...]")
    print("🔹 Decoder: Uses the vector to generate translated sentence step-by-step.")
    print("   Example: Output → 'Je mange'")
    print("\n🔹 Attention: Instead of using one fixed vector, it 'attends' to")
    print("   relevant parts of the input during decoding.")
    print("   Example: For translating 'apple', it focuses on 'apple' from input.")
    print("✅ Improves translation, especially for long/complex sentences.\n")

# Main interactive loop
def main():
    while True:
        print("\n🧠 INTERBASE DICTIONARY APP - AML 2504")
        print("1. Translate English → French → German (Part I)")
        print("2. Rule-Based Sentence Translation (Part II)")
        print("3. Explanation of Encoder-Decoder & Attention (Part III)")
        print("4. Exit")

        choice = input("Select an option (1-4): ")

        if choice == '1':
            english_to_german()
        elif choice == '2':
            rule_based_sentence()
        elif choice == '3':
            explain_models()
        elif choice == '4':
            print("👋 Exiting the app. Goodbye!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

# Run the app
if __name__ == "__main__":
    main()
