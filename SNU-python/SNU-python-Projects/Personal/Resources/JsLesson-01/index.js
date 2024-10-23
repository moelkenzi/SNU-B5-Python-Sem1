// let open = document.getElementsByClassName(".signup_form");
// let open = document.addEventListener("click", formOpen);

const formOpenBtn = document.querySelector('#form-open');
    home = document.querySelector('.home');
    formContainer = document.querySelector('.form_container');
    formCloseBtn = document.querySelector('.form_close');
    signupBtn = document.querySelector('#signup');
    loginBtn = document.querySelector('#login');
    // pwShowHide = document.querySelector('.pw_hide');
    // singUp = document.querySelector('#signup_1')

formOpenBtn.addEventListener("click", () => home.ClassList.add("show"));
formCloseBtn.addEventListener("click", () => home.ClassList.remove("show"));

signupBtn.addEventListener("click", (e) => {
    e.preventDefault()
    formContainer.ClassList.add("active")
});

loginBtn.addEventListener("click", (e) => {
    e.preventDefault()
    formContainer.ClassList.remove("active")
});

singUp.addEventlistener('click', (e) => {
    e.preventDefault()
    formContainer.ClassList.add("active")
});


