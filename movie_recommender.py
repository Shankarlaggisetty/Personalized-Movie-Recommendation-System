import json
import math
from collections import defaultdict

# Simple in-memory movie database
movies = {
    "1": {
        "title": "The Matrix",
        "overview": "A computer programmer discovers a mysterious world of artificial reality.",
        "genres": ["sci-fi", "action"]
    },
    "2": {
        "title": "Inception",
        "overview": "A thief who enters the dreams of others to steal secrets.",
        "genres": ["sci-fi", "action", "thriller"]
    },
    "3": {
        "title": "The Dark Knight",
        "overview": "Batman faces his greatest challenge against the Joker.",
        "genres": ["action", "crime", "drama"]
    }
}

# Sample reviews with sentiment
reviews = {
    "1": [
        {"text": "Mind-blowing special effects and deep philosophical themes", "sentiment": "positive"},
        {"text": "Revolutionary sci-fi that changed the genre", "sentiment": "positive"}
    ],
    "2": [
        {"text": "Complex plot with amazing visuals", "sentiment": "positive"},
        {"text": "Sometimes confusing but overall great", "sentiment": "neutral"}
    ],
    "3": [
        {"text": "Heath Ledger's performance is legendary", "sentiment": "positive"},
        {"text": "Dark and intense superhero movie", "sentiment": "positive"}
    ]
}

def calculate_term_frequency(text):
    """Calculate term frequency for text"""
    words = text.lower().split()
    word_count = defaultdict(int)
    for word in words:
        word_count[word] += 1
    return dict(word_count)

def calculate_cosine_similarity(text1, text2):
    """Calculate cosine similarity between two texts"""
    vec1 = calculate_term_frequency(text1)
    vec2 = calculate_term_frequency(text2)
    
    # Find common words
    intersection = set(vec1.keys()) & set(vec2.keys())
    
    # Calculate numerator (dot product)
    numerator = sum(vec1[x] * vec2[x] for x in intersection)
    
    # Calculate denominator (product of magnitudes)
    sum1 = sum(vec1[x]**2 for x in vec1.keys())
    sum2 = sum(vec2[x]**2 for x in vec2.keys())
    denominator = math.sqrt(sum1) * math.sqrt(sum2)
    
    if not denominator:
        return 0.0
    return float(numerator) / denominator

def get_movie_recommendations(user_preferences, n=2):
    """Get movie recommendations based on user preferences"""
    # Combine all reviews for each movie
    movie_profiles = {}
    for movie_id, movie_reviews in reviews.items():
        combined_text = " ".join(review["text"] for review in movie_reviews)
        movie_profiles[movie_id] = combined_text
    
    # Calculate similarity scores
    similarities = []
    for movie_id, profile in movie_profiles.items():
        similarity = calculate_cosine_similarity(user_preferences, profile)
        similarities.append((movie_id, similarity))
    
    # Sort by similarity and return top N recommendations
    similarities.sort(key=lambda x: x[1], reverse=True)
    recommendations = []
    for movie_id, similarity in similarities[:n]:
        movie = movies[movie_id]
        recommendations.append({
            "movie": movie,
            "similarity": similarity
        })
    return recommendations

def analyze_sentiment(text):
    """Simple rule-based sentiment analysis"""
    positive_words = {"great", "amazing", "excellent", "good", "wonderful", "fantastic"}
    negative_words = {"bad", "poor", "terrible", "awful", "horrible"}
    
    words = text.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count > neg_count:
        return "positive"
    elif neg_count > pos_count:
        return "negative"
    return "neutral"

# Example usage
if __name__ == "__main__":
    # Example user preferences
    user_preferences = "I love sci-fi movies with deep philosophical themes and amazing visual effects"
    
    print("Movie Recommendation System")
    print("-" * 50)
    print(f"User Preferences: {user_preferences}")
    print("\nRecommended Movies:")
    
    recommendations = get_movie_recommendations(user_preferences)
    for i, rec in enumerate(recommendations, 1):
        movie = rec["movie"]
        similarity = rec["similarity"]
        print(f"\n{i}. {movie['title']}")
        print(f"   Similarity Score: {similarity:.2f}")
        print(f"   Overview: {movie['overview']}")
        print(f"   Genres: {', '.join(movie['genres'])}")