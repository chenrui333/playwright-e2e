import Link from 'next/link';
import { getFlashcards, getFlashcardsByTag, getAllTags } from '@/app/utils/flashcards';
import { Flashcard } from '@/app/types';
import { notFound } from 'next/navigation';

interface TagPageProps {
  params: {
    tag: string;
  };
}

export function generateStaticParams() {
  const tags = getAllTags();

  return tags.map((tag) => ({
    tag: tag.toLowerCase(),
  }));
}

export default function TagPage({ params }: TagPageProps) {
  const tag = params.tag.charAt(0).toUpperCase() + params.tag.slice(1);
  const flashcards = getFlashcardsByTag(tag);

  if (flashcards.length === 0) {
    notFound();
  }

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
          <h1 className="text-3xl font-bold text-gray-900 mb-2">Flashcards: {tag}</h1>
          <p className="text-xl text-gray-600">
            Showing {flashcards.length} flashcards with tag "{tag}"
          </p>
        </header>

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
          {flashcards.map((card: Flashcard) => (
            <Link key={card.id} href={`/flashcards/${card.id}`}>
              <div className="bg-white p-6 rounded-xl shadow-md hover:shadow-lg transition-shadow h-full flex flex-col">
                <div className="flex justify-between items-start mb-4">
                  <h3 className="text-xl font-bold">{card.question}</h3>
                  <span className={`
                    px-3 py-1 rounded-full text-sm font-semibold ml-2
                    ${card.difficulty === 'Easy' ? 'bg-green-100 text-green-800' : ''}
                    ${card.difficulty === 'Medium' ? 'bg-yellow-100 text-yellow-800' : ''}
                    ${card.difficulty === 'Hard' ? 'bg-red-100 text-red-800' : ''}
                  `}>
                    {card.difficulty}
                  </span>
                </div>

                <p className="text-gray-600 mb-4 line-clamp-3">{card.description}</p>

                <div className="mt-auto flex flex-wrap gap-2">
                  {card.tags.map((cardTag) => (
                    <span
                      key={`${card.id}-${cardTag}`}
                      className={`px-2 py-1 rounded text-sm ${
                        cardTag === tag
                          ? 'bg-blue-100 text-blue-800 font-semibold'
                          : 'bg-gray-100 text-gray-600'
                      }`}
                    >
                      {cardTag}
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
