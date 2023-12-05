// Check browser support
if ('speechSynthesis' in window) {
    const speechSynthesis = window.speechSynthesis;

    // Create a new SpeechSynthesisUtterance
    const message = new SpeechSynthesisUtterance('This is a test message.');

    // Set voice, rate, volume, etc.

    // Start speech synthesis
    speechSynthesis.speak(message);
} else {
    // Browser doesn't support speech synthesis
}

// 