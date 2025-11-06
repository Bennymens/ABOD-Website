document.addEventListener("DOMContentLoaded", function () {
  const container = document.querySelector(".design-cards");
  const prev = document.querySelector(".design-prev");
  const next = document.querySelector(".design-next");
  if (!container || !prev || !next) return;

  // Determine an appropriate scroll amount: either the card width or a portion of
  // the container width. Prefer card width when available.
  function getScrollAmount() {
    const card = container.querySelector(".design-card");
    if (card) {
      return Math.round(card.getBoundingClientRect().width + 28); // include gap
    }
    return Math.round(container.clientWidth * 0.8);
  }

  function updateButtons() {
    // Disable prev when at left-most, disable next when at right-most
    const maxScrollLeft = container.scrollWidth - container.clientWidth - 1;
    prev.disabled = container.scrollLeft <= 2;
    next.disabled = container.scrollLeft >= maxScrollLeft;
  }

  prev.addEventListener("click", function (e) {
    const amt = getScrollAmount();
    container.scrollBy({ left: -amt, behavior: "smooth" });
    setTimeout(updateButtons, 300);
  });

  next.addEventListener("click", function (e) {
    const amt = getScrollAmount();
    container.scrollBy({ left: amt, behavior: "smooth" });
    setTimeout(updateButtons, 300);
  });

  // Support keyboard arrow keys when the container is focused
  container.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") {
      e.preventDefault();
      prev.click();
    } else if (e.key === "ArrowRight") {
      e.preventDefault();
      next.click();
    }
  });

  // Update buttons on scroll and resize
  container.addEventListener("scroll", function () {
    // tiny debounce
    if (this._updating) return;
    this._updating = true;
    setTimeout(() => {
      updateButtons();
      this._updating = false;
    }, 120);
  });
  window.addEventListener("resize", updateButtons);

  // Initial state
  updateButtons();

  // Make controls visible only when JS is active (optional)
  document.body.classList.add("design-carousel-ready");
});
