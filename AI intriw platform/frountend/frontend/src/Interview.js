import React, { useEffect, useRef, useState } from "react";
import "./App.css";

function App() {
  const videoRef = useRef(null);
  const recognitionRef = useRef(null);
  const silenceTimerRef = useRef(null);

  const [question, setQuestion] = useState("");
  const [interviewEnded, setInterviewEnded] = useState(false);
  const [finalFeedback, setFinalFeedback] = useState("");
  const [isInterviewActive, setIsInterviewActive] = useState(false);

  useEffect(() => {
    startCamera();

    const SpeechRecognition =
      window.SpeechRecognition || window.webkitSpeechRecognition;

    if (SpeechRecognition) {
      recognitionRef.current = new SpeechRecognition();
      recognitionRef.current.continuous = true;
      recognitionRef.current.interimResults = true;
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
    setIsInterviewActive(true);
    setInterviewEnded(false);
    setFinalFeedback("");

    try {
      const res = await fetch("http://127.0.0.1:8000/api/start/");
      const data = await res.json();

      if (data.question) {
        speakQuestion(data.question);
      }
    } catch (err) {
      console.log("Start Interview Error:", err);
      alert("Backend connection failed");
    }
  };

  // AI Speaks Question
  const speakQuestion = (text) => {
    if (!isInterviewActive) return;

    setQuestion(text);

    window.speechSynthesis.cancel();

    const utterance = new SpeechSynthesisUtterance(text);

    utterance.lang = "en-US";
    utterance.rate = 1;
    utterance.pitch = 1;
    utterance.volume = 1;

    const voices = window.speechSynthesis.getVoices();

    if (voices.length > 0) {
      utterance.voice = voices.find(v => v.lang.includes("en")) || voices[0];
    }

    utterance.onend = () => {
      if (isInterviewActive) {
        listenToStudent();
      }
    };

    window.speechSynthesis.speak(utterance);
  };

  // Listen To Student Answer
  const listenToStudent = () => {
    if (!recognitionRef.current || !isInterviewActive) return;

    let finalTranscript = "";

    clearTimeout(silenceTimerRef.current);

    recognitionRef.current.start();

    recognitionRef.current.onstart = () => {
      console.log("🎤 Mic Started Listening");
    };

    recognitionRef.current.onresult = (event) => {
      console.log("Speech Detected");

      finalTranscript = "";

      for (let i = event.resultIndex; i < event.results.length; i++) {
        finalTranscript += event.results[i][0].transcript + " ";
      }

      console.log("Transcript:", finalTranscript);

      clearTimeout(silenceTimerRef.current);

      silenceTimerRef.current = setTimeout(() => {
        recognitionRef.current.stop();

        if (finalTranscript.trim()) {
          submitAnswer(finalTranscript.trim());
        } else {
          submitAnswer("No Answer");
        }
      }, 3000);
    };

    recognitionRef.current.onerror = (event) => {
      console.log("Speech Recognition Error:", event.error);
    };

    // If user never speaks
    silenceTimerRef.current = setTimeout(() => {
      recognitionRef.current.stop();
      submitAnswer("No Answer");
    }, 3000);
  };

  // Submit Answer
  const submitAnswer = async (spokenAnswer) => {
    if (!isInterviewActive) return;

    try {
      const res = await fetch("http://127.0.0.1:8000/api/submit/", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ answer: spokenAnswer }),
      });

      const data = await res.json();

      if (!isInterviewActive) return;

      if (data.next_question) {
        speakQuestion(data.next_question);
      } else {
        setIsInterviewActive(false);
        setInterviewEnded(true);
        setQuestion("");
        setFinalFeedback(data.feedback_summary);
      }
    } catch (err) {
      console.log("Submit Error:", err);
    }
  };

  // End Interview
  const endInterview = () => {
    setIsInterviewActive(false);

    clearTimeout(silenceTimerRef.current);

    recognitionRef.current?.stop();

    window.speechSynthesis.cancel();

    setQuestion("");
    setInterviewEnded(true);

    setFinalFeedback(
      "Interview Ended Successfully. Improve communication, confidence, and technical depth."
    );
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
        <div className="button-group">
          <button className="start-btn" onClick={startInterview}>
            Start Interview
          </button>

          {isInterviewActive && (
            <button className="end-btn" onClick={endInterview}>
              End Interview
            </button>
          )}
        </div>
      )}

      {question && isInterviewActive && (
        <div className="question-box">
          <h2>{question}</h2>
          <p>🎤 Listening for your answer...</p>
          <small>AI waits until you stop speaking for 3 seconds</small>
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



