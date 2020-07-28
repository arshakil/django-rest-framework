All Request Are Post Request, you can check via postman

<!-- Register User -->
Endpoint: http://127.0.0.1:8000/auth/register/

{
    "email":"azizur.rahman363410@gmail.com",
    "username":"shakil3",
    "password":"shakil363410445"
}
<!-- Login -->
LoginEnd  http://127.0.0.1:8000/auth/login/

{
    "email":"azizur.rahman363410@gmail.com",
    "username":"shakil3",
    "password":"shakil363410445"
}

<!-- Reset Password -->
PassResetEnd http://127.0.0.1:8000/auth/request-reset-email/
{
    "email":"azizur.rahman363410@gmail.com"
}

<!-- Set New Password -->
New PasswordEnd http://127.0.0.1:8000/auth/password-reset-complete/

{
    "password": "shakil36341044",
    "token": "5ih-dcc8f92fd5f12257f403",
    "uidb64": "MjU"
    
}
