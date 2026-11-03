BOXES = {
    "Sports": "the team won the football match and the crowd cheered the goal "
              "she runs fast in the race and wins the gold medal for the team",
    "Food": "we cook pasta with tomato sauce and the soup is hot "
            "he bakes bread and the cake tastes sweet with cream",
    "Music": "the band plays a loud song and the singer sings with the guitar "
             "she learns the piano and sings a song in the choir",
}
TEST_NOTES = [
    ("the goal won the match", "Sports"),
    ("he bakes the cake and the bread", "Food"),
    ("the singer plays the guitar", "Music"),
    ("pasta with sweet cream", "Food"),
    ("the band wins the match", "Music"),
    ("", "unknown"),
]
THRESHOLD = 0.2
def word_counts(text):
    counts = {}
    return counts
PROFILES = {box: word_counts(text) for box, text in BOXES.items()}
print("PART 1: Word counts")
print(PROFILES["Food"].get("the", 0), PROFILES["Food"].get("goal", 0))
def cosine(a, b):
    return 0.0
print("\nPART 2: Cosine")
print(round(cosine(word_counts("the team"), PROFILES["Sports"]), 2))
def classify(note):
    return "unknown"
print("\nPART 3: Classify")
print(classify("the goal won the match"), "|", classify("zzz"))
print("\nPART 4: Test all notes")
mistakes = 0