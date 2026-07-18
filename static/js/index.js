import {App} from './libs/calculator.js'
import { Disable } from './libs/disable_zoom_events.js';

const thekiller= new Disable();

//Basic menu icon controller
document.addEventListener('DOMContentLoaded', () => {
  const menuToggle = document.getElementById('menu-toggle');
  const mainHeader = document.getElementById('main-header');

  menuToggle.addEventListener('click', () => {
    mainHeader.classList.toggle('active');

    // menu rotator (a bit fun)
    if (mainHeader.classList.contains('active')) {
      menuToggle.style.transform = 'rotate(90deg) scale(1.1)';
    } else {
      menuToggle.style.transform = 'rotate(0deg) scale(1)';
    };
  });
});

window.app = new App();

//disable some events
window.addEventListener('wheel', thekiller.mouseKiller, { passive: false })
window.addEventListener('keydown', thekiller.keyboardKiller)
window.addEventListener('touchstart', thekiller.touchKiller, { passive: false })
window.addEventListener('touchend', thekiller.doubleTabKiller, { passive: false })
