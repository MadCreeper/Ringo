def jwt_response_payload_handler(token, user, request):
    return {
        'token':token,
        'uid':user.id,
        'username':user.username,
        'email':user.email
    }