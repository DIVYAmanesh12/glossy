function sign(){
    name1=document.getElementById('name1').value
    email=document.getElementById('email').value
    mob=document.getElementById('mob').value
    password=document.getElementById('password').value
    confirmpassword=document.getElementById('cpswd').value
    if (name1==""||email==""||mob== ""||confirmpassword==""){
        document.getElementById('message').innerHTML="enter details"
        return false
    }
    else if(password==confirmpassword){
        document.getElementById('message').innerHTML='match'
        return true
    }
    else{
        document.getElementById('message').innerHTML='password doesnt match'
        return false
    }
}