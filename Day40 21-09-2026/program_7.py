# Python Program 7: Understand Tokens

# A token is a temporary string used to identify a logged-in user.
#
# Simple authentication flow:
# 1. User sends username and password to the login API.
# 2. The API validates the credentials.
# 3. If the credentials are correct, the API creates a token.
# 4. The API sends the token back to the user.
# 5. The user sends the token with later API requests.
# 6. The API checks the token before allowing access.
#
# Example login response:
# {
#     "message": "Login successful",
#     "token": "abc123xyz"
# }
#
# The token is not the user's password.
# It is proof that the user has already logged in.
#
# Example request with a token in the HTTP header:
# Authorization: Bearer abc123xyz
#
# "Bearer" tells the API that abc123xyz is an authentication token.
#
# If the token is valid:
#     The API allows the user to access protected data.
#
# If the token is missing, invalid, or expired:
#     The API returns 401 Unauthorized.
#
# Important:
# - Tokens should be difficult to guess.
# - Tokens should have an expiry time.
# - Tokens should be sent over HTTPS.
# - Never share a token publicly.
# - In real applications, libraries such as JWT are used to create tokens.