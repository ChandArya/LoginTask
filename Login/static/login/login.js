/**
 * Created by chandan on 3/18/2017.
 */
function formValid() {
       var title=login.head.value;
       var firstname=login.firstname.value;
       var lastname=login.lastname.value;
       var email=login.email.value;
       var pass=login.pass.value;
       var repass=login.repass.value;
       var mobile=login.mobile.value;
       if(title==0)
       {
                  alert("please select Title");
                    return false

       }else if(firstname==null||firstname=="")
       {
            alert("please enter first name");
                    return false

       }else if(lastname==null||lastname=="")
       {
            alert("please enter last name");
                    return false

       }else if(email==null||email=="")
       {
            alert("please enter email");
                    return false

       }else if(pass==null||pass=="")
       {
            alert("please enter password");
                    return false

       }else if(repass==null||repass=="")
       {
            alert("please enter repassword");
                    return false

       }else if(mobile==null||mobile=="")
       {
            alert("please enter mobile no");
                    return false

       }else if(mobile.length!=10)
       {
            alert("please enter valid mobile no");
                    return false

       }else if(pass.length<6){
          alert("password lenth should be more than 6 character");
                    return false

       }
       else if(pass!=repass){
          alert("password and repassword should be same.");
                    return false

       }
       else
       {
        //   document.write("profile successfully created.")
           return true
       }
}
function loginFromValid() {
    // document.write("chahdhdhdhhd")
     var email=abc.email.value;
       var pass=abc.pass.value;
    if(email==null||email=="")
       {
            alert("please enter email");
                    return false

       }else if(pass==null||pass=="")
       {
            alert("please enter password");
                    return false

       }else if(pass.length<6){
          alert("password lenth should be more than 6 character");
                    return false

       }else
       {
        //   document.write("profile successfully created.")
           return false
       }

}