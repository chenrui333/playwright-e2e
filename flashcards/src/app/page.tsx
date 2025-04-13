import FlashcardDeck from './components/FlashcardDeck';
import { getFlashcards } from './utils/flashcards';

export default function Home() {
  const flashcards = getFlashcards();

  return (
    <main className="min-h-screen bg-gray-50 flex flex-col items-center py-8 px-4">
      <header className="mb-6 text-center">
        <h1 className="text-3xl font-bold text-gray-900 mb-2">LeetCode Flashcards</h1>
        <p className="text-lg text-gray-600">
          Swipe through problems to memorize solutions
        </p>
      </header>

      <FlashcardDeck initialFlashcards={flashcards} />
    </main>
  );
}
