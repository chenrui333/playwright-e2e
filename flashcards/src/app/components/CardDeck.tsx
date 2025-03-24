'use client';

import { useState } from 'react';
import { Flashcard } from '../types';
import Link from 'next/link';
import { useRouter } from 'next/navigation';

interface CardDeckProps {
  flashcards: Flashcard[];
  initialCardIndex?: number;
}

export default function CardDeck({ flashcards, initialCardIndex = 0 }: CardDeckProps) {
  const [currentCardIndex, setCurrentCardIndex] = useState(initialCardIndex);
  const [isRevealed, setIsRevealed] = useState(false);
  const [hasAnimated, setHasAnimated] = useState(false);
  const router = useRouter();

  const currentCard = flashcards[currentCardIndex];

  const handleCardClick = () => {
    if (!isRevealed) {
      setIsRevealed(true);
      setHasAnimated(true);
    }
  };

  const handleNextCard = () => {
    if (currentCardIndex < flashcards.length - 1) {
      setCurrentCardIndex(currentCardIndex + 1);
      setIsRevealed(false);
      setHasAnimated(false);
    }
  };

  const handlePrevCard = () => {
    if (currentCardIndex > 0) {
      setCurrentCardIndex(currentCardIndex - 1);
      setIsRevealed(false);
      setHasAnimated(false);
    }
  };

  const handleSkip = () => {
    handleNextCard();
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

  if (!currentCard) {
    return (
      <div className="flex flex-col items-center justify-center h-60 bg-white rounded-xl shadow-md p-6">
        <p className="text-xl text-gray-600 mb-4">No flashcards available.</p>
        <Link href="/" className="text-blue-600 hover:text-blue-800">
          Back to Home
        </Link>
      </div>
    );
  }

  return (
    <div className="w-full max-w-xl mx-auto">
      <div className="mb-4 flex justify-between items-center">
        <div className="text-sm font-medium text-gray-500">
          Card {currentCardIndex + 1} of {flashcards.length}
        </div>

        <div className="flex gap-2">
          <button
            onClick={handleSkip}
            className="bg-gray-200 hover:bg-gray-300 text-gray-800 py-1 px-3 rounded-lg text-sm"
          >
            Skip
          </button>

          <Link
            href={`/flashcards/${currentCard.id}`}
            className="bg-blue-100 hover:bg-blue-200 text-blue-800 py-1 px-3 rounded-lg text-sm"
          >
            Full View
          </Link>
        </div>
      </div>

      <div
        className={`relative bg-white rounded-xl shadow-md overflow-hidden transition-all duration-300 ${
          hasAnimated ? 'shadow-lg' : ''
        }`}
        style={{ minHeight: '400px' }}
      >
        <div
          className={`w-full h-full p-6 cursor-pointer transition-opacity duration-300 ${
            isRevealed ? 'opacity-0 absolute inset-0 pointer-events-none' : 'opacity-100'
          }`}
          onClick={handleCardClick}
        >
          <div className="flex justify-between items-start mb-6">
            <h2 className="text-2xl font-bold text-gray-900">{currentCard.question}</h2>
            <span className={`px-3 py-1 rounded-full text-sm font-semibold ${getDifficultyColor(currentCard.difficulty)}`}>
              {currentCard.difficulty}
            </span>
          </div>

          <div className="flex flex-wrap gap-2 mb-6">
            {currentCard.tags.map((tag) => (
              <span key={tag} className="bg-gray-100 text-gray-700 px-2 py-1 rounded-md text-sm">
                {tag}
              </span>
            ))}
          </div>

          <div className="mb-4 flex justify-center items-center h-40 bg-gray-50 rounded-lg">
            <p className="text-gray-500 text-center">Click to reveal question details</p>
          </div>
        </div>

        <div
          className={`w-full h-full p-6 transition-opacity duration-300 ${
            isRevealed ? 'opacity-100' : 'opacity-0 absolute inset-0 pointer-events-none'
          }`}
        >
          <div className="flex justify-between items-start mb-4">
            <h2 className="text-2xl font-bold text-gray-900">{currentCard.question}</h2>
            <span className={`px-3 py-1 rounded-full text-sm font-semibold ${getDifficultyColor(currentCard.difficulty)}`}>
              {currentCard.difficulty}
            </span>
          </div>

          <p className="text-gray-700 mb-4">{currentCard.description}</p>

          <div className="mb-4">
            <h3 className="font-semibold mb-1">Example:</h3>
            <pre className="bg-gray-100 p-3 rounded-lg text-sm whitespace-pre-wrap">{currentCard.example}</pre>
          </div>
        </div>
      </div>

      <div className="mt-6 flex justify-between">
        <button
          onClick={handlePrevCard}
          disabled={currentCardIndex <= 0}
          className={`py-2 px-4 rounded-lg ${
            currentCardIndex <= 0
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-gray-800 text-white hover:bg-gray-700'
          }`}
        >
          Previous
        </button>

        <button
          onClick={handleNextCard}
          disabled={currentCardIndex >= flashcards.length - 1}
          className={`py-2 px-4 rounded-lg ${
            currentCardIndex >= flashcards.length - 1
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
