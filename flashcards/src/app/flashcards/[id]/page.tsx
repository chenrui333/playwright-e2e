import { getFlashcards, getFlashcardById } from '@/app/utils/flashcards';
import FlashcardComponent from '@/app/components/FlashcardComponent';
import Link from 'next/link';
import { notFound } from 'next/navigation';

interface FlashcardPageProps {
  params: {
    id: string;
  };
}

export function generateStaticParams() {
  const flashcards = getFlashcards();

  return flashcards.map((card) => ({
    id: card.id.toString(),
  }));
}

export default function FlashcardPage({ params }: FlashcardPageProps) {
  const flashcardId = parseInt(params.id);
  const flashcard = getFlashcardById(flashcardId);
  const flashcards = getFlashcards();

  if (!flashcard) {
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

        <FlashcardComponent
          flashcard={flashcard}
          total={flashcards.length}
        />
      </div>
    </div>
  );
}
