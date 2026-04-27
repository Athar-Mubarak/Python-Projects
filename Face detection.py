import cv2
import threading
import time
import numpy as np
from typing import Optional


class AdvancedVisionEngine:
    """
    High-performance threading-based video capture engine.
    Decouples frame acquisition from the processing loop.
    """

    def __init__(self, src: int = 0, width: int = 1280, height: int = 720):
        self.cap = cv2.VideoCapture(src)

        # Optimize hardware parameters
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        self.cap.set(cv2.CAP_PROP_FPS, 60)

        self.grabbed, self.frame = self.cap.read()
        self.running = False
        self.lock = threading.Lock()  # Ensures thread-safe frame access

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop()

    def start(self):
        if self.running:
            return
        self.running = True
        self.thread = threading.Thread(target=self._update_loop, daemon=True)
        self.thread.start()

    def _update_loop(self):
        while self.running:
            grabbed, frame = self.cap.read()
            if not grabbed:
                self.running = False
                break
            with self.lock:
                self.frame = frame
                self.grabbed = grabbed

    def read(self) -> Optional[np.ndarray]:
        with self.lock:
            return self.frame.copy() if self.grabbed else None

    def stop(self):
        self.running = False
        if hasattr(self, 'thread'):
            self.thread.join()
        self.cap.release()
        cv2.destroyAllWindows()


def process_pipeline(frame: np.ndarray) -> np.ndarray:
    """
    Place advanced image processing/AI models here.
    Example: Fast Vectorized Contrast Enhancement using CLAHE.
    """
    # Convert to LAB for better lighting control
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)
    l, a, b = cv2.split(lab)

    # Apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
    cl = clahe.apply(l)

    limg = cv2.merge((cl, a, b))
    return cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)


def main():
    # Configuration
    SRC = 0
    WINDOW_NAME = "Advanced Vision Engine"

    # FPS Smoothing variables
    ema_fps = 0
    alpha = 0.1  # Smoothing factor for FPS
    prev_time = time.perf_counter()

    with AdvancedVisionEngine(src=SRC) as engine:
        print(f"Engine started. Press 'ESC' to exit.")

        while True:
            start_work = time.perf_counter()

            frame = engine.read()
            if frame is None:
                continue

            # --- 1. Processing Stage ---
            # You can swap 'process_pipeline' with a YOLO/Mediapipe model here
            processed = process_pipeline(frame)

            # --- 2. Advanced Metrics Stage ---
            curr_time = time.perf_counter()
            delta_time = curr_time - prev_time
            prev_time = curr_time

            # Division-safe FPS calculation with EMA smoothing
            if delta_time > 0:
                current_fps = 1.0 / delta_time
                ema_fps = (alpha * current_fps) + (1 - alpha) * ema_fps

            work_time_ms = (time.perf_counter() - start_work) * 1000

            # --- 3. UI Overlay ---
            info_text = f"FPS: {int(ema_fps)} | Latency: {work_time_ms:.1f}ms"
            cv2.putText(processed, info_text, (20, 40),
                        cv2.FONT_HERSHEY_DUPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)

            cv2.imshow(WINDOW_NAME, processed)

            # Break on ESC key
            if cv2.waitKey(1) & 0xFF == 27:
                break


if __name__ == "__main__":
    main()