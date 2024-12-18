"""Main application entry point"""
import uvicorn
from fastapi import FastAPI
from Controllers.UserController import router as user_controller_router
from Controllers.AuthController import router as auth_controller_router
from Controllers.RoleController import router as role_controller_router

# Constants
API_PREFIX = "/api/v1"
HOST = "127.0.0.1"
PORT = 8000
RELOAD = True

# Initialize FastAPI app
app = FastAPI()


def include_routers(app: FastAPI):
    """Include all defined routers with the specified prefix."""
    routers_to_include = [
        user_controller_router,
        auth_controller_router,
        role_controller_router,
    ]
    for router in routers_to_include:
        app.include_router(router, prefix=API_PREFIX)


# Include routers
include_routers(app)


# Define utility function
def get_welcome_message():
    """Return the welcome message."""
    return {"message": "Welcome to the UserManagement API"}


# Root endpoint
@app.get("/")
def read_welcome_message():
    return get_welcome_message()


def main():
    """Run the application using uvicorn server."""
    uvicorn.run("main:app", host=HOST, port=PORT, reload=RELOAD)


if __name__ == "__main__":
    main()