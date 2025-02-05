const name = document.getElementById('name-container').getAttribute('data-name');
  // console.log(name);

function validEmail(email){
  let pattern = /^[a-zA-Z][a-zA-Z0-9]*@\w+(?:\.\w+)+/; 
    return pattern.test(email);
}
function validPass(password) {
    if (password.length > 6) {
        let firstchar = false, lower = false,upper = false, digit = false, special = false;

        if (password[0] === '_' || /[a-zA-Z]/.test(password[0])) {
            firstchar = true;
        } else {
            return false;
        }

        for (let i = 0; i < password.length; i++) {
            let x = password[i];
            if (/[a-z]/.test(x)) {
                lower = true;
            }
            if (/[0-9]/.test(x)) {
                digit = true;
            }
            if (/[A-Z]/.test(x)) {
                upper = true;
            }
            if (!/[a-zA-Z0-9]/.test(x)) {
                special = true;
            }
        }

        if (firstchar && lower && upper && digit && special) {
            return true;
        }
    }
    return false;
}
 function btnClicked() {
  let password = document.getElementsByClassName('password')[0].value;
     // console.log(password);
  let email = document.getElementsByClassName('email')[0].value;
     // console.log(email);
  if (email == "" || password == ""){  
      event.preventDefault();
      document.querySelector(`.invalid`).innerHTML = "All fields are required";
  }
  else{   
      if(!validEmail(email)){
        event.preventDefault();
         document.querySelector(`.invalid`).innerHTML = "Invalid Email";
      }
      else if(!validPass(password)){
        event.preventDefault();
        document.querySelector(`.invalid`).innerHTML = "Invalid Password";
       }
      else if(name == "signup"){
          let conpass = document.getElementsByClassName('Confirm')[0].value;
          if (password != conpass){
              event.preventDefault();
              document.querySelector(`.invalid`).innerHTML = "Password not a match";
          }    
      }
  }    
} 
