def jwt_response_payload_handler(token, user, request):
    return {
        'token':token,
        ** request.data
    }