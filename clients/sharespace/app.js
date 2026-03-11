const API = "http://localhost:5000";

async function loadSources(type = "") {
  const url = type ? `${API}/api/sources?type=${type}` : `${API}/api/sources`;
  const res = await fetch(url);
  const data = await res.json();
  const grid = document.getElementById("grid");
  grid.innerHTML = data.sources.map(s => `
    <div class="card">
      ${s.thumbnail ? `<img src="${s.thumbnail}" alt="${s.title}"/>` : ""}
      <h3>${s.title}</h3>
      <p>${s.description || ""}</p>
      <span class="badge">${s.type}</span>
      <a href="${s.url}" target="_blank">▶ Open</a>
    </div>
  `).join("");
}

async function addSource() {
  const body = {
    id: document.getElementById("s-id").value,
    title: document.getElementById("s-title").value,
    type: document.getElementById("s-type").value,
    url: document.getElementById("s-url").value,
    thumbnail: document.getElementById("s-thumb").value,
    description: document.getElementById("s-desc").value,
    tags: document.getElementById("s-tags").value.split(",").map(t => t.trim())
  };
  const res = await fetch(`${API}/api/sources`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(body)
  });
  const data = await res.json();
  document.getElementById("add-status").textContent =
    res.ok ? `✅ "${data.source.title}" added!` : `❌ Error: ${data.error}`;
  if (res.ok) loadSources();
}

loadSources();
