document.addEventListener("DOMContentLoaded", function () {
  // Your script here
  console.log("DOM fully loaded and parsed");
  const cards = document.querySelectorAll(".card");
  cards.forEach((card) => {
    const el = card.querySelector(".preview");
    const playBtnEl = el.querySelector(".btnPlay");
    const pauseBtnEl = el.querySelector(".btnPause");
    const audioEl = el.querySelector("audio");

    playBtnEl.addEventListener("click", () => {
      audioEl.play();
      pauseBtnEl.classList.remove("hidden");
      playBtnEl.classList.add("hidden");
    });
    pauseBtnEl.addEventListener("click", () => {
      audioEl.pause();
      playBtnEl.classList.remove("hidden");
      pauseBtnEl.classList.add("hidden");
    });
  });
});
