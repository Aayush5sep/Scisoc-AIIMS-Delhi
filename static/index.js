//nav
document.addEventListener('DOMContentLoaded', () => {

  // Get all "navbar-burger" elements
  const $navbarBurgers = Array.prototype.slice.call(document.querySelectorAll('.navbar-burger'), 0);

  // Add a click event on each of them
  $navbarBurgers.forEach( el => {
    el.addEventListener('click', () => {

      // Get the target from the "data-target" attribute
      const target = el.dataset.target;
      const $target = document.getElementById(target);

      // Toggle the "is-active" class on both the "navbar-burger" and the "navbar-menu"
      el.classList.toggle('is-active');
      $target.classList.toggle('is-active');

    });
  });
});
//Animations

let tl=gsap.timeline({
  scrollTrigger:{
    trigger:".spacer",
    start:"top top",
    end:"bottom bottom",
    toggleActions:"restart none none reset"
  }
});
tl.from(".x1",{y:-300,opacity:0,duration:1})
.from(".y1",{x:-200,opacity:0,duration:1.5},"-=1");
//swiper

var swiper = new Swiper(".slide-content", {
  slidesPerView: 3,
  spaceBetween: 15,
  loop: true,
  centerSlide: 'true',
  fade: 'true',
  grabCursor: 'true',
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
    dynamicBullets: true,
  },
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },

  breakpoints:{
      0: {
          slidesPerView: 1.1,
      },
      520: {
          slidesPerView: 2,
      },
      950: {
          slidesPerView: 3.1,
      },
  },
});