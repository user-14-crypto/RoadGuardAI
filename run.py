"""
RoadGuard AI — One-click launcher
Starts the FastAPI backend and serves the frontend.
"""

import os
import sys
import webbrowser
import threading

def main():
    # Ensure working directory is the project root
    project_root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(project_root)

    # Add backend to Python path
    backend_dir = os.path.join(project_root, "webapp", "backend")
    sys.path.insert(0, backend_dir)

    # Create required directories
    for d in ["webapp/uploads", "webapp/outputs", "webapp/data"]:
        os.makedirs(d, exist_ok=True)

    import uvicorn
    from main import app  # noqa: E402 — imported after path setup

    host = os.environ.get("HOST", "0.0.0.0")
    port = int(os.environ.get("PORT", 8000))

    print()
    print("=" * 56)
    print("  ◈  RoadGuard AI — Road Damage Detection")
    print("=" * 56)
    print(f"  Server  :  http://localhost:{port}")
    print(f"  Mode    :  {'Production' if os.environ.get('RENDER') else 'Local Development'}")
    print("=" * 56)
    print()

    # Open browser (only locally, not on Render)
    if not os.environ.get("RENDER"):
        threading.Timer(1.5, lambda: webbrowser.open(f"http://localhost:{port}")).start()

    uvicorn.run(app, host=host, port=port, log_level="info")


if __name__ == "__main__":
    main()
