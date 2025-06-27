from src.main.server.server import app

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=4500, debug=True)