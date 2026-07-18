import { Disable } from "./disable_zoom_events.js";

const thekiller=new Disable();

//to go back
document.addEventListener('keydown', function (event) {
  if (event.altKey && event.key === 'ArrowLeft') {
    event.preventDefault();
    window.history.back();
  }
});

//disable some events
window.addEventListener('wheel', thekiller.mouseKiller, { passive: false })
window.addEventListener('keydown', thekiller.keyboardKiller)
window.addEventListener('touchstart', thekiller.touchKiller, { passive: false })
window.addEventListener('touchend', thekiller.doubleTabKiller, { passive: false })