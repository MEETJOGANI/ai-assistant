import multiprocessing
import traceback

def startJarvis():
    try:
        print("🔵 Process 1: Starting Jarvis...")
        from main import start
        start()
    except Exception as e:
        print("❌ Error in startJarvis:")
        traceback.print_exc()

def listenHotword():
    try:
        print("🟢 Process 2: Starting hotword detection...")
        from backend.feature import hotword
        hotword()
    except Exception as e:
        print("❌ Error in listenHotword:")
        traceback.print_exc()

if __name__ == "__main__":
    print("⚙️ Starting multiprocessing for Jarvis...")

    process1 = multiprocessing.Process(target=startJarvis)
    process2 = multiprocessing.Process(target=listenHotword)

    process1.start()
    process2.start()

    process1.join()

    # After main Jarvis process finishes
    if process2.is_alive():
        print("🛑 Terminating hotword detection...")
        process2.terminate()
        process2.join()

    print("✅ System is terminated.")
