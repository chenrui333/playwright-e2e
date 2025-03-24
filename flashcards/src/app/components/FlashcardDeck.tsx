'use client';

import { useState, useRef, useEffect } from 'react';
import { Flashcard } from '../types';
import ReactMarkdown from 'react-markdown';

interface FlashcardDeckProps {
  initialFlashcards: Flashcard[];
}

export default function FlashcardDeck({ initialFlashcards }: FlashcardDeckProps) {
  const [flashcards] = useState(initialFlashcards);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isFlipped, setIsFlipped] = useState(false);
  const cardRef = useRef<HTMLDivElement>(null);
  const startX = useRef(0);
  const currentX = useRef(0);

  const currentCard = flashcards[currentIndex];

  const handleTouchStart = (e: React.TouchEvent) => {
    startX.current = e.touches[0].clientX;
  };

  const handleTouchMove = (e: React.TouchEvent) => {
    if (!cardRef.current) return;

    currentX.current = e.touches[0].clientX;
    const diffX = currentX.current - startX.current;

    // Limit the card movement
    if (Math.abs(diffX) < 150) {
      cardRef.current.style.transform = `translateX(${diffX}px) rotate(${diffX * 0.05}deg)`;
    }
  };

  const handleTouchEnd = () => {
    if (!cardRef.current) return;

    const diffX = currentX.current - startX.current;

    // Reset card position
    cardRef.current.style.transition = 'transform 0.3s ease';

    if (diffX > 100 && currentIndex > 0) {
      // Swiped right - go to previous card
      setCurrentIndex(currentIndex - 1);
      setIsFlipped(false);
    } else if (diffX < -100 && currentIndex < flashcards.length - 1) {
      // Swiped left - go to next card
      setCurrentIndex(currentIndex + 1);
      setIsFlipped(false);
    } else {
      // Not enough movement - return to center
      cardRef.current.style.transform = 'translateX(0) rotate(0)';
    }
  };

  // Reset card transition after changing cards
  useEffect(() => {
    if (cardRef.current) {
      cardRef.current.style.transition = 'none';
      cardRef.current.style.transform = 'translateX(0) rotate(0)';

      // Add a small delay to ensure transition is reset
      setTimeout(() => {
        if (cardRef.current) {
          cardRef.current.style.transition = 'transform 0.3s ease';
        }
      }, 50);
    }
  }, [currentIndex]);

  const handleCardClick = () => {
    setIsFlipped(!isFlipped);
  };

  const handleNextCard = () => {
    if (currentIndex < flashcards.length - 1) {
      setCurrentIndex(currentIndex + 1);
      setIsFlipped(false);
    }
  };

  const handlePrevCard = () => {
    if (currentIndex > 0) {
      setCurrentIndex(currentIndex - 1);
      setIsFlipped(false);
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

  if (!currentCard) {
    return (
      <div className="flex justify-center items-center h-64 w-full">
        <p className="text-gray-600">No flashcards available</p>
      </div>
    );
  }

  return (
    <div className="w-full max-w-md mx-auto">
      <div className="mb-3 text-center text-sm text-gray-500">
        Swipe left/right or use buttons to navigate • Card {currentIndex + 1} of {flashcards.length}
      </div>

      <div
        ref={cardRef}
        className={`relative w-full bg-white rounded-xl shadow-lg overflow-hidden ${
          isFlipped ? 'bg-blue-50' : ''
        }`}
        style={{
          minHeight: '450px',
          perspective: '1000px',
          transformStyle: 'preserve-3d',
          transition: 'transform 0.3s ease'
        }}
        onClick={handleCardClick}
        onTouchStart={handleTouchStart}
        onTouchMove={handleTouchMove}
        onTouchEnd={handleTouchEnd}
      >
        <div
          className="absolute inset-0 w-full h-full p-6 transition-transform duration-500 ease-in-out backface-hidden"
          style={{
            backfaceVisibility: 'hidden',
            transform: isFlipped ? 'rotateY(-180deg)' : 'rotateY(0)',
          }}
        >
          <div className="flex justify-between items-start mb-4">
            <h2 className="text-2xl font-bold text-gray-900">{currentCard.question}</h2>
            <span className={`px-3 py-1 rounded-full text-sm font-semibold ${getDifficultyColor(currentCard.difficulty)}`}>
              {currentCard.difficulty}
            </span>
          </div>

          <div className="flex flex-wrap gap-2 mb-4">
            {currentCard.tags.map((tag) => (
              <span key={tag} className="bg-gray-100 text-gray-700 px-2 py-1 rounded-md text-sm">
                {tag}
              </span>
            ))}
          </div>

          <p className="text-gray-700 mb-4">{currentCard.description}</p>

          <div className="mb-4">
            <h3 className="font-semibold mb-1">Example:</h3>
            <pre className="bg-gray-100 p-3 rounded-lg text-sm whitespace-pre-wrap">{currentCard.example}</pre>
          </div>

          <div className="absolute bottom-4 left-0 right-0 text-center text-sm text-gray-500">
            Tap to see solution
          </div>
        </div>

        <div
          className="absolute inset-0 w-full h-full p-6 transition-transform duration-500 ease-in-out overflow-auto"
          style={{
            backfaceVisibility: 'hidden',
            transform: isFlipped ? 'rotateY(0)' : 'rotateY(180deg)',
          }}
        >
          <h2 className="text-2xl font-bold text-gray-900 mb-4">Solution</h2>

          <div className="solution-code prose max-w-none">
            <ReactMarkdown>{currentCard.solution}</ReactMarkdown>
          </div>

          <div className="absolute bottom-4 left-0 right-0 text-center text-sm text-gray-500">
            Tap to see question
          </div>
        </div>
      </div>

      <div className="mt-6 flex justify-between">
        <button
          onClick={handlePrevCard}
          disabled={currentIndex <= 0}
          className={`py-2 px-4 rounded-lg ${
            currentIndex <= 0
              ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
              : 'bg-gray-800 text-white hover:bg-gray-700'
          }`}
        >
          Previous
        </button>

        <button
          onClick={handleNextCard}
          disabled={currentIndex >= flashcards.length - 1}
          className={`py-2 px-4 rounded-lg ${
            currentIndex >= flashcards.length - 1
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
