'use client';

import { useState } from 'react';
import { Flashcard } from '../types';
import { useRouter } from 'next/navigation';
import ReactMarkdown from 'react-markdown';

interface FlashcardComponentProps {
  flashcard: Flashcard;
  total: number;
}

export default function FlashcardComponent({ flashcard, total }: FlashcardComponentProps) {
  const [isFlipped, setIsFlipped] = useState(false);
  const router = useRouter();

  const handleFlip = () => {
    setIsFlipped(!isFlipped);
  };

  const navigateToPrevious = () => {
    if (flashcard.id > 1) {
      router.push(`/flashcards/${flashcard.id - 1}`);
    }
  };

  const navigateToNext = () => {
    if (flashcard.id < total) {
      router.push(`/flashcards/${flashcard.id + 1}`);
    }
  };

  const getDifficultyColor = (difficulty: string) => {
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
    <div className="w-full max-w-4xl mx-auto">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-xl font-semibold">Flashcard {flashcard.id} of {total}</h2>
        <button
          onClick={handleFlip}
          className="bg-blue-500 hover:bg-blue-600 text-white font-medium py-2 px-4 rounded-lg"
        >
          {isFlipped ? 'Show Question' : 'Show Solution'}
        </button>
      </div>

      <div
        className={`relative w-full h-[500px] rounded-xl shadow-lg transition-all duration-500 ${
          isFlipped ? 'transform rotate-y-180' : ''
        }`}
        style={{
          perspective: '1000px',
          transformStyle: 'preserve-3d',
        }}
      >
        {/* Front side - Question */}
        <div
          className={`absolute w-full h-full bg-white rounded-xl p-8 backface-hidden ${
            isFlipped ? 'hidden' : ''
          }`}
        >
          <div className="flex justify-between mb-4">
            <h1 className="text-2xl font-bold">{flashcard.question}</h1>
            <span className={`px-3 py-1 rounded-full text-sm font-semibold ${getDifficultyColor(flashcard.difficulty)}`}>
              {flashcard.difficulty}
            </span>
          </div>

          <p className="text-gray-700 mb-6 text-lg">{flashcard.description}</p>

          <div className="mb-6">
            <h3 className="font-semibold mb-2">Example:</h3>
            <pre className="bg-gray-100 p-4 rounded-lg whitespace-pre-wrap">{flashcard.example}</pre>
          </div>

          <div className="flex flex-wrap gap-2 mt-auto">
            {flashcard.tags.map((tag) => (
              <span key={tag} className="bg-gray-200 text-gray-700 px-2 py-1 rounded-md text-sm">
                {tag}
              </span>
            ))}
          </div>
        </div>

        {/* Back side - Solution */}
        <div
          className={`absolute w-full h-full bg-white rounded-xl p-8 ${
            isFlipped ? '' : 'hidden'
          }`}
          style={{
            transform: 'rotateY(180deg)',
            backfaceVisibility: 'hidden',
          }}
        >
          <h2 className="text-2xl font-bold mb-4">Solution</h2>
          <div className="solution-code prose max-w-none overflow-auto h-[380px]">
            <ReactMarkdown>{flashcard.solution}</ReactMarkdown>
          </div>
        </div>
      </div>

      <div className="flex justify-between mt-6">
        <button
          onClick={navigateToPrevious}
          disabled={flashcard.id <= 1}
          className={`py-2 px-4 rounded-lg ${
            flashcard.id <= 1
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-gray-800 text-white hover:bg-gray-700'
          }`}
        >
          Previous
        </button>
        <button
          onClick={navigateToNext}
          disabled={flashcard.id >= total}
          className={`py-2 px-4 rounded-lg ${
            flashcard.id >= total
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-gray-800 text-white hover:bg-gray-700'
          }`}
        >
          Next
        </button>
      </div>
    </div>
  );
}
