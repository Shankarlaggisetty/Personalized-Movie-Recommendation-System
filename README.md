# Movie Recommendation System

A content-based movie recommendation system built with Python that suggests movies based on user preferences using natural language processing techniques and sentiment analysis.

## Features

- **Content-Based Filtering**: Uses cosine similarity to match user preferences with movie profiles
- **Sentiment Analysis**: Basic rule-based sentiment analysis for movie reviews
- **Text Processing**: Term frequency calculation and similarity metrics
- **In-Memory Database**: Sample movie database with reviews and metadata

## Technical Implementation

### Core Components

1. **Movie Profiling**
   - Movie metadata (title, overview, genres)
   - Review aggregation and sentiment analysis
   - Text-based similarity matching

2. **Recommendation Engine**
   - Cosine similarity calculation
   - Term frequency analysis
   - Content-based filtering algorithm

3. **Sentiment Analysis**
   - Rule-based sentiment classification
   - Positive/Neutral/Negative categorization
   - Review text processing

## Usage

```python
# Example usage
user_preferences = "I love sci-fi movies with deep philosophical themes and amazing visual effects"
recommendations = get_movie_recommendations(user_preferences)
```

### Running the System

```bash
python3 movie_recommender.py
```

## Project Structure

```
.
├── movie_recommender.py    # Main recommendation system
├── src/                    # React frontend components
│   ├── App.tsx            # Main application component
│   ├── components/        # UI components
│   └── types.ts           # TypeScript interfaces
```

## Functions

### `get_movie_recommendations(user_preferences, n=2)`
Returns movie recommendations based on user preferences.
- `user_preferences`: String containing user's movie preferences
- `n`: Number of recommendations to return (default: 2)

### `analyze_sentiment(text)`
Performs sentiment analysis on review text.
- `text`: Review text to analyze
- Returns: "positive", "negative", or "neutral"

### `calculate_cosine_similarity(text1, text2)`
Calculates similarity between two text strings.
- `text1`, `text2`: Texts to compare
- Returns: Similarity score between 0 and 1

## Sample Output

```
Movie Recommendation System
--------------------------------------------------
User Preferences: I love sci-fi movies with deep philosophical themes and amazing visual effects

Recommended Movies:

1. The Matrix
   Similarity Score: 0.75
   Overview: A computer programmer discovers a mysterious world of artificial reality.
   Genres: sci-fi, action

2. Inception
   Similarity Score: 0.65
   Overview: A thief who enters the dreams of others to steal secrets.
   Genres: sci-fi, action, thriller
```

## Future Enhancements

- Integration with external movie databases
- Advanced NLP using machine learning models
- Collaborative filtering implementation
- User profile management
- Review database expansion
- Real-time recommendation updates

## Technical Notes

- Built with pure Python (no external dependencies)
- Uses in-memory data structures for demonstration
- Implements basic NLP techniques
- Includes TypeScript types for frontend integration
