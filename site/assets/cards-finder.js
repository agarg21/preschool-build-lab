(() => {
  const controls = document.querySelector(".card-finder-controls");
  const grid = document.querySelector(".library-grid");
  const query = document.querySelector("#card-finder-query");
  const clear = document.querySelector("#card-finder-clear");
  const count = document.querySelector("#card-finder-count");
  const empty = document.querySelector("#card-finder-empty");
  if (!controls || !grid || !query || !clear || !count || !empty) return;

  const cards = [...grid.querySelectorAll(".mini-card")].map((link) => ({
    link,
    search: (link.querySelector("template")?.dataset.search || "").toLocaleLowerCase(),
  }));

  const update = () => {
    const terms = query.value.trim().toLocaleLowerCase().split(/\s+/).filter(Boolean);
    let shown = 0;
    for (const card of cards) {
      const match = terms.every((term) => card.search.includes(term));
      card.link.hidden = !match;
      if (match) shown += 1;
    }
    count.textContent = terms.length
      ? `${shown} of ${cards.length} activity cards`
      : `${cards.length} activity cards`;
    empty.hidden = shown !== 0;
    clear.disabled = query.value.length === 0;
  };

  query.addEventListener("input", update);
  clear.addEventListener("click", () => {
    query.value = "";
    update();
    query.focus();
  });
  update();
  controls.hidden = false;
})();
