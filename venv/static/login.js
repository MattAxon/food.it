

$(document).ready(function(){
    usernameInput = $('#usernameInput');
    passwordInput = $('#passwordInput');
    submitBtn = $('#submitBtn');
    submitBtn.click(function(){
        submitBtnClicked();
    });
});
// ////







 
/////////


function submitBtnClicked(){
    username = usernameInput.val();
    password = passwordInput.val();
    var dataToSend = {
        'username': username,
        'password': password
    }

    $.ajax({
        method: 'POST',
        url: 'login',
        type: 'json',
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(dataToSend),
        success: function(result){
            console.log(result);
        },
        error: function(error){
            console.log(error);
        }
    })

}

