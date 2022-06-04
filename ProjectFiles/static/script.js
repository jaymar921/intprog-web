document.getElementById("password").addEventListener("invalid", myFunction);
function myFunction() {
  document.getElementById("invalid_pass").style.display = 'block';
}


function confirm_password(password, confirm_password){
    if(password!= confirm_password){
        window.alert("password doesn't match!");
        document.getElementById("flag").value = "deny";
    }
}
