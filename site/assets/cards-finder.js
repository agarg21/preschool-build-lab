(() => {
  const controls = document.querySelector(".card-finder-controls");
  const grid = document.querySelector(".library-grid");
  const query = document.querySelector("#card-finder-query");
  const clear = document.querySelector("#card-finder-clear");
  const count = document.querySelector("#card-finder-count");
  const empty = document.querySelector("#card-finder-empty");
  if (!controls || !grid || !query || !clear || !count || !empty) return;

  const words = (value) => {
    const tokens = value.toLocaleLowerCase().replace(/['\u2019]s\b/gu, "").match(/[\p{L}\p{N}]+/gu) || [];
    return tokens.map((word) => word.length > 3 && word.endsWith("s") && !word.endsWith("ss") ? word.slice(0, -1) : word);
  };
  const cards = [...grid.querySelectorAll(".mini-card")].map((link) => ({
    link,
    search: new Set(words(link.querySelector("template")?.dataset.search || "")),
  }));

  const update = () => {
    const terms = words(query.value);
    let shown = 0;
    for (const card of cards) {
      const match = terms.every((term) => card.search.has(term));
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
