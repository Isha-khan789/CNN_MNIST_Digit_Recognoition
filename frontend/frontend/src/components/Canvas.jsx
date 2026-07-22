import { useEffect, useRef } from "react";

const Canvas = ({ canvasRef }) => {
  // Tracks whether the user is currently drawing
  const isDrawing = useRef(false);

  // Set up the canvas when the component loads
  useEffect(() => {
    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    // White background
    ctx.fillStyle = "white";
    ctx.fillRect(0, 0, canvas.width, canvas.height);

    // Drawing settings
    ctx.strokeStyle = "black";
    ctx.lineWidth = 10;
    ctx.lineCap = "round";
    ctx.lineJoin = "round";
  }, []);

  // Start drawing
  const startDrawing = (e) => {
    isDrawing.current = true;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    ctx.beginPath();
    ctx.moveTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
  };

  // Draw while moving the mouse
  const draw = (e) => {
    if (!isDrawing.current) return;

    const canvas = canvasRef.current;
    const ctx = canvas.getContext("2d");

    ctx.lineTo(e.nativeEvent.offsetX, e.nativeEvent.offsetY);
    ctx.stroke();
  };

  // Stop drawing
  const stopDrawing = () => {
    isDrawing.current = false;
  };

  return (
    <canvas
      ref={canvasRef}
      width={300}
      height={300}
      onMouseDown={startDrawing}
      onMouseMove={draw}
      onMouseUp={stopDrawing}
      onMouseLeave={stopDrawing}
      className="bg-white border-4 border-slate-600 rounded-xl shadow-lg cursor-crosshair"
    />
  );
};

export default Canvas;
