import React, { useRef, useState } from "react";
import Canvas from "./Canvas";
import API from "../services/api";
const Hero = () => {
  const [prediction, setPrediction] = useState(null);
  const predictDigit = async () => {
    const canvas = canvasRef.current;

    canvas.toBlob(async (blob) => {
      const formData = new FormData();

      formData.append("image", blob, "digit.png");

      try {
        const response = await API.post("/predict", formData);

        setPrediction(response.data.prediction);
      } catch (error) {
        console.log(error);
        alert("Prediction Failed");
      }
    });
  };
  const canvasRef = useRef(null);
  const clearCanvas = () => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);
  };
  return (
    <section className="flex justify-center items-center py-12 px-4">
      <div className="w-full max-w-4xl bg-slate-800 rounded-2xl shadow-xl p-8">
        <h2 className="text-3xl font-bold text-white text-center">
          Draw a handwritten digit
        </h2>
        <p className="text-slate-400 text-center mt-3">
          Draw any digit from 0 to 9 and let AI to predict it.
        </p>
        <div className="mt-10 flex justify-center">
          <div className="w-[320px] h-80 bg-white rounded-xl border-4 border-slate-700 flex items-center justify-center">
            <p className="text-gray-500">
              <Canvas canvasRef={canvasRef} />
            </p>
          </div>
        </div>
        <div className="flex justify-center gap-4 mt-8">
          <button
            onClick={predictDigit}
            className="bg-blue-600 hover:bg-blue-700 px-6 py-3 rounded-lg text-white font-semibold transition"
          >
            Predict
          </button>

          <button
            onClick={clearCanvas}
            className="bg-red-600 hover:bg-red-700 px-6 py-3 rounded-lg text-white font-semibold transition"
          >
            Clear
          </button>
          <div className="mt-10 text-center">
            <h2 className="text-2xl text-white font-semibold">
              Prediction:
              <span className="text-green-400 ml-3">
                {prediction !== null ? prediction : "--"}
              </span>
            </h2>
          </div>
        </div>
      </div>
    </section>
  );
};

export default Hero;
