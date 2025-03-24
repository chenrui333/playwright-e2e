export interface Flashcard {
  id: number;
  question: string;
  description: string;
  example: string;
  solution: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  tags: string[];
}
