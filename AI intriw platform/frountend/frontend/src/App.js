import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const videoRef = useRef(null);
  const recognitionRef = useRef(null);

  const [question, setQuestion] = useState("");
  const [interviewEnded, setInterviewEnded] = useState(false);
  const [finalFeedback, setFinalFeedback] = useState("");

  useEffect(() => {
    startCamera();

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = false;
      recognitionRef.current.interimResults = false;
      recognitionRef.current.lang = "en-US";
    } else {
      alert("Speech Recognition not supported in this browser");
    }
  }, []);

  // Start Camera
  const startCamera = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({
        video: true,
        audio: true,
      });

      if (videoRef.current) {
        videoRef.current.srcObject = stream;
      }
    } catch (err) {
      console.log("Camera Error:", err);
    }
  };

  // Start Interview
 const startInterview = async () => {
  try {
    console.log("Start button clicked");

    const res = await fetch("http://127.0.0.1:8000/api/start/");
    console.log("Status:", res.status);

    const data = await res.json();
    console.log("Backend Data:", data);

    if (data.question) {
      speakQuestion(data.question);
    } else {
      alert("Backend did not return question");
    }

  } catch (err) {
    console.error("Start Interview Error:", err);
    alert("Backend connection failed");
  }
};
  // AI Speaks Question
 const speakQuestion = (text) => {
  setQuestion(text);

  window.speechSynthesis.cancel();

  const utterance = new SpeechSynthesisUtterance(text);

  utterance.lang = "en-US";
  utterance.rate = 1;
  utterance.pitch = 1;
  utterance.volume = 1;

  const loadVoicesAndSpeak = () => {
    const voices = window.speechSynthesis.getVoices();

    console.log("Available Voices:", voices);

    if (voices.length > 0) {
      utterance.voice = voices.find(v => v.lang.includes("en")) || voices[0];
    }

    window.speechSynthesis.speak(utterance);
  };

  if (window.speechSynthesis.getVoices().length === 0) {
    window.speechSynthesis.onvoiceschanged = loadVoicesAndSpeak;
  } else {
    loadVoicesAndSpeak();
  }

  utterance.onend = () => {
    listenToStudent();
  };
};

  // Listen To Student
  const listenToStudent = () => {
    if (!recognitionRef.current) return;

    let hasSpoken = false;

    recognitionRef.current.start();

    recognitionRef.current.onresult = (event) => {
      hasSpoken = true;

      const transcript = event.results[0][0].transcript;

      submitAnswer(transcript);
    };

    // Auto Skip If Silent For 3 Sec
    setTimeout(() => {
      if (!hasSpoken) {
        recognitionRef.current.stop();

        submitAnswer("No Answer");
      }
    }, 3000);
  };

  // Submit Answer To Backend
  const submitAnswer = async (spokenAnswer) => {
    try {
      const res = await fetch("http://127.0.0.1:8000/api/submit/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ answer: spokenAnswer }),
      });

      const data = await res.json();

      if (data.next_question) {
        speakQuestion(data.next_question);
      } else {
        setInterviewEnded(true);
        setFinalFeedback(data.feedback_summary);
        setQuestion("");
      }
    } catch (err) {
      console.log("Submit Error:", err);
    }
  };

  return (
    <div className="container">
      <h1>AI Interview Platform</h1>

      <div className="video-layout">
        <div className="card">
          <img
            src="https://images.unsplash.com/photo-1573496359142-b8d87734a5a2"
            alt="Interviewer"
          />
          <p>Interviewer</p>
        </div>

        <div className="card">
          <video ref={videoRef} autoPlay playsInline />
          <p>Student Camera</p>
        </div>
      </div>

      {!interviewEnded && (
        <button className="start-btn" onClick={startInterview}>
          Start Interview
        </button>
      )}

      {question && (
        <div className="question-box">
          <h2>{question}</h2>
          <p>🎤 Listening for student response...</p>
          <small>If no answer in 3 sec, next question will start</small>
        </div>
      )}

      {interviewEnded && (
        <div className="feedback-box">
          <h2>Interview Feedback</h2>
          <p>{finalFeedback}</p>
        </div>
      )}
    </div>
  );
}

export default App;