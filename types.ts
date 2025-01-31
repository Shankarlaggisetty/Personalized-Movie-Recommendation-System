export interface Movie {
  id: string;
  title: string;
  overview: string;
  posterUrl: string;
  rating: number;
  genres: string[];
  releaseYear: number;
}

export interface Review {
  id: string;
  movieId: string;
  text: string;
  rating: number;
  sentiment: 'positive' | 'neutral' | 'negative';
  timestamp: string;
}

export interface MovieRecommendation {
  movie: Movie;
  similarity: number;
}