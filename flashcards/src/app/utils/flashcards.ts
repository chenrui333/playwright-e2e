import fs from 'fs';
import path from 'path';
import yaml from 'js-yaml';
import { Flashcard } from '../types';

export function getFlashcards(): Flashcard[] {
  try {
    const filePath = path.join(process.cwd(), 'src', 'app', 'flashcards.yaml');
    const fileContents = fs.readFileSync(filePath, 'utf8');
    const flashcards = yaml.load(fileContents) as Flashcard[];
    return flashcards;
  } catch (error) {
    console.error('Error loading flashcards:', error);
    return [];
  }
}

export function getFlashcardById(id: number): Flashcard | undefined {
  const flashcards = getFlashcards();
  return flashcards.find(card => card.id === id);
}

export function getFlashcardsByTag(tag: string): Flashcard[] {
  const flashcards = getFlashcards();
  return flashcards.filter(card => card.tags.includes(tag));
}

export function getFlashcardsByDifficulty(difficulty: Flashcard['difficulty']): Flashcard[] {
  const flashcards = getFlashcards();
  return flashcards.filter(card => card.difficulty === difficulty);
}

export function getAllTags(): string[] {
  const flashcards = getFlashcards();
  const tagsSet = new Set<string>();

  flashcards.forEach(card => {
    card.tags.forEach(tag => tagsSet.add(tag));
  });

  return Array.from(tagsSet);
}

export function getAllDifficulties(): Flashcard['difficulty'][] {
  return ['Easy', 'Medium', 'Hard'];
}
