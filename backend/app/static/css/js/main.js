async function fetchReviews() {
  const res = await fetch('/api/reviews');
  if (!res.ok) throw new Error('Failed to load reviews');
  return await res.json();
}

function reviewCard(r) {
  const div = document.createElement('article');
  div.className = 'card';
  div.innerHTML = `
    <img src="${r.cover_url || ''}" alt="${r.artist} — ${r.album} cover" onerror="this.style.display='none'" />
    <div class="body">
      <h3>${r.artist} — <em>${r.album}</em></h3>
      <div class="meta">
        <span>${new Date(r.created_at).toLocaleDateString()}</span>
        <span class="badge">${r.rating.toFixed(1)}/10</span>
      </div>
      <p>${r.body}</p>
    </div>
  `;
  return div;
}

(async () => {
  const mount = document.getElementById('reviews');
  try {
    const data = await fetchReviews();
    if (data.length === 0) {
      mount.innerHTML = '<p>No reviews yet. Hit <code>/api/seed</code> once for demo data.</p>';
      return;
    }
    data.forEach(r => mount.appendChild(reviewCard(r)));
  } catch (e) {
    mount.innerHTML = `<p> ${e.message}</p>`;
  }
})();