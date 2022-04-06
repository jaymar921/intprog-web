function confirm_password(password, confirm_password){
    if(password== confirm_password){
        postFunction();
        location.href="/login";
    }else{
        window.alert("password doesn't match!");
        document.getElementById("flag").value = "deny";
    }
}

function postFunction(){
    var ajax = new XMLHttpRequest();
    var data = document.getElementById("registration_form");
    var formData = new FormData(data);
    ajax.open("POST","/register_account", true);
    ajax.send(formData);
}