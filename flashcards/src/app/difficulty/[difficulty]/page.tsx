import Link from 'next/link';
import { getFlashcardsByDifficulty, getAllDifficulties } from '@/app/utils/flashcards';
import { Flashcard } from '@/app/types';
import { notFound } from 'next/navigation';

interface DifficultyPageProps {
  params: {
    difficulty: string;
  };
}

export function generateStaticParams() {
  const difficulties = getAllDifficulties();

  return difficulties.map((difficulty) => ({
    difficulty: difficulty.toLowerCase(),
  }));
}

export default function DifficultyPage({ params }: DifficultyPageProps) {
  const difficultyParam = params.difficulty;
  let difficulty: Flashcard['difficulty'];

  if (difficultyParam.toLowerCase() === 'easy') {
    difficulty = 'Easy';
  } else if (difficultyParam.toLowerCase() === 'medium') {
    difficulty = 'Medium';
  } else if (difficultyParam.toLowerCase() === 'hard') {
    difficulty = 'Hard';
  } else {
    notFound();
    return null; // This is just to satisfy TypeScript
  }

  const flashcards = getFlashcardsByDifficulty(difficulty);

  const getDifficultyColor = () => {
    switch (difficulty) {
      case 'Easy':
        return 'bg-green-100 text-green-800';
      case 'Medium':
        return 'bg-yellow-100 text-yellow-800';
      case 'Hard':
        return 'bg-red-100 text-red-800';
      default:
        return 'bg-gray-100 text-gray-800';
    }
  };

  return (
    <div className="min-h-screen bg-gray-50 py-8">
      <div className="max-w-6xl mx-auto px-4">
        <div className="mb-6">
          <Link
            href="/"
            className="text-blue-600 hover:text-blue-800 flex items-center"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5 mr-1"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M10 19l-7-7m0 0l7-7m-7 7h18"
              />
            </svg>
            Back to All Flashcards
          </Link>
        </div>

        <header className="mb-12">
          <h1 className="text-3xl font-bold text-gray-900 mb-2">
            <span className={`px-3 py-1 rounded-lg inline-block mr-2 ${getDifficultyColor()}`}>
              {difficulty}
            </span>
            Difficulty Flashcards
          </h1>
          <p className="text-xl text-gray-600">
            Showing {flashcards.length} flashcards with {difficulty} difficulty
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {flashcards.map((card: Flashcard) => (
            <Link key={card.id} href={`/flashcards/${card.id}`}>
              <div className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow h-full flex flex-col">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-xl font-bold">{card.question}</h3>
                  <span className={`px-3 py-1 rounded-full text-sm font-semibold ml-2 ${getDifficultyColor()}`}>
                    {card.difficulty}
                  </span>
                </div>

                <p className="text-gray-600 mb-4 line-clamp-3">{card.description}</p>

                <div className="mt-auto flex flex-wrap gap-2">
                  {card.tags.map((tag) => (
                    <span
                      key={`${card.id}-${tag}`}
                      className="bg-gray-100 text-gray-600 px-2 py-1 rounded text-sm"
                    >
                      {tag}
                    </span>
                  ))}
                </div>
              </div>
            </Link>
          ))}
        </div>
      </div>
    </div>
  );
}
