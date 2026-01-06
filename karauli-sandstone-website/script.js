/* ===============================
   AOS SCROLL ANIMATIONS
================================ */
AOS.init({
  duration: 1200,
  easing: "ease-in-out",
  once: true
});

/* ===============================
   PREMIUM CARD HOVER GLOW
================================ */
document.querySelectorAll('.card').forEach(card => {
  card.addEventListener('mouseenter', () => {
    card.style.boxShadow = "0 20px 40px rgba(212,175,55,0.25)";
    card.style.transform = "translateY(-8px)";
  });

  card.addEventListener('mouseleave', () => {
    card.style.boxShadow = "none";
    card.style.transform = "translateY(0)";
  });
});

/* ===============================
   CINEMATIC HERO PARALLAX (SAFE)
================================ */
const heroTitle = document.querySelector(".hero h1");
const heroText  = document.querySelector(".hero p");

if (heroTitle && heroText) {
  window.addEventListener("scroll", () => {
    const scrollValue = window.scrollY;

    heroTitle.style.transform =
      `translateY(${scrollValue * 0.15}px)`;

    heroText.style.transform =
      `translateY(${scrollValue * 0.25}px)`;
  });
}
