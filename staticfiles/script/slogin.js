function login(){
    email=document.getElementById('email').value
    password=document.getElementById('password').value
    if (email==""|| password==""){
        document.getElementById('message').innerHTML="please enter your email and password "
        return false

    }
    else{
        return true
    }
    

}