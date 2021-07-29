
$(document).ready(function(){
    usernameInput = $('#usernameInput');
    passwordInput = $('#passwordInput');
    emailInput = $('#emailInput');
    passwordConfirmationInput = $('#passwordConfirm');
    submitBtn = $('#submitBtn');
    createSubmitBtnEvent();
});

function createSubmitBtnEvent(){
    submitBtn.click(function(){
        username = usernameInput.val();
        password = passwordInput.val();
        email = emailInput.val();
        confirmPassword = passwordConfirmationInput.val();
        if(confirmPassword === password){
            var dataToSend= {
                'username': username,
                'password': password,
                'email': email
            }
            $.ajax({
                method: "POST",
                url: 'registerData',
                type: 'json',
                contentType: "application/json; charset=utf-8",
                data: JSON.stringify(dataToSend),
                success: function(result){
                    console.log(result);
                },
                error: function(error){
                    console.log(error);
                }
            });
        }else{
            alert("passwords don't match");
        }
    });
}
