export class Disable{

  constructor (){
    this.lastTouchEnd = 0;
  }

  mouseKiller=(e)=>{
    if (e.ctrlKey || e.metaKey) {
      e.preventDefault();
    }
  };

  keyboardKiller=(e)=>{
    if (e.ctrlKey || e.metaKey) {
      const zoomKeys = ['+', '-', '=', '0', 'NumpadAdd', 'NumpadSubtract', 'Numpad0'];
      if (zoomKeys.includes(e.key) || zoomKeys.includes(e.code)) {
        e.preventDefault();
      };
    };
  };

  touchKiller=(e)=>{
    if (e.touches.length > 1) {
      e.preventDefault();
    };
  };

  doubleTabKiller=(e)=>{
    const now = Date.now();
    if (now - this.lastTouchEnd <= 300) {
      e.preventDefault();
    };
    this.lastTouchEnd=now;
  };
}