from flask import Flask, jsonify, request
from flask_cors import CORS
import json, os

app = Flask(__name__)
CORS(app)

SOURCES_FILE = os.path.join(os.path.dirname(__file__), "sources.json")

def load_sources():
    with open(SOURCES_FILE, "r") as f:
        return json.load(f).get("sources", [])

@app.route("/api/sources", methods=["GET"])
def get_sources():
    sources = load_sources()
    media_type = request.args.get("type")
    tag = request.args.get("tag")
    if media_type:
        sources = [s for s in sources if s.get("type") == media_type]
    if tag:
        sources = [s for s in sources if tag in s.get("tags", [])]
    return jsonify({"sources": sources})

@app.route("/api/sources/<source_id>", methods=["GET"])
def get_source(source_id):
    sources = load_sources()
    match = next((s for s in sources if s["id"] == source_id), None)
    if not match:
        return jsonify({"error": "Not found"}), 404
    return jsonify(match)

@app.route("/api/sources", methods=["POST"])
def add_source():
    new_source = request.get_json()
    required = ["id", "title", "type", "url"]
    if not all(k in new_source for k in required):
        return jsonify({"error": f"Missing required fields: {required}"}), 400
    with open(SOURCES_FILE, "r+") as f:
        data = json.load(f)
        data["sources"].append(new_source)
        f.seek(0)
        json.dump(data, f, indent=2)
    return jsonify({"status": "added", "source": new_source}), 201

if __name__ == "__main__":
    app.run(debug=True, port=5000)
