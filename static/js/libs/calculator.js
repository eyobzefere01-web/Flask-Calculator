export class App {

  constructor (){
    this.display=document.getElementById('display');
    this.arguments_='';
  };

  nBtn(e){//number Btn handler
    this.display.value+=e;
  };

  oBtn(e){//operator Btn handler
    if (['+', '-', '*', '/'].includes(this.display.value.slice(-1))){
      return null;
    }else{
      this.display.value+=e;
    };
  };

  rBtn(){//result Btn handler
    try {
      let result=eval(this.display.value);//the calculated value

      if (!isFinite(result)){//Error:something divided by  0
        this.display.value='Err:(n/0) is invalid.';
        return null;
      }else{
        this.arguments_=this.display.value;
        this.display.value=result;

        //Send 2 important info to flask server that will going be save in to the Database
        (async () => {
          const sendingRoute=await fetch('/save_to_database',{
            method:'POST',
            headers:{'Content-Type': 'application/json'},
            body:JSON.stringify({
              arguments: this.arguments_,
              result: result
            })
          });
          const sendIt=await sendingRoute.json();
        })();
      };  
    } catch (error) {
      this.display.value='Err';
    };
    
  };

  fcBtn(){//full clear Btn handler
    this.display.value='';
  };

  pcBtn(){//partial clear handler
    this.display.value=String(this.display.value).slice(0, -1);
  };

  hBtn(){//history Btn handler
    window.location.href ='/history';
  };

  eBtn(){
    window.location.href='/export'
  }
};